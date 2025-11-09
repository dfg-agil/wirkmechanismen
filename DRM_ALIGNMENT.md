# DRM Alignment Review: Wirkmechanismen Workflow

## Overview

This document reviews the Wirkmechanismen workflow against the Design Research Methodology (DRM) framework by Blessing and Chakrabarti (2009) and identifies alignments, discrepancies, and recommendations.

## DRM Framework Summary

### Core DRM Research Stages

The DRM framework defines four main research stages:

1. **Research Clarification (RC)**
   - Define research goals and scope
   - Create initial Reference Model (existing situation)
   - Create initial Impact Model (desired situation)
   - Define preliminary success criteria
   - Plan overall research approach

2. **Descriptive Study I (DS-I)**
   - Understand the existing situation in detail
   - Validate and refine the Reference Model
   - Methods: Literature review, observations, interviews, case studies
   - Goal: Evidence-based understanding of current state

3. **Prescriptive Study (PS)**
   - Develop support/intervention based on DS-I findings
   - Refine Impact Model with specific supports
   - Design the solution (tool, method, process)
   - Goal: Create intervention to improve the situation

4. **Descriptive Study II (DS-II)**
   - Evaluate the impact of the support
   - Validate Impact Model through empirical testing
   - Methods: Experiments, case studies, pilots
   - Goal: Measure actual vs. expected improvements

### DRM Model Definitions (from Blessing & Chakrabarti)

**Reference Model (RM)**:
- Network of influencing factors depicting the **existing/current situation**
- Benchmark against which improvements are evaluated
- Based on literature, experience, and investigation
- Represents "what is" (descriptive)

**Impact Model (IM)**:
- Network depicting the **desired situation** after introducing support
- Includes support interventions and expected effects
- May add, remove, or modify factors/links relative to RM
- Assumptions must be explicit
- Represents "what should be" (prescriptive)

**Influencing Factors**:
- Formulated as **"attribute-of-element"**
- Observable, measurable, or assessable aspects
- Examples: "quality of problem definition" (not "problem definition")
- No value judgments in labels (not "high quality...")

**Key Factors** (Schlüsselfaktor):
- Most promising factors to address for improvement
- Core/root-cause factors that support should target
- Identified through analysis of factor network

**Success Factors** (Erfolgsfaktor):
- Long-term outcomes at the "top" of the network
- Justify the research (e.g., profit, customer satisfaction)

**Measurable Success Factors** (Messbarer Erfolgsfaktor):
- Proxies for success factors
- Closer to project scope and time horizon
- Reliable indicators (e.g., time-to-market as proxy for profit)

**Support**:
- Intervention introduced in Impact Model
- Tool, method, process, or technique
- Targets key factors to improve the situation

## Current Workflow vs. DRM Framework

### ✅ Alignments (What's Correct)

| Wirkmechanismen Concept | DRM Equivalent | Status |
|------------------------|----------------|--------|
| Reference Model | Reference Model (RM) | ✅ Correct usage |
| Impact Model | Impact Model (IM) | ✅ Correct usage |
| Schlüsselfaktor | Key Factor | ✅ Correct |
| Erfolgsfaktor | Success Factor | ✅ Correct |
| Messbarer Erfolgsfaktor | Measurable Success Factor | ✅ Correct |
| Support | Support/Intervention | ✅ Correct |
| "Attribute-of-element" formulation | DRM Factor Formulation | ✅ Correct |
| Source attribution `[1-9]+]`, `[A]`, `[E]`, `[O]` | DRM Evidence Marking | ✅ Correct |
| Connection type `++`, `+-`, `-+`, `--` | DRM Link Signs | ✅ Correct |

### ⚠️ Discrepancies and Issues

#### 1. "Problem" Element Type (NON-STANDARD)

**Current Practice**:
```json
{
  "_id": "elem-QOBGtWqO",
  "attributes": {
    "label": "Qualität des Dailies",
    "element type": "Problem"
  }
}
```

