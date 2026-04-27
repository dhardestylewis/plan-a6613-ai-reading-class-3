# Annotation: Patterson et al. (2022) — ML Training Carbon Footprint
**Source**: Patterson, D., Gonzalez, J., Hölzle, U., et al. (2022). The carbon footprint of machine learning training will plateau, then shrink. Computer, 55(7), 18-28.
**arXiv**: https://arxiv.org/abs/2204.05149
**Stakeholder**: Academic (Google-affiliated researchers)
**Conflict of interest**: ALL authors are Google affiliates. Paper argues that ML carbon footprint will decrease — aligning with Google's corporate narrative.

## Key Extractions

### Core Argument
- Four best practices can reduce ML training energy by up to 100x and CO2 emissions by up to 1,000x
  - Used in writeup: "combining multiple best practices can reduce AI training energy by 100 times and associated emissions by 1,000 times" ✅
  - CRITICAL: "up to" = theoretical maximum; "when used together" = conditional

### Four Best Practices (the 4 Ms)
1. **Model**: Select efficient ML architectures (5-10x computation reduction)
2. **Machine**: Use ML-optimized processors like TPUs/GPUs (2-5x performance/watt)
3. **Mechanization**: Cloud computing vs. on-premise (1.4-2x efficiency)
4. **Map**: Choose DC locations with cleaner energy (5-10x carbon reduction)
  - Used in writeup: "explicitly conditional on applying all practices simultaneously" ✅

### Additional Claims
- ML energy held steady at <15% of Google's total energy use for 3 years
  - NOT used in writeup — pre-GenAI figure (paper published July 2022, before ChatGPT Nov 2022)

- Previous ML emissions estimates off by 100x-100,000x
  - NOT used in writeup — defensive claim

### Pre-GenAI Timing
- Paper submitted April 2022, published July 2022
- ChatGPT launched November 2022 — the explosive generative AI growth came AFTER this paper
- Google's own emissions have RISEN since publication, contradicting the paper's "plateau, then shrink" thesis
  - NOT stated explicitly in writeup but implied by the juxtaposition with IEA data

## What This Source Does NOT Address
- Post-2022 generative AI energy demands
- Inference energy (only discusses training)
- Total volume growth effects
