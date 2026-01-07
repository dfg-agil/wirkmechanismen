# Reference Model Generation Criteria (V3)

## Overview

This file defines specific criteria for generating reference models in the Wirkmechanismen project. It complements the general gatekeeping criteria with concrete structural rules for consistent and focused models.

## Structural Requirements

### 1. Element taxonomy (MANDATORY)

#### 1.1 Key Factor structure (updated: primary + optional secondary)
- **MANDATORY**: At least **ONE (1) Key Factor** per reference model.
- **MANDATORY**: Exactly **ONE (1) primary Key Factor** MUST be designated.
- **OPTIONAL**: Additional **secondary Key Factors** are allowed (e.g., multi-causal starting points or multiple intervention levers).
- **DEFINITION**: Key Factors represent central problem drivers and serve as primary intervention targets.
- **CLASSIFICATION**: `"element type": "Schlüsselfaktor"`
- **PRIMARY/SECONDARY TAGGING (schema-neutral)**:
  - **MANDATORY**: The primary Key Factor MUST include the tag `[PRIMARY]` at the beginning of `attributes.description`.
  - **OPTIONAL/RECOMMENDED**: Secondary Key Factors SHOULD include `[SECONDARY]` at the beginning of `attributes.description`.
- **REJECT**:
  - models with **zero** Key Factors
  - models with **more than one** `[PRIMARY]` Key Factor tag

#### 1.2 Success Factor structure (updated: not restricted to exactly one)
- **MANDATORY**: At least **ONE (1) Success Factor** per reference model.
- **ALLOWED**: Multiple Success Factors are permitted to represent multi-dimensional goal systems (e.g., quality, cost, time, sustainability).
- **DEFINITION**: Long-term, overarching objectives (e.g., product quality, customer satisfaction).
- **CLASSIFICATION**: `"element type": "Erfolgsfaktor"`
- **MANDATORY (proxy rule, generalized)**: If a Success Factor is not directly measurable (`measurability < 0.8`), a measurable proxy MUST be added.
  - **CLASSIFICATION (proxy)**: `"element type": "Messbarer Erfolgsfaktor"`
  - **TRACEABILITY (schema-neutral)**: The proxy relationship MUST be explained in the proxy's `attributes.description` (e.g., "Proxy for Erfolgsfaktor X because …").
- **REJECT**: models with **zero** Success Factors.

#### 1.3 Influencing Factors classification (updated: remove 3–7 recommendation)
- **MANDATORY**: All other factors MUST be classified as Influencing Factors.
- **CLASSIFICATION**: `"element type": "Einflussfaktoren"`
- **REMOVED**: No fixed recommendation of "3–7 Influencing Factors".
- **REVIEW REQUIRED**: Models with **>10** Influencing Factors (complexity and maintainability check).

### 2. Causal chain / network structure (MANDATORY)

#### 2.1 Causal network topology (updated to support network structure with feedback loops)
- **MANDATORY**: The **primary Key Factor** SHOULD be a start node (no incoming connections within the model), but secondary Key Factors MAY have incoming connections if justified.
- **MANDATORY**: All Success Factors SHOULD be end nodes (no outgoing connections within the model), but feedback loops to Influencing Factors are allowed if they represent dynamic system behavior.
- **MANDATORY**: All Influencing Factors MUST be causally positioned between Key Factor(s) and Success Factor(s).
- **STRUCTURE (network-based, dynamic)**:
  - Primary flow: `Key Factor(s) → [Influencing Factors] → [Measurable Success Factor(s)] → Success Factor(s)`
  - Allowed: Feedback loops between Influencing Factors, from Success Factors to Influencing Factors (if mechanism is explicit), and between Influencing Factors and Key Factors (representing dynamic reinforcement)
- **RATIONALE**: Reference Models should represent complex, dynamic systems. Simple linear chains don't capture how factors influence each other over time.

#### 2.2 Path requirements (updated to support dynamic network topology with feedback)
- **MANDATORY**: There MUST be at least one directed path from the **primary Key Factor** to **at least one** Success Factor.
- **MANDATORY**: Each Key Factor (primary and secondary) MUST have at least one directed path to **at least one** Success Factor.
- **MANDATORY**: Maximum path length for primary chains: **4 directed connections** between any Key Factor and any Success Factor along a valid path.
- **ALLOWED (NEW)**: Feedback loops and cyclic connections representing dynamic system behavior:
  - From Influencing Factors back to other Influencing Factors (reinforcement loops, time delays)
  - From Success Factors back to Influencing Factors (if representing dynamic outcomes feeding back into the system)
  - Between Key Factors and Influencing Factors (representing mutual influences or learning)
- **CRITICAL**: All feedback loops MUST be explicitly justified in connection descriptions (mechanism, time horizon, feedback mechanism)
- **REJECT**:
  - Influencing Factors with no connection to any Key→Success path
  - Feedback loops without explicit causal explanation

