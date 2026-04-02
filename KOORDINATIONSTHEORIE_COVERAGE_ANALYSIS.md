# Abdeckungsanalyse: Koordinationstheorie im Main Model

**Quellen:**
- Okhuysen, G. A., & Bechky, B. A. (2009). Coordination in organizations: An integrative perspective. Academy of Management Annals, 3(1), 463-502.
- Dingsøyr, T., Moe, N. B., & Seim, E. A. (2018). Coordinating knowledge work in multiteam programs: Findings from a large-scale agile development program. Project Management Journal, 49(6), 64-77.

---

## Executive Summary

**Gesamtabdeckung: ~75%**

Das Wirkmechanismen-Main-Model bildet die drei Core Coordination Mechanisms nach Okhuysen & Bechky (2009) **substanziell, aber nicht vollständig** ab. Die **Common Understanding**-Dimension ist am stärksten repräsentiert (~85%), **Predictability** ist gut abgedeckt (~75%), während **Accountability** zwar vorhanden, aber weniger tiefgehend modelliert ist (~60%). Die Multi-Team Koordination nach Dingsøyr et al. (2018) ist **strukturell angelegt, aber unterrepräsentiert** (~45%).

---

## 1. Common Understanding (Gemeinsames Verständnis)

### Abdeckung: ~85% ✅

**Kernfaktor im Model:**
- **`elem-gemeinsamVerstaendnis`** - "Gemeinsames Verständnis des Teams" (Erfolgsfaktor)
  - ✅ **EXPLIZITE Referenz** auf Okhuysen & Bechky (2009)
  - Tag: "O&B Framework"
  - Description: "Zentrale Erfolgsdimension gemäß Okhuysen & Bechky (2009) Common Understanding"
  - Connections: 5 (3 in, 2 out)
  - measurability: 0.5, influenceability: 0.5

**Unterstützende Faktoren:**

| Element ID | Label | Element Type | Coverage |
|------------|-------|--------------|----------|
| `elem-mentalModelle` | Qualität gemeinsamer mentaler Modelle | Einflussfaktoren | ✅ Vollständig |
| `elem-VombH8FP` | Konvergenz des Teamverständnisses | Einflussfaktoren | ✅ Vollständig |
| `elem-ivDOaa1S` | Zielkongruenz des Teams | Einflussfaktoren | ✅ Vollständig |
| `elem-QkWKoQ14` | Gemeinsames Verständnis von Erfolgskriterien | Einflussfaktoren | ✅ Vollständig |
| `elem-externalisierungAnnahmen` | Externalisierung impliziter Annahmen | Einflussfaktoren | ✅ Vollständig |
| `elem-gdWissAust01` | Grad des Wissensaustauschs | Einflussfaktoren | ✅ Vollständig |

**Mechanismen zur Herstellung von Common Understanding:**
- Synchronisationsfrequenz (elem-synchronisationsfrequenz)
- Kommunikationsmedien-Passung (elem-mediPassung)
- Team-Partizipation (elem-1oLVNA94)
- Qualität der Retrospektiven (elem-retrospektive001)
- Qualität der Reviews (elem-reviewQualitaet)
- Refinement-Prozessqualität (refinement-related factors)
- Planning-Qualität (planning-related factors)

**Wirkzusammenhänge dokumentiert:**
```
Connection: conn-COMMON-UNDERSTANDING-TO-COORDINATION
From: elem-gemeinsamVerstaendnis → To: elem-koordin001
Type: ++ (Higher common understanding improves coordination)
Description: "Gemeinsames Verständnis verbessert den Grad der Koordination durch 
bessere implizite Koordination, konsistente Erwartungen und reduzierte Koordinationskosten."
```

**Was fehlt (15%):**
- ❌ **Shared Temporal Structures**: Zeitliche Dimension des gemeinsamen Verständnisses (Timing-Awareness, Rhythmen)
- ⚠️ **Narrative Coordination**: Geteilte Stories/Narrative als Koordinationsmechanismus (nur implicit in Retros)
- ⚠️ **Epistemische Diversität**: Wie Teams mit unterschiedlichen Wissensdomänen gemeinsame Verständnisgrundlagen schaffen

---

