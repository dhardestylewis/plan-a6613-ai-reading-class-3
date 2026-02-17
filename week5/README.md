# Week 5 — AI Reading Exercise: From Digital to Physical Infrastructure

**Course**: PLAN A6613: AI and the Future of Cities (Spring 2026)
**Author**: Daniel Hardesty Lewis
**Date**: February 17, 2026

## Assignment

Use an AI tool to research: *"What are three real-world examples of AI being used to 'actively manage' city assets like the curb or the power grid, and how are cities funding these new digital systems?"*

Create a max 1-page document covering: Tool & Process, Key Findings, Verification ("Human-in-the-Loop" Check), and Critical Reflection. Full assignment prompt saved in `AI_Reading_Exercise_Class_5.tex.d/assignment_prompt.md`.

## Contents

| File | Description |
|------|-------------|
| `AI_Reading_Exercise_Class_5.tex` | LaTeX source for the one-page exercise |
| `AI_Reading_Exercise_Class_5.pdf` | Compiled PDF |
| `prompt.md` | Verbatim prompt log with timestamped user feedback + request status tracking |
| `AI_Reading_Exercise_Class_5.tex.d/assignment_prompt.md` | Verbatim assignment prompt from Canvas |
| `AI_Reading_Exercise_Class_5.tex.d/refs/sources/` | 8 downloaded primary source texts |
| `AI_Reading_Exercise_Class_5.tex.d/refs/annotations/` | 3 annotations + synthesis matrix |
| `AI_Reading_Exercise_Class_5.tex.d/refs/Verification_Audit.md` | Claim-by-claim pipeline audit (41 claims, 97% at 2+ sources) |

## Source Pipeline

All claims in the document are traced to downloaded source texts in `refs/sources/`:

| Source file | Stakeholder type | Key use |
|-------------|-----------------|---------|
| `Automotus_Pittsburgh_full.txt` | Vendor | Zone count, turnover claims, SaaS model |
| `Pittsburgh_CityGov_full.txt` | City government | Independent pilot statistics |
| `DOE_Grant_full.txt` | Federal funder | $3.8M VTO grant details |
| `Flow_Labs_NCDOT_full.txt` | Vendor | System capabilities, "recommends" language |
| `GovTech_NCDOT_full.txt` | Independent journalism | Aaron Moody quote, human oversight confirmation |
| `Tapestry_Google_X_full.txt` | Vendor (Alphabet) | Multi-year partnership, not yet deployed |
| `PJM_Newsroom_full.txt` | Grid operator | 67M people, 13 states, interconnection queue |
| `YaleE360_AI_Energy_full.txt` | Independent journalism | AI energy demand, Google conflict of interest |

## Annotations & Verification

| File | Coverage |
|------|----------|
| `01_Annotation_Automotus.md` | Stakeholder analysis, data discrepancy, conflict of interest |
| `02_Annotation_FlowLabs.md` | Language comparison (vendor vs. government vs. independent) |
| `03_Annotation_Tapestry.md` | Google dual role, revolving door (Andy Ott), deployment status |
| `00_Synthesis_Matrix.md` | Cross-source verification, what Claude missed |
| `Verification_Audit.md` | Claim-by-claim pipeline audit (41 claims, 97% at 2+ sources) |

## How to Review the Process

1. **Writeup** (`AI_Reading_Exercise_Class_5.pdf`) — inline APA citations trace each claim to a source
2. **Prompt log** (`prompt.md`) — every user directive timestamped verbatim, with completion status
3. **Source files** (`refs/sources/*_full.txt`) — downloaded primary sources with line references
4. **Annotations** (`refs/annotations/0*_Annotation_*.md`) — stakeholder analysis per source
5. **Verification audit** (`refs/Verification_Audit.md`) — every claim mapped through full pipeline
6. **Git history** — `git log --oneline` shows incremental commits at each major step
