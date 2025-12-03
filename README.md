# Wirkmechanismen - Design Research Methodology Factor Networks

A research repository implementing influencing factors network modeling for analyzing complex mechanism of action in product development, based on Design Research Methodology (DRM) by Blessing & Chakrabarti framework.

## Overview

This project focuses on creating structured models of influencing factors in design processes and their causal relationships. The models are serialized as KUMU-compatible JSON blueprints for visualization and analysis.

### Key Concepts

- **Reference Models (RM)**: Network representations of existing situations, serving as benchmarks for evaluation
- **Impact Models (IM)**: Networks depicting desired situations after introducing support interventions
- **Influencing Factors**: Attributes of elements that can be observed, measured, or assessed (e.g., "quality of problem definition")
- **Factor Networks**: Directed graphs showing causal relationships between factors with explicit source attribution

## Methodology

### Design Research Methodology (DRM)

This project implements the DRM framework developed by Blessing & Chakrabarti for systematic design research.

**Reference**: Blessing, L. T. M., & Chakrabarti, A. (2009). *DRM, a Design Research Methodology*. Springer. https://doi.org/10.1007/978-1-84882-587-1

**DRM Research Stages**:
1. **Research Clarification (RC)**: Define research goals, create initial Reference and Impact Models
2. **Descriptive Study I (DS-I)**: Understand existing situation, validate Reference Model empirically
3. **Prescriptive Study (PS)**: Develop support/intervention, design detailed Impact Model
4. **Descriptive Study II (DS-II)**: Evaluate impact of support, validate Impact Model through testing

**Our Implementation**:
1. **Factor Identification**: Systematic discovery of influencing factors from literature, experience, and investigation
2. **Network Construction**: Building causal relationships with explicit source attribution
3. **Model Validation**: Ensuring semantic precision and evidence traceability through DRM stages
4. **Impact Assessment**: Comparing reference and impact models to evaluate interventions

See [WORKFLOW.md](WORKFLOW.md) for detailed mapping of our workflow phases to DRM research stages.

### Factor Network Modeling Principles

#### Factor Formulation
- **Correct**: "Qualität der Problemdefinition" (attribute-of-element)
- **Incorrect**: "Problemdefinition" (raw element) or "Hohe Qualität..." (includes values)

#### Connection Semantics
- **Source Attribution**: `[X]` literature, `[A]` assumption, `[E]` experience, `[O]` investigation, `[?]` unknown
- **Relationship Signs**: `++`, `+-`, `-+`, `--` indicating polarity at connection endpoints
- **Causality**: Directed links representing cause-effect relationships

#### Element Classification
- `Einflussfaktoren` - Standard influencing factors
- `Schlüsselfaktor` - Key factors (most promising to address)
- `Erfolgsfaktor` - Success factors (long-term outcomes)
- `Messbarer Erfolgsfaktor` - Measurable success factors (proxies)
- `Support` - Interventions (Impact Models only)

## KUMU JSON Format

Models are serialized as KUMU-compatible JSON blueprints with the following structure:

```json
{
  "elements": [
    {
      "_id": "elem-unique-id",
      "attributes": {
        "label": "Factor Name (attribute-of-element)",
        "element type": "Einflussfaktoren",
        "description": "Detailed explanation"
      }
    }
  ],
  "connections": [
    {
      "_id": "conn-unique-id",
      "from": "elem-source-id",
      "to": "elem-target-id",
      "direction": "directed",
      "attributes": {
        "label": "[X]",
        "connection type": "++"
      }
    }
  ]
}
```

## Getting Started

### For Researchers

1. **Read the Methodology**: Start with `general/prompt_instructions.md` for complete DRM guidance
2. **Examine Examples**: Study `reference_model/wirkmechanismen-reference-model-blueprint.json`
3. **Understand Validation**: Review quality standards and consistency checks in the AI instructions

### For Contributors

1. **Factor Naming**: Always use "attribute-of-element" formulations
2. **Source Attribution**: Label every causal relationship with evidence type
3. **Model Consistency**: Maintain semantic precision and evidence traceability
4. **JSON Validation**: Ensure unique IDs and valid references between elements and connections

### Development Workflow

1. **Reference Model Creation**:
   - Identify factors from literature/experience
   - Formulate as attributes of elements
   - Build causal network with source attribution
   - Mark key factors for intervention potential

2. **Impact Model Development**:
   - Start from reference model
   - Add support interventions
   - Modify affected relationships
   - Mark assumptions explicitly as `[A]`

3. **Validation Process**:
   - Verify factor formulations follow DRM principles
   - Check all connections have source attribution
   - Ensure proxy relationships are explicit
   - Validate JSON schema compliance
4. **Blueprint Linting**:
   - Run `scripts/lint_blueprint.py` before committing changes (recursively scans `models/`)
   - Address reported issues such as missing IDs, invalid directions, or broken references
   - Optional: enable the shared git hook via `git config core.hooksPath githooks` to run the linter automatically on every commit

### Model Relationship Overview

- **Main Model** (`models/main_model`): the comprehensive factor network that consolidates shared knowledge, evidence, and naming conventions across domains.
- **Reference Models** (`models/reference_models`): problem-focused extracts of the main model that describe the current state for a specific question or scenario.
- **Impact Models** (`models/impact_models`): future-state counterparts to the reference models that include the supports or interventions intended to shift outcomes.

High-level flow: expand and maintain the main model → derive a problem-specific reference model → evolve it into an impact model to explore interventions → feed validated changes back into the main model.

## Research Applications

### Design Process Analysis
- Systematic identification of improvement opportunities
- Evidence-based intervention planning  
- Impact assessment through model comparison

### Complex Systems Modeling
- Multi-factor dependency analysis
- Intervention point identification
- Assumption tracking and validation

### Academic Research
- Reproducible methodology implementation
- Collaborative model development
- Cross-domain factor network comparison

## Quality Standards

- **Semantic Precision**: Factor labels must be measurable attributes
- **Evidence Traceability**: All causal claims require source documentation
- **Model Completeness**: Clear pathways from key factors through interventions to success measures
- **Assumption Transparency**: Explicit marking of uncertain relationships

## Contributing

1. Follow DRM methodology principles outlined in `general/prompt_instructions.md`
2. Maintain consistent JSON schema for KUMU compatibility
3. Document all assumptions and evidence sources
4. Validate models against quality standards before submission

## Academic Context

This work supports systematic design research through structured factor network modeling, enabling:
- Reproducible analysis of complex design situations
- Evidence-based intervention planning
- Collaborative model development across research teams
- Transparent assumption tracking for validation studies

## License

This research repository is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

This research repository is intended for academic and educational use in design research methodology.

---

For detailed methodology guidance, see [`general/prompt_instructions.md`](general/prompt_instructions.md).
For AI agent instructions, see [`.github/copilot-instructions.md`](.github/copilot-instructions.md).
