# Wirkmechanismen Workflow Documentation

## Overview

This document describes the complete workflow for managing and evolving the Wirkmechanismen factor network models. The workflow ensures scientific rigor, methodological consistency, and systematic validation through a structured gate-keeping and review process.

### Methodological Foundation: Design Research Methodology (DRM)

The Wirkmechanismen workflow implements the **Design Research Methodology (DRM)** framework by Blessing and Chakrabarti (2009), which provides a systematic approach to design research.

**Reference**: Blessing, L. T. M., & Chakrabarti, A. (2009). *DRM, a Design Research Methodology*. Springer. https://doi.org/10.1007/978-1-84882-587-1

**DRM Research Stages**:
1. **Research Clarification (RC)**: Define research goals, create initial Reference and Impact Models
2. **Descriptive Study I (DS-I)**: Understand existing situation, validate Reference Model empirically
3. **Prescriptive Study (PS)**: Develop support/intervention, design detailed Impact Model
4. **Descriptive Study II (DS-II)**: Evaluate impact of support, validate Impact Model through testing

Our workflow phases map directly to these DRM stages - see "DRM Research Stage Alignment" section below for detailed mapping.

## Core Principles

### 1. Main Model as Source of Truth
The [Wirkmechanismen Main Model](models/main_model/wirkmechanismen-main-model-blueprint.json) is the single source of truth representing consolidated knowledge about influencing factors in agile product development.

**Characteristics**:
- Comprehensive network of validated factors and relationships
- Continuously refined based on evidence
- Shared knowledge base across domains
- Naming conventions and factor definitions

**Evolution**: The Main Model grows through:
- Validated findings from Reference Models
- Confirmed interventions from Impact Models
- Literature reviews and expert interviews
- Incremental refinement of existing factors

### 2. Reference Models as Problem-Specific Extracts
Reference Models represent the **current state** for specific problems or domains.

**Purpose**:
- Focus on specific problem areas
- Establish baseline understanding
- Identify key intervention points
- Provide benchmark for impact assessment

**Source**: Scaffolded from Main Model with agentic support

### 3. Impact Models as Future-State Visions
Impact Models represent the **desired state** after introducing interventions (Supports).

**Purpose**:
- Test intervention hypotheses
- Model causal effects of supports
- Guide implementation planning
- Enable before/after comparison

**Source**: Derived from validated Reference Models

## Complete Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                        MAIN MODEL                               │
│                   (Source of Truth)                             │
│         Continuously refined and validated                      │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     │ Agentic Scaffolding
                     ↓
         ┌───────────────────────┐
         │  REFERENCE MODEL      │
         │  (Current State)      │
         │  Problem-Specific     │
         └───────┬───────────────┘
                 │
                 │ Automated → Agentic → Human → Peer Review
                 ↓
         ┌───────────────────────┐
         │  VALIDATED REFERENCE  │
         │  MODEL                │
         └───────┬───────────────┘
                 │
                 │ Agentic Scaffolding (add Supports)
                 ↓
         ┌───────────────────────┐
         │  IMPACT MODEL         │
         │  (Future State)       │
         │  With Interventions   │
         └───────┬───────────────┘
                 │
                 │ Automated → Agentic → Human → Peer Review
                 ↓
         ┌───────────────────────┐
         │  VALIDATED IMPACT     │
         │  MODEL                │
         └───────┬───────────────┘
                 │
                 │ Incremental Validation (Pilots, Studies)
                 ↓
         ┌───────────────────────┐
         │  CONFIRMED            │
         │  INTERVENTIONS        │
         │  [A] → [O] → [1-9]+   │
         └───────┬───────────────┘
                 │
                 │ Feed validated findings back
                 ↓
         ┌───────────────────────┐
         │  MAIN MODEL UPDATE    │
         └───────────────────────┘
