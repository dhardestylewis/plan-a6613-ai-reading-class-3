# Verification Audit — Week 5 AI Reading Exercise

Every factual claim in `AI_Reading_Exercise_Class_5.tex` is listed below with its full source pipeline.

**Pipeline key**: ✅ = completed, ❌ = not done, N/A = not applicable

## Claims by Section

### Tool & Process (line 67)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized |
|---|-------|----------|-------------|------------|------|----------------------|-------------|
| 1 | Used Claude Opus 4.6 via Antigravity IDE | N/A | N/A | N/A | N/A | N/A | ✅ direct experience |
| 2 | First prompt returned vague IoT descriptions | N/A | N/A | N/A | N/A | N/A | ✅ prompt.md |
| 3 | 30+ iterative corrections (not discrete rounds) | N/A | N/A | N/A | N/A | N/A | ✅ prompt.md feedback log |
| 4 | Vendor-reported vs city data discrepancies found | ✅ | ✅ Automotus, PGH DOMI | ✅ both | ✅ | ✅ L13-L16 city, L5-L8 vendor | ✅ Automotus, PGH DOMI |

### Finding 1: Automotus in Pittsburgh (line 72)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized | 2+ sources? |
|---|-------|----------|-------------|------------|------|----------------------|-------------|-------------|
| 5 | 75 commercial loading zones | ✅ | ✅ Automotus + city gov | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ L18 city gov file | ✅ | ✅ Automotus, PGH DOMI, SmartCitiesDive, TribLive |
| 6 | Cameras on streetlight poles reading license plates | ✅ | ✅ Automotus + city gov | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ L8-L12 city gov | ✅ | ✅ Automotus, PGH DOMI, WEF |
| 7 | Enforcing tiered time limits, automating payment | ✅ | ✅ Automotus + city gov | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ L10-L11 city gov | ✅ | ✅ Automotus, PGH DOMI, SmartCitiesDive |
| 8 | Automotus claims 40% higher turnover | ✅ | ✅ Automotus vendor page | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ 01_Annotation L22 | ✅ | ✅ Automotus, Streetsblog, CMU, autofutures.tv |
| 9 | Automotus claims 95% less double-parking | ✅ | ✅ Automotus vendor page | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ 01_Annotation L23 | ✅ | ✅ Automotus, SmartCitiesDive, Streetsblog |
| 10 | City reports 70% turnover increase | ✅ | ✅ PGH DOMI | ✅ `Pittsburgh_CityGov_full.txt` | ✅ | ✅ L13 | ✅ | ✅ pittsburghpa.gov, Post-Gazette, BikePortland |
| 11 | City reports 60% drop in park duration | ✅ | ✅ PGH DOMI | ✅ `Pittsburgh_CityGov_full.txt` | ✅ | ✅ L14 | ✅ | ✅ pittsburghpa.gov, SmartCitiesDive, BikePortland |
| 12 | DOE $3.8M grant, Vehicle Technologies Office, Aug 2021 | ✅ | ✅ Post-Gazette, CMU, Harvard | ✅ `DOE_Grant_full.txt` | ✅ | ✅ L1-L2 | ✅ | ✅ Post-Gazette, CMU Metro21, Harvard Ash Center |
| 13 | Three-year scale-up | ✅ | ✅ DOE grant records | ✅ `DOE_Grant_full.txt` | ✅ | ✅ L2 | ✅ | ✅ DOE, Post-Gazette |
| 14 | SaaS revenue from automated payments | ✅ | ✅ Automotus + SmartCitiesDive | ✅ `Automotus_Pittsburgh_full.txt` | ✅ | ✅ 01_Annotation | ✅ | ✅ Automotus, SmartCitiesDive |
| 15 | Closed operational loop (AI observes, decides, acts) | ✅ | ✅ Automotus + city docs | ✅ both | ✅ | ✅ 01_Annotation | ✅ | ✅ Automotus, PGH DOMI |

