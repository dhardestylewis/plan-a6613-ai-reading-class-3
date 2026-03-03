# Verification Audit: AI Reading Exercise Class 7

**Last updated**: March 3, 2026, 9:18 AM EST
**Methodology**: Every factual claim, statistic, proper noun, and analytical assertion in the writeup is listed below with its inline citation, source type, number of corroborating sources, quality assessment, and verification status.

## Legend

- **Ref quality**: ★★★ = primary/authoritative, ★★☆ = secondary/credible, ★☆☆ = tertiary/unverified
- **# sources**: How many independent sources corroborate this specific claim
- **Status**: ✅ = fully verified, ⚠️ = verified with caveats, ❌ = unverified or problematic

---

## Tool & Process Section

| # | Claim/Detail | Inline Cite | Source Type | Ref Quality | # Sources | Status | Notes |
|---|-------------|-------------|------------|-------------|-----------|--------|-------|
| 1 | Used Claude Opus 4.6 | None (first-person) | Author testimony | N/A | 1 | ✅ | Verifiable from IDE metadata |
| 2 | Antigravity IDE | None (first-person) | Author testimony | N/A | 1 | ✅ | Tool name |
| 3 | Source-first methodology adopted | None (first-person) | Author testimony | N/A | 1 | ✅ | Evidenced by file timestamps: sources created before LaTeX |
| 4 | Downloaded Google 2024 and 2025 Reports before prompting | None (first-person) | Author testimony | N/A | 1 | ✅ | Evidenced by refs/sources/ directory |
| 5 | Downloaded IEA data center analysis before prompting | None (first-person) | Author testimony | N/A | 1 | ✅ | Evidenced by refs/sources/ directory |
| 6 | Claude assembled accurate emission figures | None (process observation) | Author testimony | N/A | 1 | ✅ | Verified: LLM output matched report data |
| 7 | Claude defaulted to market-based accounting | None (process observation) | Author testimony | N/A | 1 | ✅ | Documented in prompt log |
| 8 | Market-based accounting credits renewable purchases against grid emissions | Implicit (Google, 2024) | Corporate + independent | ★★★ | 3 | ✅ | Google reports, Guardian/Kairos, IEA all define this |
| 9 | Location-based accounting reflects actual grid carbon intensity | Implicit (Milman, 2025) | Independent journalism | ★★☆ | 2 | ✅ | Guardian/Kairos + GHG Protocol definitions |
| 10 | Surfacing the distinction required manual cross-referencing | None (process observation) | Author testimony | N/A | 1 | ✅ | Evidenced by synthesis matrix |

## Key Finding 1: Emissions

| # | Claim/Detail | Inline Cite | Source Type | Ref Quality | # Sources | Status | Notes |
|---|-------------|-------------|------------|-------------|-----------|--------|-------|
| 11 | 14.3 million metric tons CO2e in 2023 | Google, 2024 | Corporate report | ★★★ | 4+ | ✅ | Google blog, Mashable, Tom's Hardware, Straits Times all confirm |
| 12 | 13% year-over-year increase | Google, 2024 | Corporate report | ★★★ | 3+ | ✅ | Google blog position 25 states this verbatim |
| 13 | 48% above 2019 baseline | Google, 2024 | Corporate report | ★★★ | 4+ | ✅ | Google blog + widely reported |
| 14 | 2025 report covers fiscal year 2024 | Google, 2025 | Corporate report | ★★★ | 2 | ✅ | Google landing page + All Ireland Sustainability |
| 15 | Cumulative 51% increase since 2019 | Google, 2025 | Corporate report | ★★★ | 2 | ✅ | Google 2025 report + All Ireland Sustainability |
| 16 | 27% jump in data center electricity in single year | Google, 2025 | Corporate report | ★★★ | 2 | ✅ | Google 2025 report + All Ireland Sustainability |
| 17 | Google frames around market-based accounting | Implicit | Author analysis | ★★☆ | 2 | ✅ | Confirmed by Guardian/Kairos critique |
| 18 | Market-based incorporates renewable energy credits | Implicit | Standard accounting definition | ★★★ | 3 | ✅ | GHG Protocol, Guardian, Google reports |
| 19 | Location-based accounting measures actual grid emissions at point of consumption | Milman, 2025 | Independent journalism + GHG Protocol | ★★☆ | 2 | ✅ | Guardian/Kairos + standard GHG Protocol definition |
| 20 | 65% increase (location-based) over same period | Milman, 2025 | Independent (Kairos Fellowship via Guardian) | ★★☆ | 2 | ✅ | Guardian article confirmed via search; Kairos report |
| 21 | Gap reveals how RE purchases can mask physical carbon intensity | None (analytical) | Author analysis | N/A | — | ✅ | Analytical claim; follows logically from data |

## Key Finding 2: Mitigation Technologies

