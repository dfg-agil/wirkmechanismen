# Gatekeeping Criteria for Wirkmechanismen Model Changes (V4)

## Overview

This document establishes mandatory criteria for accepting or rejecting changes to the Wirkmechanismen factor network models. These criteria ensure model integrity, methodological consistency, and scientific rigor while maintaining compatibility with KUMU visualization and DRM methodology principles.

V4 keeps the proven V3 structure and quality gates, and adds explicit Main Model governance rules for controlled growth.

**Scope and normative language**
- Gatekeeping rules govern merge-ready changes, especially changes to the Main Model.
- RM-specific and IM-specific criteria remain the controlling rules for the respective model type where this document defines only a general quality target.
- `MUST`/`MANDATORY` are hard acceptance criteria; `MUST NOT`/`REJECT` are hard exclusion criteria; `SHOULD`/`REVIEW REQUIRED` are review guidance unless an applicable RM/IM criterion makes the requirement mandatory.

## Critical Gate-Keeping Criteria

### 1. DRM Methodology Compliance

#### 1.1 Factor Formulation Requirements
- **MANDATORY**: All factor labels MUST follow "attribute-of-element" formulation
  - ✅ `"Qualität der Problemdefinition"`
  - ❌ `"Problemdefinition"` (raw element)
  - ❌ `"Hohe Qualität der Problemdefinition"` (includes values)
- **MANDATORY**: Factor labels MUST be measurable/observable attributes
- **MANDATORY**: No value judgments (high/low/good/bad) in factor labels
- **REJECT**: Any change introducing non-DRM factor naming

#### 1.2 Element Type Classification
- **MANDATORY**: All elements MUST have valid `"element type"` from approved taxonomy:
  - `"Einflussfaktoren"` - Standard influencing factors
  - `"Schlüsselfaktor"` - Key factors (intervention targets)
  - `"Erfolgsfaktor"` - Success factors (outcomes)
  - `"Messbarer Erfolgsfaktor"` - Measurable success factors (proxies)
  - `"Support"` - Interventions (Impact Models only)
  - `"Problem"` - Scoping anchor where explicitly justified
- **REJECT**: Any element without proper classification
- **REJECT**: Arbitrary or non-standard element types

#### 1.3 Source Attribution Requirements
- **MANDATORY**: ALL causal connections MUST have source attribution in `attributes.label`:
  - `[0-9]+` - Literature reference number
  - `[A]` - Assumption (requires justification)
  - `[E]` - Stakeholder experience
  - `[O]` - Own investigation/empirical data
  - `[?]` - Unknown source (temporary and draft-only; requires investigation)
- **REJECT**: Any connection without source attribution
- **REJECT**: Merge-ready RM, IM, or Main Model connections with `[?]`; `[?]` may exist only in explicitly marked draft-only work.
- **REVIEW REQUIRED**: High proportion of `[?]` or `[A]` sources without documentation
- **REJECT**: Merge-ready Main Model changes containing `[?]` sources

### 2. Technical Schema Validation

#### 2.1 JSON Structure Integrity
- **MANDATORY**: All changes MUST pass `lint_blueprint.py` validation
- **MANDATORY**: Unique `_id` fields for all elements and connections
- **MANDATORY**: Valid references - all connection `from`/`to` MUST reference existing element `_id`
- **MANDATORY**: Required fields present:
  - Elements: `_id`, `attributes.label`, `attributes["element type"]`
  - Connections: `_id`, `from`, `to`, `direction`, `attributes.label`, `attributes["connection type"]`
- **REJECT**: Any JSON schema violations
- **REJECT**: Duplicate IDs across elements or connections

#### 2.2 Connection Semantics
- **MANDATORY**: `direction` MUST be from supported set: `["directed", "undirected", "mutual"]`
- **MANDATORY**: For causal RM/IM/Main links, `"directed"` is mandatory. `"undirected"` or `"mutual"` may be used only for explicitly documented non-causal relations outside the causal factor network.
- **MANDATORY**: `connection type` MUST use DRM sign pairs: `["++", "+-", "-+", "--"]` or single `"+"` for overall positive
- **MANDATORY**: Directional consistency - use `"directed"` for causal factor relations; any non-causal `"undirected"` or `"mutual"` relation requires explicit documentation.
- **REJECT**: Invalid direction values
- **REJECT**: Non-standard connection type codes

