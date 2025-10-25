# AI Agent Instructions for Wirkmechanismen Project

## Overview
This project focuses on Design Research Methodology (DRM) using factor network modeling for analyzing complex systems. It implements the Blessing & Chakrabarti framework through structured JSON models compatible with KUMU visualization platform.

## Core Architecture

### Project Structure
- `general/prompt_instructions.md` - Master guide for DRM methodology and KUMU JSON encoding
- `reference_model/` - Contains Reference Model blueprints (existing situation analysis)  
- `impact_models/` - Houses Impact Models (desired post-intervention situations)

### Key Concepts
**Reference Models (RM)**: Network of influencing factors depicting existing situations as benchmarks
**Impact Models (IM)**: Networks showing desired post-support states with explicit assumptions
**Influencing factors**: Attributes of elements (e.g., "quality of product definition") - never include values in labels

## DRM-Specific Patterns

### Factor Node Structure
Elements represent factors as "attribute-of-element" formulations:
- ✅ `"Qualität der Problemdefinition"` 
- ❌ `"Problemdefinition"` or `"Hohe Qualität der Problemdefinition"`

Node classification via `attributes["element type"]`:
- `"Einflussfaktoren"` - Standard influencing factors
- `"Schlüsselfaktor"` - Key factors (most promising to address)
- `"Erfolgsfaktor"` - Success factors (long-term outcomes)
- `"Messbarer Erfolgsfaktor"` - Measurable success factors (proxies)
- `"Support"` - Interventions (Impact Models only)

### Connection Semantics
Links carry directional causality with source attribution:
- `attributes.label`: Source type `[X]` literature, `[A]` assumption, `[E]` experience, `[O]` investigation, `[?]` unknown
- `attributes["connection type"]`: Sign pairs `++`, `+-`, `-+`, `--` indicating relationship polarity at each end
- `direction: "directed"` for causal relationships

### Model Evolution Process
1. **Reference Model**: Map existing factor networks with evidence-based links
2. **Impact Model**: Add Support node, modify affected relationships, mark new links as `[A]` assumptions
3. **Validation**: Ensure proxy relationships between measurable and success factors are explicit

## Development Workflow

### JSON Validation
When working with KUMU blueprints:
- Validate element `_id` uniqueness across nodes
- Ensure connection `from`/`to` reference valid element IDs
- Maintain consistent attribute schema per element type
- Preserve analytics fields (degree, betweenness, etc.) when present

### Model Consistency Checks
- Every causal claim requires source attribution in link labels
- Success factor hierarchies must have explicit proxy relationships
- Impact Models must identify which Reference Model links no longer hold
- Key factors should connect to Support interventions in Impact Models

## File Patterns

### Naming Conventions
- Reference models: `*-reference-model-blueprint.json`
- Impact models: `*-impact-model-blueprint.json`
- Documentation follows German terminology per academic context

### JSON Structure
Follow the exact schema demonstrated in `wirkmechanismen-reference-model-blueprint.json`:
```json
{
  "elements": [{"_id": "elem-*", "attributes": {...}}],
  "connections": [{"_id": "conn-*", "from": "elem-*", "to": "elem-*", "attributes": {...}}]
}
```

## Quality Standards
- Maintain semantic precision in factor labeling per DRM methodology
- Document assumptions explicitly when creating Impact Models
- Preserve evidence traceability through connection source labels
- Ensure model completeness: key factors → support → measurable outcomes → success factors