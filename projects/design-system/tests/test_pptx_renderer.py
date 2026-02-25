"""Tests for PPTX renderer — verifies slide generation and file output."""

from pathlib import Path

from design_system.models import (
    Presentation,
    SlideContent,
    SlideType,
    TableData,
)
from design_system.renderers.pptx import PptxRenderer
from design_system.token_loader import load_theme


def _make_presentation() -> Presentation:
    """Create a minimal test presentation."""
    return Presentation(
        title="Test Report",
        slides=[
            SlideContent(slide_type=SlideType.COVER, title="Test Report"),
            SlideContent(slide_type=SlideType.SECTION, title="Section 1"),
            SlideContent(
                slide_type=SlideType.BULLET,
                title="Key Points",
                bullets=["Point A", "Point B", "Point C"],
            ),
            SlideContent(
                slide_type=SlideType.TABLE,
                title="Data",
                table=TableData(
                    headers=["Name", "Value"],
                    rows=[["Alpha", "100"], ["Beta", "200"]],
                ),
            ),
            SlideContent(
                slide_type=SlideType.QUOTE,
                title="Insight",
                quote="This is a key insight that drives the recommendation.",
            ),
            SlideContent(
                slide_type=SlideType.TEXT,
                title="Details",
                body="Detailed explanation text goes here.",
            ),
            SlideContent(slide_type=SlideType.CLOSING, title="Thank You"),
        ],
    )


class TestPptxRenderer:
    def test_render_professional(self, tmp_path: Path):
        theme = load_theme("professional")
        renderer = PptxRenderer()
        pres = _make_presentation()
        output = tmp_path / "test_professional.pptx"

        result = renderer.render(pres, theme, output)

        assert result.output_path.exists()
        assert result.format == "pptx"
        assert result.theme == "professional"
        assert result.slide_count == 7

    def test_render_minimal(self, tmp_path: Path):
        theme = load_theme("minimal")
        renderer = PptxRenderer()
        pres = _make_presentation()
        output = tmp_path / "test_minimal.pptx"

        result = renderer.render(pres, theme, output)

        assert result.output_path.exists()
        assert result.slide_count == 7

    def test_render_dark(self, tmp_path: Path):
        theme = load_theme("dark")
        renderer = PptxRenderer()
        pres = _make_presentation()
        output = tmp_path / "test_dark.pptx"

        result = renderer.render(pres, theme, output)

        assert result.output_path.exists()
        assert result.slide_count == 7

    def test_output_file_created(self, tmp_path: Path):
        theme = load_theme("professional")
        renderer = PptxRenderer()
        pres = _make_presentation()
        output = tmp_path / "subdir" / "output.pptx"

        renderer.render(pres, theme, output)

        assert output.exists()
        assert output.stat().st_size > 0

    def test_korean_content(self, tmp_path: Path):
        """Verify Korean text doesn't cause errors."""
        theme = load_theme("professional")
        renderer = PptxRenderer()
        pres = Presentation(
            title="한글 테스트",
            slides=[
                SlideContent(
                    slide_type=SlideType.COVER, title="한글 프레젠테이션 테스트"
                ),
                SlideContent(
                    slide_type=SlideType.BULLET,
                    title="핵심 포인트",
                    bullets=["첫 번째 항목", "두 번째 항목", "세 번째 항목"],
                ),
                SlideContent(
                    slide_type=SlideType.TABLE,
                    title="데이터",
                    table=TableData(
                        headers=["항목", "값"],
                        rows=[["매출", "1,000억원"], ["영업이익", "200억원"]],
                    ),
                ),
                SlideContent(slide_type=SlideType.CLOSING, title="감사합니다"),
            ],
        )
        output = tmp_path / "korean_test.pptx"

        result = renderer.render(pres, theme, output)

        assert result.output_path.exists()
        assert result.slide_count == 4

    def test_format_name(self):
        renderer = PptxRenderer()
        assert renderer.format_name == "pptx"
