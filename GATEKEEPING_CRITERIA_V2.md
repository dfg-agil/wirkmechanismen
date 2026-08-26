# Gatekeeping Criteria for Wirkmechanismen Model Changes (V2)

## Overview

This document establishes mandatory criteria for accepting or rejecting changes to the Wirkmechanismen factor network models. These criteria ensure model integrity, methodological consistency, and scientific rigor while maintaining compatibility with KUMU visualization and DRM methodology principles.

V2 keeps the proven V1 structure and quality gates, and adds explicit Main Model governance rules for controlled growth.

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
  - `[?]` - Unknown source (temporary, requires investigation)
- **REJECT**: Any connection without source attribution
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
- **MANDATORY**: For causal RM/IM/Main links, `"directed"` is the default expectation unless bidirectionality is explicitly justified.
- **MANDATORY**: `connection type` MUST use DRM sign pairs: `["++", "+-", "-+", "--"]` or single `"+"` for overall positive
- **MANDATORY**: Directional consistency - prefer `"directed"` over `"mutual"` unless truly bidirectional
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

### 4. Model Evolution Governance

#### 4.1 Reference vs Impact Model Integrity
- **MANDATORY**: Reference Models represent existing/current state only
- **MANDATORY**: Impact Models MUST clearly identify which Reference Model relationships no longer hold
- **MANDATORY**: Impact Models MUST include `"Support"` elements for interventions
- **MANDATORY**: New relationships in Impact Models MUST be marked as assumptions `[A]` unless evidenced
- **REJECT**: Support interventions in Reference Models
- **REJECT**: Impact Models without clear intervention elements

#### 4.2 Quantitative Attribute Consistency
- **MANDATORY**: `measurability` and `influenceability` scores (if present) MUST be in range [0, 1]. Valid values are [0, 0.5, 1.0].
- **MANDATORY**: Main Model intake for new influencing factors requires both values explicitly provided.
- **MANDATORY**: Quantitative attributes MUST have documented methodology/source
- **REVIEW REQUIRED**: Significant changes to existing quantitative scores require justification
- **REJECT**: Arbitrary or unsupported quantitative values
- **REJECT**: New influencing factor in Main Model without both `measurability` and `influenceability`

#### 4.3 Main Model Growth Governance (new in V2)
- **MANDATORY**: New factors MUST be checked for semantic overlap with existing factors before insertion (MECE = mutually exclusive and collectively exhaustive).
- **MANDATORY**: If overlap exists, split/merge decision and rationale MUST be documented.
- **MANDATORY**: New factors SHOULD improve practical MECE quality (as far as realistically possible).
- **REVIEW REQUIRED**: Strong overlap with existing factors without clear differentiation.
- **REJECT**: Duplicate factor without explicit consolidation decision.

### 5. Documentation and Traceability

#### 5.1 Change Documentation Requirements
- **MANDATORY**: All model changes MUST include clear rationale
- **MANDATORY**: Source materials/references MUST be provided for new factors or connections
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
- **Evidence Coverage**: >90% of connections with documented sources (not `[?]`)
- **Assumption Ratio**: <30% of Impact Model connections marked as `[A]`
- **Factor Precision**: 100% compliance with attribute-of-element formulation
- **Network Connectivity**: <5% orphaned elements
- **Reference Integrity**: 100% valid element/connection references

### Rejection Thresholds
- Any JSON schema violation -> **AUTOMATIC REJECT**
- >10% factors with invalid formulation -> **REJECT**
- >25% connections without source attribution -> **REJECT**
- >50% assumptions without documentation -> **REJECT**
- Any circular references in element/connection IDs -> **REJECT**
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

## Ergänzung (perspektivisch): Cluster-Pflicht für Einflussfaktoren

- **STATUS**: Diese Regel wird aktiv, sobald ein versionierter Cluster-Katalog eingeführt ist (z. B. als dedizierte Datei mit zulässigen Cluster-IDs und Definitionen).
- **MANDATORY (ab Aktivierung)**: Jeder neue Einflussfaktor muss genau einem definierten Cluster zugeordnet sein.
- **MANDATORY (ab Aktivierung)**: Die Cluster-Zuordnung muss als eindeutiges Attribut geführt werden (z. B. `attributes.cluster_id`) und gegen den aktiven Cluster-Katalog validierbar sein.
- **REJECT (ab Aktivierung)**: Neue Einflussfaktoren ohne gültige Cluster-Zuordnung werden nicht aufgenommen.
- **REJECT (ab Aktivierung)**: Mehrfachzuordnungen ohne explizit freigegebenes Multi-Cluster-Konzept werden nicht aufgenommen.

- **Übergangsregel bis Aktivierung**:
  - Solange kein Cluster-Katalog versioniert vorliegt, ist die Cluster-Zuordnung optional und darf den Merge nicht blockieren.
  - Nach Einführung des Katalogs wird die Regel auf "MANDATORY" gesetzt und durch CI/Linter durchgesetzt.

  Clusterung nach Informationsfluss:
  1. Informationsinput (Erzeugung)
  2. Informationsverteilung (Zugänglichkeit)
  3. Informationsverarbeitung (Verstehen/Bewerten)
  4. Informationsspeicherung (Persistenz)
  5. Informationsnutzung (Entscheidung/Handlung)
  6. Rahmenbedingungen (Kontext & Moderatoren)
  7. Ergebnisgrößen (Outcomes)

## Ergänzung (perspektivisch): Zuordnung für Einflussfaktoren zu MTO und St. Galler Management Model (TAGS)

- **STATUS**: Diese Regel wird aktiv, sobald ein versionierter TAGS-Katalog eingeführt ist (z. B. als dedizierte Datei mit zulässigen TAGS-IDs und Definitionen).
- **MANDATORY (ab Aktivierung)**: Jedem neuen Einflussfaktor muss mindestens ein MTO-Tag und ein St. Galler Management-Model-Tag zugeordnet sein.

Aufteilung MTO:
1. M = Mensch, 
2. T = Technik, 
3. O = Organisation.

Aufteilung St. Galler Management Model:
1. operativ = operative Ebene (z.B. Entwicklerteam),
2. taktisch = taktische Ebene (z.B. Scrum Master (SM), Product Owner (PO), Teamleiter (TL)),
3. strategisch = strategische Ebene (z.B. Abteilungsleiter),
4. normativ = normative Ebene (z.B. Management)

- **MANDATORY (ab Aktivierung)**: Die TAGS-Zuordnung muss über die in KUMU vorhandenen TAGS geführt werden und gegen den aktiven TAGS-Katalog validierbar sein.
Beim Anlegen eines neuen Elements ohne TAGS-Zuordnung soll folgender Hinweis angezeigt werden:

  "Hinweis: Neuen Einflussfaktoren müssen MTO- und St. Galler TAGS zugeordnet werden. Ohne diese Werte ist der Vorschlag nicht mergefähig."
- **REJECT (ab Aktivierung)**: Neue Einflussfaktoren ohne gültige TAGS-Zuordnung werden nicht aufgenommen.

- **Übergangsregel bis Aktivierung**:
  - Solange kein TAGS-Katalog versioniert vorliegt, ist die TAGS-Zuordnung optional und darf den Merge nicht blockieren.
  - Nach Einführung des Katalogs wird die Regel auf "MANDATORY" gesetzt und durch CI/Linter durchgesetzt.