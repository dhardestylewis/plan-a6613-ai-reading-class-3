# Annotation: Uptime Institute 2023 Global Data Center Survey
**Source**: Uptime Institute. (2023). 2023 Global Data Center Survey.
**URL**: https://uptimeinstitute.com/resources/research-and-reports/uptime-institute-global-data-center-survey-results-2023
**Stakeholder**: Industry research (independent, non-vendor)
**Conflict of interest**: None identified — Uptime Institute is a respected industry advisory organization
**Access note**: Full report behind membership paywall; executive summary available free.

## Key Extractions

### PUE Data
- Global average PUE of respondents' data centers: approximately 1.58 (2023)
  - Used in writeup: "the industry average of 1.58 reported by the Uptime Institute" ✅

- PUE has been "flatlining" in recent years
  - NOT used directly — but context for why 1.58 hasn't improved

### Methodology Caveats
- Primary contributor to flatlining: "a richer geographical mix of surveyed data centers, with an increasing number of data centers in the Asia, Middle East, Africa, and Latin America regions"
- "Facilities in these regions tend to be smaller in capacity and located in warmer climates — both factors which typically require greater energy consumption."
  - NOT stated in writeup — but relevant: comparing hyperscale PUE (1.10) against an average dragged up by small, warm-climate DCs flatters Google

### Survey Context
- 13th year of the survey (longest-running study of its kind)
- Authors: Donnellan, Bizo, Davis, Lawrence, Rogers, Simon, Smolaks

## What This Source Does NOT Address
- Google specifically (industry-wide survey)
- Location-based vs. market-based emissions
- AI-specific energy consumption
- Absolute energy consumption (PUE measures efficiency ratio, not total energy)

## Analytical Note
PUE is a LIMITED metric. A PUE of 1.10 means that for every watt of IT equipment power, only 0.10 watts are used for overhead (cooling, lighting, etc.). But PUE says nothing about how much total IT equipment power is being consumed. A highly efficient data center that doubles its IT load still doubles its total energy consumption, even with excellent PUE. This is the core tension in Google's efficiency narrative.
