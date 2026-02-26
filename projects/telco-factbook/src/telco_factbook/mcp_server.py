"""MCP server for telco-factbook — provides tools for Claude Code to query earnings data."""

from __future__ import annotations

import json
import logging
import sys

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

server = Server("telco-factbook")


def _get_repo():  # noqa: ANN202
    from telco_factbook.db.repository import FactbookRepository
    return FactbookRepository()


@server.list_tools()
async def list_tools() -> list[Tool]:
    """Register available MCP tools."""
    return [
        Tool(
            name="get_financial_metrics",
            description="통신사 재무 지표를 조회합니다. 매출, 영업이익, 순이익, EBITDA 등.",
            inputSchema={
                "type": "object",
                "properties": {
                    "carrier": {
                        "type": "string",
                        "enum": ["SKT", "KT"],
                        "description": "통신사 코드",
                    },
                    "year": {
                        "type": "integer",
                        "description": "조회 연도 (예: 2024)",
                    },
                    "quarter": {
                        "type": "integer",
                        "enum": [1, 2, 3, 4],
                        "description": "분기 (1-4). 생략하면 전체 분기 조회.",
                    },
                },
                "required": ["year"],
            },
        ),
        Tool(
            name="compare_carriers",
            description="SKT와 KT의 특정 재무 지표를 비교합니다.",
            inputSchema={
                "type": "object",
                "properties": {
                    "metric": {
                        "type": "string",
                        "enum": [
                            "revenue",
                            "operating_income",
                            "net_income",
                            "ebitda",
                            "capex",
                            "mobile_subscribers",
                        ],
                        "description": "비교할 재무 지표",
                    },
                    "year": {"type": "integer", "description": "비교 연도"},
                    "quarter": {
                        "type": "integer",
                        "enum": [1, 2, 3, 4],
                        "description": "비교 분기",
                    },
                },
                "required": ["metric", "year"],
            },
        ),
        Tool(
            name="get_revenue_trend",
            description="특정 통신사의 매출 추이를 조회합니다 (YoY/QoQ 성장률 포함).",
            inputSchema={
                "type": "object",
                "properties": {
                    "carrier": {
                        "type": "string",
                        "enum": ["SKT", "KT"],
                        "description": "통신사 코드",
                    },
                    "year_from": {"type": "integer", "description": "시작 연도"},
                    "year_to": {"type": "integer", "description": "종료 연도"},
                },
                "required": ["carrier", "year_from", "year_to"],
            },
        ),
        Tool(
            name="get_subscriber_data",
            description="통신사 가입자 현황을 조회합니다 (모바일, 5G, IPTV, 초고속인터넷).",
            inputSchema={
                "type": "object",
                "properties": {
                    "carrier": {
                        "type": "string",
                        "enum": ["SKT", "KT"],
                        "description": "통신사 코드",
                    },
                    "year": {"type": "integer", "description": "조회 연도"},
                    "quarter": {"type": "integer", "enum": [1, 2, 3, 4]},
                },
                "required": ["carrier", "year"],
            },
        ),
        Tool(
            name="query_factbook",
            description="팩트북 DB에 자유 SQL 쿼리를 실행합니다 (SELECT만 허용).",
            inputSchema={
                "type": "object",
                "properties": {
                    "sql": {
                        "type": "string",
                        "description": "실행할 SQL 쿼리 (SELECT문만 허용)",
                    },
                },
                "required": ["sql"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle MCP tool calls."""
    try:
        result = _dispatch(name, arguments)
        return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False, indent=2))]
    except Exception as e:
        logger.exception("Tool call failed: %s", name)
        return [TextContent(type="text", text=f"Error: {e}")]


def _dispatch(name: str, args: dict) -> dict | list:
    repo = _get_repo()

    if name == "get_financial_metrics":
        data = repo.get_metrics(
            carrier=args.get("carrier"),
            year=args["year"],
            quarter=args.get("quarter"),
        )
        return {"metrics": data, "count": len(data)}

    elif name == "compare_carriers":
        data = repo.get_carrier_comparison(
            metric_name=args["metric"],
            year=args["year"],
            quarter=args.get("quarter"),
        )
        return {"comparison": data, "metric": args["metric"]}

    elif name == "get_revenue_trend":
        # Query multiple years
        all_data = []
        for y in range(args["year_from"], args["year_to"] + 1):
            rows = repo.get_metrics(carrier=args["carrier"], year=y)
            all_data.extend(rows)

        trend = []
        for row in sorted(all_data, key=lambda r: (r["year"], r["quarter"])):
            entry = {
                "year": row["year"],
                "quarter": row["quarter"],
                "revenue": row.get("revenue"),
            }
            # Find same quarter in previous year for YoY
            prev_year_rows = [
                r for r in all_data
                if r["year"] == row["year"] - 1 and r["quarter"] == row["quarter"]
            ]
            if prev_year_rows and prev_year_rows[0].get("revenue") and row.get("revenue"):
                prev_rev = prev_year_rows[0]["revenue"]
                entry["yoy_growth_pct"] = round((row["revenue"] - prev_rev) / prev_rev * 100, 2)
            trend.append(entry)

        return {"carrier": args["carrier"], "trend": trend}

    elif name == "get_subscriber_data":
        data = repo.get_metrics(
            carrier=args["carrier"],
            year=args["year"],
            quarter=args.get("quarter"),
        )
        sub_fields = [
            "mobile_subscribers",
            "mobile_5g_subscribers",
            "iptv_subscribers",
            "broadband_subscribers",
            "arpu_mobile",
        ]
        result = []
        for row in data:
            entry = {
                "year": row["year"],
                "quarter": row["quarter"],
            }
            for field in sub_fields:
                if row.get(field) is not None:
                    entry[field] = row[field]
            result.append(entry)
        return {"carrier": args["carrier"], "subscribers": result}

    elif name == "query_factbook":
        sql = args["sql"].strip()
        if not sql.upper().startswith("SELECT"):
            return {"error": "Only SELECT queries are allowed"}
        return {"data": repo.execute_select(sql)}

    return {"error": f"Unknown tool: {name}"}


async def main() -> None:
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