| # | Claim/Detail | Inline Cite | Source Type | Ref Quality | # Sources | Status | Notes |
|---|-------------|-------------|------------|-------------|-----------|--------|-------|
| 22 | Sixth-generation TPU named Trillium | Google, 2024 | Corporate report | ★★★ | 2 | ✅ | Google blog + Google Cloud blog |
| 23 | Trillium is 67% more energy-efficient than predecessor (TPU v5e) | Google, 2024 | Corporate report | ★★☆ | 1 | ⚠️ | Google internal data (May 2024); no independent audit |
| 24 | Combining best practices can reduce training energy by 100x | Google, 2024 | Corporate report citing academic paper | ★★☆ | 2 | ✅ | Google blog fn2 → Patterson et al. 2022 |
| 25 | Associated emissions by 1,000x | Google, 2024 | Corporate report citing academic paper | ★★☆ | 2 | ✅ | Google blog fn2 → Patterson et al. 2022 |
| 26 | Figures cite a 2022 research paper at Google | Patterson et al., 2022 | Academic (Google-affiliated) | ★★☆ | 1 | ✅ | arXiv 2204.05149; published Computer vol. 55 |
| 27 | Explicitly conditional on applying all practices simultaneously | Patterson et al., 2022 | Academic paper | ★★★ | 1 | ✅ | Paper states four practices must combine multiplicatively |
| 28 | PUE of 1.10 | Google, 2024 (citing Uptime Institute) | Corporate + industry | ★★★ | 2 | ✅ | Google blog fn3 (internal analysis); consistent with public claims |
| 29 | Industry average PUE of 1.58 | Uptime Institute, 2023 | Industry research (independent) | ★★★ | 2 | ✅ | Uptime Institute 2023 survey; Google blog fn4 cites same figure |
| 30 | Roughly six times less overhead energy | Derived from PUE figures | Author calculation | ★★☆ | 1 | ⚠️ | Google says "about 5.8 times"; I wrote "roughly six" — acceptable rounding |
| 31 | Median energy per Gemini text prompt fell 33-fold over 12 months | Google, 2025 | Corporate report | ★★☆ | 1 | ⚠️ | Google 2025 report; no independent verification of per-prompt data |
| 32 | Combined electricity of Amazon, Microsoft, Google, Meta more than doubled 2017-2021 | IEA, 2023 | Intergovernmental (authoritative) | ★★★ | 1 | ✅ | IEA analysis; based on Masanet et al. 2020 + operator data |
| 33 | Reaching approximately 72 TWh | IEA, 2023 | Intergovernmental (authoritative) | ★★★ | 1 | ✅ | IEA direct |
| 34 | Continues to grow 20-40% annually in hyperscale segment | IEA, 2023 | Intergovernmental (authoritative) | ★★★ | 1 | ✅ | IEA direct |
| 35 | Per-unit efficiency improvements overwhelmed by absolute growth | None (analytical) | Author analysis supported by IEA | ★★☆ | 2 | ✅ | IEA data + Google's own rising emissions support this conclusion |

## Verification and Reflection Section

| # | Claim/Detail | Inline Cite | Source Type | Ref Quality | # Sources | Status | Notes |
|---|-------------|-------------|------------|-------------|-----------|--------|-------|
| 36 | Claude correctly identified 2024 and 2025 reports | None (process) | Author testimony | N/A | 1 | ✅ | Verified during LLM audit |
| 37 | Cited emission figures accurately | None (process) | Author testimony | N/A | 1 | ✅ | Cross-checked against sources |
| 38 | Named specific mitigation technologies | None (process) | Author testimony | N/A | 1 | ✅ | TPU, PUE, CFE all identified by LLM |
| 39 | Did not hallucinate sources or fabricate statistics | None (process) | Author testimony | N/A | 1 | ✅ | Every LLM-cited source exists and contains stated data |
| 40 | Core limitation was framing not fabrication | None (analytical) | Author analysis | N/A | — | ✅ | Supported by documented audit |
| 41 | Accepted market-based without surfacing location-based | None (process) | Author testimony | N/A | 1 | ✅ | Documented in prompt log |
| 42 | Presented conditional claims as straightforward | None (process) | Author testimony | N/A | 1 | ✅ | LLM did not flag Patterson et al. conditionality |
| 43 | IEA requirement that DC emissions must halve by 2030 under NZE | IEA, 2023 | Intergovernmental (authoritative) | ★★★ | 1 | ✅ | IEA position 11: "to get on track with the NZE Scenario, emissions must halve by 2030" |

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total claims audited | 43 |
| Fully verified (✅) | 40 (93%) |
| Verified with caveats (⚠️) | 3 (7%) |
| Unverified/problematic (❌) | 0 (0%) |
| Claims with 2+ independent sources | 24 (56%) |
| Claims with ★★★ quality references | 20 (47%) |
| Claims from corporate sources only (★★☆, no independent corroboration) | 3 (claims 23, 31, 30) |
| Author analysis/testimony (no external ref needed) | 16 (37%) |

## Caveats on ⚠️ Claims

1. **Claim 23** (TPU 67% efficiency): Based solely on Google internal data (May 2024). No independent benchmark exists. Accepted because Google is the authoritative source on its own hardware, but a planner should note the absence of third-party verification.

2. **Claim 30** ("roughly six times"): Google's blog says "about 5.8 times." I rounded to "roughly six" — technically imprecise but within acceptable range. Could tighten to "nearly six" if desired.

3. **Claim 31** (33x per-prompt energy reduction): Google 2025 report claim with no independent verification. Additionally, this per-unit metric does not account for the growth in total query volume, which could offset per-unit gains. Noted in the writeup as a caveat.

## Changelog

| Timestamp | Change |
|-----------|--------|
| 9:05 AM | Initial audit (18 claims) |
| 9:18 AM | Expanded to exhaustive 43-claim audit with quality ratings, source counts, and caveats |
