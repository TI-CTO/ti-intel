"""MCP server for design-system — provides tools for theme browsing and rendering."""

from __future__ import annotations

import json
import logging
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

server = Server("design-system")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """Register available MCP tools."""
    return [
        Tool(
            name="list_themes",
            description="사용 가능한 디자인 테마 목록을 조회합니다.",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
        Tool(
            name="get_theme",
            description="특정 테마의 상세 정보(토큰 값)를 조회합니다.",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "테마 이름 (예: professional, minimal, dark)",
                    },
                },
                "required": ["name"],
            },
        ),
        Tool(
            name="render_pptx",
            description="마크다운 파일을 PPTX 프레젠테이션으로 변환합니다.",
            inputSchema={
                "type": "object",
                "properties": {
                    "markdown_path": {
                        "type": "string",
                        "description": "변환할 마크다운 파일의 절대 경로",
                    },
                    "theme": {
                        "type": "string",
                        "description": "적용할 테마 이름 (기본: professional)",
                        "default": "professional",
                    },
                    "output_path": {
                        "type": "string",
                        "description": "출력 PPTX 파일 경로 (생략 시 마크다운과 같은 디렉토리에 생성)",
                    },
                },
                "required": ["markdown_path"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle MCP tool calls."""
    try:
        result = _dispatch(name, arguments)
        return [
            TextContent(
                type="text", text=json.dumps(result, ensure_ascii=False, indent=2)
            )
        ]
    except Exception as e:
        logger.exception("Tool call failed: %s", name)
        return [TextContent(type="text", text=f"Error: {e}")]


def _dispatch(name: str, args: dict) -> dict:
    from design_system.token_loader import list_themes, load_theme
    from design_system.parsers.markdown import parse_markdown
    from design_system.renderers.pptx import PptxRenderer

    if name == "list_themes":
        return {"themes": list_themes()}

    elif name == "get_theme":
        theme = load_theme(args["name"])
        return {
            "name": theme.name,
            "display_name": theme.display_name,
            "description": theme.description,
            "tokens": theme.tokens.model_dump(),
        }

    elif name == "render_pptx":
        md_path = Path(args["markdown_path"])
        if not md_path.exists():
            return {"error": f"File not found: {md_path}"}

        md_text = md_path.read_text(encoding="utf-8")
        theme_name = args.get("theme", "professional")
        theme = load_theme(theme_name)
        presentation = parse_markdown(md_text)

        output = args.get("output_path")
        if output:
            output_path = Path(output)
        else:
            output_path = md_path.with_suffix(f".{theme_name}.pptx")

        renderer = PptxRenderer()
        result = renderer.render(presentation, theme, output_path)

        return {
            "status": "success",
            "output_path": str(result.output_path),
            "theme": result.theme,
            "slide_count": result.slide_count,
            "format": result.format,
        }

    return {"error": f"Unknown tool: {name}"}


async def main() -> None:
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream, write_stream, server.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