## 2. Predictability (Vorhersagbarkeit)

### Abdeckung: ~75% ✅

**Kernfaktoren im Model:**

| Element | Label | Coverage | Notes |
|---------|-------|----------|-------|
| `elem-absichtKoordinationsmechanismus` | Bewusstsein für gezielte Absicht eines Koordinationsmechanismus | ✅ | Explicates **why** rituals exist |
| Scrum-Events | Retrospektive, Review, Planning, Daily, Refinement | ✅ | Predictable routines |
| `elem-JmXiROgv` | Verständlichkeit des Entwicklungsprozesses | ✅ | Process clarity |
| `elem-0er3OquT` | Expliziter Wissensstand der Organisation | ✅ | Standards, docs |
| `elem-synchronisationsfrequenz` | Synchronisationsfrequenz | ✅ | Cadence/Rhythm |

**Predictability-Mechanismen im Model:**

### **2.1 Routinen & Rituale (✅ gut abgedeckt)**
- **Scrum Events als Routinen**: Daily, Planning, Review, Retrospektive, Refinement
  - ✅ Alle Events als Faktoren vorhanden
  - ✅ Quality-Dimensionen für jeden Event modelliert
  - ✅ Strukturierungsklarheit des Meetings (elem-struktuKlarheit)

### **2.2 Prozessklarheit (✅ gut abgedeckt)**
- Verständlichkeit des Entwicklungsprozesses (elem-JmXiROgv)
- Prozess-Ambiguität (elem-1mAqDgJB) - inverse Predictability
- Definition of Ready/Done (part of refinement quality)

```
Connection: conn-PROCESS-CLARITY-TO-COORDINATION
From: elem-JmXiROgv → To: elem-koordin001
Type: +- (Higher process clarity reduces coordination effort)
Description: "Höhere Verständlichkeit des Entwicklungsprozesses reduziert den 
Koordinationsaufwand durch klarere Abläufe und Rollen."
```

### **2.3 Standards & Dokumentation (✅ gut abgedeckt)**
- Expliziter Wissensstand (elem-0er3OquT)
- Kontrakt-Präzision (implizit in DoR/DoD)
- Architektur-Dokumentation (implizit in Tech Stack)

### **2.4 Zeitliche Vorhersagbarkeit (⚠️ teilweise)**
- ✅ Synchronisationsfrequenz vorhanden
- ✅ Zeitliche Überlappung der Arbeitszeiten (elem-zeitlUeberlappung)
- ⚠️ Sprint/Iteration Rhythms (implicit, aber nicht explizit als Faktor)
- ❌ **Service Level Expectations (SLE)** fehlen (Kanban)
- ❌ **Flow Metrics für Vorhersagbarkeit** fehlen (Cycle Time Variabilität)

**Was fehlt (25%):**
- ❌ **Formale Commitment-Mechanismen**: Wie Teams verbindliche Zusagen geben und einhalten
- ❌ **Temporal Synchrony**: Explizite Modellierung von Timing-Koordination (wann welche Aufgabe fertig sein muss)
- ❌ **Workflow Policies**: WIP-Limits, Pull-Policies als Predictability-Mechanismen (nur teilweise in Kanban-Faktoren)
- ⚠️ **Escalation Pathways**: Was passiert, wenn Predictability bricht? (nur in "Hindernisse" aggregiert)

---

## 3. Accountability (Verantwortlichkeit)

### Abdeckung: ~60% ⚠️

**Kernfaktoren im Model:**

| Element | Label | Coverage | Limitation |
|---------|-------|----------|------------|
| `elem-6tHZ4FNz` | Klarheit der Verantwortlichkeiten im Team | ✅ | Generic role clarity |
| `elem-klarZustaend` | Klarheit über die Zuständigkeiten der Teammitglieder | ✅ | Similar to above |
| (missing) | **Explizite Ownership-Mechanismen** | ❌ | Keine Faktoren für Code Ownership, Feature Ownership |
| (missing) | **Rechenschaftspflicht** | ❌ | Keine Faktoren für Review-Accountability, Decision-Accountability |

**Was vorhanden ist:**
- ✅ **Role Clarity**: Klarheit der Verantwortlichkeiten (elem-6tHZ4FNz)
  - Description: "Klare Rollenverteilung"
  - 11 connections (5 in, 6 out)
