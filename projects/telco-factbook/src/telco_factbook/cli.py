"""CLI interface for telco-factbook."""

from __future__ import annotations

import hashlib
import logging
from datetime import datetime, timezone
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from telco_factbook.config import settings
from telco_factbook.models import Carrier, DocType

app = typer.Typer(help="Telco competitor earnings factbook")
console = Console()


def _setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )


@app.command()
def collect(
    carrier: str = typer.Option("all", help="Carrier: skt, kt, or all"),
    year: int = typer.Option(2024, help="Year to collect"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Collect earnings data: download Excel → parse → store in Supabase."""
    _setup_logging(verbose)
    from telco_factbook.db.repository import FactbookRepository

    repo = FactbookRepository()
    carriers = _resolve_carriers(carrier)

    run_id = repo.start_collection_run(
        carrier=carrier if carrier != "all" else None,
        year_from=year,
        year_to=year,
    )

    total_found = 0
    total_downloaded = 0
    total_parsed = 0
    total_errors = 0
    error_messages: list[str] = []

    for c in carriers:
        console.print(f"\n[bold blue]Collecting {c.value} {year}...[/]")

        scraper = _get_scraper(c)
        parser = _get_parser(c)

        try:
            docs = scraper.fetch_documents(year)
            excel_docs = [d for d in docs if d.doc_type == DocType.FINANCIAL_STATEMENT]
            total_found += len(excel_docs)

            for doc in excel_docs:
                try:
                    # Download
                    local_path = scraper.download_file(doc, settings.raw_dir)
                    doc.local_path = local_path
                    doc.downloaded_at = datetime.now(timezone.utc)
                    total_downloaded += 1

                    # Store document metadata
                    doc_id = repo.upsert_document(doc)

                    # Parse
                    result = parser.parse(local_path, doc.year, doc.quarter)
                    result.metrics.source_doc_id = doc_id

                    # Store metrics
                    repo.upsert_metrics(result.metrics)
                    repo.mark_parsed(doc_id)
                    total_parsed += 1

                    # Store parse issues
                    for issue in result.issues:
                        repo.insert_parse_issue(issue, doc_id)

                    confidence_color = _confidence_color(result.confidence)
                    console.print(
                        f"  Q{doc.quarter}: revenue={result.metrics.revenue:,}M "
                        f"[{confidence_color}](confidence: {result.confidence:.0%})[/]"
                        if result.metrics.revenue
                        else f"  Q{doc.quarter}: [red]no revenue data[/]"
                    )

                except Exception as e:
                    total_errors += 1
                    error_messages.append(f"{c.value} Q{doc.quarter}: {e}")
                    console.print(f"  [red]Q{doc.quarter}: ERROR — {e}[/]")

        except Exception as e:
            total_errors += 1
            error_messages.append(f"{c.value}: {e}")
            console.print(f"  [red]ERROR — {e}[/]")

        finally:
            scraper.close()

    repo.finish_collection_run(
        run_id,
        documents_found=total_found,
        documents_downloaded=total_downloaded,
        documents_parsed=total_parsed,
        errors=total_errors,
        error_log="\n".join(error_messages) if error_messages else None,
    )

    console.print(
        f"\n[bold]Done:[/] {total_found} found, {total_downloaded} downloaded, "
        f"{total_parsed} parsed, {total_errors} errors"
    )


@app.command(name="import")
def import_file(
    file: Path = typer.Argument(..., help="Path to Excel (.xlsx) file"),
    carrier: str = typer.Option(..., help="Carrier: skt or kt"),
    year: int = typer.Option(..., help="Year (e.g. 2025)"),
    quarter: int = typer.Option(..., help="Quarter (1-4)"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Import a manually downloaded Excel file → parse → store in Supabase."""
    _setup_logging(verbose)
    from telco_factbook.db.repository import FactbookRepository

    if not file.exists():
        console.print(f"[red]File not found: {file}[/]")
        raise typer.Exit(1)

    if file.suffix.lower() not in (".xlsx", ".xls"):
        console.print(f"[red]Unsupported file type: {file.suffix}. Use .xlsx[/]")
        raise typer.Exit(1)

    carrier_enum = Carrier(carrier.upper())
    parser = _get_parser(carrier_enum)
    repo = FactbookRepository()

    console.print(f"\n[bold blue]Importing {carrier.upper()} {year}Q{quarter} from {file.name}...[/]")

    # Store document metadata
    file_hash = hashlib.sha256(file.read_bytes()).hexdigest()

    from telco_factbook.models import IRDocument
    doc = IRDocument(
        carrier=carrier_enum,
        year=year,
        quarter=quarter,
        doc_type=DocType.FINANCIAL_STATEMENT,
        file_format=file.suffix.lstrip(".").lower(),
        source_url=f"manual://{file.name}",
        local_path=file,
        file_hash=file_hash,
        downloaded_at=datetime.now(timezone.utc),
    )
    doc_id = repo.upsert_document(doc)

    # Parse
    result = parser.parse(file, year, quarter)
    result.metrics.source_doc_id = doc_id

    # Store metrics
    repo.upsert_metrics(result.metrics)
    repo.mark_parsed(doc_id)

    # Store parse issues
    for issue in result.issues:
        repo.insert_parse_issue(issue, doc_id)

    if result.metrics.revenue:
        confidence_color = _confidence_color(result.confidence)
        console.print(
            f"  revenue={result.metrics.revenue:,}M, "
            f"op_income={result.metrics.operating_income or 0:,}M "
            f"[{confidence_color}](confidence: {result.confidence:.0%})[/]"
        )
    else:
        console.print("  [red]No revenue data found[/]")

    if result.issues:
        console.print(f"  [yellow]{len(result.issues)} parse issue(s)[/]")

    console.print("[bold green]Done.[/]")


@app.command()
def status(verbose: bool = typer.Option(False, "--verbose", "-v")) -> None:
    """Show current database collection status."""
    _setup_logging(verbose)
    from telco_factbook.db.repository import FactbookRepository

    repo = FactbookRepository()
    data = repo.get_collection_status()

    if not data:
        console.print("[yellow]No data collected yet. Run 'factbook collect' first.[/]")
        return

    # Group by carrier
    by_carrier: dict[str, list[str]] = {}
    for row in data:
        cid = row["carrier_id"]
        by_carrier.setdefault(cid, []).append(f"{row['year']}Q{row['quarter']}")

    table = Table(title="Factbook Collection Status")
    table.add_column("Carrier", style="bold")
    table.add_column("Collected Quarters")

    for cid, quarters in sorted(by_carrier.items()):
        table.add_row(cid, ", ".join(quarters))

    console.print(table)


@app.command()
def query(
    carrier: str = typer.Option("all", help="Carrier: skt, kt, or all"),
    year: int = typer.Option(2024, help="Year"),
    quarter: int = typer.Option(0, help="Quarter (0=all)"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Query financial metrics from the database."""
    _setup_logging(verbose)
    from telco_factbook.db.repository import FactbookRepository

    repo = FactbookRepository()
    data = repo.get_metrics(
        carrier=carrier.upper() if carrier != "all" else None,
        year=year,
        quarter=quarter if quarter > 0 else None,
    )

    if not data:
        console.print("[yellow]No data found for the given filters.[/]")
        return

    table = Table(title=f"Financial Metrics — {year}" + (f" Q{quarter}" if quarter else ""))
    table.add_column("Carrier", style="bold")
    table.add_column("Quarter")
    table.add_column("Revenue (M)", justify="right")
    table.add_column("Op. Income (M)", justify="right")
    table.add_column("Net Income (M)", justify="right")
    table.add_column("EBITDA (M)", justify="right")

    for row in data:
        table.add_row(
            row.get("carrier_id", ""),
            f"Q{row.get('quarter', '')}",
            f"{row['revenue']:,}" if row.get("revenue") else "-",
            f"{row['operating_income']:,}" if row.get("operating_income") else "-",
            f"{row['net_income']:,}" if row.get("net_income") else "-",
            f"{row['ebitda']:,}" if row.get("ebitda") else "-",
        )

    console.print(table)


def _confidence_color(confidence: float) -> str:
    """Return Rich color name based on parse confidence score."""
    if confidence >= 0.66:
        return "green"
    return "yellow" if confidence >= 0.33 else "red"


def _resolve_carriers(carrier_str: str) -> list[Carrier]:
    if carrier_str == "all":
        return [Carrier.KT, Carrier.SKT]
    return [Carrier(carrier_str.upper())]


def _get_scraper(carrier: Carrier):  # noqa: ANN202
    if carrier == Carrier.KT:
        from telco_factbook.scrapers.kt import KTScraper
        return KTScraper(timeout=settings.http_timeout)
    elif carrier == Carrier.SKT:
        from telco_factbook.scrapers.skt import SKTScraper
        return SKTScraper(timeout=settings.http_timeout)
    raise ValueError(f"Unknown carrier: {carrier}")


def _get_parser(carrier: Carrier):  # noqa: ANN202
    if carrier == Carrier.KT:
        from telco_factbook.parsers.kt_parser import KTExcelParser
        return KTExcelParser()
    elif carrier == Carrier.SKT:
        from telco_factbook.parsers.skt_parser import SKTExcelParser
        return SKTExcelParser()
    raise ValueError(f"Unknown carrier: {carrier}")


if __name__ == "__main__":
    app()
