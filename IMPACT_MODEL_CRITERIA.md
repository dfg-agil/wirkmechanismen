# Impact Model Generierungskriterien

## Übersicht

Diese Datei definiert spezifische Kriterien für die Generierung von Impact Models (Wirkmodellen) im Wirkmechanismen-Projekt. Impact Models bauen auf validierten Reference Models auf und modellieren die erwünschte Zukunftssituation nach Einführung von Unterstützungsmaßnahmen (Supports/Interventions).

## Grundprinzipien

### Verhältnis zum Reference Model
- **MANDATORY**: Jedes Impact Model MUSS von einem validierten Reference Model abgeleitet sein
- **MANDATORY**: Impact Model MUSS denselben Domain-Scope verwenden (z.B. `dailies-effectiveness-reference-model.json` → `dailies-effectiveness-impact-model.json`)
- **MANDATORY**: Das zugrundeliegende Problem und der Erfolgsfaktor bleiben identisch
- **TRANSFORMATION**: Intervention-Elemente (Supports) werden hinzugefügt
- **TRANSFORMATION**: Neue oder veränderte Kausalbeziehungen werden explizit markiert

## Strukturelle Anforderungen

### 1. Element-Taxonomie (MANDATORY)

#### 1.1 Problem-Element (Optional behalten)
- **OPTIONAL**: Das ursprüngliche Problem-Element aus dem Reference Model kann beibehalten werden
- **KLASSIFIKATION**: `"element type": "Problem"`
- **ZWECK**: Dokumentiert die Ausgangssituation als Kontext
- **KEINE VERBINDUNGEN**: Problem-Element hat keine ausgehenden Verbindungen im Impact Model

#### 1.2 Schlüsselfaktor-Erhaltung
- **MANDATORY**: Alle Schlüsselfaktoren aus dem Reference Model MÜSSEN übernommen werden
- **KLASSIFIKATION**: `"element type": "Schlüsselfaktor"`
- **ROLLE**: Primäre Interventionsziele - werden durch Supports beeinflusst

#### 1.3 Support-Elemente (Interventionen)
- **MANDATORY**: Mindestens **EIN (1) Support-Element** pro Impact Model
- **DEFINITION**: Konkrete Maßnahmen, Werkzeuge oder Interventionen zur Verbesserung der Schlüsselfaktoren
- **KLASSIFIKATION**: `"element type": "Support"`
- **EMPFEHLUNG**: 1-3 Support-Elemente für fokussierte Interventionen
- **REJECT**: Impact Models ohne Support-Elemente

**Support-Formulierung**:
- **KORREKT**: `"Daily-Moderationsleitfaden"`, `"Visuelles Board"`, `"Timeboxing-Timer"`
- **KORREKT**: Konkrete Werkzeuge, Prozesse oder Hilfsmittel
- **FALSCH**: Abstrakte Ziele oder gewünschte Zustände

#### 1.4 Erfolgsfaktor-Struktur
- **MANDATORY**: Erfolgsfaktor aus Reference Model MUSS übernommen werden
- **KLASSIFIKATION**: `"element type": "Erfolgsfaktor"` oder `"Messbarer Erfolgsfaktor"`
- **UNVERÄNDERLICH**: Erfolgsfaktor-Definition bleibt identisch zum Reference Model

#### 1.5 Einflussfaktoren-Anpassung
- **MANDATORY**: Einflussfaktoren aus Reference Model werden übernommen
- **ERLAUBT**: Neue Einflussfaktoren, die durch Supports entstehen
- **KLASSIFIKATION**: `"element type": "Einflussfaktoren"`
- **MANDATORY**: Neue Einflussfaktoren MÜSSEN als Annahmen `[A]` dokumentiert werden

### 2. Kausale Netzwerkstruktur (MANDATORY)

#### 2.1 Support-zu-Schlüsselfaktor Beziehungen
- **MANDATORY**: Jeder Support MUSS mindestens einen Schlüsselfaktor beeinflussen
- **STRUKTUR**: `Support → Schlüsselfaktor → [Einflussfaktoren] → Erfolgsfaktor`
- **MANDATORY**: Support-Elemente sind **Startknoten** (keine eingehenden Verbindungen)
- **REJECT**: Supports ohne ausgehende Verbindungen zu Schlüsselfaktoren

#### 2.2 Modifizierte Kausalbeziehungen
- **MANDATORY**: Durch Supports veränderte Beziehungen MÜSSEN dokumentiert werden
- **MECHANISMUS**:
  - **Option A**: Alte Verbindung entfernen, neue Verbindung mit `[A]` hinzufügen
  - **Option B**: Verbindungsstärke/Polarität ändern und in `description` begründen
- **MANDATORY**: Änderungen MÜSSEN im connection `description` erklärt werden