### 3. Source attribution (MANDATORY)

#### 3.1 Literature-based connections (priority 1)
- **TARGET**: >50% of all connections with literature sources `[1]`, `[2]`, etc.
- **MANDATORY**: Literature sources MUST be documented in `connection.attributes.description`.
- **FORMAT**: Full academic citation (APA style).
- **REJECT**: literature labels without corresponding documentation.

#### 3.2 Empirical evidence (priority 2)
- **ALLOWED**: stakeholder experience `[E]`, assumption `[A]`, or own investigations `[O]`.
- **MANDATORY**: Describe the evidence basis in `connection.attributes.description`.
- **LIMIT**: Max. 50% of connections without literature basis.

#### 3.3 Invalid sources
- **REJECT**: connections with `[?]` (unknown source)
- **REJECT**: connections without source attribution

### 4. Measurability and influenceability criteria

#### 4.1 Measurability (`measurability`)
**Scale: 0, 0.5, or 1.0 (discrete values, not continuous)**

- **0 = Not directly measurable** (z.B. qualitative Befragung, subjektive Beobachtung ohne klare Metrik)
  - No clear quantitative or defined qualitative indicators
  - Requires expert judgment for assessment
  - Example: "Vertrauen im Team", "Kulturelle Akzeptanz"

- **0.5 = Partially/indirectly measurable** (z.B. qualitative Daten, aber ergänzt durch quantitative Indikatoren oder Skalen)
  - Measurable through qualitative data with structured indicators or scales
  - Combination of qualitative assessment and quantitative proxies
  - Example: "Qualität der Kommunikation" (via surveys + frequency analysis)

- **1 = Directly measurable** (z.B. Kennzahlen, Anzahl, Zeitmessungen, Scores, klar definierte Metriken)
  - Clear numerical values, counts, time measurements, well-defined metrics
  - No ambiguity in measurement
  - Example: "Anzahl der gelösten Issues", "Durchschnittliche Cycle Time"

- **MANDATORY**: Key Factors MUST be measurable (`measurability ≥ 0.5`). Preference for `measurability = 1.0`.
- **MANDATORY**: Measurable Success Factors MUST be highly measurable (`measurability = 1.0`).
- **MANDATORY**: Success Factors may have lower measurability (`measurability ≥ 0`), but at least one measurable proxy should exist.
- **DOCUMENTATION**: Measurement methods MUST be specified in `attributes.description`.

#### 4.2 Influenceability (`influenceability`)
**Scale: 0, 0.5, or 1.0 (discrete values, not continuous)**

- **0 = Difficult or not directly influenceable** (schwer beeinflussbar)
  - External factors, boundary conditions, not under control
  - Require indirect mitigation strategies
  - Example: "Marktnachfrage", "Regulatorische Anforderungen"

- **0.5 = Partially influenceable via intermediary factors** (teilweise beeinflussbar / nur über mittlebare Faktoren)
  - Influenceable only through influencing other factors
  - Requires multi-step interventions
  - Example: "Teamvertrauen" (influenced via better communication, shared goals)

- **1.0 = Directly influenceable** (direkt beeinflussbar, z.B. konkrete Maßnahmen, Regeln, Tools)
  - Direct control through concrete measures, rules, tools, processes
  - Clear intervention points
  - Example: "Durchsatzzeit" (via process changes), "Dokumentation" (via tool implementation)

- **MANDATORY**: Key Factors MUST be influenceable (`influenceability ≥ 0.5`). Preference for `influenceability = 1.0`.
- **EXPECTATION**: Success Factors typically have low influenceability (often ≤ 0.5), as they are outcomes.
- **LOGIC CHECK**: Influenceability MUST be consistent with factor role and design research philosophy (focus on actionable factors).

### 5. Connection semantics

#### 5.1 Direction and polarity
- **MANDATORY**: All connections MUST be directed (`"direction": "directed"`).
- **MANDATORY**: Connection type MUST use DRM polarities (`++`, `+-`, `-+`, `--`).
- **RECOMMENDATION**: Positive main chain from Key Factor(s) to Success Factor(s), where plausible.

#### 5.2 Connection descriptions
- **MANDATORY**: Each connection MUST explain the causal mechanism in `attributes.description`.
- **FORMAT**: "Factor X leads to Factor Y through mechanism Z."
- **LENGTH**: 20–150 words per description.

### 6. Validation steps

#### 6.1 Automated validation
1. JSON schema compliance (`lint_blueprint.py`)
2. Element/connection ID uniqueness
3. Reference integrity (`from`/`to` refer to existing IDs)
4. Factor taxonomy compliance
5. **Topology validation**:
   - exactly one `[PRIMARY]` Key Factor tag
   - Primary Key Factor SHOULD be a start node (or justified if not)
   - Success Factor(s) SHOULD be end nodes (or justified if not)
   - No isolated factors