```

## Detailed Workflow Steps

### Phase 1: Main Model Change Management

**Trigger**: New factor, refined description, new causal relationship for Main Model

**Process**:
1. **Propose Change**: Create feature branch or direct commit to main
2. **Automated Review** (Technical Gate-Keeper):
   - JSON schema validation via `lint_blueprint.py`
   - Structural integrity checks
   - Element/connection ID uniqueness
3. **Agentic Review** (Methodological Gate-Keeper - Currently Manual):
   - AI/LLM-based semantic review (e.g., asking Claude to review factors)
   - Check compliance with [GATEKEEPING_CRITERIA.md](GATEKEEPING_CRITERIA.md)
   - DRM methodology compliance (attribute-of-element formulation)
   - Source attribution requirements
   - Causal plausibility assessment
   - Generate recommendation report
   - **Status**: Currently on-demand/manual; systematization planned
4. **Human Review** (First Decision):
   - Review automated and agentic recommendations
   - Assess scientific plausibility
   - Check evidence quality
   - Decision: Approve, Reject, or Request Changes
5. **Peer Review** (Final Gate):
   - Independent validation by domain expert
   - Verify literature references
   - Check model consistency
   - Final Decision: Merge or Reject
6. **Commit & Merge**: Changes integrated into Main Model

**Quality Gates**:
- ✅ JSON schema validation passes
- ✅ DRM formulation compliance (100%)
- ✅ Source attribution for all connections (>90%)
- ✅ No contradictions with existing knowledge
- ✅ Peer review approval

**Rejection Criteria**: See [GATEKEEPING_CRITERIA.md](GATEKEEPING_CRITERIA.md) Section 6

---

### Phase 2: Reference Model Creation

**Trigger**: Specific problem or research question identified

**Process**:
1. **Problem Definition**:
   - Define problem scope and domain
   - Identify relevant factors from Main Model
   - Determine success factors and measurable proxies

2. **Agentic Scaffolding**:
   - Extract relevant factors from Main Model
   - Build causal chain: Key Factor → Success Factor
   - Apply [REFERENCE_MODEL_CRITERIA.md](REFERENCE_MODEL_CRITERIA.md) constraints:
     - Exactly 1 Key Factor (Schlüsselfaktor)
     - Exactly 1 Success Factor (Erfolgsfaktor)
     - 3-7 Influence Factors (Einflussfaktoren)
     - 1 Measurable Success Factor (if needed)
   - Maintain source attribution from Main Model
   - Save as `{domain}-reference-model.json` in `models/reference_models/`

3. **Human Review**:
   - Verify causal logic and completeness
   - Check that Key Factor is intervention-worthy
   - Validate literature sources
   - Assess model complexity (not too simple/complex)
   - Decision: Approve for Peer Review or Request Changes

4. **Peer Review**:
   - Independent expert validation
   - Topological integrity check (Key Factor = start node, Success Factor = end node)
   - Evidence coverage check (>75% literature sources)
   - Path completeness (at least one full path)
   - Final Decision: Validate or Reject

5. **Incremental Validation**:
   - Literature review to fill evidence gaps
   - Expert interviews to validate causal relationships
   - Update `[?]` or `[A]` sources with `[1-9]+` or `[E]`/`[O]`
   - Document validation in commit messages

6. **Status Update**: Mark model as "validated" (remove `-wip` suffix if present)

**Quality Gates**:
- ✅ Exactly 1 Schlüsselfaktor (no incoming connections)
- ✅ Exactly 1 Erfolgsfaktor (no outgoing connections)
- ✅ >75% connections with literature sources `[1-9]+`
- ✅ At least one complete causal path Key Factor → Success Factor
- ✅ All factors use "attribute-of-element" formulation
- ✅ Peer review approval

**Outputs**:
- `models/reference_models/{domain}-reference-model.json`
- Commit: `[REFERENCE] Add {domain} reference model`

---

### Phase 3: Impact Model Creation

**Trigger**: Validated Reference Model + Intervention hypothesis

**Process**:
1. **Intervention Planning**:
   - Identify concrete support interventions (tools, processes, methods)
   - Hypothesize causal mechanisms: Support → Key Factor
   - Plan measurement strategy for interventions

2. **Agentic Scaffolding**:
   - Copy Reference Model structure
   - Add Support elements (element type: "Support")
   - Create connections: Support → Key Factor
   - Mark new connections as assumptions `[A]`
   - Document assumed causal mechanisms in `description`
   - Apply [IMPACT_MODEL_CRITERIA.md](IMPACT_MODEL_CRITERIA.md) constraints
   - Save as `{domain}-impact-model.json` in `models/impact_models/`

3. **Human Review**:
   - Verify Support interventions are concrete and implementable
   - Check causal plausibility of Support → Key Factor relationships
   - Validate that Problem and Success Factor match Reference Model
   - Assess assumption quality and documentation
   - Decision: Approve for Peer Review or Request Changes

4. **Peer Review**:
   - Independent validation of intervention logic
   - Check Support coverage (all Key Factors addressed?)
   - Verify all new connections marked as `[A]` with justification
   - Topological integrity (Supports = start nodes)
   - Final Decision: Approve for Piloting or Reject

5. **Incremental Validation** (Critical Phase):
   - **Pilot Study**: Small-scale implementation
   - **Data Collection**: Measure Key Factor improvements
   - **Qualitative Evidence**: Interviews, observations
   - **Update Model**: `[A]` → `[O]` for confirmed relationships
   - **Iteration**: Refine Supports based on learnings

6. **Quantitative Validation** (Optional):
   - Before/after measurements
   - Control group comparisons
   - Statistical significance testing
   - Update: `[O]` → `[1-9]+` if published

7. **Feedback to Main Model**:
   - Integrate validated Support-relationships into Main Model
   - Document evidence quality
   - Share learnings across domains

**Quality Gates**:
- ✅ Derived from validated Reference Model (same domain-scope)
- ✅ At least 1 Support element present
- ✅ All Supports connected to Key Factors
- ✅ All new connections marked `[A]` with justification
- ✅ Complete causal path Support → Success Factor
- ✅ Validation plan documented for each assumption
- ✅ Peer review approval

**Outputs**:
- `models/impact_models/{domain}-impact-model.json`
- Commit: `[IMPACT] Add {domain} impact model with {N} support interventions`
- Validation commits: `[IMPACT] Validate assumption for {connection} based on {pilot/study}`

---

## DRM Research Stage Alignment

This section maps the Wirkmechanismen workflow to the four main DRM research stages, clarifying how our phases implement the DRM framework.

### DRM Stage Overview

| DRM Stage | Purpose | Key Activities | Wirkmechanismen Phase |
|-----------|---------|----------------|----------------------|
| **RC** (Research Clarification) | Define research goals and scope | Create initial RM and IM, define success criteria | Reference/Impact Model Creation |
| **DS-I** (Descriptive Study I) | Understand existing situation | Validate RM through literature, interviews, observations | Reference Model Validation |
| **PS** (Prescriptive Study) | Develop intervention | Design support, refine IM, document assumptions | Impact Model Design |
| **DS-II** (Descriptive Study II) | Evaluate impact | Pilot support, measure effects, validate IM | Impact Model Validation |

### Detailed Stage Mapping

#### Research Clarification (RC)

**DRM Definition**: Initial stage where research goals are defined, the problem is clarified, and initial models are created.

**Wirkmechanismen Implementation**:
- **Phase**: Reference Model Creation (steps 1-2) + Impact Model Scaffolding (steps 1-2)
- **Activities**:
  - Define problem scope and domain
  - Identify relevant factors from Main Model
  - Create initial Reference Model (existing situation)
  - Create initial Impact Model (desired situation with planned supports)
  - Define preliminary success criteria and measurable proxies
  - Plan validation approach

**Deliverables**:
- `{domain}-reference-model-wip.json` (draft)
- `{domain}-impact-model-wip.json` (draft)
- Research plan documented in commit messages

**Quality Gate**: Human Review approval to proceed to DS-I

---

#### Descriptive Study I (DS-I) - Understanding Current Situation

**DRM Definition**: Comprehensive study to understand and validate the existing situation depicted in the Reference Model.

**Wirkmechanismen Implementation**:
- **Phase**: Reference Model Validation (steps 3-5)
- **Activities**:
  - **Literature Review**: Find academic sources for causal relationships
  - **Expert Interviews**: Gather stakeholder experiences `[E]`
  - **Observations/Case Studies**: Collect empirical evidence `[O]`
  - **Evidence Integration**: Update connections from `[?]` or `[A]` to `[1-9]+]`, `[E]`, or `[O]`
  - **Model Refinement**: Adjust factors, relationships, or descriptions based on evidence

**Deliverables**:
- Validated Reference Model: `{domain}-reference-model.json`
- >75% connections with literature sources `[1-9]+]`
- Documented evidence in connection descriptions
- Commits: `[REFERENCE] Add literature source [X] for {connection}`

**Quality Gate**: Peer Review approval - Reference Model is now empirically grounded

**Evidence Coverage Target**: >90% connections with documented sources (not `[?]`)

---

#### Prescriptive Study (PS) - Designing Intervention

**DRM Definition**: Development of support/intervention based on findings from DS-I to address key factors.

**Wirkmechanismen Implementation**:
- **Phase**: Impact Model Design and Review (steps 3-4)
- **Activities**:
  - **Support Design**: Create concrete interventions (tools, methods, processes)
  - **Causal Modeling**: Define Support → Key Factor relationships
  - **Assumption Documentation**: Mark all new relationships as `[A]` with theoretical justification
  - **Mechanism Explanation**: Document how each support is expected to work
  - **Implementation Planning**: Define how supports will be deployed and measured

**Deliverables**:
- Detailed Impact Model: `{domain}-impact-model.json` (may still have `-wip`)
- Support elements with clear descriptions
- All new connections marked `[A]` with justifications
- Validation plan for each assumption
- Commits: `[IMPACT] Add {N} support interventions targeting {key factors}`

**Quality Gate**: Peer Review approval - Impact Model is theoretically sound and ready for testing

**Assumption Quality Target**: 100% of `[A]` connections have documented justification

---

#### Descriptive Study II (DS-II) - Evaluating Impact

**DRM Definition**: Empirical evaluation of the support's impact by comparing actual outcomes to the Impact Model's predictions.

**Wirkmechanismen Implementation**:
- **Phase**: Impact Model Piloting and Validation (steps 5-7)
- **Activities**:
  - **Pilot Implementation**: Deploy supports in small-scale setting
  - **Before/After Measurement**: Measure key factors pre- and post-intervention
  - **Qualitative Evidence**: Conduct interviews and observations
  - **Hypothesis Testing**: Compare actual vs. expected causal effects
  - **Model Updates**: Change `[A]` → `[O]` for validated relationships
  - **Iteration**: Refine supports based on pilot learnings
  - **Quantitative Validation** (optional): Larger-scale controlled studies

**Deliverables**:
- Empirically validated Impact Model: `{domain}-impact-model.json` (finalized)
- Evidence of pilot results (data, interview summaries)
- Updated connections: `[A]` → `[O]` for confirmed relationships
- Commits: `[IMPACT] Validate assumption for {connection} based on {pilot/study}`
- Validation report or summary

**Quality Gate**: Empirical evidence confirms (or refutes) assumptions

**Validation Target**: ≥75% of assumptions validated through pilots or studies

**Feedback Loop**: Validated support-relationships integrated into Main Model

---

### DRM Stage Progression Workflow

```
┌──────────────────────────────────────────────────────────────┐
│                    DRM RESEARCH CYCLE                        │
└──────────────────────────────────────────────────────────────┘

