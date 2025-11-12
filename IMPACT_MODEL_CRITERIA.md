# Impact Model Generation Criteria

## Overview

This document defines specific criteria for generating Impact Models in the Wirkmechanismen project. Impact Models build on validated Reference Models and model the desired future state after introducing support interventions.

## Core Principles

### Relationship to Reference Model
- **MANDATORY**: Each Impact Model MUST be derived from a validated Reference Model
- **MANDATORY**: Impact Model MUST use the same domain scope
- **MANDATORY**: Problem and Success Factor remain identical
- **TRANSFORMATION**: Support elements (interventions) are added
- **TRANSFORMATION**: New or modified causal relationships are explicitly marked

## Structural Requirements

### 1. Element Taxonomy (MANDATORY)

#### 1.1 Support Elements (Interventions)
- **MANDATORY**: At least ONE (1) Support element per Impact Model
- **DEFINITION**: Concrete measures, tools, or interventions to improve Key Factors
- **CLASSIFICATION**: `"element type": "Support"`
- **RECOMMENDATION**: 1-3 Support elements for focused interventions
- **REJECT**: Impact Models without Support elements

**Support Formulation**:
- **CORRECT**: `"Daily Moderation Guide"`, `"Visual Board"`, `"Timeboxing Timer"`
- **CORRECT**: Concrete tools, processes, or aids
- **WRONG**: Abstract goals or desired states

#### 1.2 Key Factor Preservation
- **MANDATORY**: All Key Factors from Reference Model MUST be adopted
- **CLASSIFICATION**: `"element type": "Schlüsselfaktor"` (Key Factor)
- **ROLE**: Primary intervention targets - influenced by Supports

#### 1.3 Success Factor Structure
- **MANDATORY**: Success Factor from Reference Model MUST be adopted
- **CLASSIFICATION**: `"element type": "Erfolgsfaktor"` (Success Factor) or `"Messbarer Erfolgsfaktor"` (Measurable Success Factor)
- **IMMUTABLE**: Success Factor definition remains identical to Reference Model

#### 1.4 Influencing Factors Adaptation
- **MANDATORY**: Influencing Factors from Reference Model are adopted
- **ALLOWED**: New Influencing Factors created by Supports
- **CLASSIFICATION**: `"element type": "Einflussfaktoren"` (Influencing Factors)
- **MANDATORY**: New Influencing Factors MUST be documented as assumptions `[A]`

### 2. Causal Network Structure (MANDATORY)

#### 2.1 Support-to-Key Factor Relationships
- **MANDATORY**: Each Support MUST influence at least one Key Factor
- **STRUCTURE**: `Support → Key Factor → [Influencing Factors] → Success Factor`
- **MANDATORY**: Support elements are **start nodes** (no incoming connections)
- **REJECT**: Supports without outgoing connections to Key Factors

#### 2.2 Modified Causal Relationships
- **MANDATORY**: Relationships changed by Supports MUST be documented
- **MECHANISM**:
  - **Option A**: Remove old connection, add new connection with `[A]`
  - **Option B**: Change connection strength/polarity and explain in `description`
- **MANDATORY**: Changes MUST be explained in connection `description`

#### 2.3 New Causal Relationships
- **ALLOWED**: Supports can create new causal relationships
- **MANDATORY**: All new connections MUST be marked with `[A]` (Assumption)
- **MANDATORY**: `description` MUST contain theoretical or empirical justification
- **RECOMMENDATION**: Validate assumptions through pilot projects or literature

#### 2.4 Path Requirements
- **MANDATORY**: At least one complete path from Support → Success Factor
- **MANDATORY**: Maximum path length: 5 connections (Support + 4 intermediate steps)
- **LOGIC CHECK**: All Supports MUST be causally connected to Success Factor

### 3. Source Attribution (MANDATORY)

#### 3.1 Literature and Evidence (from Reference Model)
- **INHERITED**: Literature sources `[1]`, `[2]`, etc. from Reference Model remain unchanged
- **MANDATORY**: Source attribution for unchanged connections remains identical

#### 3.2 Assumptions for Interventions (Priority for new connections)
- **MANDATORY**: All new connections (through Supports) MUST be marked as `[A]` (Assumption)
- **MANDATORY**: `description` MUST contain justification of assumption:
  - Theoretical foundation (design principles, methodology)
  - Empirical evidence (pilot projects, expert opinions)
  - Analogies to similar interventions
- **GOAL**: Transform assumptions into evidence through incremental validation

#### 3.3 Validated Interventions (after piloting)
- **ALLOWED**: After successful piloting, replace `[A]` with `[O]` (own investigation)
- **ALLOWED**: With literature evidence, replace `[A]` with `[1-9]+`
- **MANDATORY**: Document validation process in commit message

#### 3.4 Inadmissible Sources
- **REJECT**: Connections with `[?]` (unknown source)
- **REJECT**: New connections without source attribution (even if assumption)

### 4. Measurability and Influenceability Criteria

#### 4.1 Support Properties
- **EXPECTATION**: Supports have high influenceability (≥ 0.9)
- **RATIONALE**: Interventions are under direct team control
- **EXPECTATION**: Supports have low inherent measurability (0.3-0.6)
- **DOCUMENTATION**: Support implementation degree MUST be measurable (e.g., "Board present: yes/no", "Guide usage rate")

