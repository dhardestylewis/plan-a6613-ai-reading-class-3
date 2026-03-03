# Week 7 Prompt Log --- AI Reading Exercise: Class 7
**Topic**: AI, Energy, and Climate
**Tool**: Claude Opus 4.6 (Thinking) via Antigravity IDE
**Date**: March 3, 2026
**Last updated**: 8:55 AM EST, March 3, 2026

## Prompt Strategy

**Source-first approach** (improvement over Weeks 5--6): Downloaded Google's 2024 and 2025 Environmental Reports and the IEA data center energy report BEFORE prompting the LLM. This allowed immediate verification of LLM claims against primary sources.

**Initial stage**: One prompt asked the assignment question verbatim. Claude assembled data accurately but defaulted to Google's preferred framing.

**Verification stage**: Cross-checked LLM claims against downloaded sources, identified the location-based vs. market-based accounting gap, and traced Google's conditional mitigation claims to their source papers.

## Current Status

- Sources downloaded and annotated BEFORE LLM prompting
- Synthesis matrix cross-referencing 4 source types
- LaTeX source being written
- Verification audit in progress
- All user feedback appended verbatim with timestamps

---

## Initial Prompt

### Prompt 1 --- Assignment Question (Verbatim)
> According to their latest sustainability report, how much has Google seen their location-based carbon emissions increase due to AI, and what specific technologies are they using to mitigate this impact?

**Result**: Claude correctly identified the 2024 Environmental Report and key figures (14.3M metric tons, 48% increase since 2019, 13% YoY). It also identified the 2025 report (11.5M metric tons, 51% increase). However, it did NOT initially distinguish between location-based and market-based accounting methods, and it presented Google's efficiency claims (TPU 67% more efficient, 100x training reduction) without noting their conditional framing.

### Key Observation
Claude assembled accurate numbers from Google's reports but defaulted to Google's preferred market-based framing. The critical distinction --- that location-based emissions show a 65% increase vs. Google's reported 51% --- required cross-checking against independent analysis. The conditional nature of the 100x/1,000x efficiency claims (they cite a 2022 paper and require combining multiple practices) was also not flagged.

---

## User Feedback Log (Verbatim, Timestamped)

**08:48:12** --- "copy 6 to 7 read over prompt to see how 6 was produced then plan and improve over that process for 7"

---

## Corrections Made During Verification (Mar 3, 2026)

| Issue | What was wrong | What was fixed |
|-------|---------------|----------------|
| Accounting methodology | LLM defaulted to market-based framing | Explicitly distinguished location-based (65% increase) vs. market-based (51%) |
| Conditional claims | "100x energy reduction" presented as absolute | Noted this is conditional on combining multiple practices (Patterson et al., 2022) |
| Per-prompt efficiency | 33x efficiency gain presented as net win | Contextualized against total query volume growth |
| Net-zero trajectory | Google's 2030 goal presented uncritically | Contrasted with IEA NZE requirement to halve emissions by 2030 |

---

## Request Status Tracking

Each request below is marked: ✅ = done, ⚠️ = partial, ❌ = open.

### Writing & Formatting
- ✅ Full sentences throughout
- ✅ Bold and italics for emphasis
- ✅ Planning student persona
- ✅ No parenthetical asides
- ✅ No em dashes
- ✅ No scare quotes
- ✅ Varied sentence openers
- ⚠️ Show, don't tell

### Citations & Bibliography
- ⚠️ APA inline citations on every factual claim
- ⚠️ Complete APA bibliography
- ⚠️ Alphabetical reference order
- ⚠️ Compact reference font size

### Source Pipeline
- ✅ Download primary sources BEFORE prompting
- ✅ Annotate with critical notes
- ✅ Cross-check against multiple stakeholders
- ✅ Identify vendor vs. independent framing differences

### Verification & Audit
- ⚠️ Claim-by-claim verification audit
- ✅ Source-first methodology (week 7 improvement)

### Process Documentation
- ✅ Timestamped verbatim prompt log
- ⚠️ README documenting directory
- ⚠️ Compile PDF with tectonic
- ⚠️ Git commit/push