**DRM Standard**:
- No "Problem" element type in DRM
- Problems are described in research context, not as network nodes
- All nodes should be influencing factors (attributes of elements)

**Recommendation**:
- **Option A** (Strict DRM): Remove "Problem" element type entirely
- **Option B** (Pragmatic): Keep as non-standard documentation element but clarify:
  - Mark as "descriptive context only"
  - Do NOT connect to factor network
  - Use only for documentation purposes
- **Option C** (Reformulate): Convert to proper factor: "Qualität des Dailies" → classify as "Schlüsselfaktor" or "Einflussfaktoren"

**Decision Needed**: User should choose which approach to adopt.

#### 2. "Einflussfaktoren" Classification

**Current Practice**:
- Used as catch-all for factors that are neither Key nor Success factors

**DRM Standard**:
- All factors are "influencing factors"
- Classification (Key, Success) is based on role, not type
- No explicit "other factors" category in DRM

**Status**:
- ✅ Acceptable as a practical classification convention
- Helps with visualization and filtering in KUMU
- Could be clearer in documentation that ALL factors are influencing factors

**Recommendation**:
- Add clarification in documentation:
  - "All factors in the network are influencing factors (per DRM)"
  - "Element type 'Einflussfaktoren' is used for factors that are neither Key nor Success factors"
  - "This is a KUMU visualization convention, not a DRM category"

#### 3. Multiple Key Factors in Some Models

**Current Practice in Impact Models**:
```json
// dailies-effectiveness-impact-model.json has multiple "Schlüsselfaktor" elements
```

**DRM Standard**:
- Key factors are identified as "most promising to address"
- Multiple key factors are acceptable in DRM
- Reference Models typically focus on one key factor for clarity

**Status**:
- ⚠️ Reference Model Criteria requires exactly 1 Schlüsselfaktor (strict)
- ℹ️ Impact Models may have multiple key factors (more flexible)
- ℹ️ DRM doesn't mandate a single key factor

**Recommendation**:
- **Reference Models**: Maintain "exactly 1 Schlüsselfaktor" rule for clarity
- **Impact Models**: Allow multiple key factors if multiple interventions target different factors
- Update [IMPACT_MODEL_CRITERIA.md](IMPACT_MODEL_CRITERIA.md) to clarify this is acceptable

#### 4. Missing DRM Research Stage Context

**Current Documentation**:
- Focuses on model evolution workflow
- Doesn't explicitly map to DRM research stages

**DRM Framework**:
- Models exist within research stages (RC → DS-I → PS → DS-II)
- Each stage has specific goals and methods

**Recommendation**:
- Add DRM research stage mapping to WORKFLOW.md
- Clarify which validation activities correspond to which DRM stages

## Proposed DRM Research Stage Mapping

### Workflow Phase → DRM Stage Alignment

| Wirkmechanismen Phase | DRM Stage(s) | DRM Activities |
|----------------------|--------------|----------------|
| **Main Model** | Ongoing across all stages | Consolidated knowledge base |
| **Reference Model Creation** | **RC** (Research Clarification) | Define scope, identify factors, build initial RM |
| **Reference Model Validation** | **DS-I** (Descriptive Study I) | Literature review, expert interviews, validate causal relationships |
| **Impact Model Scaffolding** | **RC + PS** (Clarification + Prescriptive) | Plan interventions, design supports, create initial IM |
| **Impact Model Review** | **PS** (Prescriptive Study) | Refine intervention design, validate assumptions theoretically |
| **Impact Model Piloting** | **DS-II** (Descriptive Study II) | Pilot implementation, collect evidence, measure effects |
| **Impact Model Validation** | **DS-II** (Descriptive Study II) | Evaluate actual vs. expected impact, validate IM empirically |
| **Feedback to Main Model** | All stages | Consolidate validated findings |

### Detailed Mapping

