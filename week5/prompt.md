# AI Reading Exercise: Class 5 — Prompt File
## Topic: From Digital to Physical Infrastructure

## Core Question
"What are three real-world examples of AI being used to 'actively manage' city assets like the curb or the power grid, and how are cities funding these new digital systems?"

---

## Prompt Strategy

### Prompt v1 — Initial Broad Query
```
What are three real-world examples of AI being used to actively manage city assets like the curb or the power grid? For each example, name the specific city, the specific AI system or vendor, and the funding mechanism the city used to pay for it. Do not give generic concepts — I need named programs with verifiable details.
```

### Prompt v2 — Refinement (if v1 is too vague)
```
The previous answer was too generic. I need three specific, named deployments — not categories. For each, provide:
1. The exact city and agency deploying the AI system.
2. The name of the AI platform or vendor (e.g., Coord, Automotus, Kevala).
3. What city asset it manages (curb, grid, water, traffic signals, etc.).
4. How the city funded or procured it (federal grant, P3, SaaS contract, rate-payer funds, etc.).
5. A citation I can verify — a news article, press release, or government RFP.
```

### Prompt v3 — Mechanism Deep-Dive
```
For each of the three examples you provided, explain the *mechanism* of active management. How does the AI system actually work — what data does it ingest, what decisions does it make autonomously vs. recommend to a human operator, and what happens when it fails? I want to understand the operational loop, not just the marketing pitch.
```

---

## Notes
- Model used: **Claude 3.5 Sonnet** (via Gemini Code Assist / Antigravity)
- Strategy: Iterative refinement — reject generic answers, demand named programs, then probe mechanisms.
- Key pitfall from Week 4: AI conflates similar-sounding programs (e.g., Innovation Districts vs. Opportunity Zones). Watch for similar conflation here (e.g., "smart grid" marketing vs. actual AI-managed grid operations).
