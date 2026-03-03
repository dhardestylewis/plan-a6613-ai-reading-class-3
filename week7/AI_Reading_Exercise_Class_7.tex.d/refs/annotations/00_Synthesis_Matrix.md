# Synthesis Matrix: Google's AI-Driven Carbon Emissions

## Cross-Source Comparison

| Claim | Google Blog (2024 Report) | Google 2025 Report | IEA | Independent Analyses |
|-------|--------------------------|-------------------|-----|---------------------|
| Emissions level | 14.3M mt CO2e (2023) | 11.5M mt (2024) | N/A (global: 330 Mt CO2e) | 14.3M confirmed widely |
| % increase since 2019 | 48% | 51% (market-based) | N/A | 65% (location-based; Guardian Feb 2025) |
| YoY increase | 13% (2022→2023) | 11% (2023→2024) | N/A | Confirmed |
| Primary driver | DC energy + supply chain | AI + DC expansion | Hyperscaler electricity doubled 2017-2021 | AI energy demand |
| TPU efficiency | 67% more efficient (v6 vs v5e) | Same claim | N/A | Unchallenged but also unaudited |
| PUE | 1.10 vs 1.58 industry | Same claim | Industry data consistent | Uptime Institute methodology caveats |
| Training energy savings | 100x energy, 1,000x emissions | Same | N/A | Conditional: "when used together" |
| Per-prompt efficiency | N/A | 33x energy, 44x carbon (Gemini 12mo) | N/A | Does not account for total volume growth |
| CFE progress | 64% global average; 10 regions 90%+ | N/A | N/A | Does not equate to 24/7 matching |
| Net-zero goal | 2030 | 2030 | NZE Scenario: need to HALVE by 2030 | IEA benchmark makes Google's trajectory inconsistent |

## Key Patterns

1. **Accounting methodology gap**: Google prefers market-based accounting (includes renewable energy credits/purchases). Location-based accounting — which reflects actual grid emissions — tells a worse story. Guardian analysis: 65% increase vs. Google's 51%.

2. **Efficiency vs. absolute growth**: Google's data centers ARE more efficient (PUE 1.10), but absolute energy consumption and emissions continue to rise rapidly. The IEA confirms this pattern: hyperscaler efficiency gains are overwhelmed by demand growth.

3. **Conditional mitigation claims**: The 100x/1,000x training reduction is conditional on combining multiple practices and cites a 2022 paper. The 33x per-prompt reduction in Gemini ignores that total query volume has also grown, potentially offsetting per-unit gains.

4. **Offsetting vs. reducing**: Google's clean energy purchases and geothermal investments are real, but they offset grid emissions rather than reducing Google's actual energy consumption. The distinction between offsetting and reducing is central to a planner's evaluation.

## What the LLM Missed

When prompted with the assignment question, the AI (this instance of Claude):
- Correctly identified the 2024 Environmental Report and key emission figures
- Did NOT initially distinguish between location-based and market-based accounting methods
- Accepted Google's efficiency claims (TPU, PUE) without noting their conditional framing
- Did not surface the IEA's finding that hyperscaler efficiency gains are being overwhelmed by volume
- Did not flag that Google's 51% increase trajectory is inconsistent with the IEA's NZE requirement to halve emissions by 2030