- ✅ **Zuständigkeiten**: Klarheit über die Zuständigkeiten (elem-klarZustaend)
- ✅ **Transparenz der Fähigkeiten**: Transparenz der Fähigkeiten der Teammitglieder (helps with task allocation)

**Was schwach/fehlend ist:**

### **3.1 Ownership-Dimensionen (❌ fehlen weitgehend)**
- ❌ **Code/Component Ownership**: Wer ist verantwortlich für welchen Codebereich?
- ❌ **Feature Ownership**: Wer trägt die Verantwortung für End-to-End-Delivery?
- ❌ **Decision Ownership**: Wer darf welche Entscheidungen treffen (Decision Rights)?

### **3.2 Rechenschaftspflicht-Mechanismen (❌ fehlen)**
- ❌ **Consequence Structures**: Was passiert bei Nicht-Erfüllung von Commitments?
- ❌ **Accountability in Reviews**: Review als Accountability-Mechanismus nicht thematisiert
- ❌ **Retrospectve Accountability**: Follow-up auf Action Items aus Retros

### **3.3 Verfolgbarkeit (⚠️ teilweise)**
- ⚠️ **Traceability**: Implizit in "Transparenz" vorhanden, aber nicht als Accountability-Mechanismus explizit
- ✅ **Sprint Goal Commitment**: Implizit in Planning-Qualität, aber nicht explizit als Accountability-Faktor

**Connection-Beispiel:**
```
Klarheit der Verantwortlichkeiten → Koordinationsaufwand
BUT: Connection wirkt NUR über Klarheit, nicht über Enforcement/Consequences
```

**Was fehlt (40%):**
- ❌ **Authority Structures**: Wer hat Entscheidungsmacht in welchen Domänen?
- ❌ **Contract-Based Coordination**: Team-Contracts, API-Contracts als Accountability-Layer
- ❌ **Peer Review Accountability**: Code Review nicht als gegenseitige Rechenschaftspflicht modelliert
- ❌ **Sprint Commitment Tracking**: Wie Teams für ihre Sprint-Commitments zur Verantwortung gezogen werden
- ❌ **Cross-Team Dependencies Ownership**: Bei Abhängigkeiten – wer ist accountable für Blockade-Lösung?

---

## 4. Dingsøyr et al. (2018): Multi-Team Coordination in Scaled Agile

### Abdeckung: ~45% ⚠️

**Was vorhanden ist:**

### **4.1 Large-Scale Agile (⚠️ strukturell vorhanden, wenig ausgearbeitet)**
- ✅ `elem-bOQiQpQ5` - "Skalierbarkeit agiler Praktiken"
  - Description: "Das Arbeiten auf verschiedenen Programmebenen, bei der Praktiken in großen und komplexen Projekten über mehrere Teams hinweg skaliert werden"
  - BUT: 0 connections → **isoliertes Konzept ohne Wirkmechanismen**

### **4.2 Boundary Spanning (✅ gut abgedeckt)**
- ✅ `elem-boundarySpannerNeed` - "Notwendigkeit eines Boundary Spanners"
  - Well-connected: Driven by Systemkomplexität, Abhängigkeiten, Kommunikationskomplexität
  - Affects: Koordinationsaufwand, Boundary Objects, Team Understanding

```
Connection: conn-BOUNDARY-SPANNER-NEED-TO-COORDINATION
From: elem-boundarySpannerNeed → To: elem-koordin001
Type: ++ (More boundary spanning → more coordination effort)
```

### **4.3 Inter-Team Coordination (❌ weitgehend fehlend)**
- ❌ **Inter-Team Meetings/Rituale**: SoS (Scrum of Scrums), MetaScrum fehlen
- ❌ **Cross-Team Dependencies**: Abhängigkeiten werden aggregiert modelliert (`elem-7sSep5II`), aber nicht als **inter-team phenomenon**
- ⚠️ **Communities of Practice**: Implizit in Wissensaustausch, aber nicht explizit

### **4.4 Knowledge Coordination in Multi-Team Programs (⚠️ teilweise)**