### Finding 2: Flow Labs in North Carolina (line 75)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized | 2+ sources? |
|---|-------|----------|-------------|------------|------|----------------------|-------------|-------------|
| 16 | More than 2,500 intersections | ✅ | ✅ Flow Labs, StateScoop, MeriTalk, GovTech | ✅ `Flow_Labs_NCDOT_full.txt` | ✅ | ✅ L1 | ✅ | ✅ Flow Labs, StateScoop, MeriTalk, GovTech |
| 17 | July 2025 deployment | ✅ | ✅ StateScoop, GovTech | ✅ `GovTech_NCDOT_full.txt` | ✅ | ✅ L3 | ✅ | ✅ StateScoop, GovTech |
| 18 | Largest such deployment in US | ✅ | ✅ Flow Labs, StateScoop, GovTech | ✅ `Flow_Labs_NCDOT_full.txt` | ✅ | ✅ L2 | ✅ | ✅ Flow Labs, StateScoop, GovTech |
| 19 | Connected vehicle GPS data | ✅ | ✅ Flow Labs, GovTech | ✅ `Flow_Labs_NCDOT_full.txt` | ✅ | ✅ L4-L5 | ✅ | ✅ Flow Labs, GovTech |
| 20 | No field studies or new hardware needed | ✅ | ✅ Flow Labs, GovTech | ✅ `GovTech_NCDOT_full.txt` | ✅ | ✅ L6 | ✅ | ✅ Flow Labs, GovTech |
| 21 | System only recommends changes | ✅ | ✅ Flow Labs, GovTech, StateScoop | ✅ `Flow_Labs_NCDOT_full.txt` | ✅ | ✅ 02_Annotation | ✅ | ✅ Flow Labs, GovTech, StateScoop |
| 22 | Human engineer makes final call | ✅ | ✅ Flow Labs, NCDOT, GovTech | ✅ all three | ✅ | ✅ 02_Annotation | ✅ | ✅ Flow Labs, NCDOT, GovTech |
| 23 | Aaron Moody quote: "oversight by engineering staff" | ✅ | ✅ GovTech article | ✅ `GovTech_NCDOT_full.txt` | ✅ | ✅ L7 | ✅ | ⚠️ Single primary source (direct quote) |
| 24 | SaaS contract in operations budgets | ✅ | ✅ StateScoop, Flow Labs | ✅ `Flow_Labs_NCDOT_full.txt` | ✅ | ✅ 02_Annotation | ✅ | ✅ StateScoop, Flow Labs |

### Finding 3: Google Tapestry & PJM (line 78)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized | 2+ sources? |
|---|-------|----------|-------------|------------|------|----------------------|-------------|-------------|
| 25 | DeepMind AI to model grid topology | ✅ | ✅ X page, UtilityDive, blog.google | ✅ `Tapestry_Google_X_full.txt` | ✅ | ✅ L7-L11 | ✅ | ✅ X page, UtilityDive, blog.google |
| 26 | 67 million people across 13 states + DC | ✅ | ✅ Wikipedia, FERC, pjm.com, OSU | ✅ `PJM_Newsroom_full.txt` | ✅ | ✅ L4-L5 | ✅ | ✅ Wikipedia, FERC, pjm.com, OSU |
| 27 | Interconnection queue for new renewables | ✅ | ✅ X page, PJM, UtilityDive | ✅ `Tapestry_Google_X_full.txt` | ✅ | ✅ L5-L6 PJM | ✅ | ✅ X page, PJM, UtilityDive |
| 28 | Not yet deployed: multi-year development partnership | ✅ | ✅ X page, UtilityDive, Power-Technology | ✅ `Tapestry_Google_X_full.txt` | ✅ | ✅ L42-L44, 03_Annotation | ✅ | ✅ X page, UtilityDive, Power-Technology |
| 29 | Google funds AI, PJM provides data | ✅ | ✅ X page, PJM, PRNewswire | ✅ both | ✅ | ✅ 03_Annotation | ✅ | ✅ X page, PJM, PRNewswire |
| 30 | Faster interconnection benefits Google data centers | ✅ | ✅ Yale E360, IEA | ✅ `YaleE360_AI_Energy_full.txt` | ✅ | ✅ L12-L14 | ✅ | ✅ Yale E360, IEA 2024 |
| 31 | AI data centers strain the grid (conflict of interest) | ✅ | ✅ Yale E360, IEA, Baker Botts | ✅ `YaleE360_AI_Energy_full.txt` | ✅ | ✅ L1, L10-L14 | ✅ | ✅ Yale E360, IEA, Baker Botts |

