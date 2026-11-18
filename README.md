# office-tools

Free, local, model-agnostic document I/O for **DOCX, XLSX, PPTX, PDF and CSV**,
plus a style/template system that keeps output consistent across sessions and
projects.

Ask for a report and it comes out in your report style. Say *"change the header
to red"* and the agent derives a new named version, so future reports use red
headers without being told again.

Repo `OH-OfficeTools` maps to plugin name **`office-tools`**.

## Templates are JSON, not binaries

A template is a declarative `StyleSpec` (JSON) rendered to `.docx`/`.pptx` at
generation time. Shipping `.docx` templates would mean binary files in git,
unmergeable diffs, and "change the header to red" becoming arbitrary OOXML
patching. JSON gives a text-only repo, one-field restyling and clean diffs.

## Licence policy

Every dependency must be `pip`-installable, run locally, and be MIT / BSD /
Apache. AGPL and proprietary are banned — **PyMuPDF is AGPL-3.0** and would force
this MIT repo to AGPL, so it is out; `pypdf` (BSD-3) reads PDFs and `reportlab`
(BSD-3) writes them. `tests/unit/test_licences.py` enforces this, and the local
CI runs `pip-licenses` as a second gate.

| Package | Licence | Role |
|---|---|---|
| `python-docx` | MIT | DOCX read/write |
| `openpyxl` | MIT | XLSX read/write |
| `python-pptx` | MIT | PPTX read/write |
| `pypdf` | BSD-3 | PDF read |
| `reportlab` | BSD-3 | PDF generation |

## Status

**Not installable yet.** Scaffolded in Wave 0 (OT-01): manifest, launcher and MCP
handshake work, and `document_formats` answers. The sandbox (which gates every
later step), block model, template system and the five format backends land in
Waves 5–6.

## Layout

```
plugin.json                       manifest (Agent Plugins 1.0.0)
mcp.json                          stdio server declaration
bin/office-tools-mcp              launcher, exec'd by mcp.json
src/office_tools/
  hook_runtime.py                 vendored hook contract, hash-locked
  config.py                       paths, limits
  errors.py                       typed, code-carrying errors
  server.py                       MCP stdio dispatch
tests/unit/                       manifest, licence and hash-lock tests
```

## Development

```bash
uv sync
uv run pytest -q
uv run ruff check . && uv run ruff format --check . && uv run mypy src
```

`src/office_tools/hook_runtime.py` is a verbatim copy of the control-plane
canonical runtime (present for the hash-lock test; office-tools ships no hooks).
Do not edit it here: edit the canonical copy, re-copy, and update
`CANONICAL_SHA256` in `tests/unit/test_hook_runtime_hash.py`.

## Licence

MIT.
