"""Tests for the USPTO PatentsView normalisation logic."""

from patent_intel.collectors.patents_view import _normalise


def test_normalise_full_patent():
    raw = {
        "patent_id": "10000001",
        "patent_number": "10000001",
        "patent_title": "AI-Based Network Optimization",
        "patent_abstract": "A method for optimizing networks using AI...",
        "app_date": "2022-06-01",
        "patent_date": "2023-02-14",
        "assignees": [{"assignee_organization": "Qualcomm Inc.", "assignee_country": "US"}],
        "ipcs": [{"ipc_subgroup_id": "H04W24/02"}, {"ipc_subgroup_id": "G06N20/00"}],
    }
    patent = _normalise(raw)
    assert patent is not None
    assert patent["external_id"] == "uspto:10000001"
    assert patent["source"] == "uspto"
    assert patent["title"] == "AI-Based Network Optimization"
    assert patent["applicant"] == "Qualcomm Inc. (US)"
    assert patent["filing_date"] == "2022-06-01"
    assert patent["publication_date"] == "2023-02-14"
    assert "H04W24/02" in patent["ipc_codes"]
    assert patent["reliability_tag"] == "A"
    assert "10000001" in patent["raw_url"]


def test_normalise_missing_patent_id():
    raw = {"patent_title": "No ID", "app_date": "2023-01-01"}
    assert _normalise(raw) is None


def test_normalise_missing_title():
    raw = {"patent_id": "99999999", "patent_number": "99999999", "patent_title": ""}
    assert _normalise(raw) is None


def test_normalise_no_assignee():
    raw = {
        "patent_id": "20000002",
        "patent_number": "20000002",
        "patent_title": "Edge Computing Patent",
        "patent_abstract": "",
        "app_date": "2023-05-10",
        "patent_date": None,
        "assignees": [],
        "ipcs": [],
    }
    patent = _normalise(raw)
    assert patent is not None
    assert patent["applicant"] == "Unknown"
    assert patent["ipc_codes"] == []


def test_normalise_deduplicates_ipc_codes():
    raw = {
        "patent_id": "30000003",
        "patent_number": "30000003",
        "patent_title": "6G Antenna",
        "patent_abstract": "Antenna design for 6G...",
        "app_date": "2024-01-01",
        "patent_date": None,
        "assignees": [{"assignee_organization": "Nokia", "assignee_country": "FI"}],
        "ipcs": [
            {"ipc_subgroup_id": "H01Q1/24"},
            {"ipc_subgroup_id": "H01Q1/24"},  # duplicate
            {"ipc_subgroup_id": "H04B7/06"},
        ],
    }
    patent = _normalise(raw)
    assert patent is not None
    assert patent["ipc_codes"].count("H01Q1/24") == 1
    assert len(patent["ipc_codes"]) == 2