#### 2.3 Neue Kausalbeziehungen
- **ERLAUBT**: Supports können neue Kausalbeziehungen schaffen
- **MANDATORY**: Alle neuen Verbindungen MÜSSEN mit `[A]` (Annahme) markiert werden
- **MANDATORY**: `description` MUSS theoretische oder empirische Begründung enthalten
- **EMPFEHLUNG**: Annahmen durch Pilotprojekte oder Literatur validieren

#### 2.4 Pfad-Anforderungen
- **MANDATORY**: Mindestens ein vollständiger Pfad von Support → Erfolgsfaktor
- **MANDATORY**: Maximale Pfadlänge: 5 Verbindungen (Support + 4 Zwischenschritte)
- **LOGIK-CHECK**: Alle Supports MÜSSEN kausal mit dem Erfolgsfaktor verbunden sein

### 3. Quellenattribution (MANDATORY)

#### 3.1 Literatur und Evidenz (aus Reference Model)
- **ÜBERNOMMEN**: Literaturquellen `[1]`, `[2]`, etc. aus dem Reference Model bleiben erhalten
- **MANDATORY**: Quellenattribution für unveränderte Verbindungen bleibt identisch

#### 3.2 Annahmen für Interventionen (Priorität für neue Verbindungen)
- **MANDATORY**: Alle neuen Verbindungen (durch Supports) MÜSSEN als `[A]` (Annahme) markiert werden
- **MANDATORY**: `description` MUSS Begründung der Annahme enthalten:
  - Theoretische Grundlage (Design-Prinzipien, Methodologie)
  - Empirische Indizien (Pilotprojekte, Expert:innen-Meinungen)
  - Analogien zu ähnlichen Interventionen
- **ZIEL**: Annahmen durch inkrementelle Validierung in Evidenz überführen

#### 3.3 Validierte Interventionen (nach Pilotierung)
- **ERLAUBT**: Nach erfolgreicher Pilotierung `[A]` durch `[O]` (eigene Untersuchung) ersetzen
- **ERLAUBT**: Bei Literaturnachweis `[A]` durch `[1-9]+` ersetzen
- **MANDATORY**: Validierungsprozess in commit message dokumentieren

#### 3.4 Unzulässige Quellen
- **REJECT**: Verbindungen mit `[?]` (unbekannte Quelle)
- **REJECT**: Neue Verbindungen ohne Quellenattribution (auch wenn Annahme)

### 4. Messbarkeits- und Beeinflussbarkeits-Kriterien

#### 4.1 Support-Eigenschaften
- **ERWARTUNG**: Supports haben hohe Beeinflussbarkeit (influenceability ≥ 0.9)
- **BEGRÜNDUNG**: Interventionen sind unter direkter Kontrolle des Teams
- **ERWARTUNG**: Supports haben niedrige inhärente Messbarkeit (0.3-0.6)
- **DOKUMENTATION**: Implementierungsgrad des Supports MUSS messbar sein (z.B. "Board vorhanden: ja/nein", "Leitfaden-Nutzungsquote")

#### 4.2 Schlüsselfaktor-Veränderungen
- **HYPOTHESE**: Durch Supports verbessern sich Schlüsselfaktoren
- **MANDATORY**: Erwartete Verbesserung MUSS in Support-Verbindung beschrieben werden
- **MESSBARKEIT**: Schlüsselfaktor-Messbarkeit bleibt identisch (aus Reference Model)
- **BEEINFLUSSBARKEIT**: Kann sich erhöhen, wenn Support direkte Steuerungsmöglichkeit schafft

#### 4.3 Erfolgsfaktor-Invarianz
- **MANDATORY**: Erfolgsfaktor-Messbarkeit und -Beeinflussbarkeit bleiben unverändert
- **BEGRÜNDUNG**: Langfristige Ziele ändern sich nicht durch kurzfristige Interventionen

### 5. Verbindungssemantik

#### 5.1 Richtung und Polarität
- **MANDATORY**: Alle Verbindungen MÜSSEN gerichtet sein (`"direction": "directed"`)
- **MANDATORY**: Verbindungstyp MUSS DRM-Polaritäten verwenden (`++`, `+-`, `-+`, `--`)
- **ERWARTUNG**: Support → Schlüsselfaktor Verbindungen sind typisch positiv (`++`)

#### 5.2 Verbindungsbeschreibungen für Supports
- **MANDATORY**: Support-Verbindungen MÜSSEN Wirkmechanismus erklären
- **FORMAT**: "Support X verbessert Faktor Y durch Mechanismus Z"
- **LÄNGE**: 30-200 Wörter für neue Annahme-basierte Verbindungen
- **INHALT**:
  - Wie funktioniert der Support?
  - Warum sollte er den Faktor verbessern?
  - Welche Annahmen liegen zugrunde?

