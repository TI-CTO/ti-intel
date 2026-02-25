"""Test configuration and fixtures."""

import pytest


@pytest.fixture
def sample_kt_response() -> dict:
    """Sample KT API response for testing."""
    return {
        "achPreList": [
            {
                "yyInfo": "2024",
                "title": "2024년 3분기 실적",
                "qqInfo": "3",
                "saveFilePath01": "/files/ir/",
                "saveFileNm01": "KT_3Q2024_Earnings.pdf",
                "saveFilePath02": "/files/ir/",
                "saveFileNm02": "KT_3Q2024_FinancialStatements.xlsx",
            },
            {
                "yyInfo": "2024",
                "title": "2024년 2분기 실적",
                "qqInfo": "2",
                "saveFilePath01": "/files/ir/",
                "saveFileNm01": "KT_2Q2024_Earnings.pdf",
                "saveFilePath02": "/files/ir/",
                "saveFileNm02": "KT_2Q2024_FinancialStatements.xlsx",
            },
        ]
    }


@pytest.fixture
def sample_skt_html() -> str:
    """Sample SKT IR page HTML for testing."""
    return """
    <html>
    <body>
    <select class="year-select">
        <option>2024</option>
        <option>2023</option>
    </select>
    <div class="content">
        <a href="/img/eng/qua/20240725/FinancialStatements2Q24Engilsh.xlsx">Excel</a>
        <a href="/img/eng/qua/20240725/2Q24InvestorBriefing_Eng.pdf">Briefing</a>
        <a href="/img/eng/qua/20241024/FinancialStatements3Q24Engilsh.xlsx">Excel</a>
    </div>
    </body>
    </html>
    """
