"""Repository layer for Supabase CRUD operations."""

from __future__ import annotations

import logging
from datetime import datetime, timezone

from telco_factbook.db.client import get_client
from telco_factbook.models import FinancialMetrics, IRDocument, ParseIssue

logger = logging.getLogger(__name__)


class FactbookRepository:
    """CRUD operations for the telco factbook database."""

    def __init__(self) -> None:
        self._client = get_client()

    # -- Source Documents --

    def upsert_document(self, doc: IRDocument) -> int:
        """Insert or update a source document. Returns the document ID."""
        data = {
            "carrier_id": doc.carrier.value,
            "year": doc.year,
            "quarter": doc.quarter,
            "doc_type": doc.doc_type.value,
            "source_url": doc.source_url,
            "local_path": str(doc.local_path) if doc.local_path else None,
            "file_hash": doc.file_hash,
            "downloaded_at": (doc.downloaded_at or datetime.now(timezone.utc)).isoformat(),
        }

        result = (
            self._client.table("source_documents")
            .upsert(data, on_conflict="carrier_id,year,quarter,doc_type")
            .execute()
        )

        doc_id = result.data[0]["id"]
        logger.info("Upserted document id=%d: %s %dQ%d", doc_id, doc.carrier, doc.year, doc.quarter)
        return doc_id

    def mark_parsed(self, doc_id: int) -> None:
        """Mark a document as parsed."""
        self._client.table("source_documents").update(
            {"parsed_at": datetime.now(timezone.utc).isoformat()}
        ).eq("id", doc_id).execute()

    # -- Financial Metrics --

    def upsert_metrics(self, metrics: FinancialMetrics) -> int:
        """Insert or update financial metrics. Returns the metrics ID."""
        data = metrics.model_dump(
            exclude={"source_doc_id", "carrier", "period_type"},
            exclude_none=True,
        )

        # Map model fields to DB column names
        data["carrier_id"] = metrics.carrier.value
        data["period_type"] = metrics.period_type.value

        if metrics.source_doc_id is not None:
            data["source_doc_id"] = metrics.source_doc_id

        result = (
            self._client.table("financial_metrics")
            .upsert(data, on_conflict="carrier_id,year,quarter,period_type")
            .execute()
        )

        metric_id = result.data[0]["id"]
        logger.info(
            "Upserted metrics id=%d: %s %dQ%d revenue=%s",
            metric_id,
            metrics.carrier,
            metrics.year,
            metrics.quarter,
            metrics.revenue,
        )
        return metric_id

    def insert_parse_issue(self, issue: ParseIssue, source_doc_id: int) -> None:
        """Record a parse issue."""
        self._client.table("parse_issues").insert({
            "source_doc_id": source_doc_id,
            "field_name": issue.field_name,
            "raw_value": issue.raw_value,
            "issue_type": issue.issue_type,
        }).execute()

    # -- Queries --

    def get_metrics(
        self,
        carrier: str | None = None,
        year: int | None = None,
        quarter: int | None = None,
    ) -> list[dict]:
        """Query financial metrics with optional filters."""
        query = self._client.table("financial_metrics").select("*")

        if carrier:
            query = query.eq("carrier_id", carrier)
        if year:
            query = query.eq("year", year)
        if quarter:
            query = query.eq("quarter", quarter)

        result = query.order("year", desc=True).order("quarter", desc=True).execute()
        return result.data

    def get_carrier_comparison(
        self, metric_name: str, year: int, quarter: int | None = None
    ) -> list[dict]:
        """Get a specific metric for all carriers for comparison."""
        query = (
            self._client.table("financial_metrics")
            .select(f"carrier_id, year, quarter, {metric_name}")
            .eq("year", year)
        )
        if quarter:
            query = query.eq("quarter", quarter)

        result = query.order("carrier_id").execute()
        return result.data

    def get_collection_status(self) -> list[dict]:
        """Get summary of collected data per carrier/year."""
        result = (
            self._client.table("financial_metrics")
            .select("carrier_id, year, quarter")
            .order("carrier_id")
            .order("year", desc=True)
            .order("quarter", desc=True)
            .execute()
        )
        return result.data

    def execute_select(self, sql: str) -> list[dict]:
        """Execute a raw SELECT query via Supabase RPC."""
        result = self._client.rpc("exec_sql", {"query": sql}).execute()
        return result.data

    # -- Collection Runs --

    def start_collection_run(
        self, carrier: str | None, year_from: int, year_to: int
    ) -> int:
        """Start a new collection run and return its ID."""
        result = (
            self._client.table("collection_runs")
            .insert({
                "started_at": datetime.now(timezone.utc).isoformat(),
                "carrier_id": carrier,
                "year_from": year_from,
                "year_to": year_to,
                "status": "running",
            })
            .execute()
        )
        return result.data[0]["id"]

    def finish_collection_run(
        self,
        run_id: int,
        *,
        documents_found: int = 0,
        documents_downloaded: int = 0,
        documents_parsed: int = 0,
        errors: int = 0,
        error_log: str | None = None,
    ) -> None:
        """Finalize a collection run."""
        status = "failed" if errors > 0 and documents_parsed == 0 else "completed"
        self._client.table("collection_runs").update({
            "completed_at": datetime.now(timezone.utc).isoformat(),
            "documents_found": documents_found,
            "documents_downloaded": documents_downloaded,
            "documents_parsed": documents_parsed,
            "errors": errors,
            "status": status,
            "error_log": error_log,
        }).eq("id", run_id).execute()
