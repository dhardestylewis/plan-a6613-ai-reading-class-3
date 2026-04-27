# Week 11: AI and Public Safety — AI Reading Exercise

**Course**: PLAN A6613: AI and the Future of Cities (Spring 2026)
**Author**: Daniel Hardesty Lewis
**Date**: April 6, 2026

## Directory Structure
```
week11/
â”œâ”€â”€ README.md                    # This file (Includes V4 Methodology)
â”œâ”€â”€ assignment.tex               # LaTeX source (Hybrid extraction + Semantic Tracing + Adversarial Audit)
â”œâ”€â”€ assignment.pdf               # Compiled PDF
â”œâ”€â”€ prompt.md                    # Full prompt log
â”œâ”€â”€ synthesis_matrix.md          # Cross-source synthesis matrix
â”œâ”€â”€ audit_table.md               # **V4 Adversarial Verification Audit Protocol**
â”œâ”€â”€ sources/
â”‚   â”œâ”€â”€ aclu_pr_2024.md             # Source 1: ACLU (Advocacy)
â”‚   â”œâ”€â”€ dpd_policy_2024.md          # Source 2: DPD Revised Policy (Government)
â”‚   â””â”€â”€ dataworks_vendor.md         # Source 3: DataWorks Plus (Industry)
â””â”€â”€ annotations/
    â”œâ”€â”€ aclu_pr_2024_annotated.md   # Annotations
    â”œâ”€â”€ dpd_policy_2024_annotated.md
    â””â”€â”€ dataworks_plus_vendor_annotated.md
```

## Advanced Methodology: V4 Adversarial Audit Protocol

This directory executes the ultimate refinement of the Source-First verification framework, designed to solve the epistemological trade-off between AI hallucination safety (V1) and elevated academic prose (V2), while destroying the "closed-loop" assumption (V3).

The `audit_table.md` utilizes a **Trifurcated System**:

1. **Track 1: Strict Data Extraction (V1 Rules)**
   Empirical facts, settlement amounts ($300,000), and legal directives. Structurally forbidden from paraphrase.
2. **Track 2: Semantic Tracing (V2 Rules)**
   Qualitative rhetoric, theoretical impacts (e.g., "automation bias"), granting editorial freedom for high-level academic synthesis.
3. **Track 3: Adversarial External Audit (V4 Override)**
   Mandatory external query designed to disprove the primary sources. Here, it triggered a NIST evaluation check, disproving the ACLU's blanket claim of algorithmic racism and redefining the danger as the intersection of "low-quality operational input" and "human automation bias."

## Throughline Thesis
Industry positions facial recognition technology merely as a neutral investigative tool kept in check by a "Human-in-the-Loop." However, an adversarial synthesis proves that while modern algorithms may approach lab neutrality, real-world deployment on low-quality data reliably triggers catastrophic human automation bias, as seen in Detroit. Municipalities are being forced to enact aggressive, legally binding protocols to actively degrade the institutional authority of the algorithm to protect civil liberties.

## Compilation
```bash
pdflatex -interaction=nonstopmode assignment.tex
```

