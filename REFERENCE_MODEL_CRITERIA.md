# Referenzmodell Generierungskriterien

## Übersicht

Diese Datei definiert spezifische Kriterien für die Generierung von Referenzmodellen im Wirkmechanismen-Projekt. Sie ergänzt die allgemeinen Gatekeeping-Kriterien um konkrete Strukturvorgaben für konsistente und fokussierte Modelle.

## Strukturelle Anforderungen

### 1. Element-Taxonomie (MANDATORY)

#### 1.1 Schlüsselfaktor-Beschränkung
- **MANDATORY**: Genau **EIN (1) Schlüsselfaktor** pro Referenzmodell
- **DEFINITION**: Der zentrale Faktor, der das Hauptproblem repräsentiert und als primäres Interventionsziel dient
- **KLASSIFIKATION**: `"element type": "Schlüsselfaktor"`
- **REJECT**: Modelle mit null oder mehreren Schlüsselfaktoren

#### 1.2 Erfolgsfaktor-Struktur
- **MANDATORY**: Genau **EIN (1) Erfolgsfaktor** pro Referenzmodell
- **DEFINITION**: Langfristiges, übergeordnetes Ziel (z.B. Produktqualität, Kundenzufriedenheit)
- **KLASSIFIKATION**: `"element type": "Erfolgsfaktor"`
- **MANDATORY**: Falls Erfolgsfaktor nicht direkt messbar (measurability < 0.8), MUSS ein messbarer Erfolgsfaktor als Proxy hinzugefügt werden
- **KLASSIFIKATION Proxy**: `"element type": "Messbarer Erfolgsfaktor"`
- **REJECT**: Modelle ohne Erfolgsfaktor oder mit mehreren Erfolgsfaktoren

#### 1.3 Einflussfaktoren-Klassifikation  
- **MANDATORY**: Alle anderen Faktoren MÜSSEN als Einflussfaktoren klassifiziert werden
- **KLASSIFIKATION**: `"element type": "Einflussfaktoren"`
- **EMPFEHLUNG**: 3-7 Einflussfaktoren für ausgewogene Modellkomplexität
- **REVIEW REQUIRED**: Modelle mit >10 Einflussfaktoren (Komplexitätsprüfung)

### 2. Kausale Kettenstruktur (MANDATORY)

#### 2.1 Kausale Netzwerk-Topologie
- **MANDATORY**: Schlüsselfaktor ist der **einzige Startknoten** (keine eingehenden Verbindungen)
- **MANDATORY**: Erfolgsfaktor ist der **einzige Endknoten** (keine ausgehenden Verbindungen)
- **MANDATORY**: Alle Einflussfaktoren MÜSSEN sich kausal zwischen Schlüsselfaktor und Erfolgsfaktor befinden
- **STRUKTUR**: `Schlüsselfaktor → [Einflussfaktoren] → [Messbarer Erfolgsfaktor] → Erfolgsfaktor`

#### 2.2 Pfad-Anforderungen
- **MANDATORY**: Mindestens ein direkter Pfad vom Schlüsselfaktor zum Erfolgsfaktor
- **MANDATORY**: Maximale Pfadlänge: 4 Verbindungen zwischen Schlüsselfaktor und Erfolgsfaktor
- **MANDATORY**: Alle Einflussfaktoren MÜSSEN auf diesem Hauptpfad liegen oder darauf einwirken
- **REJECT**: Einflussfaktoren ohne Verbindung zum Hauptpfad
- **REJECT**: Einflussfaktoren mit eingehenden Verbindungen von außerhalb des Modells

### 3. Quellenattribution (MANDATORY)

#### 3.1 Literaturbasierte Verbindungen (Priorität 1)
- **TARGET**: >50% aller Verbindungen mit Literaturquellen `[1]`, `[2]`, etc.
- **MANDATORY**: Literaturquellen MÜSSEN in `connection.description` dokumentiert werden
- **FORMAT**: Vollständige akademische Zitation (APA-Style)
- **REJECT**: Literaturverweise ohne entsprechende Dokumentation

