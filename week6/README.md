# Week 6 — AI Reading Exercise: Urban Development in an Age of Automation

**Course**: PLAN A6613: AI and the Future of Cities (Spring 2026)
**Author**: Daniel Hardesty Lewis
**Date**: February 24, 2026

## Assignment

Use an AI tool to research: *"Identify two examples of 'agentic' urban systems (systems that make autonomous decisions in real-time) and explain how their governance models address---or fail to address---public transparency and community consent."*

Create a max 1-page document covering: Tool & Process, Key Findings, Verification ("Human-in-the-Loop" Check), and Critical Reflection. Full assignment prompt saved in `AI_Reading_Exercise_Class_6.tex.d/assignment_prompt.md`.

## Contents

| File | Description |
|------|-------------|
| `AI_Reading_Exercise_Class_6.tex` | LaTeX source for the one-page exercise |
| `AI_Reading_Exercise_Class_6.pdf` | Compiled PDF |
| `prompt.md` | Verbatim prompt log with timestamped user feedback + request status tracking |
| `AI_Reading_Exercise_Class_6.tex.d/assignment_prompt.md` | Verbatim assignment prompt from Canvas |
| `AI_Reading_Exercise_Class_6.tex.d/refs/sources/` | 6 downloaded primary source texts |
| `AI_Reading_Exercise_Class_6.tex.d/refs/annotations/` | 2 annotations + synthesis matrix |
| `AI_Reading_Exercise_Class_6.tex.d/refs/Verification_Audit.md` | Claim-by-claim pipeline audit (28 claims, 93% at 2+ sources) |

## Source Pipeline

All claims in the document are traced to downloaded source texts in `refs/sources/`:

| Source file | Stakeholder type | Key use |
|-------------|-----------------|---------|
| `OIG_Chicago_ShotSpotter_full.txt` | City oversight | 50K+ alerts analyzed; 9.1% evidence rate |
| `ACLU_ShotSpotter_full.txt` | Civil liberties | No community consent; proprietary algorithm; racial concentration |
| `MacArthur_ShotSpotter_full.txt` | Legal (federal lawsuit) | 117 sq mi coverage; 86% no case report; racial discrimination claim |
| `SouthSideWeekly_ShotSpotter_full.txt` | Independent journalism | Contract end Sept 2024; 1% arrest rate |
| `SidewalkLabs_MIDP_full.txt` | Vendor (Alphabet) | 12-acre plan; Civic Data Trust; 190-acre expansion |
| `Cavoukian_Resignation_full.txt` | Independent (compiled) | Privacy advisor resignation; voluntary protections; trust crisis |

## Annotations & Verification

| File | Coverage |
|------|----------|
| `01_Annotation_ShotSpotter.md` | Stakeholder analysis, accuracy vs. operational value discrepancy |
| `02_Annotation_Quayside.md` | Three governance failures, advisor resignations, what AI missed |
| `00_Synthesis_Matrix.md` | Cross-source comparison, pattern recognition, AI blind spots |
| `Verification_Audit.md` | Claim-by-claim pipeline audit (28 claims, 93% at 2+ sources) |

## How to Review the Process

1. **Writeup** (`AI_Reading_Exercise_Class_6.pdf`) — inline APA citations trace each claim to a source
2. **Prompt log** (`prompt.md`) — every user directive timestamped verbatim, with completion status
3. **Source files** (`refs/sources/*_full.txt`) — downloaded primary sources with line references
4. **Annotations** (`refs/annotations/0*_Annotation_*.md`) — stakeholder analysis per source
5. **Verification audit** (`refs/Verification_Audit.md`) — every claim mapped through full pipeline
6. **Git history** — `git log --oneline` shows incremental commits at each major step
