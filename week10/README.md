# Week 10: AI and City Building — AI Reading Exercise

**Course**: PLAN A6613: AI and the Future of Cities (Spring 2026)
**Author**: Daniel Hardesty Lewis
**Date**: March 31, 2026

## Directory Structure

```
week10/
├── README.md                    # This file
├── assignment.tex               # LaTeX source (two-column, compact)
├── assignment.pdf               # Compiled PDF
├── prompt.md                    # Full prompt log with claim audit
├── synthesis_matrix.md          # Cross-source synthesis matrix
├── sources/
│   ├── walker_lincoln_2024.md            # Source 1: Lincoln Institute (policy)
│   ├── symbium_stanford_2024.md          # Source 2: Symbium/Stanford CodeX (gov-tech)
│   └── vendor_testfit_doxel_2024.md      # Source 3: TestFit + Doxel (industry)
└── annotations/
    ├── walker_lincoln_2024_annotated.md           # Annotations: policy source
    ├── symbium_stanford_2024_annotated.md          # Annotations: gov-tech source
    └── vendor_testfit_doxel_2024_annotated.md      # Annotations: vendor source
```

## Methodology

Source-first approach (continuation of Weeks 7 and 9): three primary sources representing distinct stakeholder positions were identified and annotated before the LLM was asked to synthesize. A synthesis matrix cross-references every claim to its source and annotation tag.

## Throughline Thesis

AI tools are entering three phases of the city-building pipeline (site design, permitting, construction monitoring), each automating a form of professional judgment that currently carries individual liability. The market is deploying these tools faster than municipalities are developing audit frameworks to govern them.

## Three AI Products

1. **TestFit** — Generative site planning and feasibility analysis
2. **Symbium (Complaw®)** — Automated permitting via computational law
3. **Doxel** — Computer vision construction progress tracking

## Compilation

```bash
tectonic assignment.tex
```