RC: Research Clarification
│
├─ Activity: Define problem and scope
├─ Output: Initial Reference Model (draft)
├─ Output: Initial Impact Model (draft)
└─ Decision: Proceed to DS-I
    │
    ↓
DS-I: Descriptive Study I (Understand Current State)
│
├─ Activity: Literature review
├─ Activity: Expert interviews
├─ Activity: Case studies / observations
├─ Output: Validated Reference Model (>75% literature coverage)
└─ Decision: Proceed to PS
    │
    ↓
PS: Prescriptive Study (Design Intervention)
│
├─ Activity: Design support interventions
├─ Activity: Model expected causal effects
├─ Activity: Document assumptions [A]
├─ Output: Detailed Impact Model with supports
└─ Decision: Proceed to DS-II
    │
    ↓
DS-II: Descriptive Study II (Evaluate Impact)
│
├─ Activity: Pilot implementation
├─ Activity: Before/after measurement
├─ Activity: Validate assumptions [A] → [O]
├─ Output: Empirically validated Impact Model
└─ Decision: Integrate findings into Main Model
    │
    ↓
Main Model Update: Consolidate validated knowledge
```

### Using DRM Stages in Practice

**For Researchers**:
1. **Start with RC**: Clearly define your research question and scope before creating models
2. **Don't skip DS-I**: Validate your Reference Model with evidence before designing interventions
3. **Be explicit in PS**: Document all assumptions - they will be tested in DS-II
4. **Measure in DS-II**: Plan measurement criteria during PS, execute during DS-II

**For Reviewers**:
- **RC Review**: Check clarity of research goals and model scope
- **DS-I Review**: Verify evidence quality and coverage
- **PS Review**: Assess intervention logic and assumption quality
- **DS-II Review**: Validate empirical methods and evidence interpretation

**Commit Message Tagging** (Optional):
```
[REFERENCE|RC] Initial reference model for {domain}
[REFERENCE|DS-I] Add literature evidence for {connections}
[IMPACT|RC] Initial impact model with {N} supports
[IMPACT|PS] Refine support design based on review
[IMPACT|DS-II] Validate assumptions from pilot study
```

---

## Review Process Details

### 1. Automated Review (Technical Gate-Keeper)

**Purpose**: Technical validation of model structure and syntax

**Tools**:
- `scripts/lint_blueprint.py` - JSON schema validation

**Checks**:
- JSON syntax correctness
- Schema compliance
- Element/connection ID uniqueness
- Referential integrity (from/to IDs exist)

**Output**: Pass/Fail with error messages

**Decision**: Automatically block commit/merge if validation fails

### 2. Agentic Review (Methodological Gate-Keeper)

**Purpose**: Semantic and methodological quality assessment using AI/LLM

**Current Implementation**: Manual/on-demand (e.g., asking Claude to review factors or models)

**AI-assisted checks**:
- DRM methodology compliance (attribute-of-element formulation)
- Factor formulation quality and precision
- Source attribution completeness
- Topological integrity (causal logic)
- Relevance to domain context
- Causal plausibility assessment

**Output**: Recommendation report with:
- ✅ Pass/❌ Fail for each criterion
- List of issues to address
- Suggestions for improvement
- Contextual explanations

**Decision**: Recommend approval, changes, or rejection (advisory to Human Review)

**Future Enhancement**: Systematized/automated triggering of agentic review in workflow (e.g., pre-commit hook, GitHub Action)

### 3. Human Review

**Purpose**: Expert assessment of scientific validity and practical utility

**Responsibilities**:
- Verify causal logic and theoretical grounding
- Assess literature quality and relevance
- Check practical implementability (for Impact Models)
- Validate measurement approaches
- Ensure clarity and precision of descriptions

**Decision Authority**: Approve, Request Changes, or Reject

**Documentation**: Code review comments on GitHub PR or commit

### 4. Peer Review

**Purpose**: Independent validation and final quality gate

**Responsibilities**:
- Independent verification of all human review points
- Cross-check literature references
- Validate evidence quality and completeness
- Assess downstream impact on model ecosystem
- Final approval for merge/validation status

**Decision Authority**: Final Approve or Reject

**Documentation**: PR approval or rejection with detailed comments

---

## Quality Metrics and Monitoring

### Model Health Indicators

Track these metrics for each model:

| Metric | Target | Measurement |
|--------|--------|-------------|
| Evidence Coverage | >90% | Percentage of connections with documented sources (not `[?]`) |
| Literature Coverage | >75% (Reference) / >50% (Impact) | Percentage of connections with literature references `[1-9]+` |
| Assumption Ratio | <30% (Impact Models) | Percentage of connections marked `[A]` |
| Factor Precision | 100% | Compliance with "attribute-of-element" formulation |
| Network Connectivity | <5% | Percentage of orphaned elements |
| Topological Integrity | 100% | Reference: Key Factor → Success Factor; Impact: Support → Success Factor |

### Rejection Thresholds

See detailed criteria in:
- [GATEKEEPING_CRITERIA.md](GATEKEEPING_CRITERIA.md) - General thresholds
- [REFERENCE_MODEL_CRITERIA.md](REFERENCE_MODEL_CRITERIA.md) - Reference Model specific
- [IMPACT_MODEL_CRITERIA.md](IMPACT_MODEL_CRITERIA.md) - Impact Model specific

---

## File Organization

```
models/
├── main_model/
│   └── wirkmechanismen-main-model-blueprint.json  # Source of truth
├── reference_models/
│   ├── {domain}-reference-model.json              # Validated reference models
│   └── {domain}-reference-model-wip.json          # Work-in-progress
└── impact_models/
    ├── {domain}-impact-model.json                 # Validated impact models
    └── {domain}-impact-model-wip.json             # Work-in-progress