### 3. Model Consistency Requirements

#### 3.1 Network Topology Validation
- **MANDATORY**: No orphaned elements (elements without connections) unless justified as isolated factors
- **MANDATORY**: Newly introduced influencing factors in Main Model MUST have at least 1 incoming and 1 outgoing connection.
- **MANDATORY**: Key factors (`"Schlüsselfaktor"`) MUST connect to success factors via causal chains
- **MANDATORY**: Measurable success factors MUST have explicit proxy relationships to success factors
- **REVIEW REQUIRED**: Cycles in causal network (may be valid but require justification)
- **REVIEW REQUIRED**: Elements with extremely high connectivity (potential model complexity issues)

#### 3.2 Evidence Quality Standards
- **MANDATORY**: Literature references (`[1]`, `[2]`, etc.) MUST be documented and verifiable
- **MANDATORY**: Assumptions (`[A]`) in Impact Models MUST include rationale in connection `description`
- **REJECT**: Claims without evidence or clear assumption marking
- **ESCALATE**: Contradictory evidence requiring expert resolution

#### 3.3 Developer Confirmation for New Connections
- **MANDATORY (ABSOLUT)**: Neue Verbindungen (inkl. `from`, `to`, Richtung und `connection type`) dürfen **niemals** vom Assistenzsystem eigenständig festgelegt werden.
- **MANDATORY (ABSOLUT)**: Jede neue Verbindung muss **immer** vom Entwickler **explizit vorgegeben oder bestätigt** werden.
- **REVIEW REQUIRED**: Wenn der Entwickler die Bestätigung nicht gegeben hat, MUSS das Assistenzsystem dies aktiv einfordern und darf die Verbindung nicht implementieren.

**Exception for standalone Impact Model generation**
- The confirmation rule above governs changes to the Main Model and merge-ready
  model changes. It MUST NOT block generation of a standalone Impact Model for
  a user-described problem.
- In that workflow, the assistant MAY autonomously create Support elements and
  their new `[A]` connections, including an explicitly labelled
  `AI-generated support`, without intermediate developer confirmation.
- The exception is valid only when the Impact Model criteria are satisfied:
  the Support is explicitly labelled, targets inherited Main-Model factors,
  follows the Main Model's causal logic, and documents mechanism, direction,
  scoring, and validation plan.
- This exception does not permit an autonomous change to the Main Model. Any
  later promotion of an IM finding into the Main Model remains subject to this
  developer-confirmation rule.

### 4. Model Evolution Governance

#### 4.1 Reference vs Impact Model Integrity
- **MANDATORY**: Reference Models represent existing/current state only
- **MANDATORY**: Impact Models MUST clearly identify inherited, changed, removed, and newly introduced Reference Model relationships in the IM change log.
- **MANDATORY**: Impact Models MUST include `"Support"` elements for interventions
- **MANDATORY**: New relationships in Impact Models MUST be marked as assumptions `[A]` unless evidenced
- **REJECT**: Support interventions in Reference Models
- **REJECT**: Impact Models without clear intervention elements

#### 4.2 Context-sensitive polarity handling for RM/IM
- **MANDATORY**: RM and IM links MUST reflect the model context they represent.
- **MANDATORY**: RM links MUST represent the current/existing situation, while IM links MUST represent the desired post-intervention situation.
- **MANDATORY**: The polarity of RM/IM links MUST be chosen based on whether the link accurately represents that context, not by mechanically copying the Main Model.
- **ALLOWED**: If a Main Model connection is already source-supported and its polarity still accurately represents the RM/IM context, it MAY be adopted unchanged.
- **MANDATORY**: If the Main Model polarity would misrepresent the RM/IM context, the RM/IM connection MUST be adjusted and the rationale documented.
- **MANDATORY**: RM/IM connections that deviate from the Main Model polarity or direction for context reasons MUST include a short explanation in `description` or the applicable derivation log.

