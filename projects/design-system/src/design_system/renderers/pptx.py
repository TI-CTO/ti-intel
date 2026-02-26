"""PPTX renderer — generates PowerPoint presentations using python-pptx."""

from __future__ import annotations

import logging
from pathlib import Path

from pptx import Presentation as PptxPresentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

from design_system.models import (
    DesignTokens,
    Presentation,
    RenderResult,
    SlideContent,
    SlideType,
    ThemeInfo,
)
from design_system.renderers.base import BaseRenderer

logger = logging.getLogger(__name__)

# Slide dimensions: Widescreen 16:9
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# Layout margins
MARGIN_LEFT = Inches(0.8)
MARGIN_TOP = Inches(0.6)
CONTENT_WIDTH = Inches(11.733)
CONTENT_HEIGHT = Inches(5.5)


def _hex_to_rgb(hex_color: str) -> RGBColor:
    """Convert hex color string to RGBColor."""
    h = hex_color.lstrip("#")
    return RGBColor(int(h[:2], 16), int(h[2:4], 16), int(h[4:6], 16))


class PptxRenderer(BaseRenderer):
    """Render presentations as PPTX files using python-pptx."""

    @property
    def format_name(self) -> str:
        return "pptx"

    def render(
        self,
        presentation: Presentation,
        theme: ThemeInfo,
        output_path: Path,
    ) -> RenderResult:
        """Render a Presentation to a .pptx file."""
        prs = PptxPresentation()
        prs.slide_width = SLIDE_WIDTH
        prs.slide_height = SLIDE_HEIGHT

        tokens = theme.tokens

        for slide_content in presentation.slides:
            self._add_slide(prs, slide_content, tokens)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        prs.save(str(output_path))
        logger.info("Saved PPTX: %s (%d slides)", output_path, len(presentation.slides))

        return RenderResult(
            output_path=output_path,
            format="pptx",
            theme=theme.name,
            slide_count=len(presentation.slides),
        )

    def _add_slide(
        self,
        prs: PptxPresentation,
        content: SlideContent,
        tokens: DesignTokens,
    ) -> None:
        """Add a single slide based on its type."""
        layout = prs.slide_layouts[6]  # Blank layout
        slide = prs.slides.add_slide(layout)

        handlers = {
            SlideType.COVER: self._render_cover,
            SlideType.SECTION: self._render_section,
            SlideType.BULLET: self._render_bullet,
            SlideType.TABLE: self._render_table,
            SlideType.QUOTE: self._render_quote,
            SlideType.TEXT: self._render_text,
            SlideType.CLOSING: self._render_closing,
        }

        handler = handlers.get(content.slide_type, self._render_text)
        handler(slide, content, tokens)

    # ----- Slide type renderers -----

    def _render_cover(self, slide, content: SlideContent, tokens: DesignTokens) -> None:
        """Cover slide with full-width colored background."""
        # Background
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = _hex_to_rgb(tokens.color.primary)

        # Title
        title_box = slide.shapes.add_textbox(
            MARGIN_LEFT,
            Inches(2.2),
            CONTENT_WIDTH,
            Inches(1.5),
        )
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = content.title
        p.font.size = Pt(tokens.typography.title_size + 8)
        p.font.bold = True
        p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        p.font.name = tokens.typography.font_family
        p.alignment = PP_ALIGN.LEFT

        # Subtitle
        if content.subtitle:
            sub_box = slide.shapes.add_textbox(
                MARGIN_LEFT,
                Inches(3.9),
                CONTENT_WIDTH,
                Inches(0.8),
            )
            tf2 = sub_box.text_frame
            p2 = tf2.paragraphs[0]
            p2.text = content.subtitle
            p2.font.size = Pt(tokens.typography.subheading_size)
            p2.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            p2.font.name = tokens.typography.font_family

        # Accent line
        slide.shapes.add_shape(
            1,  # Rectangle
            MARGIN_LEFT,
            Inches(3.6),
            Inches(2),
            Pt(4),
        )

    def _render_section(
        self, slide, content: SlideContent, tokens: DesignTokens
    ) -> None:
        """Section divider slide."""
        # Subtle background
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = _hex_to_rgb(tokens.color.surface)

        # Accent bar on left
        bar = slide.shapes.add_shape(
            1,
            Inches(0.4),
            Inches(2.0),
            Pt(6),
            Inches(3.0),
        )
        bar_fill = bar.fill
        bar_fill.solid()
        bar_fill.fore_color.rgb = _hex_to_rgb(tokens.color.primary)
        bar.line.fill.background()

        # Section title
        title_box = slide.shapes.add_textbox(
            Inches(1.2),
            Inches(2.5),
            Inches(10),
            Inches(2),
        )
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = content.title
        p.font.size = Pt(tokens.typography.heading_size + 4)
        p.font.bold = True
        p.font.color.rgb = _hex_to_rgb(tokens.color.text)
        p.font.name = tokens.typography.font_family

    def _render_bullet(
        self, slide, content: SlideContent, tokens: DesignTokens
    ) -> None:
        """Bullet list slide."""
        self._add_slide_background(slide, tokens)
        self._add_title_bar(slide, content.title, tokens)

        body_box = slide.shapes.add_textbox(
            MARGIN_LEFT,
            Inches(1.8),
            CONTENT_WIDTH,
            CONTENT_HEIGHT,
        )
        tf = body_box.text_frame
        tf.word_wrap = True

        for i, bullet in enumerate(content.bullets):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = bullet
            p.font.size = Pt(tokens.typography.body_size)
            p.font.color.rgb = _hex_to_rgb(tokens.color.text)
            p.font.name = tokens.typography.font_family
            p.space_after = Pt(tokens.spacing.sm)
            p.level = 0
            p.runs[0].text = f"\u2022  {bullet}"

    def _render_table(self, slide, content: SlideContent, tokens: DesignTokens) -> None:
        """Table slide."""
        self._add_slide_background(slide, tokens)
        self._add_title_bar(slide, content.title, tokens)

        if not content.table:
            return

        rows = len(content.table.rows) + 1  # +1 for header
        cols = len(content.table.headers)
        if cols == 0:
            return

        # Calculate table dimensions
        table_width = min(CONTENT_WIDTH, Inches(12))
        table_height = Inches(min(0.4 * rows, 5.0))

        table_shape = slide.shapes.add_table(
            rows,
            cols,
            MARGIN_LEFT,
            Inches(1.8),
            table_width,
            table_height,
        )
        table = table_shape.table

        # Style header row
        for j, header in enumerate(content.table.headers):
            cell = table.cell(0, j)
            cell.text = header
            self._style_cell(cell, tokens, is_header=True)

        # Style data rows
        for i, row in enumerate(content.table.rows):
            for j, value in enumerate(row):
                if j < cols:
                    cell = table.cell(i + 1, j)
                    cell.text = value
                    self._style_cell(cell, tokens, is_header=False, row_idx=i)

    def _render_quote(self, slide, content: SlideContent, tokens: DesignTokens) -> None:
        """Quote/key message slide."""
        self._add_slide_background(slide, tokens)

        # Large quote mark
        quote_mark = slide.shapes.add_textbox(
            Inches(1.0),
            Inches(1.2),
            Inches(2),
            Inches(1.5),
        )
        tf_q = quote_mark.text_frame
        p_q = tf_q.paragraphs[0]
        p_q.text = "\u201c"
        p_q.font.size = Pt(96)
        p_q.font.color.rgb = _hex_to_rgb(tokens.color.primary)
        p_q.font.name = tokens.typography.font_family

        # Quote text
        quote_box = slide.shapes.add_textbox(
            Inches(1.5),
            Inches(2.5),
            Inches(10),
            Inches(3),
        )
        tf = quote_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = content.quote
        p.font.size = Pt(tokens.typography.subheading_size + 2)
        p.font.italic = True
        p.font.color.rgb = _hex_to_rgb(tokens.color.text)
        p.font.name = tokens.typography.font_family
        p.alignment = PP_ALIGN.LEFT

    def _render_text(self, slide, content: SlideContent, tokens: DesignTokens) -> None:
        """General text/body slide."""
        self._add_slide_background(slide, tokens)
        self._add_title_bar(slide, content.title, tokens)

        body_box = slide.shapes.add_textbox(
            MARGIN_LEFT,
            Inches(1.8),
            CONTENT_WIDTH,
            CONTENT_HEIGHT,
        )
        tf = body_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = content.body
        p.font.size = Pt(tokens.typography.body_size)
        p.font.color.rgb = _hex_to_rgb(tokens.color.text)
        p.font.name = tokens.typography.font_family
        p.space_after = Pt(tokens.spacing.md)

    def _render_closing(
        self, slide, content: SlideContent, tokens: DesignTokens
    ) -> None:
        """Closing/thank you slide."""
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = _hex_to_rgb(tokens.color.primary)

        title_box = slide.shapes.add_textbox(
            MARGIN_LEFT,
            Inches(2.8),
            CONTENT_WIDTH,
            Inches(2),
        )
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = content.title
        p.font.size = Pt(tokens.typography.title_size + 4)
        p.font.bold = True
        p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        p.font.name = tokens.typography.font_family
        p.alignment = PP_ALIGN.CENTER

    # ----- Helper methods -----

    def _add_slide_background(self, slide, tokens: DesignTokens) -> None:
        """Set slide background color."""
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = _hex_to_rgb(tokens.color.background)

    def _add_title_bar(self, slide, title: str, tokens: DesignTokens) -> None:
        """Add a title bar at the top of the slide."""
        if not title:
            return

        # Accent line under title
        line = slide.shapes.add_shape(
            1,  # Rectangle
            MARGIN_LEFT,
            Inches(1.35),
            Inches(1.5),
            Pt(3),
        )
        line_fill = line.fill
        line_fill.solid()
        line_fill.fore_color.rgb = _hex_to_rgb(tokens.color.primary)
        line.line.fill.background()

        # Title text
        title_box = slide.shapes.add_textbox(
            MARGIN_LEFT,
            Inches(0.5),
            CONTENT_WIDTH,
            Inches(0.8),
        )
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(tokens.typography.heading_size)
        p.font.bold = True
        p.font.color.rgb = _hex_to_rgb(tokens.color.text)
        p.font.name = tokens.typography.font_family

    def _style_cell(
        self,
        cell,
        tokens: DesignTokens,
        *,
        is_header: bool = False,
        row_idx: int = 0,
    ) -> None:
        """Style a table cell."""
        for paragraph in cell.text_frame.paragraphs:
            paragraph.font.size = Pt(tokens.typography.caption_size + 1)
            paragraph.font.name = tokens.typography.font_family

            if is_header:
                paragraph.font.bold = True
                paragraph.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            else:
                paragraph.font.color.rgb = _hex_to_rgb(tokens.color.text)

        cell.vertical_anchor = MSO_ANCHOR.MIDDLE

        if is_header:
            fill = cell.fill
            fill.solid()
            fill.fore_color.rgb = _hex_to_rgb(tokens.color.primary)
        elif row_idx % 2 == 1:
            fill = cell.fill
            fill.solid()
            fill.fore_color.rgb = _hex_to_rgb(tokens.color.surface)