```

**Naming Conventions**: See [NAMING_CONVENTIONS.md](NAMING_CONVENTIONS.md)

---

## Version Control and Git Workflow

### Commit Message Format

```
[MODEL_TYPE] Brief description

Detailed explanation:
- What changed
- Why it changed
- Evidence sources (if applicable)
- Validation status (if applicable)
```

**Examples**:
```
[MAIN] Add "Präzision der adressierten Probleme" factor

Added new factor distinguishing problem discovery (why/what) from
refinement execution (how). Based on Opportunity Canvas framework
and validated through expert interviews [E].

[REFERENCE] Add backlog-refinement quality reference model

Scaffolded from main model following strict topology requirements.
Includes 5 factors with >80% literature coverage.

[IMPACT] Validate assumption for backlog-refinement support

Pilot study with 3 teams confirmed that moderation guidelines improve
refinement quality. Updated connection from [A] to [O] with pilot data.
```

### Branch Strategy (Optional)

**For Main Branch Development**:
- Direct commits for minor refinements
- Feature branches for major restructuring

**For PR-Based Workflow**:
```
main (protected)
├── feature/{domain}-reference-model
├── feature/{domain}-impact-model
└── refactor/{description}
```

**Merge Process**:
1. Create feature branch
2. Make changes and commit
3. Push branch: `git push -u origin feature/{name}`
4. Create PR: `gh pr create` (after `gh auth login`)
5. Agentic + Human + Peer Review
6. Merge to main
7. Delete feature branch

---

## Validation Status Tracking

### Status Levels

| Status | Meaning | Indicator |
|--------|---------|-----------|
| Draft | Initial scaffolding | `-wip` suffix in filename |
| Human Reviewed | Passed initial review | Commit with `[REVIEW]` tag |
| Peer Validated | Ready for use/piloting | Standard filename (no `-wip`) |
| Empirically Validated | Pilot-tested (Impact Models) | Commit: `[IMPACT] Validate assumption...` |
| Production | Integrated into Main Model | Present in `main_model/` |

### Tracking Validation Progress

**Method**: Git commit history and messages

**Pattern**:
1. Initial: `[REFERENCE] Add {domain} reference model (draft)`
2. Human Review: `[REFERENCE] Address review comments for {domain}`
3. Peer Validation: `[REFERENCE] Finalize {domain} reference model after peer review`
4. Rename: Remove `-wip` suffix, commit as `[REFERENCE] Promote {domain} to validated status`

**For Impact Models**:
1. Initial: `[IMPACT] Add {domain} impact model with {N} supports (draft)`
2. Pilot: `[IMPACT] Update {domain} based on pilot results`
3. Validation: `[IMPACT] Validate assumption [A] → [O] for {connection}`
4. Multiple validations tracked as separate commits

---

## Tools and Automation

### Blueprint Linter
**Script**: `scripts/lint_blueprint.py`

**Usage**:
```bash
# Validate all models
python scripts/lint_blueprint.py