**Aus Dingsøyr et al. (2018) - was vorhanden:**
- ✅ **Knowledge Sharing**: elem-gdWissAust01
- ✅ **Boundary Objects**: Elem-boundaryObject (implizit erwähnt in Connections)
- ⚠️ **Architecture as Coordination Mechanism**: Implizit in Systemkomplexität, aber nicht explizit

**Was fehlt:**
- ❌ **Program-Level Coordination Roles**: Program Manager, Release Train Engineer (SAFe)
- ❌ **Cross-Team Backlogs**: Portfolio-Backlog, Program-Backlog
- ❌ **Synchronization Events**: PI Planning (SAFe), Big Room Planning
- ❌ **Integration Challenges**: Continuous Integration in Multi-Team Settings

---

## 5. Weitere Koordinationstheorie-Konzepte

### **5.1 Task Interdependencies (Thompson, 1967) ✅**
- ✅ `elem-wtELkHfE` - "Abhängigkeitstyp der Aufgabenbeziehungen"
  - Description: "Klassifizierung der Abhängigkeiten (z.B. sequenziell)"
  - Connection: → Koordinationsaufwand

### **5.2 Temporal Coordination (Ancona & Waller, 2007) ⚠️**
- ⚠️ Zeitliche Überlappung der Arbeitszeiten (elem-zeitlUeberlappung)
- ⚠️ Synchronisationsfrequenz (elem-synchronisationsfrequenz)
- ❌ **Pacing**: Sprint-Rhythmus als Koordinationsmechanismus nicht explizit
- ❌ **Entrainment**: Wie Teams sich synchronisieren (Zeitzonen, Deadlines)

### **5.3 Organizational Structures (Galbraith, 1977) ⚠️**
- ⚠️ Implizit in Rollen-Faktoren
- ❌ **Matrix Structures**: Nicht modelliert
- ❌ **Hierarchical Coordination**: Escalation, Management-Koordination fehlt

---

## 6. Gap Analysis: Was fehlt komplett?

### **Critical Gaps:**