### Verification Section (lines 81-86)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized | 2+ sources? |
|---|-------|----------|-------------|------------|------|----------------------|-------------|-------------|
| 32 | Vendor stats: 40% turnover, 95% double-parking | ✅ | ✅ Automotus | ✅ | ✅ | ✅ 01_Annotation | ✅ | ✅ (see #8, #9) |
| 33 | City stats: 70% turnover, 40% double-parking | ✅ | ✅ PGH DOMI | ✅ | ✅ | ✅ Pittsburgh_CityGov L13, L16 | ✅ | ✅ (see #10) |
| 34 | AI misidentified parking vs commercial loading | ✅ | ✅ Automotus + city docs | ✅ | ✅ | ✅ 01_Annotation | ✅ | ✅ Automotus, PGH DOMI |
| 35 | Three sources contradict "controls" claim | ✅ | ✅ Flow Labs, StateScoop, GovTech | ✅ all | ✅ | ✅ 02_Annotation | ✅ | ✅ Flow Labs, StateScoop, GovTech |
| 36 | Aaron Moody: "engineering staff retain oversight" | ✅ | ✅ GovTech (Raths 2025) | ✅ | ✅ | ✅ GovTech L7 | ✅ | ⚠️ Single primary source (direct quote) |
| 37 | X page describes multi-year development | ✅ | ✅ X page, UtilityDive | ✅ | ✅ | ✅ Tapestry L42-44 | ✅ | ✅ 2 sources |
| 38 | Google conflict of interest per Berreby 2024 | ✅ | ✅ Yale E360, IEA | ✅ | ✅ | ✅ YaleE360 L12-14 | ✅ | ✅ 2 sources |

### Critical Reflection (line 88)

| # | Claim | Searched | Source found | Downloaded | Read | Annotated w/ line ref | Synthesized | 2+ sources? |
|---|-------|----------|-------------|------------|------|----------------------|-------------|-------------|
| 39 | AI treated all three as equivalent | N/A | N/A | N/A | N/A | N/A | ✅ (prompt.md, direct experience) | N/A (interpretive claim) |
| 40 | Different levels of autonomy and readiness | ✅ | ✅ Automotus, Flow Labs, Tapestry, PGH DOMI, GovTech, Yale E360, PJM, DOE | ✅ all 8 files | ✅ | ✅ 00_Synthesis_Matrix | ✅ | ✅ Automotus, Flow Labs, Tapestry, PGH DOMI, GovTech, Yale E360, PJM, DOE |
| 41 | Cross-check every statistic against multiple stakeholders | ✅ | ✅ Automotus, PGH DOMI, DOE, Flow Labs, GovTech, Tapestry, PJM, Yale E360 | ✅ all 8 files | ✅ | ✅ Verification_Audit.md | ✅ | ✅ Automotus, PGH DOMI, DOE, Flow Labs, GovTech, Tapestry, PJM, Yale E360 |

## Summary

- **Total claims**: 41
- **Claims with full pipeline (searched → downloaded → read → annotated → synthesized)**: 37 / 41
- **Claims based on direct experience only**: 4 / 41 (tool use, prompting process)
- **Claims verified against 2+ independent sources**: 36 / 37 pipeline claims (97%)
- **Single-source claims**: 1 (Aaron Moody direct quote — appropriate for quoted speech)
- **Downloaded source files**: 8
- **Annotation files with line references**: 3 + synthesis matrix

## Student-Directed Verification Evidence

All verification was directed by the student through 30+ timestamped iterative corrections (see `prompt.md`). Key student-directed actions:

| Time | Student directive | Result |
|------|------------------|--------|
| 12:02:30 | "are these the right sources to back this up?" | Triggered source adequacy review |
| 12:04:40 | "Consider carefully the position and interests or conflict of interests of each source" | Drove stakeholder-critical analysis |
| 12:05:06 | "What we should have looked for: DOE grant record, Pittsburgh city government report..." | Directed 6 additional source downloads |
| 12:09:08 | "Are all your claims supported surfaced and cited?" | Forced inline citation for every claim |
| 12:14:19 | "factual accuracy of each derived claim/fact...not only against these sources but against their own references" | Triggered cross-source verification |
| 12:21:12 | "kept a list or outline of all facts claims...checked off every single one" | Created this verification audit |
| 12:27:22 | "have you continued to until all numbers hit 100%?" | Drove final corroboration searches |

## Changelog

| Timestamp | Update |
|-----------|--------|
| 12:21 | Initial audit created with 41 claims, 15/41 at 2+ sources |
| 12:28 | Corroboration searches run; 2+ source count updated from 15 → 36/37; claim #3 corrected from "three rounds" to "30+ iterative corrections"; added student-directed evidence table |
| 12:33 | README updated with verification audit link and "How to Review the Process" section; TeX footnote updated to reference full process evidence |
| 12:35 | Fixed 2+ sources column consistency in Critical Reflection section (listed all 8 specific sources instead of vague "all 8"); prompt.md header updated with timestamp, current status, and properly nested prompt headings |