# Validate specific model
python scripts/lint_blueprint.py models/reference_models/your-model.json
```

**Pre-commit Hook** (Optional):
```bash
git config core.hooksPath githooks
```
This runs linter automatically before each commit.

### Agentic Review Systematization (Future Enhancement)
**Purpose**: Automated triggering and orchestration of AI/LLM-based methodological review

**Current State**: Agentic review is performed manually/on-demand (e.g., asking Claude to review factors)

**Planned Capabilities**:
- Automated invocation of AI/LLM review (pre-commit hook, GitHub Action)
- Check DRM formulation compliance
- Verify source attribution completeness
- Validate topology (start/end nodes)
- Calculate quality metrics
- Generate structured review report
- Integration with pull request workflow

**Status**: Manual/on-demand currently; systematization to be implemented

---

## Common Workflows

### Workflow A: Refining Main Model Description

```bash
# 1. Edit the main model
vim models/main_model/wirkmechanismen-main-model-blueprint.json

# 2. Run linter
python scripts/lint_blueprint.py

# 3. Commit with descriptive message
git add models/main_model/wirkmechanismen-main-model-blueprint.json
git commit -m "[MAIN] Refine description for {factor name}

Updated description to clarify distinction between {concept A} and {concept B}.
Added measurability indicators for better operationalization."

