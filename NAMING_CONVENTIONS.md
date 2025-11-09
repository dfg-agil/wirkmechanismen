# Naming Conventions for Wirkmechanismen Models

## File Naming Standards

### Main Model
**Location**: `models/main_model/`
**Format**: `wirkmechanismen-main-model-blueprint.json`

The main model serves as the single source of truth and maintains this fixed name.

### Reference Models
**Location**: `models/reference_models/`
**Format**: `{domain-scope}-reference-model.json`

**Examples**:
- `dailies-effectiveness-reference-model.json`
- `wirkmechanismen-reference-model-quality-problems.json`
- `sprint-planning-reference-model.json`
- `retrospective-quality-reference-model.json`

**Naming Guidelines**:
- Use **kebab-case** (lowercase with hyphens)
- **domain-scope**: Brief descriptor (2-3 words) of the specific problem domain
- Keep names concise but descriptive
- Avoid redundant terms (e.g., "quality" if already implied by domain)
- Use English or German consistently per project preference

### Impact Models
**Location**: `models/impact_models/`
**Format**: `{domain-scope}-impact-model.json`

**Examples**:
- `dailies-effectiveness-impact-model.json`
- `sprint-planning-impact-model.json`
- `backlog-refinement-impact-model.json`

**Naming Guidelines**:
- **MUST** match the corresponding reference model's domain-scope
- Reference model: `{domain}-reference-model.json` → Impact model: `{domain}-impact-model.json`
- This creates clear traceability: `dailies-effectiveness-reference-model.json` ↔ `dailies-effectiveness-impact-model.json`

### Work-in-Progress Models
**Format**: `{domain-scope}-{model-type}-wip.json`

**Examples**:
- `wirkmechanismen-reference-model-wip.json`
- `wirkmechanismen-impact-model-wip.json`

**Guidelines**:
- Use `-wip` suffix for models under active development
- Remove `-wip` suffix once model passes peer review and validation
- WIP models are excluded from production use but included in version control

## Element ID Naming

### Element IDs (`_id` field)
**Format**: `elem-{descriptive-name}`

**Examples**:
- `elem-backlogRefinement`
- `elem-YDXh1U6N` (auto-generated acceptable for prototypes)
- `elem-uDiTVbXE` (auto-generated acceptable for prototypes)

**Guidelines**:
- Prefix with `elem-`
- Use camelCase for descriptive names
- Auto-generated IDs are acceptable during scaffolding
- **RECOMMENDED**: Replace auto-generated IDs with descriptive names during review
- Descriptive IDs improve model readability and maintenance

### Connection IDs (`_id` field)
**Format**: `conn-{source}-{target}` or `conn-{domain}-###`

**Examples**:
- `conn-quality-001`
- `conn-quality-002`
- `conn-backlogRefinement-to-criteriaClarity`

**Guidelines**:
- Prefix with `conn-`
- For sequential numbering: `conn-{domain}-001`, `conn-{domain}-002`, etc.
- For descriptive names: `conn-{sourceFactor}-to-{targetFactor}` (abbreviated)
- Maintain uniqueness within the model

## Tag Naming

**Format**: Title Case or Domain-Specific

**Examples**:
- `"Planning"`
- `"Backlog Refinement"`
- `"Struktur und Zielorientierung"`
- `"Daily"`
- `"Qualität"`
- `"Produktqualität"`

**Guidelines**:
- Use consistent capitalization (Title Case recommended)
- Tags should represent broad categories or domains
- Keep tag vocabulary controlled and reused across models
- Document tag taxonomy in main model or separate glossary

## Label Naming (Factor Names)

**Format**: DRM "attribute-of-element" formulation

**Guidelines**:
- **CORRECT**: `"Qualität des Backlog-Refinements"` (attribute of element)
- **INCORRECT**: `"Backlog-Refinement"` (raw element)
- **INCORRECT**: `"Hohe Qualität des Backlog-Refinements"` (includes value judgment)
- Follow DRM methodology strictly (see [GATEKEEPING_CRITERIA.md](GATEKEEPING_CRITERIA.md))

## Version Control and Commits

### Commit Message Format
**Format**: `[MODEL_TYPE] Brief description`

**Examples**:
- `[MODEL] Add backlog-refinement reference model`
- `[MAIN] Refine description for "Präzision der adressierten Probleme"`
- `[IMPACT] Add support interventions for daily effectiveness`
- `[REFERENCE] Add literature references to quality-problems model`

**Prefixes**:
- `[MODEL]` - Generic model changes (use when multiple types affected)
- `[MAIN]` - Main model changes
- `[REFERENCE]` - Reference model changes
- `[IMPACT]` - Impact model changes
- `[CRITERIA]` - Changes to criteria or documentation
- `[VALIDATION]` - Changes to validation scripts

### Branch Naming (Optional)
**Format**: `{type}/{domain-scope}`

**Examples**:
- `feature/backlog-refinement-model`
- `refactor/main-model-restructure`
- `docs/workflow-documentation`

**Guidelines**:
- Use for feature branches when creating PRs
- Main branch remains `main`
- Delete feature branches after merge

## Model Relationship Naming

### Cross-Model References (Future Enhancement)
**Format**: TBD - Explicit links between main → reference → impact models

**Placeholder Structure** (to be defined):
```json
{
  "model_metadata": {
    "source_model": "wirkmechanismen-main-model-blueprint.json",
    "related_impact_model": "backlog-refinement-impact-model.json",
    "version": "1.0",
    "status": "validated"
  }
}
```

**Status**: Not yet implemented - under discussion

## Validation and Compliance

All file names MUST:
- Pass `lint_blueprint.py` validation
- Use consistent casing (kebab-case for files, camelCase for IDs)
- Avoid special characters except hyphens and underscores
- Be unique within their directory

## Summary Table

| Model Type | Location | Format | Example |
|------------|----------|--------|---------|
| Main Model | `models/main_model/` | Fixed name | `wirkmechanismen-main-model-blueprint.json` |
| Reference Model | `models/reference_models/` | `{domain}-reference-model.json` | `dailies-effectiveness-reference-model.json` |
| Impact Model | `models/impact_models/` | `{domain}-impact-model.json` | `dailies-effectiveness-impact-model.json` |
| WIP Model | Same as above | `{domain}-{type}-wip.json` | `sprint-planning-reference-model-wip.json` |
| Element ID | Within JSON | `elem-{name}` | `elem-backlogRefinement` |
| Connection ID | Within JSON | `conn-{domain}-###` | `conn-quality-001` |

## Questions or Updates

For questions about naming conventions:
1. Check existing models for precedent
2. Consult [GATEKEEPING_CRITERIA.md](GATEKEEPING_CRITERIA.md) for methodological requirements
3. Propose naming convention updates via pull request to this document
