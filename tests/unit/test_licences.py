"""The dependency licence policy must be enforced by the dependency set.

AGPL and proprietary are banned outright (the plan bans PyMuPDF for exactly this
reason). This test fails the build if a banned dependency is ever added.
"""

from __future__ import annotations

import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

BANNED = {
    "pymupdf",  # AGPL-3.0 - would force this MIT repo to AGPL
    "fitz",  # PyMuPDF's import name
    "docx2pdf",  # proprietary, needs MS Word
    "pdfplumber",  # pulls image libs with mixed licensing; use pypdf instead
}


def _bare(spec: str) -> str:
    """Reduce a PEP 508 requirement to its bare project name."""
    return spec.split(">")[0].split("=")[0].split("[")[0].split("<")[0].strip().lower()


def _dependencies() -> list[str]:
    data = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    return list(data["project"]["dependencies"])


def _names() -> set[str]:
    return {_bare(dep) for dep in _dependencies()}


def test_no_banned_dependencies() -> None:
    names = _names()
    assert not (names & BANNED), f"banned dependency present: {sorted(names & BANNED)}"


def test_expected_document_dependencies() -> None:
    assert {"python-docx", "openpyxl", "python-pptx", "pypdf", "reportlab"} <= _names()