# 4. Push (if using remote)
git push origin main

# Note: For Main Model changes, follow Phase 1 review process
```

### Workflow B: Creating New Reference Model

```bash
# 1. Scaffold from main model (manual or agentic)
# Create: models/reference_models/my-problem-reference-model-wip.json

# 2. Validate against criteria
python scripts/lint_blueprint.py models/reference_models/my-problem-reference-model-wip.json

# 3. Commit draft
git add models/reference_models/my-problem-reference-model-wip.json
git commit -m "[REFERENCE] Add my-problem reference model (draft)

Scaffolded from main model focusing on {problem description}.
Includes {N} factors with causal chain from {key factor} to {success factor}.
Initial literature coverage: {X}%."

# 4. Human review → address comments → peer review

# 5. After validation, rename and finalize
git mv models/reference_models/my-problem-reference-model-wip.json \
       models/reference_models/my-problem-reference-model.json
git commit -m "[REFERENCE] Finalize my-problem reference model

Passed peer review with {N} literature sources and complete causal chain.
Ready for use as basis for impact model."
```

### Workflow C: Creating and Validating Impact Model

```bash
# 1. Start from validated reference model
# Create: models/impact_models/my-problem-impact-model-wip.json
# Add Supports and [A] connections

# 2. Validate
python scripts/lint_blueprint.py models/impact_models/my-problem-impact-model-wip.json

