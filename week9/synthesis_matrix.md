# Week 9 Synthesis Matrix: NYC MyCity Chatbot Liability Shift

This matrix synthesizes claims across the three primary, exhaustively annotated sources. It demonstrates how facts from official municipal framing (NYC Press Release) are contradicted or problematized by investigative reporting (The Markup) and advocacy pushback (AP News).

| Core Analytical Claim | NYC Primary Frame (Source 1) | Investigative Reality (Source 2) | Advocate Consequence (Source 3) | Synthesis Conclusion |
|-----------------------|------------------------------|----------------------------------|---------------------------------|----------------------|
| **Goal of System** | Let business owners "access trusted information from more than 2,000 NYC Business web pages." (*Source: NYC Press Release, para. 2*) | System hallucinates answers independent of the corpus due to Microsoft Azure AI predictive nature. (*Source: Lecher, The Markup, paras. 1-2*) | System provides false info on tenant/labor rights, creating legal trap. (*Source: Offenhartz, AP News, para. 3*) | **The tool fails its core mandate by replacing bureaucratic friction with legal/liability friction.** |
| **Status of System** | Part of the AI Action Plan, "the first of its kind for a major U.S. city." (*Source: NYC Press Release, para. 1*) | Includes a small note that it "may occasionally produce incorrect, harmful or biased content" but acts as official city source. (*Source: Lecher, The Markup, para. 3*) | Adams acknowledged answers were "wrong in some areas" but defended keeping it online. (*Source: Offenhartz, AP News, paras. 1-2*) | **A pilot test on regulatory compliance is reckless because citizens are the unconsenting beta testers.** |
| **Burden of Truth** | Intent is to save business owners time from reading the 2,000 pages themselves. (*Source: NYC Press Release, para. 2*) | Advised illegal acts: taking tips (violating Labor Law 196-d), refusing Section 8 vouchers (2008 law), operating cashless (2020 law). (*Source: Lecher, The Markup, para. 4*) | Stoyanovich: city is "rolling out software that is unproven without oversight"; Rosalind Black: chatbot "should be taken down" if inaccurate. (*Sources: Offenhartz, AP News; Lecher, The Markup*) | **This creates an unfunded mandate of verification: users must double-check the City's own bot, defeating the purpose.** |

## Verification Trace
* **Claim:** Chatbot told users they could take worker tips.
  * **Trace:** The Markup (Lecher) Annotation -> Section: Hallucinated Legal Risk -> Source Line: "bot said it was fine to take workers' tips"
* **Claim:** Chatbot launched in October 2023 under AI Action Plan.
  * **Trace:** NYC Press Release Annotation -> Section: Policy Origin -> Source Line: "New York City Artificial Intelligence Action Plan"
* **Claim:** Stoyanovich called deployment "reckless and irresponsible."
  * **Trace:** AP News (Offenhartz) Annotation -> Section: Expert Verification -> Source Line: "Stoyanovich called that approach 'reckless and irresponsible.'"