```
┌─────────────────────────────────────────────────────────────────┐
│                    DRM RESEARCH STAGES                          │
└─────────────────────────────────────────────────────────────────┘

RC: Research Clarification
├─ Define research question/problem
├─ Identify relevant factors from Main Model
├─ Create initial Reference Model (existing situation)
├─ Create initial Impact Model (desired situation with supports)
└─ Define success criteria and validation plan

DS-I: Descriptive Study I (Understand Current Situation)
├─ Literature review to validate RM factors and relationships
├─ Expert interviews to gather evidence
├─ Observations/case studies of current practice
├─ Update RM: [?] → [1-9]+], [E], or [O]
└─ Output: Validated Reference Model

PS: Prescriptive Study (Design Intervention)
├─ Design support interventions based on DS-I findings
├─ Refine Impact Model with specific supports
├─ Document assumptions [A] for new relationships
├─ Plan implementation and measurement
└─ Output: Detailed Impact Model with supports

DS-II: Descriptive Study II (Evaluate Impact)
├─ Pilot implementation of supports
├─ Measure key factors before/after intervention
├─ Collect qualitative evidence (interviews, observations)
├─ Compare actual vs. expected improvements
├─ Update IM: [A] → [O] for validated relationships
└─ Output: Empirically validated Impact Model
```

## Terminology Corrections Needed

### 1. Update WORKFLOW.md

**Section to Add**: DRM Research Stage Context

```markdown
## DRM Research Stage Alignment

The Wirkmechanismen workflow implements the Design Research Methodology (DRM)
framework by Blessing and Chakrabarti (2009). Our workflow phases map to DRM
research stages as follows:

### Research Clarification (RC)
- **Wirkmechanismen Phase**: Reference Model Creation + Impact Model Scaffolding
- **Activities**: Define problem scope, extract relevant factors from Main Model,
  create initial RM and IM, plan validation approach

### Descriptive Study I (DS-I)
- **Wirkmechanismen Phase**: Reference Model Validation
- **Activities**: Literature review, expert interviews, evidence gathering
- **Goal**: Validate existing situation model with empirical evidence

### Prescriptive Study (PS)
- **Wirkmechanismen Phase**: Impact Model Design and Review
- **Activities**: Design support interventions, document assumptions, plan implementation
- **Goal**: Create intervention to address key factors

### Descriptive Study II (DS-II)
- **Wirkmechanismen Phase**: Impact Model Piloting and Validation
- **Activities**: Pilot implementation, before/after measurement, empirical evaluation
- **Goal**: Validate expected improvements actually occur

This mapping ensures methodological rigor and aligns with established design
research best practices.
```

### 2. Clarify "Einflussfaktoren" in REFERENCE_MODEL_CRITERIA.md

**Current**: "Alle anderen Faktoren MÜSSEN als Einflussfaktoren klassifiziert werden"

**Recommended Addition**:
```markdown
#### 1.3 Einflussfaktoren-Klassifikation
- **MANDATORY**: Alle anderen Faktoren MÜSSEN als Einflussfaktoren klassifiziert werden
- **KLASSIFIKATION**: `"element type": "Einflussfaktoren"`
- **DRM-HINWEIS**: Per DRM sind ALLE Faktoren im Netzwerk "influencing factors".
  Die Klassifikation "Einflussfaktoren" bezeichnet hier Faktoren, die weder
  Schlüsselfaktor noch Erfolgsfaktor sind. Dies ist eine KUMU-Visualisierungs-Konvention.
- **EMPFEHLUNG**: 3-7 Einflussfaktoren für ausgewogene Modellkomplexität
```

### 3. Address "Problem" Element Type

**Current Models Using "Problem"**:
- `dailies-effectiveness-reference-model.json`
- `dailies-effectiveness-impact-model.json`

**Recommendation**: Add to GATEKEEPING_CRITERIA.md