# 3. Commit draft
git add models/impact_models/my-problem-impact-model-wip.json
git commit -m "[IMPACT] Add my-problem impact model with {N} supports (draft)

Derived from validated reference model. Introduces supports:
- {Support 1}: {brief description}
- {Support 2}: {brief description}

All new connections marked [A] with theoretical justification.
Pilot study planned for {timeframe}."

# 4. Human + Peer review

# 5. Pilot implementation
# ... collect data ...

# 6. Update model with pilot results
vim models/impact_models/my-problem-impact-model-wip.json
# Change [A] → [O] for validated connections

git add models/impact_models/my-problem-impact-model-wip.json
git commit -m "[IMPACT] Validate assumptions for my-problem based on pilot

Pilot study with {N} teams/{participants} confirmed:
- Support {X} → Factor {Y}: {result summary}
- Updated connections from [A] to [O]

Next: Scale to larger group for quantitative validation."

# 7. After full validation, finalize
git mv models/impact_models/my-problem-impact-model-wip.json \
       models/impact_models/my-problem-impact-model.json
git commit -m "[IMPACT] Finalize my-problem impact model

All assumptions validated through {pilot/study}.
{X}% of support-connections confirmed with empirical evidence [O].
Ready for production use and main model integration."

# 8. Feed back to main model
# Extract validated Support-relationships and add to main model
```

---

## Best Practices

### For Contributors

1. **Start Small**: Begin with focused, well-scoped models (3-7 factors)
2. **Follow DRM Strictly**: Always use "attribute-of-element" formulation
3. **Document Sources**: Never skip source attribution - use `[A]` if uncertain
4. **Validate Incrementally**: Don't wait to validate all at once
5. **Communicate**: Use descriptive commit messages and PR descriptions
6. **Iterate**: Expect multiple review cycles - embrace feedback

### For Reviewers

1. **Be Systematic**: Check each criterion category in order
2. **Verify Evidence**: Don't accept sources without checking validity
3. **Think Causality**: Question "does X really cause Y?" rigorously
4. **Check Assumptions**: For Impact Models, ensure all `[A]` are justified
5. **Provide Constructive Feedback**: Suggest improvements, not just rejections
6. **Document Decisions**: Write clear review comments for traceability

### For Maintainers

1. **Monitor Quality Metrics**: Track evidence coverage and model health over time
2. **Update Criteria**: Evolve gatekeeping criteria based on learnings
3. **Enhance Tooling**: Improve linter and automation as needed
4. **Facilitate Reviews**: Connect contributors with appropriate peer reviewers
5. **Maintain Main Model**: Ensure Main Model remains the authoritative source

---

## Frequently Asked Questions

### Q: When should I create a new Reference Model vs. extending the Main Model?

**A**: Create a Reference Model when:
- You have a specific problem or research question
- You need a focused causal chain for analysis
- You want to isolate a subset of factors for intervention planning

Extend the Main Model when:
- You've validated new factors or relationships across multiple contexts
- You're refining definitions or adding universal attributes
- You're consolidating knowledge from multiple Reference/Impact Models

### Q: Can I skip the Automated Review?

**A**: No. Automated Review via `lint_blueprint.py` is mandatory as the first technical quality gate. It catches structural and syntactic errors that would block the workflow.

### Q: Is Agentic Review required?

**A**: Highly recommended but currently manual. Agentic review (AI/LLM-based semantic and methodological review) provides valuable feedback on DRM compliance, factor formulation quality, and causal plausibility. Currently, this is done by asking Claude to review factors or models on-demand. Future enhancement will systematize this as an automated workflow step.

### Q: What if my Impact Model assumption `[A]` cannot be validated?

**A**:
1. Document the blocker: "Cannot validate due to {reason}"
2. Keep as `[A]` with clear documentation
3. Consider alternative validation methods (expert validation `[E]`, analogies)
4. If critical, may need to reject or revise the intervention

### Q: How do I handle contradictory evidence?

**A**:
1. Document both perspectives in connection `description`
2. Escalate to Peer Review for expert arbitration
3. Consider context-dependent relationships (may vary by domain)
4. If unresolvable, mark as `[?]` and plan investigation

### Q: Can Impact Models have multiple Supports?

**A**: Yes! Impact Models commonly have 1-3 Supports addressing different aspects of Key Factors. Ensure each Support has clear causal connections and validation plans.

### Q: What's the difference between `[E]` (experience) and `[O]` (own investigation)?

**A**:
- `[E]`: Stakeholder experience, qualitative insights, domain expertise (less formal)
- `[O]`: Systematic investigation - pilot studies, data collection, controlled observations (more rigorous)

Use `[E]` for expert opinions, `[O]` for empirical evidence you've collected.

---

## Summary

The Wirkmechanismen workflow ensures:
- **Scientific Rigor**: Through four-stage review (Automated → Agentic → Human → Peer) and incremental validation
- **Methodological Consistency**: Via DRM compliance and quality gates
- **Systematic Evolution**: Main Model ← Reference Models ← Impact Models
- **Evidence-Based**: All claims traced to literature, experience, or investigation
- **AI-Enhanced Quality**: Agentic review for semantic and methodological assessment (currently manual, systematization planned)
- **Collaborative**: Clear roles for contributors, reviewers, and maintainers
- **Transparent**: Version-controlled with comprehensive documentation

Follow this workflow to maintain the integrity and utility of the Wirkmechanismen factor network models for design research.

---

## Related Documentation

- [GATEKEEPING_CRITERIA.md](GATEKEEPING_CRITERIA.md) - General quality criteria for all models
- [REFERENCE_MODEL_CRITERIA.md](REFERENCE_MODEL_CRITERIA.md) - Specific criteria for Reference Models
- [IMPACT_MODEL_CRITERIA.md](IMPACT_MODEL_CRITERIA.md) - Specific criteria for Impact Models
- [NAMING_CONVENTIONS.md](NAMING_CONVENTIONS.md) - File and element naming standards
- [README.md](README.md) - Project overview and methodology introduction
