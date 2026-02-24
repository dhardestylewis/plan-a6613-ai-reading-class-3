# Annotation: ShotSpotter/SoundThinking in Chicago

## Stakeholder Analysis

| Stakeholder | Position | Potential Bias |
|-------------|----------|----------------|
| SoundThinking (vendor) | Claims 97% accuracy | Revenue depends on contract renewal; accuracy metric based on "customer feedback" not independent audit |
| Chicago OIG (city oversight) | Found 9.1% produced evidence of crime | Government watchdog; no revenue interest |
| ACLU (civil liberties) | Opposes deployment | Advocacy organization; may emphasize worst cases |
| MacArthur Justice Center (legal) | Filed federal lawsuit | Litigation interest; but uses verifiable CPD data |
| South Side Weekly (independent) | Documented contract end | Community journalism; neighborhood perspective |
| Cook County State's Attorney | Found 1% arrest rate | Prosecution perspective; reviewed own case data |

## Data Discrepancy

The central discrepancy: SoundThinking claims 97% *technical accuracy* (the sensor correctly identifies a sound as a gunshot), while the OIG measures *operational value* (whether police responding to alerts find evidence of a crime — only 9.1%). These are different metrics measuring different things, but the vendor's framing obscures the distinction.

## Key Governance Failures (from sources)

1. **No community consent**: Sensors placed in 12 police districts (all predominantly Black/Latino) without public hearings (ACLU_ShotSpotter_full.txt, Lines 1, 6, 7)
2. **Proprietary algorithm**: Inner workings undisclosed to public and defendants (ACLU_ShotSpotter_full.txt, Line 3)
3. **Contract renewals without scrutiny**: $49M contract renewed without public hearings (ACLU_ShotSpotter_full.txt, Lines 5, 7)
4. **Racial concentration**: Deployment exclusively in communities of color (MacArthur_ShotSpotter_full.txt, Line 2)

## What the AI Missed

- The distinction between technical accuracy (97%) and operational value (9.1% evidence rate)
- That the vendor's "independent audit" was based on customer feedback, not an external review
- The feedback loop: sensors in high-crime areas generate more alerts, justifying continued placement
- The due process implications of using proprietary alerts as evidence in criminal proceedings
