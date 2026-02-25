"""Abstract base renderer interface for design system outputs."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from design_system.models import Presentation, RenderResult, ThemeInfo


class BaseRenderer(ABC):
    """Abstract renderer that converts Presentation + Theme into an output file."""

    @abstractmethod
    def render(
        self,
        presentation: Presentation,
        theme: ThemeInfo,
        output_path: Path,
    ) -> RenderResult:
        """Render a presentation with the given theme to the output path."""

    @property
    @abstractmethod
    def format_name(self) -> str:
        """Return the output format identifier (e.g. 'pptx', 'html')."""