#### 4.3 Quantitative Attribute Consistency
- **MANDATORY**: `measurability` and `influenceability` scores (if present) MUST be in range [0, 1]. Valid values are [0, 0.5, 1.0].
- **MANDATORY**: Main Model intake for new influencing factors requires both values explicitly provided.
- **MANDATORY**: Quantitative attributes in the Main Model MUST have documented methodology/source. RM/IM-specific measurement and validation requirements are governed by the applicable RM/IM criteria.
- **REVIEW REQUIRED**: Significant changes to existing quantitative scores require justification
- **REJECT**: Arbitrary or unsupported quantitative values
- **REJECT**: New influencing factor in Main Model without both `measurability` and `influenceability`

#### 4.4 Main Model Growth Governance (new in V2)
- **MANDATORY**: New factors MUST be checked for semantic overlap with existing factors before insertion (MECE = mutually exclusive and collectively exhaustive).
- **MANDATORY**: If overlap exists, split/merge decision and rationale MUST be documented.
- **MANDATORY**: New factors SHOULD improve practical MECE quality (as far as realistically possible).
- **REVIEW REQUIRED**: Strong overlap with existing factors without clear differentiation.
- **REJECT**: Duplicate factor without explicit consolidation decision.

### 5. Documentation and Traceability

#### 5.1 Change Documentation Requirements
- **MANDATORY**: All model changes MUST include clear rationale
- **MANDATORY**: Source materials/references MUST be provided for new Main Model factors or evidenced connections. Support-driven IM connections may use `[A]` with the rationale and validation plan required by the IM criteria; an external source is not required before standalone IM generation.
- **MANDATORY**: Impact on existing model structure MUST be analyzed
- **REJECT**: Changes without adequate documentation

#### 5.2 Version Control Standards
- **MANDATORY**: Atomic commits - related changes in single commit
- **MANDATORY**: Descriptive commit messages following format: `[MODEL] Brief description of change`
- **MANDATORY**: Changes MUST pass automated linting before merge
- **REJECT**: Commits that break model integrity

### 6. Scientific Rigor Requirements

#### 6.1 Theoretical Foundation
- **MANDATORY**: New factors MUST align with established design research theory
- **MANDATORY**: Causal relationships MUST be theoretically sound or empirically supported
- **REVIEW REQUIRED**: Novel theoretical contributions require expert validation
- **REJECT**: Factors or relationships contradicting established design theory without justification

#### 6.2 Semantic Precision
- **MANDATORY**: Factor definitions MUST be precise and unambiguous
- **MANDATORY**: Avoid overlapping or redundant factors
- **MANDATORY**: German terminology MUST be consistent with established academic usage
- **REVIEW REQUIRED**: New terminology requires consensus validation
- **REJECT**: Vague or imprecise factor definitions

## Review Process Levels

### 1. Automated Validation (Pre-commit)
- JSON schema validation via `lint_blueprint.py`
- Unique ID verification
- Reference integrity checks
- Basic format compliance

### 2. Peer Review (Required)
- DRM methodology compliance
- Factor formulation quality
- Evidence quality assessment
- Model consistency validation

### 3. Expert Review (Escalation Triggers)
- Contradictory evidence resolution
- Novel theoretical contributions
- Significant model restructuring
- Cross-domain factor integration

### 4. Scientific Advisory (Complex Cases)
- Major methodology changes
- Cross-institutional model merging
- Publication-ready model validation
- Theoretical framework updates

## Quality Metrics and Thresholds

### Model Health Indicators
- **Evidence Coverage (Main Model health target)**: >90% of Main Model connections with documented sources (not `[?]`). RM-specific evidence thresholds govern Reference Models; IM assumptions are governed by the IM criteria.
- **Assumption Ratio**: No fixed percentage applies to Impact Models. Every support-driven `[A]` connection remains mandatory and requires the documentation and validation plan defined by the IM criteria.
- **Factor Precision**: 100% compliance with attribute-of-element formulation
- **Network Connectivity (health target)**: <5% unjustified orphaned elements; unjustified orphaned elements remain a rejection under the topology rules.
- **Reference Integrity**: 100% valid element/connection references

