# Prompt: Reference Model Erstellung für spezifische Probleme

## Erforderliche Dokumente (Attachments)

Für die Erstellung eines Reference Models muss das LLM Zugriff auf folgende Dokumente haben:

### 1. **Hauptquellen**
- `models/main_model/wirkmechanismen-main-model-blueprint.json` – Das Netzwerkdiagramm mit agilen Mechanismen, Faktoren und Verbindungen im KUMU-kompatiblen JSON-Format

### 2. **Kriterien & Richtlinien**
- `REFERENCE_MODEL_CRITERIA_V3.md` – Strukturelle und inhaltliche Kriterien für Reference Models (Schlüsselfaktoren, Erfolgsfaktoren, Einflussfaktoren, Kausalität, Quellenattribution, Messbarkeit)

### 3. **Methodologischer Kontext**
- `general/prompt_instructions.md` – DRM-Methodologie, KUMU-Encoding, Blessing & Chakrabarti Framework und Best Practices
- `general/Blessing_Chakrabarti_2009_DRM.pdf` – Originalpublikation "Design Research Methodology" (Blessing & Chakrabarti, 2009) mit ausführlicher Definition des Reference Models (Kapitel 2.4–2.6)

---

## Prompt: Ableitung eines Reference Models

Du hast Zugriff auf ein Netzwerkdiagramm im JSON-Format namens **"wirkmechanismen-main-model-blueprint.json"**, das agile Mechanismen, Faktoren, Verbindungen und Einflüsse in einem agilen Projektmanagement-Kontext beschreibt. Es enthält Elemente wie Knoten (z. B. Faktoren, Metriken, Unsicherheiten), Verbindungen (z. B. Einflüsse, Abhängigkeiten) und Attribute, die für die Analyse agiler Prozesse relevant sind.

Basierend auf der **Design Research Methodology (DRM)** von Blessing und Chakrabarti, insbesondere dem **Reference Model** (aus den Kapiteln 2.4–2.6), leite ein Reference Model für das folgende spezifische Problem ab:

### **Problemstellung:**
**[PROBLEM_PLACEHOLDER]**

> Ersetze `[PROBLEM_PLACEHOLDER]` mit dem spezifischen Problem, für das das Reference Model erstellt werden soll (z. B. "Verständnis für die agilen Events fehlt", "Mangelnde Priorisierung von Anforderungen", etc.)

---

## Schritte zur Ableitung

### 1. **Analyse des Netzwerkdiagramms**
Analysiere das Netzwerkdiagramm mithilfe von Tools wie File Searching oder File Viewer, um relevante Elemente, Faktoren, Verbindungen und Schleifen zu identifizieren, die mit dem **Problem [PROBLEM_PLACEHOLDER]** zusammenhängen. Konzentriere dich auf Knoten mit hoher Relevanz, wie z. B.:
- Unsicherheiten
- Metriken
- Team-Dynamiken
- Agile Prinzipien
- Event-bezogene Faktoren

### 2. **Identifizierung von Schlüsselfaktoren**
Identifiziere Schlüssel-Faktoren aus dem Diagramm, die das Problem beeinflussen, insbesondere:
- Ursachen und Auswirkungen
- Verstärkungsschleifen
- Lücken in den Verbindungen
- Faktoren, die direkt mit "Verständnis für agile Events" verknüpft sind

### 3. **Erstellung des Reference Models**
Erstelle ein Reference Model, das die **bestehende Situation** beschreibt:
- Zeige Beziehungen zwischen Faktoren als **gerichtete Verbindungen** (z. B. positive/negative Einflüsse, Unsicherheiten markiert mit "?")
- Berücksichtige vollständige Stränge, Schleifen und potenzielle Lücken, wie im Diagramm vorhanden
- Folge dem Schema: **Key Factor(s) → [Influencing Factors] → [Measurable Success Factors] → Success Factor(s)**

### 4. **Einhaltung der Kriterien (REFERENCE_MODEL_CRITERIA_V3.md)**

#### Elementtaxonomie
- **Schlüsselfaktoren**: Mindestens **EINE (1)**, genau eine mit `[PRIMARY]` Tag in `attributes.description`
- **Erfolgsfaktoren**: Mindestens **EINE (1)** als End-Node
- **Messbare Erfolgsfaktoren**: Falls Erfolgsfaktor `measurability < 0.8`, muss ein messbarer Proxy hinzugefügt werden
- **Einflussfaktoren**: Alle restlichen Faktoren; müssen auf einem gültigen Key→Success-Pfad liegen (keine isolierten Faktoren)

