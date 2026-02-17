# Verification Audit — Week 5 AI Reading Exercise

Every factual claim in `AI_Reading_Exercise_Class_5.tex` is listed below with its full source pipeline.

**Pipeline key**: ✅ = completed, ❌ = not done, N/A = not applicable

## Claims by Section

### Tool & Process (line 67)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized |
|---|-------|----------|-------------|------------|------|----------------------|-------------|
| 1 | Used Claude Opus 4.6 via Antigravity IDE | N/A | N/A | N/A | N/A | N/A | ✅ (direct experience) |
| 2 | First prompt returned vague IoT descriptions | N/A | N/A | N/A | N/A | N/A | ✅ (prompt.md) |
| 3 | Three rounds of prompting | N/A | N/A | N/A | N/A | N/A | ✅ (prompt.md) |
| 4 | Vendor-reported vs city data discrepancies found | ✅ | ✅ Automotus + PGH DOMI | ✅ both | ✅ | ✅ L13-L16 city, L5-L8 vendor | ✅ |

### Finding 1: Automotus in Pittsburgh (line 72)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized |
|---|-------|----------|-------------|------------|------|----------------------|-------------|
| 5 | 75 commercial loading zones | ✅ | ✅ Automotus vendor page | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ L18 city gov file | ✅ |
| 6 | Cameras on streetlight poles reading license plates | ✅ | ✅ Automotus vendor page | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ L8-L12 city gov | ✅ |
| 7 | Enforcing tiered time limits, automating payment | ✅ | ✅ Automotus vendor page | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ L10-L11 city gov | ✅ |
| 8 | Automotus claims 40% higher turnover | ✅ | ✅ Automotus vendor page | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ 01_Annotation L22 | ✅ |
| 9 | Automotus claims 95% less double-parking | ✅ | ✅ Automotus vendor page | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ 01_Annotation L23 | ✅ |
| 10 | City reports 70% turnover increase | ✅ | ✅ PGH DOMI search results | ✅ `Pittsburgh_CityGov_full.txt` | ✅ | ✅ L13 | ✅ |
| 11 | City reports 60% drop in park duration | ✅ | ✅ PGH DOMI search results | ✅ `Pittsburgh_CityGov_full.txt` | ✅ | ✅ L14 | ✅ |
| 12 | DOE $3.8M grant, Vehicle Technologies Office, Aug 2021 | ✅ | ✅ Post-Gazette, CMU, Harvard | ✅ `DOE_Grant_full.txt` | ✅ | ✅ L1-L2 | ✅ |
| 13 | Three-year scale-up | ✅ | ✅ DOE grant records | ✅ `DOE_Grant_full.txt` | ✅ | ✅ L2 | ✅ |
| 14 | SaaS revenue from automated payments | ✅ | ✅ Automotus vendor page | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ 01_Annotation | ✅ |
| 15 | Closed operational loop (AI observes, decides, acts) | ✅ | ✅ Automotus + city docs | ✅ both | ✅ | ✅ 01_Annotation | ✅ |

### Finding 2: Flow Labs in North Carolina (line 75)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized |
|---|-------|----------|-------------|------------|------|----------------------|-------------|
| 16 | More than 2,500 intersections | ✅ | ✅ Flow Labs, StateScoop, MeriTalk | ✅ `Flow_Labs_NCDOT_full.txt` | ✅ | ✅ L1 | ✅ |
| 17 | July 2025 deployment | ✅ | ✅ StateScoop, GovTech | ✅ `GovTech_NCDOT_full.txt` | ✅ | ✅ L3 | ✅ |
| 18 | Largest such deployment in US | ✅ | ✅ Flow Labs, StateScoop | ✅ `Flow_Labs_NCDOT_full.txt` | ✅ | ✅ L2 | ✅ |
| 19 | Connected vehicle GPS data | ✅ | ✅ Flow Labs vendor page | ✅ `Flow_Labs_NCDOT_full.txt` | ✅ | ✅ L4-L5 | ✅ |
| 20 | No field studies or new hardware needed | ✅ | ✅ Flow Labs, GovTech | ✅ `GovTech_NCDOT_full.txt` | ✅ | ✅ L6 | ✅ |
| 21 | System only recommends changes | ✅ | ✅ Flow Labs docs | ✅ `Flow_Labs_NCDOT_full.txt` | ✅ | ✅ 02_Annotation | ✅ |
| 22 | Human engineer makes final call | ✅ | ✅ Flow Labs + NCDOT + GovTech | ✅ all three | ✅ | ✅ 02_Annotation | ✅ |
| 23 | Aaron Moody quote: "oversight by engineering staff" | ✅ | ✅ GovTech article | ✅ `GovTech_NCDOT_full.txt` | ✅ | ✅ L7 | ✅ |
| 24 | SaaS contract in operations budgets | ✅ | ✅ StateScoop | ✅ `Flow_Labs_NCDOT_full.txt` | ✅ | ✅ 02_Annotation | ✅ |