#### 4.2 Key Factor Changes
- **HYPOTHESIS**: Supports improve Key Factors
- **MANDATORY**: Expected improvement MUST be described in Support connection
- **MEASURABILITY**: Key Factor measurability remains identical (from Reference Model)
- **INFLUENCEABILITY**: Can increase if Support creates direct control option

#### 4.3 Success Factor Invariance
- **MANDATORY**: Success Factor measurability and influenceability remain unchanged
- **RATIONALE**: Long-term goals don't change through short-term interventions

### 5. Connection Semantics

#### 5.1 Direction and Polarity
- **MANDATORY**: All connections MUST be directed (`"direction": "directed"`)
- **MANDATORY**: Connection type MUST use DRM polarities (`++`, `+-`, `-+`, `--`)
- **EXPECTATION**: Support → Key Factor connections are typically positive (`++`)

#### 5.2 Connection Descriptions for Supports
- **MANDATORY**: Support connections MUST explain causal mechanism
- **FORMAT**: "Support X improves Factor Y through Mechanism Z"
- **LENGTH**: 30-200 words for new assumption-based connections
- **CONTENT**:
  - How does the support work?
  - Why should it improve the factor?
  - What assumptions underlie this?

## Validation Steps

### Automatic Validation
1. JSON schema compliance (`lint_blueprint.py`)
2. Element/connection ID uniqueness
3. Reference integrity (from/to reference existing IDs)
4. Factor taxonomy compliance (including Support elements)
5. **Support Validation**: At least one Support present
6. **Topology Validation**: Supports as start nodes, Success Factor as end node

### Content Validation
1. **Reference Model Consistency**: Problem/Success Factor identical to Reference Model
2. **Support Integration**: All Supports connected to Key Factors
3. **Path Completeness**: At least one path Support → Success Factor
4. **Assumption Documentation**: All `[A]` connections have meaningful descriptions
5. **Validation Plan**: Each assumption has planned validation mechanism

### Quality Metrics
- **Support Coverage**: 100% - All Key Factors addressed by at least one Support
- **Assumption Documentation**: 100% - All `[A]` connections have justification
- **Topological Integrity**: 100% - Supports (start) → Success Factor (end) structure
- **Path Completeness**: 100% - At least one complete path present
- **Validation Planning**: ≥75% of assumptions have documented validation plan

## Compliance Checklist

### Pre-Submission
- [ ] Based on validated Reference Model (identical domain scope)
- [ ] Problem and Success Factor adopted from Reference Model
- [ ] At least 1 Support element present
- [ ] All Supports connected to Key Factors
- [ ] Direct causal chain Support → Success Factor present
- [ ] All new connections marked with `[A]`
- [ ] All `[A]` connections have justification in `description`
- [ ] Supports defined as start nodes (no incoming connections)
- [ ] Measurability/influenceability values consistent
- [ ] JSON validation successful

### Review Criteria
- [ ] Support interventions are concrete and implementable
- [ ] Causal mechanisms scientifically/practically plausible
- [ ] Assumption justifications comprehensible
- [ ] Validation plans present for assumptions
- [ ] No contradictory causal relationships to Reference Model
- [ ] Model complexity appropriate (not too many Supports)

### Validation Planning
- [ ] For each `[A]` connection: validation method defined
- [ ] Pilot timeline created
- [ ] Success criteria for intervention defined
- [ ] Data collection mechanisms specified

## Rejection Criteria

- **AUTOMATIC REJECT**: No Support element present
- **AUTOMATIC REJECT**: Supports not connected to Key Factors
- **AUTOMATIC REJECT**: Broken causal chain Support → Success Factor
- **AUTOMATIC REJECT**: New connections without `[A]` marking
- **AUTOMATIC REJECT**: `[A]` connections without justification in `description`
- **AUTOMATIC REJECT**: JSON schema violations
- **AUTOMATIC REJECT**: Success Factor changed compared to Reference Model

## Incremental Validation and Integration

### Validation Workflow
1. **Impact Model Scaffolding**: Initial model with `[A]` assumptions
2. **Human + Peer Review**: Plausibility check
3. **Piloting**: Small test group, collect qualitative evidence
4. **Iteration**: `[A]` → `[O]` for validated assumptions
5. **Scaling**: Quantitative validation, possibly `[O]` → `[1-9]+` if published
6. **Integration**: Integrate validated Support relationships into Main Model

### Commit-based Tracking
- **INITIAL**: `[IMPACT] Add {domain} impact model with {N} support interventions`
- **VALIDATION**: `[IMPACT] Validate assumption [A] → [O] for {connection} based on {pilot/study}`
- **ITERATION**: `[IMPACT] Refine support {name} based on pilot results`
- **FINALIZATION**: `[IMPACT] Promote validated {domain} model to production`

## Summary

Impact Models are future-state models that build on validated Reference Models. They:
1. Introduce **Support elements** (concrete interventions)
2. Document **new causal relationships** as **assumptions** `[A]`
3. Retain **Problem and Success Factor** from Reference Model
4. Follow an **incremental validation cycle**
5. Feed validated findings back into the **Main Model**

Impact Models are experimental in nature and enable systematic testing of design interventions with clear evidence basis.
