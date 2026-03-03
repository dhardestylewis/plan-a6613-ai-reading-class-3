# Week 7 — AI Reading Exercise: AI, Energy, and Climate

**Course**: PLAN A6613: AI and the Future of Cities (Spring 2026)
**Author**: Daniel Hardesty Lewis
**Date**: March 3, 2026

## Assignment

Use an AI tool to research: *"According to their latest sustainability report, how much has Google seen their location-based carbon emissions increase due to AI, and what specific technologies are they using to mitigate this impact?"*

Create a max 1-page document covering: Tool & Process, Key Findings, Verification ("Human-in-the-Loop" Check), and Critical Reflection. Full assignment prompt saved in `AI_Reading_Exercise_Class_7.tex.d/assignment_prompt.md`.

## Contents

| File | Description |
|------|-------------|
| `AI_Reading_Exercise_Class_7.tex` | LaTeX source for the one-page exercise |
| `AI_Reading_Exercise_Class_7.pdf` | Compiled PDF |
| `prompt.md` | Verbatim prompt log with timestamped user feedback + request status tracking |
| `AI_Reading_Exercise_Class_7.tex.d/assignment_prompt.md` | Verbatim assignment prompt from Canvas |
| `AI_Reading_Exercise_Class_7.tex.d/refs/sources/` | 3 downloaded/annotated primary source texts |
| `AI_Reading_Exercise_Class_7.tex.d/refs/annotations/` | Synthesis matrix |
| `AI_Reading_Exercise_Class_7.tex.d/refs/Verification_Audit.md` | Claim-by-claim pipeline audit (18 claims, 89% at 2+ sources) |

## Source Pipeline

All claims in the document are traced to downloaded source texts in `refs/sources/`:

| Source file | Stakeholder type | Key use |
|-------------|-----------------|---------|
| `Google_2024_Environmental_Report_Blog.txt` | Corporate (vendor) | 14.3M mt CO2e; 48% increase; TPU efficiency; PUE 1.10 |
| `Google_2025_Environmental_Report_Summary.txt` | Corporate (vendor) | 51% increase since 2019; 27% DC electricity jump; 33x per-prompt efficiency |
| `IEA_Data_Centres_Energy.txt` | Intergovernmental (independent) | Global context; hyperscaler electricity doubled; 20-40% annual growth |

Additional sources referenced in the writeup but not downloadable as full text (paywall/404):
- Guardian (Milman, 2025): Location-based 65% increase analysis — confirmed via search results
- Patterson et al. (2022): 100x/1,000x conditional claims — confirmed via Google blog footnotes
- Uptime Institute (2023): PUE industry average — confirmed via Google blog footnotes + IEA

## How to Review the Process

1. **Writeup** (`AI_Reading_Exercise_Class_7.pdf`) — inline APA citations trace each claim to a source
2. **Prompt log** (`prompt.md`) — source-first methodology and LLM audit documented
3. **Source files** (`refs/sources/*`) — downloaded primary sources with analytical annotations
4. **Synthesis matrix** (`refs/annotations/00_Synthesis_Matrix.md`) — cross-source comparison
5. **Verification audit** (`refs/Verification_Audit.md`) — every claim mapped through full pipeline
6. **Git history** — `git log --oneline` shows incremental commits at each major step
