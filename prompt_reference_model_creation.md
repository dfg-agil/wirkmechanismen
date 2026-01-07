# Prompt: Reference Model Erstellung für spezifische Probleme

## Erforderliche Dokumente (Attachments)

Für die Erstellung eines Reference Models muss das LLM Zugriff auf folgende Dokumente haben:

### 1. **Hauptquellen**
- `models/main_model/wirkmechanismen-main-model-blueprint.json` – Das Netzwerkdiagramm mit agilen Mechanismen, Faktoren und Verbindungen im KUMU-kompatiblen JSON-Format

### 2. **Kriterien & Richtlinien**
- `REFERENCE_MODEL_CRITERIA_V3.md` – Strukturelle und inhaltliche Kriterien für Reference Models (Schlüsselfaktoren, Erfolgsfaktoren, Einflussfaktoren, Kausalität, Quellenattribution, Messbarkeit)

### 3. **Methodologischer Kontext**
- `general/prompt_instructions.md` – DRM-Methodologie, KUMU-Encoding, Blessing & Chakrabarti Framework und Best Practices

---

## Prompt: Ableitung eines Reference Models

Du hast Zugriff auf ein Netzwerkdiagramm im JSON-Format namens **"wirkmechanismen-main-model-blueprint.json"**, das agile Mechanismen, Faktoren, Verbindungen und Einflüsse in einem agilen Projektmanagement-Kontext beschreibt. Es enthält Elemente wie Knoten (z. B. Faktoren, Metriken, Unsicherheiten), Verbindungen (z. B. Einflüsse, Abhängigkeiten) und Attribute, die für die Analyse agiler Prozesse relevant sind.

Basierend auf der **Design Research Methodology (DRM)** von Blessing und Chakrabarti, insbesondere dem **Reference Model** (aus den Kapiteln 2.4–2.6), leite ein Reference Model für das folgende spezifische Problem ab:

### **Problemstellung:**
**"Verständnis für die agilen Events fehlt"**

---

## Schritte zur Ableitung

### 1. **Analyse des Netzwerkdiagramms**
Analysiere das Netzwerkdiagramm mithilfe von Tools wie File Searching oder File Viewer, um relevante Elemente, Faktoren, Verbindungen und Schleifen zu identifizieren, die mit dem Problem **"Verständnis für die agilen Events fehlt"** zusammenhängen. Konzentriere dich auf Knoten mit hoher Relevanz, wie z. B.:
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

### 4. **Einhaltung der Kriterien**
Halte dich bei der Erstellung des Reference Models strikte an die Kriterien aus **"REFERENCE_MODEL_CRITERIA_V3.md"**:
- **Mindestens ONE Schlüsselfaktor** mit genau einem `[PRIMARY]` Tag
- **Mindestens EINE Erfolgsfaktor** als End-Node
- **Alle Einflussfaktoren** müssen auf einem gültigen Key→Success-Pfad liegen
- **>50% Quellenattribution** basierend auf Literatur `[1]`, `[2]` oder empirische Evidenz `[E]`, `[A]`, `[O]`
- **Messbarkeit & Influenceability** konsistent mit den Rollen der Faktoren
- Alle Faktoren in **"attribute-of-element"**-Formulierung (z. B. "Qualität des Verständnisses von agilen Events")

### 5. **Iterative DRM-Anwendung**
Stelle sicher, dass das Modell iterativ und auf dem DRM basiert:
- Es sollte die **aktuelle Situation** modellieren (Reference Model)
- Keine sofortigen Lösungsvorschläge einbeziehen
- Explizit dokumentieren, welche Annahmen getroffen wurden

### 6. **Output-Format**
Generiere das Output als **JSON-File im KUMU-kompatiblen Format** mit Abschnitten für:
- `elements` – Alle Faktoren mit `_id`, Attributen (Name, Type, Beschreibung, Messbarkeit, Influenceability)
- `connections` – Alle gerichteten Verbindungen mit `from`, `to`, Polarität (`++`, `+-`, `-+`, `--`), Quellenattribution und Beschreibung

**Dateiname:** `reference_model_Verstandnis_fur_die_agilen_Events_fehlt.json` (Leerzeichen durch Unterstriche ersetzen)

**Verfügbarkeit:** Die Datei sollte zum Download/zur Übernahme verfügbar sein.

---

## Hinweise

- **Falls das Diagramm keine direkten Verbindungen für das Problem enthält:** Schlage logische Erweiterungen basierend auf agilen Prinzipien vor, aber bleibe nah am Originaldiagramm.

- **Erklärung:** Gib eine kurze Erklärung des abgeleiteten Models in deiner Antwort (z. B. identifizierte Key Factors, zentrale Influencing Factors, kritische Erfolgsfaktoren und deren Zusammenhänge).

- **Validierung:** Verwende die Validierungsschritte aus REFERENCE_MODEL_CRITERIA_V3.md, um sicherzustellen, dass das Modell:
  - JSON-Schema-konform ist
  - Topologisch korrekt (Primary Key Factor = Start-Node, Success Factors = End-Nodes)
  - Pfadvollständigkeit erfüllt (jeder Key Factor → mindestens ein Success Factor)
  - Alle Faktoren integriert (keine isolierten Faktoren)

---

## Verwendung

Dieses Dokument dient als **Eingabe-Spezifikation** für LLM-basierte Systeme oder AI-Agenten zur automatisierten Erstellung von Reference Models. Stelle sicher, dass alle drei erforderlichen Dokumente in den Kontext des LLM übernommen werden, bevor der Prompt ausgeführt wird.