### Rejection Thresholds
- Any JSON schema violation -> **AUTOMATIC REJECT**
- >10% factors with invalid formulation -> **REJECT**
- >25% connections without source attribution -> **REJECT**
- >50% assumptions without documentation -> **REJECT**
- **REJECT:** Duplicate IDs, missing IDs, or `from`/`to` references that do not resolve to existing element IDs. Valid causal feedback loops are allowed when justified by the RM/IM topology rules.
- Any merge-ready Main Model change containing `[?]` sources -> **AUTOMATIC REJECT**
- New influencing factor without both metrics (`measurability`, `influenceability`) -> **AUTOMATIC REJECT**
- New influencing factor without minimum connectivity (>=1 incoming and >=1 outgoing) -> **AUTOMATIC REJECT**

## Implementation Guidelines

### For Contributors
1. **Pre-submission Checklist**: Verify all mandatory criteria before proposing changes
2. **Documentation Standards**: Include evidence sources and change rationale
3. **Incremental Changes**: Prefer small, focused modifications over large restructuring
4. **Validation Pipeline**: Ensure automated tests pass before submission

### For Reviewers
1. **Systematic Evaluation**: Check each criterion category systematically
2. **Evidence Verification**: Validate literature references and source claims
3. **Methodology Compliance**: Ensure DRM principles are maintained
4. **Impact Assessment**: Evaluate downstream effects on model usability

### For Maintainers
1. **Criteria Evolution**: Update criteria based on learned best practices
2. **Tool Integration**: Enhance automated validation capabilities
3. **Training Resources**: Provide guidance for common compliance issues
4. **Quality Monitoring**: Track model health metrics over time

## Conclusion

These gatekeeping criteria ensure that the Wirkmechanismen model maintains its scientific rigor, methodological consistency, and practical utility for design research. They balance the need for quality control with collaborative development, providing clear guidelines for contributors while preserving the model's integrity for academic and practical applications.

Adherence to these criteria is essential for maintaining the model's value as a reliable foundation for design research methodology applications and KUMU-based visualization and analysis.

## Ergänzung: Obligatorische Metriken für neue Einflussfaktoren

- **MANDATORY**: Jeder neue Einflussfaktor, der in das `main`-Modell integriert werden soll, darf nur dann übernommen werden, wenn sowohl `measurability` als auch `influenceability` explizit angegeben sind.
- **MANDATORY (ABSOLUT)**: `measurability` und `influenceability` dürfen **niemals** vom Assistenzsystem frei gewählt werden. Die Werte müssen **immer** vom Entwickler vorgegeben oder **explizit bestätigt** werden.
- **Zulässige Werte**: `0`, `0.5`, `1` (oder eine dokumentiert vereinbarte alternative Skala).
- **REJECT**: Vorschläge, die neue Faktoren ohne beide Metrikwerte hinzufügen, werden nicht gemergt.
- **REJECT**: Neue Einflussfaktoren dürfen nicht „lose“ im Modell stehen. Jeder neue Einflussfaktor muss mindestens 1 eingehende und 1 ausgehende Verbindung haben. Fehlt dies, wird der Merge blockiert.

- **Agenten-/Chat-Regel (Connectivity)**: Wenn neue Einflussfaktoren ohne mindestens 1 `indegree` und 1 `outdegree` vorgeschlagen werden, **muss** der Agent im Chat ablehnen und einen **Vorschlag für passende Verbindungen** machen. Erst nach Bestätigung/Anpassung durch den User darf weitergearbeitet werden.

- **Verfahren bei fehlenden Werten**:
  - Neue Faktoren dürfen zur Diskussion vorgeschlagen werden, müssen aber vor Merge vollständig ergänzt sein.
  - PRs mit fehlenden Metrikwerten sind nicht mergefähig.

