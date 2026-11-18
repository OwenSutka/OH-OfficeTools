"""Typed errors surfaced to the agent as structured tool failures.

Every failure the agent can cause is one of these, so the tool layer returns a
stable ``code`` instead of a Python traceback.
"""

from __future__ import annotations

from typing import Any


class OfficeToolsError(Exception):
    """Base class: carries a stable machine-readable code."""

    code = "office_tools_error"

    def __init__(self, message: str, **details: Any) -> None:
        super().__init__(message)
        self.message = message
        self.details = details

    def to_payload(self) -> dict[str, Any]:
        payload: dict[str, Any] = {"error": self.code, "message": self.message}
        if self.details:
            payload["details"] = self.details
        return payload


class InvalidPathError(OfficeToolsError):
    """The requested path escapes the allowed roots."""

    code = "invalid_path"


class UnsupportedFormatError(OfficeToolsError):
    """The file extension has no handler."""

    code = "unsupported_format"


class DocumentReadError(OfficeToolsError):
    """The file exists but could not be parsed."""

    code = "document_read_error"


class TemplateError(OfficeToolsError):
    """A style or template spec was malformed or missing."""

    code = "template_error"


class LimitExceededError(OfficeToolsError):
    """A configured size, row or tool-output limit was hit."""

    code = "limit_exceeded"