### 6. Inkrementelle Validierung

#### 6.1 Validierungsstufen
1. **Theoretische Plausibilität** (`[A]` mit Begründung)
   - Design-Prinzipien, methodologische Grundlagen
   - Analogien zu ähnlichen Kontexten
2. **Pilotierung** (`[O]` nach Durchführung)
   - Kleine Testgruppe oder Prototyp
   - Qualitative Evidenz (Interviews, Beobachtungen)
3. **Quantitative Validierung** (`[O]` mit Daten)
   - Messungen vor/nach Intervention
   - Kontrollgruppen-Vergleiche
4. **Literaturbestätigung** (`[1-9]+`)
   - Publizierte Studien zu ähnlichen Interventionen

#### 6.2 Validierungszyklus
- **MANDATORY**: Jede Annahme `[A]` MUSS Validierungsplan haben
- **DOKUMENTATION**: Validierungsstatus in commit messages oder separate Tracking-Datei
- **ITERATION**: Validierte Interventionen fließen zurück ins Main Model

### 7. Validierungsschritte

#### 7.1 Automatische Validierung
1. JSON-Schema-Compliance (`lint_blueprint.py`)
2. Element-/Verbindungs-ID Eindeutigkeit
3. Referenz-Integrität (from/to verweisen auf existierende IDs)
4. Faktor-Taxonomie-Compliance (inkl. Support-Elemente)
5. **Support-Validierung**: Mindestens ein Support vorhanden
6. **Topologie-Validierung**: Supports als Startknoten, Erfolgsfaktor als Endknoten

#### 7.2 Inhaltliche Validierung
1. **Reference Model Konsistenz**: Problem/Erfolgsfaktor identisch zum Reference Model
2. **Support-Integration**: Alle Supports verbunden mit Schlüsselfaktoren
3. **Pfad-Vollständigkeit**: Mindestens ein Pfad Support → Erfolgsfaktor
4. **Annahmen-Dokumentation**: Alle `[A]` Verbindungen haben aussagekräftige Beschreibungen
5. **Validierungsplan**: Jede Annahme hat geplanten Validierungsmechanismus

#### 7.3 Qualitätskennzahlen
- **Support Coverage**: 100% - Alle Schlüsselfaktoren durch mindestens einen Support adressiert
- **Assumption Documentation**: 100% - Alle `[A]` Verbindungen haben Begründung
- **Topological Integrity**: 100% - Supports (Start) → Erfolgsfaktor (Ende) Struktur
- **Path Completeness**: 100% - Mindestens ein vollständiger Pfad vorhanden
- **Validation Planning**: ≥75% der Annahmen haben dokumentierten Validierungsplan

## Impact Model Template

### Minimale Struktur
```json
{
  "elements": [
    {
      "_id": "elem-PROBLEM",
      "attributes": {
        "label": "[Problem-Beschreibung]",
        "element type": "Problem",
        "description": "Ausgangssituation (aus Reference Model)"
      }
    },
    {
      "_id": "elem-SUPPORT-1",
      "attributes": {
        "label": "[Konkretes Werkzeug/Intervention]",
        "element type": "Support",
        "measurability": 0.5,
        "influenceability": 0.95,
        "description": "STARTKNOTEN: Beschreibung der Intervention und Implementierung"
      }
    },
    {
      "_id": "elem-KEY-FACTOR",
      "attributes": {
        "label": "[Attribut des Problems]",
        "element type": "Schlüsselfaktor",
        "measurability": 0.7,
        "influenceability": 0.8,
        "description": "Übernommen aus Reference Model"
      }
    },
    {
      "_id": "elem-INFLUENCING-FACTOR-1",
      "attributes": {
        "label": "[Zwischenfaktor]",
        "element type": "Einflussfaktoren",
        "measurability": 0.6,
        "influenceability": 0.5,
        "description": "Übernommen aus Reference Model"
      }
    },
    {
      "_id": "elem-SUCCESS-FACTOR",
      "attributes": {
        "label": "[Langfristiges Ziel]",
        "element type": "Erfolgsfaktor",
        "measurability": 0.4,
        "influenceability": 0.2,
        "description": "ENDKNOTEN: Übernommen aus Reference Model"
      }
    }
  ],
  "connections": [
    {
      "_id": "conn-SUPPORT-TO-KEY",
      "from": "elem-SUPPORT-1",
      "to": "elem-KEY-FACTOR",
      "direction": "directed",
      "attributes": {
        "label": "[A]",
        "connection type": "++",
        "description": "NEUE VERBINDUNG: Support verbessert Schlüsselfaktor durch [Mechanismus]. Annahme basiert auf [Begründung]. Validierung geplant durch [Methode]."
      }
    },
    {
      "_id": "conn-KEY-TO-INFLUENCING",
      "from": "elem-KEY-FACTOR",
      "to": "elem-INFLUENCING-FACTOR-1",
      "direction": "directed",
      "attributes": {
        "label": "[1]",
        "connection type": "++",
        "description": "Übernommen aus Reference Model mit Literaturquelle"
      }
    },
    {
      "_id": "conn-INFLUENCING-TO-SUCCESS",
      "from": "elem-INFLUENCING-FACTOR-1",
      "to": "elem-SUCCESS-FACTOR",
      "direction": "directed",
      "attributes": {
        "label": "[2]",
        "connection type": "++",
        "description": "Übernommen aus Reference Model"
      }
    }
  ]
}
```