- **Hinweis für Editoren/UX**: Beim Anlegen eines neuen Elements ohne Metrikwerte soll folgender Hinweis angezeigt werden:

  "Hinweis: Neue Einflussfaktoren müssen `measurability` und `influenceability` enthalten. Ohne diese Werte ist der Vorschlag nicht mergefähig."

- **Automatische Durchsetzung**: Empfohlen wird eine CI-Prüfung (oder Erweiterung von `scripts/lint_blueprint.py`), die neu hinzugefügte Elemente ohne diese Felder erkennt und den Pre-Merge-Check fehlschlagen lässt.

Ziel: Sicherstellen, dass jedes im Modell akzeptierte Element bewertbar (messbar) ist und eine dokumentierte Beeinflussbarkeit besitzt, um die analytische Nutzbarkeit des Modells zu erhalten.

## Ergänzung: Cluster-Pflicht für Einflussfaktoren

- **STATUS**: Jeder Einflussfaktor im 'wirkmechanismen-main-model-blueprint.json' hat nun eine Kategorie "cluster" und eine Kategorie "tags".
- **MANDATORY**: Jeder neue Einflussfaktor muss genau einem definierten Cluster zugeordnet sein.
- **MANDATORY**: Die Cluster-Zuordnung muss eindeutig sein und im MM beim Einflussfaktor eindeutig hinterlegt sein. (z. B. `attributes.cluster_id`).
- **REJECT (ab Aktivierung)**: Neue Einflussfaktoren ohne gültige Cluster-Zuordnung werden nicht aufgenommen.
- **REJECT (ab Aktivierung)**: Mehrfachzuordnungen ohne explizit freigegebenes Multi-Cluster-Konzept werden nicht aufgenommen.
- Die Regeln **MANDATORY**: werden durch CI/Linter durchgesetzt.

  Cluster-Katalog nach Informationsfluss:
  1. Informationsinput (Erzeugung)
  2. Informationsverteilung (Zugänglichkeit)
  3. Informationsverarbeitung (Verstehen/Bewerten)
  4. Informationsspeicherung (Persistenz)
  5. Informationsnutzung (Entscheidung/Handlung)
  6. Rahmenbedingungen (Kontext & Moderatoren)
  7. Ergebnisgrößen (Outcomes)

## Ergänzung: Zuordnung für Einflussfaktoren zu MTO und St. Galler Management Model (TAGS)

- **STATUS**: Jeder Einflussfaktor im 'wirkmechanismen-main-model-blueprint.json' hat nun eine Kategorie "cluster" und eine Kategorie "tags".
- **MANDATORY**: Jedem neuen Einflussfaktor muss mindestens ein MTO-Tag und ein St. Galler Management-Model-Tag zugeordnet sein.

TAGS-Katalog: 
Aufteilung MTO:
1. M = Mensch, 
2. T = Technik, 
3. O = Organisation.

Aufteilung St. Galler Management Model:
1. operativ = operative Ebene (z.B. Entwicklerteam),
2. taktisch = taktische Ebene (z.B. Scrum Master (SM), Product Owner (PO), Teamleiter (TL)),
3. strategisch = strategische Ebene (z.B. Abteilungsleiter),
4. normativ = normative Ebene (z.B. Management)

- **MANDATORY**: Die TAGS-Zuordnung muss über die in KUMU vorhandenen TAGS geführt werden und gegen den aktiven TAGS-Katalog validierbar sein.
Beim Anlegen eines neuen Elements ohne TAGS-Zuordnung soll folgender Hinweis angezeigt werden:

  "Hinweis: Neuen Einflussfaktoren müssen MTO- und St. Galler TAGS zugeordnet werden. Ohne diese Werte ist der Vorschlag nicht mergefähig."
- **REJECT**: Neue Einflussfaktoren ohne gültige TAGS-Zuordnung werden nicht aufgenommen.

- Die Regeln **MANDATORY**: werden durch CI/Linter durchgesetzt.