# Wirkmechanismen - Design Research Methodology Factor Networks

A research repository implementing Design Research Methodology (DRM) using factor network modeling for analyzing complex systems, based on the Blessing & Chakrabarti framework.

## Overview

This project focuses on creating structured models of influencing factors in design processes and their causal relationships. The models are serialized as KUMU-compatible JSON blueprints for visualization and analysis.

### Key Concepts

- **Reference Models (RM)**: Network representations of existing situations, serving as benchmarks for evaluation
- **Impact Models (IM)**: Networks depicting desired situations after introducing support interventions
- **Influencing Factors**: Attributes of elements that can be observed, measured, or assessed (e.g., "quality of problem definition")
- **Factor Networks**: Directed graphs showing causal relationships between factors with explicit source attribution

## Repository Structure

```
wirkmechanismen/
├── general/
│   └── prompt_instructions.md     # Complete DRM methodology guide
├── reference_model/
│   └── wirkmechanismen-reference-model-blueprint.json
├── impact_models/                 # Future impact model implementations
├── .github/
│   └── copilot-instructions.md    # AI agent guidance
└── README.md
```

## Methodology

### Design Research Methodology (DRM)

This project implements the DRM framework developed by Blessing & Chakrabarti for systematic design research:

1. **Factor Identification**: Systematic discovery of influencing factors from literature, experience, and investigation
2. **Network Construction**: Building causal relationships with explicit source attribution
3. **Model Validation**: Ensuring semantic precision and evidence traceability
4. **Impact Assessment**: Comparing reference and impact models to evaluate interventions

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

This research repository is intended for academic and educational use in design research methodology.

---

For detailed methodology guidance, see [`general/prompt_instructions.md`](general/prompt_instructions.md).
For AI agent instructions, see [`.github/copilot-instructions.md`](.github/copilot-instructions.md).
