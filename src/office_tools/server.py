"""MCP stdio entry point for office-tools.

The scaffold exposes ``document_formats`` only: it proves the handshake and the
launcher wiring. The 16 document tools land in Waves 5-6 on top of the sandbox.
"""

from __future__ import annotations

from typing import Any

from mcp.server.mcpserver import MCPServer

server = MCPServer(
    "office-tools",
    instructions=(
        "Local document I/O for DOCX, XLSX, PPTX, PDF and CSV. All work happens "
        "on disk inside the project; nothing is uploaded."
    ),
)


@server.tool()
def document_formats() -> dict[str, Any]:
    """List the document formats this server can read and write."""
    return {
        "read": ["docx", "xlsx", "pptx", "pdf", "csv"],
        "write": ["docx", "xlsx", "pptx", "pdf", "csv"],
    }


def main() -> None:
    server.run(transport="stdio")


if __name__ == "__main__":
    main()