6. **Feedback loop validation**: All feedback loops have explicit causal explanations

#### 6.2 Content validation
1. **Network topology** (dynamic, not strictly linear):
   - Primary Key Factor SHOULD have no incoming connections (justified if present)
   - Success Factor(s) SHOULD have no outgoing connections (justified if feedback loops exist)
   - Feedback loops are documented with explicit causal mechanisms
2. **Path completeness**:
   - at least one primary path: Primary Key → some Success Factor
   - each Key Factor reaches at least one Success Factor (direct or via feedback)
3. **Network integrity**:
   - all Influencing Factors are connected to at least one Key→Success path
   - feedback loops represent valid causal mechanisms (not circular reasoning)
4. Compute source attribution ratio
5. Validate measurability/influenceability consistency (using 0, 0.5, 1.0 scale)
6. Check factor formulation according to DRM principles ("attribute-of-an-element" phrasing)

#### 6.3 Quality metrics
- **Evidence Coverage**: ≥75% literature sources `[1-9]+`
- **Topological Integrity**: 100% - Primary Key Factor is a start node (or justified); all Success Factors are end nodes (or justified); no isolated factors
- **Path Completeness**: 100% - each Key Factor participates in a valid Key→Success chain (primary paths)
- **Network Dynamics**: Feedback loops (if present) are explicitly justified with causal mechanisms
- **Factor Integration**: 100% - all Influencing Factors are integrated into at least one Key→Success argument chain
- **Factor Precision**: 100% - all factors follow "attribute-of-an-element" formulation
- **Measurability Consistency**: Key Factors measurable (≥0.5, prefer 1.0); Measurable Success Factors = 1.0; Success Factors ≥0

## Compliance checklist

### Pre-submission
- [ ] At least 1 Key Factor present
- [ ] Exactly 1 Key Factor tagged `[PRIMARY]` in `attributes.description`
- [ ] At least 1 Success Factor present
- [ ] For each Success Factor with `measurability < 0.8`, a Measurable Success Factor proxy is included and documented
- [ ] At least one causal path from primary Key Factor → some Success Factor exists
- [ ] Each Key Factor has at least one causal path to at least one Success Factor
- [ ] >50% of connections have literature sources
- [ ] All literature sources are documented (APA style)
- [ ] No `[?]` sources in the model
- [ ] Measurability/influenceability values are consistent
- [ ] JSON validation passes

### Review criteria
- [ ] Causal chains are scientifically plausible
- [ ] Factor formulations are precise and unambiguous
- [ ] Literature sources are relevant and current
- [ ] Model complexity is appropriate for the research question (no fixed count; justified by scope)
- [ ] Connection descriptions are informative and mechanism-based

## Rejection criteria (updated)

- **AUTOMATIC REJECT**: Zero Key Factors
- **AUTOMATIC REJECT**: More than one Key Factor tagged `[PRIMARY]`
- **AUTOMATIC REJECT**: Zero Success Factors
- **AUTOMATIC REJECT**: Broken causal chains (factors not connected to any Key→Success argument chain)
- **AUTOMATIC REJECT**: <50% literature sources
- **AUTOMATIC REJECT**: Unknown sources `[?]`
- **AUTOMATIC REJECT**: JSON schema violations
- **AUTOMATIC REJECT**: Factors not formulated as "attribute-of-an-element"

## Summary (V3 - Updated with Dynamic Network Topology)

Reference Models represent the current state for specific problems. They:
1. Have **at least one Key Factor**, with **exactly one designated as the primary Key Factor** (preferably start node); **secondary Key Factors** are allowed.
2. Have **at least one Success Factor** (preferably end node); **multiple Success Factors** are allowed to reflect multi-dimensional objectives.
3. Use **Influencing Factors** and **feedback loops** to model complex, dynamic causal chains linking Key Factor(s) to Success Factor(s). All factors integrated into at least one valid Key→Success argument chain (no isolated factors).
4. **Support network topology** with feedback loops:
   - Primary flow: Key Factor(s) → Influencing Factors → Success Factor(s)
   - Allowed: Feedback from Success Factors to Influencing Factors, between Influencing Factors (reinforcement), and between Key Factors and Influencing Factors (dynamic mutual influences)
   - All feedback loops MUST be explicitly justified with causal mechanisms
5. Are grounded in **literature evidence** (>50% coverage) and transparent source attribution.
6. Use **discrete measurability/influenceability scales** (0, 0.5, 1.0) for consistency and clarity.
7. Follow **DRM attribute-of-element** formulation and document causal mechanisms for each connection.
8. Serve as the foundation for creating **Impact Models**.

Reference Models establish the baseline understanding of complex, dynamic systems necessary for designing and evaluating interventions.
