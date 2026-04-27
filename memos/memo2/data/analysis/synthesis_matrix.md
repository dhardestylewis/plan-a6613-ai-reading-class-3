# Memo 2 Synthesis Matrix: NYC MyCity Chatbot — From Launch to Shutdown

This matrix synthesizes claims across six primary sources spanning the chatbot's lifecycle (2023–2026), organized by the memo's three required analytical dimensions.

## I. Service Selection & How It Works

| Analytical Claim | Government Frame (NYC Press Release, 2023) | Investigative Reality (The Markup, 2024) | Advocacy/Wire (AP News, 2024) | Follow-Up (Fast Company, 2024; Vice, 2026) | Synthesis |
|---|---|---|---|---|---|
| **Purpose** | "Access trusted information from more than 2,000 NYC Business web pages" on compliance, incentives, best practices | System hallucinates answers independent of its corpus | Provides false info on tenant/labor rights | Designed to replace human navigation of municipal code | **Tool fails its core mandate: replaces bureaucratic friction with legal friction** |
| **AI Approach** | MyCity portal + Microsoft Azure AI | RAG over 2,000 web pages, but outputs not constrained to retrieval | Powered by same probabilistic generation as ChatGPT | "Official NYC Business information" framing contradicts "not professional or legal advice" disclaimers | **RAG-based LLM deployed in deterministic-answer domain** |
| **User Experience** | "Thousands of people with timely, accurate answers" (OTI) | Tips, Section 8, cashless: confident inversions of statute | "Wrong in some areas" (Adams); "reckless and irresponsible" (Stoyanovich) | 58,000 questions, claimed 95% accuracy; "functionally unusable" (Mamdani, 2026) | **Non-deterministic outputs in a domain requiring 100% accuracy** |

## II. Service Delivery: Benefits and Risks

| Dimension | Evidence For | Evidence Against | Source Trace |
|---|---|---|---|
| **Effectiveness** | 58,000 questions answered; 24/7 availability | 5% error rate = ~2,900 potentially harmful answers; independent investigations found persistent errors | Vice 2026 [EFFECTIVENESS]; Markup 2024 [Hallucinated Legal Risk] |
| **Equity** | Interface accessible in multiple languages | Errors appeared across languages (Markup); least-digitally-literate users least equipped to parse "beta" disclaimers vs. "official information" branding; unbanked immigrants most vulnerable to cashless policy misinformation | Markup 2024 [RAG Intent]; Fast Company 2024 [EQUITY] |
| **City Workers** | Intended to reduce need for human navigation of code | Created unfunded labor: housing advocates (Black at Legal Services NYC) had to test and correct bot; community organizations became involuntary quality assurance | AP News 2024 [Expert Verification]; Fast Company 2024 [CITY_WORKERS] |

## III. Viability & Governance

| Dimension | Evidence | Source Trace |
|---|---|---|
| **Financial Sustainability** | $600K+ development cost / 58,000 queries = ~$10.34/question over 28 months; NYC 311 handles ~25M contacts/year | Vice 2026 [FINANCIAL_SUSTAINABILITY] |
| **Accountability** | 2023 AI Action Plan: voluntary principles only; Local Law 144 (2021): narrowly scoped to hiring; GUARD Act (Nov 2025): mandatory standards, pre-deployment audits, Office of Algorithmic Data Accountability | GovTech 2025 [ACCOUNTABILITY]; NYC Press Release 2023 [Policy Origin] |
| **Looking Ahead** | NY State SB 7263 (2026): chatbot liability for unauthorized professional advice; GUARD Act pre-deployment assessment would have caught MyCity issues | GovTech 2025 [LOOKING_AHEAD] |

## Verification Traces (Sample)

| Claim | Source → Annotation → Tag |
|---|---|
| Chatbot cost >$600K | Vice 2026 → Annotation → [FINANCIAL_SUSTAINABILITY] |
| Mamdani: "functionally unusable" | Vice 2026 → Annotation → [GOVERNANCE_FAILURE] |
| GUARD Act passed Nov 2025 | GovTech 2025 → Annotation → [ACCOUNTABILITY] |
| SB 7263 chatbot liability bill | GovTech 2025 → Annotation → [LOOKING_AHEAD] |
| Chatbot told users employers could take tips | Markup 2024 → Annotation → [Hallucinated Legal Risk] |
| Stoyanovich: "reckless and irresponsible" | AP News 2024 → Annotation → [Expert Verification] |
| Black: "should be taken down" | Markup 2024 → Annotation → [Legal Jeopardy] |