#### 3.2 Empirische Evidenz (Priorität 2)
- **ERLAUBT**: Stakeholder-Erfahrung `[E]`, `[A]` Annahme, oder eigene Untersuchungen `[O]`
- **MANDATORY**: Beschreibung der Evidenzbasis in `connection.description`
- **LIMIT**: Max. 50% der Verbindungen ohne Literaturgrundlage

#### 3.3 Unzulässige Quellen
- **REJECT**: Verbindungen mit `[?]` (unbekannte Quelle)
- **REJECT**: Verbindungen ohne Quellenattribution

### 4. Messbarkeits- und Beeinflussbarkeits-Kriterien

#### 4.1 Messbarkeit (measurability)
- **MANDATORY**: Schlüsselfaktor MUSS messbar sein (measurability ≥ 0.6)
- **MANDATORY**: Messbarer Erfolgsfaktor MUSS hoch messbar sein (measurability ≥ 0.8)
- **MANDATORY**: Erfolgsfaktor kann niedrigere Messbarkeit haben (measurability ≥ 0.3)
- **DOKUMENTATION**: Messmethoden MÜSSEN in `description` spezifiziert werden

#### 4.2 Beeinflussbarkeit (influenceability)
- **MANDATORY**: Schlüsselfaktor MUSS beeinflussbar sein (influenceability ≥ 0.7)
- **ERWARTUNG**: Erfolgsfaktoren haben typisch niedrige Beeinflussbarkeit (≤ 0.3)
- **LOGIK-CHECK**: Beeinflussbarkeit MUSS mit Faktor-Rolle konsistent sein

### 5. Verbindungssemantik

#### 5.1 Richtung und Polarität
- **MANDATORY**: Alle Verbindungen MÜSSEN gerichtet sein (`"direction": "directed"`)
- **MANDATORY**: Verbindungstyp MUSS DRM-Polaritäten verwenden (`++`, `+-`, `-+`, `--`)
- **EMPFEHLUNG**: Positive Hauptkette vom Schlüsselfaktor zum Erfolgsfaktor

#### 5.2 Verbindungsbeschreibungen
- **MANDATORY**: Jede Verbindung MUSS kausalen Mechanismus in `description` erklären
- **FORMAT**: "Faktor X führt zu Faktor Y durch Mechanismus Z"
- **LÄNGE**: 20-150 Wörter pro Beschreibung

### 6. Validierungsschritte

#### 6.1 Automatische Validierung
1. JSON-Schema-Compliance (`lint_blueprint.py`)
2. Element-/Verbindungs-ID Eindeutigkeit
3. Referenz-Integrität (from/to verweisen auf existierende IDs)
4. Faktor-Taxonomie-Compliance
5. **Topologie-Validierung**: Schlüsselfaktor als Startknoten, Erfolgsfaktor als Endknoten

#### 6.2 Inhaltliche Validierung  
1. **Netzwerk-Topologie**: Schlüsselfaktor ohne eingehende, Erfolgsfaktor ohne ausgehende Verbindungen
2. **Pfad-Vollständigkeit**: Mindestens ein Pfad Schlüsselfaktor → Erfolgsfaktor
3. **Einflussfaktoren-Integration**: Alle Einflussfaktoren zwischen Start- und Endknoten
4. Quellenattribution-Quote berechnen
5. Messbarkeits-/Beeinflussbarkeits-Konsistenz validieren
6. Faktor-Formulierung nach DRM-Prinzipien prüfen

#### 6.3 Qualitätskennzahlen
- **Evidence Coverage**: ≥75% Literaturquellen `[1-9]+`
- **Topological Integrity**: 100% - Schlüsselfaktor (Start) → Erfolgsfaktor (Ende) Struktur
- **Path Completeness**: 100% - Mindestens ein vollständiger Pfad vorhanden
- **Factor Integration**: 100% - Alle Einflussfaktoren auf Hauptpfad integriert
- **Factor Precision**: 100% - Alle Faktoren folgen "Attribut-des-Elements" Formulierung
- **Measurability Consistency**: Messbare Erfolgsfaktoren ≥0.8, Schlüsselfaktoren ≥0.6

## Referenzmodell-Template