```markdown
#### 1.2.1 Non-Standard Element Types

**"Problem" Element Type** (Non-standard, transitional):
- **LEGACY**: Some models use `"element type": "Problem"` to document context
- **DRM STANDARD**: Not part of DRM framework - problems are described in research context
- **PERMITTED** (temporarily): For existing models as documentation-only elements
- **RESTRICTION**: Problem elements MUST NOT have outgoing connections
- **FUTURE**: New models should reformulate problems as proper factors (Schlüsselfaktoren)
- **EXAMPLE**:
  - ❌ "Qualität des Dailies" as "Problem" type
  - ✅ "Qualität des Dailies" as "Schlüsselfaktor" with clear measurability
```

### 4. Update README.md DRM Reference

**Current**: Brief mention of DRM

**Recommended Addition**:
```markdown
### Design Research Methodology (DRM)

This project implements the DRM framework (Blessing & Chakrabarti, 2009):

**Reference**: Blessing, L. T. M., & Chakrabarti, A. (2009). *DRM, a Design Research
Methodology*. Springer. https://doi.org/10.1007/978-1-84882-587-1

**DRM Stages**:
1. **Research Clarification (RC)**: Define goals, create initial models
2. **Descriptive Study I (DS-I)**: Understand existing situation (validate Reference Model)
3. **Prescriptive Study (PS)**: Develop intervention (design Impact Model)
4. **Descriptive Study II (DS-II)**: Evaluate impact (validate Impact Model)

**Our Implementation**: See [WORKFLOW.md](WORKFLOW.md) for detailed mapping of
our workflow phases to DRM research stages.
```

## Recommendations Summary

### High Priority (Do Immediately)

1. ✅ **Add DRM Research Stage mapping to WORKFLOW.md**
   - Clarify how workflow phases map to RC → DS-I → PS → DS-II
   - Helps researchers understand methodological grounding

2. ✅ **Clarify "Einflussfaktoren" classification**
   - Add note that all factors are influencing factors per DRM
   - Explain this is a KUMU visualization convention

3. ⚠️ **Document "Problem" element type status**
   - Add to GATEKEEPING_CRITERIA.md as non-standard
   - Decide: Allow as legacy, or require reformulation?

### Medium Priority (Consider)

4. **Update README.md with DRM citation**
   - Add proper academic reference to Blessing & Chakrabarti (2009)
   - Link to WORKFLOW.md for stage mapping

5. **Review existing models for "Problem" elements**
   - Decide whether to reformulate as Schlüsselfaktor
   - Ensure no outgoing connections if kept

### Low Priority (Nice to Have)

6. **Create DRM research template**
   - Guide for new researchers on RC → DS-I → PS → DS-II
   - Map each stage to specific deliverables and milestones

7. **Enhance validation documentation**
   - Explicitly label validation activities by DRM stage
   - Track DS-I evidence vs. DS-II evidence separately

## Conclusion

The Wirkmechanismen workflow is **strongly aligned with DRM framework** with only minor terminology clarifications needed:

✅ **Correct**:
- Reference Model and Impact Model concepts
- Factor formulation (attribute-of-element)
- Key Factors, Success Factors, Supports
- Source attribution system

⚠️ **Needs Clarification**:
- "Problem" element type (non-standard)
- "Einflussfaktoren" as KUMU convention
- DRM research stage mapping

🔄 **Action Items**:
1. Add DRM stage mapping to WORKFLOW.md
2. Clarify "Einflussfaktoren" classification
3. Document "Problem" element type policy
4. Add DRM citation to README.md

These are primarily **documentation improvements** - the methodology itself is sound and DRM-compliant.

---

**References**:
- Blessing, L. T. M., & Chakrabarti, A. (2009). *DRM, a Design Research Methodology*. Springer. https://doi.org/10.1007/978-1-84882-587-1
- Project prompt instructions: [general/prompt_instructions.md](general/prompt_instructions.md)