## Compliance Checklist

### Pre-Submission
- [ ] Basiert auf validiertem Reference Model (identischer Domain-Scope)
- [ ] Problem und Erfolgsfaktor aus Reference Model übernommen
- [ ] Mindestens 1 Support-Element vorhanden
- [ ] Alle Supports mit Schlüsselfaktoren verbunden
- [ ] Direkte Kausalkette Support → Erfolgsfaktor vorhanden
- [ ] Alle neuen Verbindungen mit `[A]` markiert
- [ ] Alle `[A]` Verbindungen haben Begründung in `description`
- [ ] Supports als Startknoten definiert (keine eingehenden Verbindungen)
- [ ] Messbarkeits-/Beeinflussbarkeits-Werte konsistent
- [ ] JSON-Validation erfolgreich

### Review Criteria
- [ ] Support-Interventionen sind konkret und implementierbar
- [ ] Wirkmechanismen wissenschaftlich/praktisch plausibel
- [ ] Annahmen-Begründungen nachvollziehbar
- [ ] Validierungspläne für Annahmen vorhanden
- [ ] Keine widersprüchlichen Kausalbeziehungen zum Reference Model
- [ ] Modellkomplexität angemessen (nicht zu viele Supports)

### Validation Planning
- [ ] Für jede `[A]` Verbindung: Validierungsmethode definiert
- [ ] Pilotierungs-Timeline erstellt
- [ ] Messkriterien für Intervention-Erfolg festgelegt
- [ ] Datenerhebungs-Mechanismen spezifiziert

## Rejection Criteria

- **AUTOMATIC REJECT**: Kein Support-Element vorhanden
- **AUTOMATIC REJECT**: Supports nicht mit Schlüsselfaktoren verbunden
- **AUTOMATIC REJECT**: Unterbrochene Kausalkette Support → Erfolgsfaktor
- **AUTOMATIC REJECT**: Neue Verbindungen ohne `[A]` Markierung
- **AUTOMATIC REJECT**: `[A]` Verbindungen ohne Begründung in `description`
- **AUTOMATIC REJECT**: JSON-Schema-Verletzungen
- **AUTOMATIC REJECT**: Erfolgsfaktor verändert gegenüber Reference Model
- **AUTOMATIC REJECT**: Problem-Element hat ausgehende Verbindungen

## Inkrementelle Validierung und Rückführung

### Validierungs-Workflow
1. **Impact Model Scaffolding**: Initiales Model mit `[A]` Annahmen
2. **Human + Peer Review**: Plausibilitätsprüfung
3. **Pilotierung**: Kleine Testgruppe, qualitative Evidenz sammeln
4. **Iteration**: `[A]` → `[O]` für validierte Annahmen
5. **Skalierung**: Quantitative Validierung, ggf. `[O]` → `[1-9]+` bei Publikation
6. **Rückführung**: Validierte Support-Beziehungen ins Main Model integrieren

### Commit-basiertes Tracking
- **INITIAL**: `[IMPACT] Add {domain} impact model with {N} support interventions`
- **VALIDATION**: `[IMPACT] Validate assumption [A] → [O] for {connection} based on {pilot/study}`
- **ITERATION**: `[IMPACT] Refine support {name} based on pilot results`
- **FINALIZATION**: `[IMPACT] Promote validated {domain} model to production`

## Zusammenfassung

Impact Models sind Zukunftsmodelle, die auf validierten Reference Models aufbauen. Sie:
1. Führen **Support-Elemente** (konkrete Interventionen) ein
2. Dokumentieren **neue Kausalbeziehungen** als **Annahmen** `[A]`
3. Behalten **Problem und Erfolgsfaktor** des Reference Models bei
4. Folgen einem **inkrementellen Validierungszyklus**
5. Fließen nach Validierung zurück ins **Main Model**

Impact Models sind experimenteller Natur und ermöglichen systematisches Testen von Design-Interventionen mit klarer Evidenzbasis.