### Minimale Struktur
```json
{
  "elements": [
    {
      "_id": "elem-KEY-FACTOR",
      "attributes": {
        "label": "[Attribut des Problems]",
        "element type": "Schlüsselfaktor",
        "measurability": 0.7,
        "influenceability": 0.8,
        "description": "STARTKNOTEN: Kein eingehende Verbindungen erlaubt"
      }
    },
    {
      "_id": "elem-INFLUENCING-FACTOR-1",
      "attributes": {
        "label": "[Zwischenfaktor]",
        "element type": "Einflussfaktoren",
        "measurability": 0.6,
        "influenceability": 0.5,
        "description": "Liegt kausal zwischen Start- und Endknoten"
      }
    },
    {
      "_id": "elem-MEASURABLE-SUCCESS",
      "attributes": {
        "label": "[Messbarer Proxy]", 
        "element type": "Messbarer Erfolgsfaktor",
        "measurability": 0.9,
        "influenceability": 0.3,
        "description": "Zwischenschritt auf Hauptpfad zum Erfolgsfaktor"
      }
    },
    {
      "_id": "elem-SUCCESS-FACTOR", 
      "attributes": {
        "label": "[Langfristiges Ziel]",
        "element type": "Erfolgsfaktor",
        "measurability": 0.4,
        "influenceability": 0.2,
        "description": "ENDKNOTEN: Keine ausgehende Verbindungen erlaubt"
      }
    }
  ],
  "connections": [
    {
      "_id": "conn-KEY-TO-INFLUENCING",
      "from": "elem-KEY-FACTOR",
      "to": "elem-INFLUENCING-FACTOR-1", 
      "direction": "directed",
      "attributes": {
        "label": "[1]",
        "connection type": "++",
        "description": "Startknoten beeinflusst ersten Zwischenfaktor"
      }
    },
    {
      "_id": "conn-INFLUENCING-TO-MEASURABLE",
      "from": "elem-INFLUENCING-FACTOR-1",
      "to": "elem-MEASURABLE-SUCCESS",
      "direction": "directed",
      "attributes": {
        "label": "[2]",
        "connection type": "++",
        "description": "Zwischenfaktor führt zu messbarem Erfolg"
      }
    },
    {
      "_id": "conn-MEASURABLE-TO-SUCCESS",
      "from": "elem-MEASURABLE-SUCCESS",
      "to": "elem-SUCCESS-FACTOR",
      "direction": "directed", 
      "attributes": {
        "label": "[3]",
        "connection type": "++",
        "description": "Proxy-Beziehung zum Endknoten"
      }
    }
  ]
}
```

## Compliance Checklist

### Pre-Submission
- [ ] Genau 1 Schlüsselfaktor vorhanden
- [ ] Genau 1 Erfolgsfaktor vorhanden  
- [ ] Messbarer Erfolgsfaktor bei niedrig messbarem Erfolgsfaktor hinzugefügt
- [ ] Alle anderen Faktoren als "Einflussfaktoren" klassifiziert
- [ ] Direkte Kausalkette Schlüsselfaktor → Erfolgsfaktor vorhanden
- [ ] >50% Verbindungen mit Literaturquellen
- [ ] Alle Literaturquellen dokumentiert
- [ ] Keine `[?]` Quellen in Referenzmodell
- [ ] Messbarkeits-/Beeinflussbarkeits-Werte konsistent
- [ ] JSON-Validation erfolgreich

### Review Criteria
- [ ] Kausalkette wissenschaftlich plausibel
- [ ] Faktor-Formulierungen präzise und eindeutig  
- [ ] Literaturquellen relevant und aktuell
- [ ] Modellkomplexität angemessen (3-10 Faktoren total)
- [ ] Verbindungsbeschreibungen aussagekräftig

## Rejection Criteria

- **AUTOMATIC REJECT**: Mehr oder weniger als 1 Schlüsselfaktor
- **AUTOMATIC REJECT**: Mehr oder weniger als 1 Erfolgsfaktor  
- **AUTOMATIC REJECT**: Unterbrochene Kausalkette Schlüsselfaktor → Erfolgsfaktor
- **AUTOMATIC REJECT**: <50% Literaturquellen
- **AUTOMATIC REJECT**: Unbekannte Quellen `[?]`
- **AUTOMATIC REJECT**: JSON-Schema-Verletzungen
- **AUTOMATIC REJECT**: Faktoren ohne "Attribut-des-Elements" Formulierung