1. **Accountability-Mechanismen (O&B Core Mechanism #1)**
   - Decision Rights / Authority Structures
   - Ownership (Code, Features, Decisions)
   - Rechenschaftspflicht bei Sprint Commitments
   - Consequence Structures

2. **Multi-Team/Scaled Agile Coordination (Dingsøyr et al. 2018)**
   - Scrum of Scrums / MetaScrum
   - Program Increment Planning (PI Planning)
   - Cross-Team Dependencies (als strukturierter Faktor)
   - Program-Level Backlogs
   - Communities of Practice

3. **Temporal Coordination Mechanisms**
   - Sprint/Iteration als Rhythmus-Faktor
   - Pacing & Deadlines als Koordination
   - Entrainment (zeitliche Synchronisation)
   - Service Level Expectations (SLE)

4. **Formale Strukturen (Explizite Policies)**
   - WIP-Limits (Kanban) als Koordinationsmechanismus
   - Pull Policies
   - Definition of Workflow (Kanban)
   - Team Working Agreements

---

## 7. Stärken des Models

### **Was das Model besonders gut macht:**

1. **✅ Common Understanding ist exzellent modelliert**
   - Explizite Referenz auf Okhuysen & Bechky (2009)
   - Viele Subfaktoren (mentale Modelle, Konvergenz, Externalisierung)
   - Wirkmechanismen gut dokumentiert

2. **✅ Scrum-Events als Koordinationsroutinen**
   - Alle Events vorhanden
   - Quality-Dimensionen für jeden Event
   - Connections zu Koordinationsaufwand modelliert

3. **✅ Media Richness Theory Integration**
   - Kommunikationsmedien als Koordinationsmechanismus
   - Strukturelle vs. wahrgenommene Medienreichhaltigkeit
   - Media-Task-Fit

4. **✅ Boundary Spanning**
   - Gut modelliert mit vielen Connections
   - Treiber und Auswirkungen dokumentiert

5. **✅ Knowledge Coordination**
   - Wissensaustausch, Externalisierung, mentale Modelle
   - Boundary Objects erwähnt

---

## 8. Priorisierte Ergänzungsvorschläge

### **High Priority (für 75% → 85% Coverage):**

1. **Accountability-Faktoren hinzufügen:**
   - [ ] `elem-codeOwnership` - Klarheit der Code/Component Ownership
   - [ ] `elem-decisionRights` - Klarheit der Entscheidungsrechte
   - [ ] `elem-commitmentTracking` - Follow-through auf Sprint-Commitments

2. **Multi-Team Koordination ausbauen:**
   - [ ] `elem-scrumOfScrums` - Qualität/Frequenz von Scrum of Scrums
   - [ ] `elem-interTeamDependencies` - Management von Cross-Team Dependencies
   - [ ] `elem-communitiesOfPractice` - Grad der CoP-Aktivität

3. **Temporal Coordination explizit machen:**
   - [ ] `elem-sprintRhythm` - Konsistenz des Sprint-Rhythmus
   - [ ] `elem-deadlinePressure` - bereits vorhanden (elem-zeitdruck), aber als Coordination Factor stärker verankern

### **Medium Priority (für 85% → 90% Coverage):**

4. **Workflow Policies:**
   - [ ] `elem-wipLimitAdherence` - Einhaltung von WIP-Limits
   - [ ] `elem-pullPolicies` - Nutzung von Pull-based Flow

5. **Narrative Coordination:**
   - [ ] `elem-sharedNarratives` - Grad geteilter Projekt-Narratives

---

## 9. Zusammenfassung & Empfehlung

### **Quantitative Coverage:**

| Coordination Mechanism | Coverage | Status |
|------------------------|----------|--------|
| **Common Understanding** (O&B) | ~85% | ✅ Exzellent |
| **Predictability** (O&B) | ~75% | ✅ Gut |
| **Accountability** (O&B) | ~60% | ⚠️ Ausbaufähig |
| **Multi-Team Coordination** (Dingsøyr) | ~45% | ⚠️ Signifikante Gaps |
| **GESAMT** | **~75%** | **Gut, aber verbesserbar** |

### **Qualitative Bewertung:**

**Das Model bildet die Koordinationstheorie gut ab, hat aber klare Schwächen:**

✅ **STÄRKEN:**
- Common Understanding ist State-of-the-Art modelliert
- Scrum-Events als Predictability-Mechanismen hervorragend
- Kommunikationsmedien als Koordination tiefgehend modelliert
- Boundary Spanning gut integriert

⚠️ **SCHWÄCHEN:**
- Accountability unterrepräsentiert (fehlt: Ownership, Decision Rights, Rechenschaftspflicht)
- Multi-Team Coordination kaum vorhanden (fehlt: SoS, PI Planning, Cross-Team Dependencies)
- Temporal Coordination implizit, aber nicht explizit
- Formale Policies (WIP-Limits, Pull) fehlen

### **Handlungsempfehlung:**

**Priorisierung für nächste Iteration:**
1. **Accountability ausbauen** (größte Gap in O&B-Framework)
2. **Multi-Team Faktoren hinzufügen** (relevant für Scale-Up)
3. **Temporal Coordination explizit machen** (derzeit zu implizit)

**Mit diesen 3 Schritten: Coverage ~85-90%**

---

## 10. Literatur-Reflexion

### **Ist das Model "richtig" nach Okhuysen & Bechky (2009)?**

**JA, im Kern:**
- Die 3 Core Mechanisms sind als Konzepte vorhanden
- Der Fokus auf **gemeinsames Verständnis** entspricht der Theorie
- Die Modellierung von Routinen/Ritualen als Predictability-Mechanismen ist theoriekonform

**ABER:**
- Okhuysen & Bechky betonen **Accountability stärker** als im Model abgebildet
- Das Model fokussiert stark auf **kommunikative Koordination**, weniger auf **strukturelle** (Org Design, Policies)

### **Ist das Model "richtig" nach Dingsøyr et al. (2018)?**

**TEILWEISE:**
- Boundary Spanning ist gut modelliert
- Knowledge Coordination ist vorhanden
- **ABER**: Multi-Team Rituale und Program-Level Koordination fehlen fast komplett

---

**Erstellt:** 2026-02-26  
**Analysebasis:** wirkmechanismen-main-model-blueprint.json (189 Elemente, 687 Connections)