### Finding 3: Google Tapestry & PJM (line 78)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized |
|---|-------|----------|-------------|------------|------|----------------------|-------------|
| 25 | DeepMind AI to model grid topology | ✅ | ✅ X project page | ✅ `Tapestry_Google_X_full.txt` | ✅ | ✅ L7-L11 | ✅ |
| 26 | 67 million people across 13 states + DC | ✅ | ✅ Wikipedia, FERC, pjm.com, OSU | ✅ `PJM_Newsroom_full.txt` | ✅ | ✅ L4-L5 | ✅ verified externally |
| 27 | Interconnection queue for new renewables | ✅ | ✅ X page + PJM | ✅ `Tapestry_Google_X_full.txt` | ✅ | ✅ L5-L6 PJM | ✅ |
| 28 | Not yet deployed: multi-year development partnership | ✅ | ✅ X project page | ✅ `Tapestry_Google_X_full.txt` | ✅ | ✅ L42-L44, 03_Annotation | ✅ |
| 29 | Google funds AI, PJM provides data | ✅ | ✅ X page + PJM newsroom | ✅ both | ✅ | ✅ 03_Annotation | ✅ |
| 30 | Faster interconnection benefits Google data centers | ✅ | ✅ Yale E360 (Berreby 2024) | ✅ `YaleE360_AI_Energy_full.txt` | ✅ | ✅ L12-L14 | ✅ |
| 31 | AI data centers strain the grid (conflict of interest) | ✅ | ✅ Yale E360 (Berreby 2024) | ✅ `YaleE360_AI_Energy_full.txt` | ✅ | ✅ L1, L10-L14 | ✅ |

### Verification Section (lines 81-86)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized |
|---|-------|----------|-------------|------------|------|----------------------|-------------|
| 32 | Vendor stats: 40% turnover, 95% double-parking | ✅ | ✅ Automotus | ✅ | ✅ | ✅ 01_Annotation | ✅ |
| 33 | City stats: 70% turnover, 40% double-parking | ✅ | ✅ PGH DOMI | ✅ | ✅ | ✅ Pittsburgh_CityGov L13, L16 | ✅ |
| 34 | AI misidentified parking vs commercial loading | ✅ | ✅ Automotus vendor page | ✅ | ✅ | ✅ 01_Annotation | ✅ |
| 35 | Three sources contradict "controls" claim | ✅ | ✅ Flow Labs, StateScoop, GovTech | ✅ all | ✅ | ✅ 02_Annotation | ✅ |
| 36 | Aaron Moody: "engineering staff retain oversight" | ✅ | ✅ GovTech (Raths 2025) | ✅ | ✅ | ✅ GovTech L7 | ✅ |
| 37 | X page describes multi-year development | ✅ | ✅ X project page | ✅ | ✅ | ✅ Tapestry L42-44 | ✅ |
| 38 | Google conflict of interest per Berreby 2024 | ✅ | ✅ Yale E360 | ✅ | ✅ | ✅ YaleE360 L12-14 | ✅ |

### Critical Reflection (line 88)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized |
|---|-------|----------|-------------|------------|------|----------------------|-------------|
| 39 | AI treated all three as equivalent | N/A | N/A | N/A | N/A | N/A | ✅ (prompt.md, direct experience) |
| 40 | Different levels of autonomy and readiness | ✅ | ✅ All sources | ✅ all | ✅ | ✅ 00_Synthesis_Matrix | ✅ |
| 41 | Cross-check every statistic against multiple stakeholders | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (this audit) |

## Summary

- **Total claims**: 41
- **Claims with full pipeline (searched → downloaded → read → annotated → synthesized)**: 37 / 41
- **Claims based on direct experience only**: 4 / 41 (tool use, prompting process)
- **Claims verified against 2+ independent sources**: 15 / 41
- **Downloaded source files**: 8
- **Annotation files with line references**: 3 + synthesis matrix
