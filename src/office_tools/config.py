"""Paths and limits for office-tools.

Sandbox roots are enforced later in ``sandbox.py`` (OT-02); this module only
declares what the limits are so the tool layer and the sandbox agree.
"""

from __future__ import annotations

import os
from pathlib import Path

DATA_ENV = "OFFICE_TOOLS_DATA"

TEMPLATES_DIR_NAME = "templates"
LOGS_DIR_NAME = "logs"

#: Documents the agent may read and write. Never a path outside these.
DELIVERABLES_DIR_NAME = "deliverables"

#: Hard caps, so a runaway generation cannot exhaust the sandbox.
MAX_ROWS = 100_000
MAX_SHEETS = 50
MAX_PDF_PAGES = 2_000
MAX_INLINE_TEXT_CHARS = 20_000
MAX_OUTPUT_FILES_PER_CALL = 20


class ConfigError(RuntimeError):
    """Raised when the plugin data directory is not configured."""


def data_dir() -> Path:
    """The plugin data root, from ``OFFICE_TOOLS_DATA``."""
    raw = os.environ.get(DATA_ENV, "").strip()
    if not raw:
        raise ConfigError(
            f"{DATA_ENV} is not set. It is supplied by the plugin runtime as "
            "${PLUGIN_DATA}; set it explicitly when running the server by hand."
        )
    return Path(raw)


def templates_dir() -> Path:
    """Immutable, versioned style specs live here."""
    return data_dir() / TEMPLATES_DIR_NAME


def logs_dir() -> Path:
    return data_dir() / LOGS_DIR_NAME


def deliverables_dir(working_dir: str) -> Path:
    return Path(working_dir) / DELIVERABLES_DIR_NAME
