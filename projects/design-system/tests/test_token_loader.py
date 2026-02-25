"""Tests for design token loading and theme merging."""

from design_system.token_loader import list_themes, load_base_tokens, load_theme


class TestBaseTokens:
    def test_load_base_tokens(self):
        tokens = load_base_tokens()
        assert tokens.color.primary == "#C50063"
        assert tokens.typography.font_family == "Pretendard"
        assert tokens.spacing.md == 16

    def test_all_color_fields_populated(self):
        tokens = load_base_tokens()
        assert tokens.color.primary
        assert tokens.color.secondary
        assert tokens.color.background
        assert tokens.color.text


class TestThemeLoading:
    def test_load_professional_theme(self):
        theme = load_theme("professional")
        assert theme.name == "professional"
        assert theme.display_name == "Professional"
        assert theme.tokens.color.primary == "#C50063"
        # Professional overrides secondary
        assert theme.tokens.color.secondary == "#1E3A5F"

    def test_load_minimal_theme(self):
        theme = load_theme("minimal")
        assert theme.name == "minimal"
        # Minimal overrides primary to near-black
        assert theme.tokens.color.primary == "#18181B"

    def test_load_dark_theme(self):
        theme = load_theme("dark")
        assert theme.name == "dark"
        # Dark has dark background
        assert theme.tokens.color.background == "#0F172A"
        # Light text on dark bg
        assert theme.tokens.color.text == "#F1F5F9"

    def test_theme_inherits_base_spacing(self):
        """Themes without spacing overrides should inherit base values."""
        theme = load_theme("professional")
        assert theme.tokens.spacing.md == 16
        assert theme.tokens.spacing.xl == 48

    def test_unknown_theme_raises(self):
        try:
            load_theme("nonexistent")
            assert False, "Should have raised FileNotFoundError"
        except FileNotFoundError:
            pass


class TestListThemes:
    def test_list_returns_all_themes(self):
        themes = list_themes()
        names = [t["name"] for t in themes]
        assert "professional" in names
        assert "minimal" in names
        assert "dark" in names

    def test_list_has_metadata(self):
        themes = list_themes()
        for theme in themes:
            assert "name" in theme
            assert "display_name" in theme
            assert "description" in theme
