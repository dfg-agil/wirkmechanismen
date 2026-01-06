# Reference Model Generation Criteria

## Overview

This document defines specific criteria for generating Reference Models in the Wirkmechanismen project. Reference Models complement the general gatekeeping criteria with concrete structural requirements for consistent and focused models.

## Structural Requirements

### 1. Element Taxonomy (MANDATORY)

#### 1.1 Key Factor Constraint
- **MANDATORY**: Exactly ONE (1) Key Factor per Reference Model
- **DEFINITION**: The central factor representing the main problem and serving as primary intervention target
- **CLASSIFICATION**: `"element type": "Schlüsselfaktor"` (Key Factor)
- **REJECT**: Models with zero or multiple Key Factors

#### 1.2 Success Factor Structure
- **MANDATORY**: Exactly ONE (1) Success Factor per Reference Model
- **DEFINITION**: Long-term, overarching goal (e.g., product quality, customer satisfaction)
- **CLASSIFICATION**: `"element type": "Erfolgsfaktor"` (Success Factor)
- **MANDATORY**: If Success Factor is not directly measurable (measurability < 0.8), MUST add a Measurable Success Factor as proxy
- **CLASSIFICATION Proxy**: `"element type": "Messbarer Erfolgsfaktor"` (Measurable Success Factor)
- **REJECT**: Models without Success Factor or with multiple Success Factors

#### 1.3 Influencing Factors Classification
- **MANDATORY**: All other factors MUST be classified as Influencing Factors
- **CLASSIFICATION**: `"element type": "Einflussfaktoren"` (Influencing Factors)
- **RECOMMENDATION**: 3-7 Influencing Factors for balanced model complexity
- **REVIEW REQUIRED**: Models with >10 Influencing Factors (complexity check)

### 2. Causal Chain Structure (MANDATORY)

#### 2.1 Causal Network Topology
- **MANDATORY**: Key Factor is the **only start node** (no incoming connections)
- **MANDATORY**: Success Factor is the **only end node** (no outgoing connections)
- **MANDATORY**: All Influencing Factors MUST be causally positioned between Key Factor and Success Factor
- **STRUCTURE**: `Key Factor → [Influencing Factors] → [Measurable Success Factor] → Success Factor`

#### 2.2 Path Requirements
- **MANDATORY**: At least one direct path from Key Factor to Success Factor
- **MANDATORY**: Maximum path length: 4 connections between Key Factor and Success Factor
- **MANDATORY**: All Influencing Factors MUST lie on or influence this main path
- **REJECT**: Influencing Factors without connection to main path
- **REJECT**: Influencing Factors with incoming connections from outside the model

### 3. Source Attribution (MANDATORY)

#### 3.1 Literature-Based Connections (Priority 1)
- **TARGET**: >50% of all connections with literature sources `[1]`, `[2]`, etc.
- **MANDATORY**: Literature sources MUST be documented in `connection.description`
- **FORMAT**: Complete academic citation (APA style)
- **REJECT**: Literature references without corresponding documentation

#### 3.2 Empirical Evidence (Priority 2)
- **ALLOWED**: Stakeholder experience `[E]`, assumption `[A]`, or own investigations `[O]`
- **MANDATORY**: Description of evidence basis in `connection.description`
- **LIMIT**: Max. 50% of connections without literature foundation

#### 3.3 Inadmissible Sources
- **REJECT**: Connections with `[?]` (unknown source)
- **REJECT**: Connections without source attribution

### 4. Measurability and Influenceability Criteria

#### 4.1 Measurability
- **MANDATORY**: Key Factor MUST be measurable (measurability ≥ 0.6)
- **MANDATORY**: Measurable Success Factor MUST be highly measurable (measurability ≥ 0.8)
- **MANDATORY**: Success Factor can have lower measurability (measurability ≥ 0.3)
- **DOCUMENTATION**: Measurement methods MUST be specified in `description`

#### 4.2 Influenceability
- **MANDATORY**: Key Factor MUST be influenceable (influenceability ≥ 0.7)
- **EXPECTATION**: Success Factors typically have low influenceability (≤ 0.3)
- **LOGIC CHECK**: Influenceability MUST be consistent with factor role

### 5. Connection Semantics

#### 5.1 Direction and Polarity
- **MANDATORY**: All connections MUST be directed (`"direction": "directed"`)
- **MANDATORY**: Connection type MUST use DRM polarities (`++`, `+-`, `-+`, `--`)
- **RECOMMENDATION**: Positive main chain from Key Factor to Success Factor

#### 5.2 Connection Descriptions
- **MANDATORY**: Each connection MUST explain causal mechanism in `description`
- **FORMAT**: "Factor X leads to Factor Y through Mechanism Z"
- **LENGTH**: 20-150 words per description

## Validation Steps

### Automatic Validation
1. JSON schema compliance (`lint_blueprint.py`)
2. Element/connection ID uniqueness
3. Reference integrity (from/to reference existing IDs)
4. Factor taxonomy compliance
5. **Topology Validation**: Key Factor as start node, Success Factor as end node

### Content Validation
1. **Network Topology**: Key Factor without incoming, Success Factor without outgoing connections
2. **Path Completeness**: At least one path Key Factor → Success Factor
3. **Influencing Factors Integration**: All Influencing Factors between start and end nodes
4. Calculate source attribution ratio
5. Validate measurability/influenceability consistency
6. Check factor formulation according to DRM principles

### Quality Metrics
- **Evidence Coverage**: ≥75% literature sources `[1-9]+`
- **Topological Integrity**: 100% - Key Factor (start) → Success Factor (end) structure
- **Path Completeness**: 100% - At least one complete path present
- **Factor Integration**: 100% - All Influencing Factors integrated on main path
- **Factor Precision**: 100% - All factors follow "attribute-of-element" formulation
- **Measurability Consistency**: Measurable Success Factors ≥0.8, Key Factors ≥0.6

## Compliance Checklist

### Pre-Submission
- [ ] Exactly 1 Key Factor present
- [ ] Exactly 1 Success Factor present
- [ ] Measurable Success Factor added if low-measurable Success Factor
- [ ] All other factors classified as "Influencing Factors"
- [ ] Direct causal chain Key Factor → Success Factor present
- [ ] >50% connections with literature sources
- [ ] All literature sources documented
- [ ] No `[?]` sources in Reference Model
- [ ] Measurability/influenceability values consistent
- [ ] JSON validation successful

### Review Criteria
- [ ] Causal chain scientifically plausible
- [ ] Factor formulations precise and unambiguous
- [ ] Literature sources relevant and current
- [ ] Model complexity appropriate (3-10 factors total)
- [ ] Connection descriptions meaningful

## Rejection Criteria

- **AUTOMATIC REJECT**: More or less than 1 Key Factor
- **AUTOMATIC REJECT**: More or less than 1 Success Factor
- **AUTOMATIC REJECT**: Broken causal chain Key Factor → Success Factor
- **AUTOMATIC REJECT**: <50% literature sources
- **AUTOMATIC REJECT**: Unknown sources `[?]`
- **AUTOMATIC REJECT**: JSON schema violations
- **AUTOMATIC REJECT**: Factors without "attribute-of-element" formulation

## Summary

Reference Models represent the current state for specific problems. They:
1. Have exactly **one Key Factor** (start node) and **one Success Factor** (end node)
2. Use **Influencing Factors** to model the causal chain between them
3. Are grounded in **literature evidence** (>50% coverage)
4. Follow **DRM attribute-of-element** formulation
5. Serve as the foundation for creating **Impact Models**

Reference Models establish the baseline understanding necessary for designing and evaluating interventions.
