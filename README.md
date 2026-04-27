# AI Reading Exercises — PLAN A6613

**Course:** PLAN A6613: AI and the Future of Cities (Spring 2026)  
**Author:** Daniel Hardesty Lewis  
**Institution:** Columbia GSAPP

## Overview

Weekly AI Reading Exercises and Memos for Prof. Wittels' course. Each assignment uses a generative AI tool to research a specific urban technology question, conducts human-in-the-loop verification, and synthesizes findings into an academic document.

## Repository Structure

The workspace is organized into categorized top-level directories:

| Directory | Description |
|-----------|-------------|
| `weekly_assignments/` | Weekly AI reading exercises (e.g., Week 3, Week 4) |
| `memos/` | Major multi-week memos (Memo 1, 2, 3) |
| `waymo_project/` | Standalone urban tech presentation project |
| `tools/` | Standalone binaries and compilers (e.g., tectonic) |
| `logs/` | Scripts and system logs |

### Common Assignment Schema

Every assignment and memo follows a strict internal structure:

- `*.tex` and `*.pdf` (Main source and compiled output)
- `README.md` and `prompt.md` (Documentation and prompt logs)
- `data/sources/` — Original texts, PDFs, and raw materials
- `data/annotations/` — Detailed reading notes and annotated sources
- `data/analysis/` — Synthesis matrices and verification audits
- `scripts/` — Custom Python utilities and data processing
- `build/` — LaTeX auxiliary files (`.aux`, `.log`, etc.)