#### Kausalstruktur
- Topologie: **Primary Key Factor = Start-Node** (keine eingehenden Verbindungen)
- **Success Factors = End-Nodes** (keine ausgehenden Verbindungen)
- **Pfadvollständigkeit**: Mindestens ein gerichteter Pfad vom Primary Key Factor zu mindestens einem Success Factor
- **Maximale Pfadlänge**: 4 gerichtete Verbindungen
- **Alle Faktoren integriert**: Keine isolierten Faktoren; alle Influencing Factors auf mindestens einem Key→Success-Pfad

#### Quellenattribution (MANDATORY)
- **>50%** aller Verbindungen mit Literaturquellen `[1]`, `[2]`, etc.
- **Dokumentation**: Vollständige APA-Zitate in `connection.attributes.description`
- **Erlaubte Evidenztypen**: `[E]` (Erfahrung), `[A]` (Annahme), `[O]` (Untersuchung)
- **ABLEHNUNG**: Verbindungen ohne Quellenattribution oder mit `[?]`

#### Messbarkeit & Influenceability
- **Schlüsselfaktoren**: `measurability ≥ 0.6` und `influenceability ≥ 0.7`
- **Messbare Erfolgsfaktoren**: `measurability ≥ 0.8`
- **Erfolgsfaktoren**: `measurability ≥ 0.3`, typischerweise `influenceability ≤ 0.3`

#### Faktoren-Formulierung
- Alle Faktoren in **"attribute-of-element"**-Formulierung (z. B. "Qualität des Verständnisses von agilen Events", nicht "Event-Verständnis")

### 5. **Iterative DRM-Anwendung**
Stelle sicher, dass das Modell iterativ und auf dem DRM basiert:
- Es sollte die **aktuelle Situation** modellieren (Reference Model)
- Keine sofortigen Lösungsvorschläge einbeziehen
- Explizit dokumentieren, welche Annahmen getroffen wurden

### 6. **Output-Format**
Generiere das Output als **JSON-File im KUMU-kompatiblen Format** mit Abschnitten für:
- `elements` – Alle Faktoren mit `_id`, Attributen (Name, Type, Beschreibung, Messbarkeit, Influenceability)
- `connections` – Alle gerichteten Verbindungen mit `from`, `to`, Polarität (`++`, `+-`, `-+`, `--`), Quellenattribution und Beschreibung

**Dateiname:** `reference_model_[PROBLEM_PLACEHOLDER_WITH_UNDERSCORES].json`
(Ersetze `[PROBLEM_PLACEHOLDER_WITH_UNDERSCORES]` mit dem Problem-Namen, wobei Leerzeichen und Umlaute durch Unterstriche ersetzt werden. Beispiel: "Verständnis für die agilen Events fehlt" → `reference_model_Verstandnis_fuer_die_agilen_Events_fehlt.json`)

**Verfügbarkeit:** Die Datei sollte zum Download/zur Übernahme verfügbar sein.

---

## Hinweise

- **Datenquelle (KRITISCH):** Verwende **NUR** das Netzwerkdiagramm `wirkmechanismen-main-model-blueprint.json` als Quelle für die Reference Model Erstellung. Keine zusätzlichen externen Quellen oder Annahmen ohne explizite Kennzeichnung `[A]`.

- **Keine Extrapolationen:** Falls das Diagramm keine direkten Verbindungen für das Problem enthält, kann eine **minimale logische Erweiterung** basierend auf agilen Prinzipien und dem Originaldiagramm vorgenommen werden – markiere diese jedoch explizit als Annahmen `[A]` in den Verbindungsbeschreibungen.

- **Erklärung des Modells:** Gib eine kurze Zusammenfassung des abgeleiteten Models aus (z. B. identifizierte Key Factors, zentrale Influencing Factors, kritische Erfolgsfaktoren und deren Zusammenhänge).

- **Validierung:** Verwende die Validierungsschritte aus REFERENCE_MODEL_CRITERIA_V3.md, um sicherzustellen, dass das Modell:
  - JSON-Schema-konform ist
  - Topologisch korrekt (Primary Key Factor = Start-Node, Success Factors = End-Nodes)
  - Pfadvollständigkeit erfüllt (Primary Key Factor → mindestens ein Success Factor)
  - Alle Faktoren integriert (keine isolierten Faktoren)
  - Quellenattribution korrekt dokumentiert

---

## Verwendung

Dieses Dokument dient als **Eingabe-Spezifikation** für LLM-basierte Systeme oder AI-Agenten zur automatisierten Erstellung von Reference Models. Stelle sicher, dass alle drei erforderlichen Dokumente in den Kontext des LLM übernommen werden, bevor der Prompt ausgeführt wird.
