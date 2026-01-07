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

## Verwendungsanleitung

1. **Dokumente anhängen**: Stelle sicher, dass das LLM Zugriff auf alle erforderlichen Dokumente hat (siehe oben).
2. **Platzhalter ersetzen**: Ersetze vor dem Kopieren die Platzhalter:
   - `[PROBLEM_PLACEHOLDER]` → Das spezifische Problem (z. B. "Verständnis für die agilen Events fehlt")
   - `[PROBLEM_PLACEHOLDER_WITH_UNDERSCORES]` → Problem mit Unterstrichen statt Leerzeichen für den Dateinamen
3. **Prompt kopieren**: Kopiere den kompletten Prompt-Text (Abschnitt "Der reine Prompt" unten) und gebe ihn dem LLM.

---

## Der reine Prompt (zum Kopieren)

Du hast Zugriff auf ein Netzwerkdiagramm im JSON-Format namens **"wirkmechanismen-main-model-blueprint.json"**, das agile Mechanismen, Faktoren, Verbindungen und Einflüsse in einem agilen Projektmanagement-Kontext beschreibt. Es enthält Elemente wie Knoten (z. B. Faktoren, Metriken, Unsicherheiten), Verbindungen (z. B. Einflüsse, Abhängigkeiten) und Attribute, die für die Analyse agiler Prozesse relevant sind.

Basierend auf der **Design Research Methodology (DRM)** von Blessing und Chakrabarti, insbesondere dem **Reference Model** (aus den Kapiteln 2.4–2.6), leite ein Reference Model für das folgende spezifische Problem ab:

### **Problemstellung:**
[PROBLEM_PLACEHOLDER]

---

## Schritte zur Ableitung

### 1. **Analyse des Netzwerkdiagramms**
Analysiere das Netzwerkdiagramm, um relevante Elemente, Faktoren, Verbindungen und Schleifen zu identifizieren, die mit dem definierten Problem zusammenhängen. Konzentriere dich auf Knoten mit hoher Relevanz, wie z. B.:
- Unsicherheiten
- Metriken
- Team-Dynamiken
- Agile Prinzipien
- Event-bezogene Faktoren

### 2. **Identifizierung von Schlüsselfaktoren**
Identifiziere Schlüssel-Faktoren aus dem Diagramm, die das identifizierte Problem beeinflussen, insbesondere:
- Ursachen und Auswirkungen
- Verstärkungsschleifen
- Lücken in den Verbindungen
- Faktoren, die direkt mit dem Problem verknüpft sind

### 3. **Erstellung des Reference Models**
Erstelle ein Reference Model, das die **bestehende Situation** beschreibt:
- Zeige Beziehungen zwischen Faktoren als **gerichtete Verbindungen** (z. B. positive/negative Einflüsse, Unsicherheiten markiert mit "?")
- Berücksichtige vollständige Stränge, **Rückkopplungsschleifen** und potenzielle Lücken, wie im Diagramm vorhanden
- Das Modell sollte eine **Netzwerk-Struktur** mit dynamischen Rückkopplungen haben (nicht nur linear):
  - **Primärer Fluss**: Key Factor(s) → Influencing Factors → Success Factor(s)
  - **Erlaubt**: Rückkopplungen zwischen Einflussfaktoren, von Erfolgsfaktoren zu Einflussfaktoren, zwischen Key Factors und Influencing Factors
  - Alle Rückkopplungen müssen explizit mit ihren kausalen Mechanismen dokumentiert sein
- Folge dem Schema: **Key Factor(s) → [Influencing Factors] → [Measurable Success Factors] → Success Factor(s)** mit möglichen Rückkopplungen

### 4. **Einhaltung der Kriterien**

**Elementtaxonomie:**
- Schlüsselfaktoren: Mindestens EINE (1), genau eine mit [PRIMARY] Tag in attributes.description
- Erfolgsfaktoren: Mindestens EINE (1) als bevorzugt End-Node (oder justifizieren falls nicht)
- Messbare Erfolgsfaktoren: Falls Erfolgsfaktor nicht direkt messbar (measurability < 1.0), muss ein messbarer Proxy mit measurability = 1.0 hinzugefügt werden
- Einflussfaktoren: Alle restlichen Faktoren; müssen auf einem gültigen Key→Success-Pfad liegen (keine isolierten Faktoren)

**Kausalstruktur:**
- Primary Key Factor = bevorzugt Start-Node (oder justifizieren falls nicht)
- Success Factors = bevorzugt End-Nodes (oder justifizieren falls nicht)
- Mindestens ein gerichteter Pfad vom Primary Key Factor zu mindestens einem Success Factor
- Maximale Pfadlänge (primär): 4 gerichtete Verbindungen
- Alle Faktoren integriert: Keine isolierten Faktoren
- **Rückkopplungen (NEW)**: Erlaubt und erwünscht zwischen Einflussfaktoren, von Success zu Influencing, und zwischen Key zu Influencing (mit expliziter Erklärung)

**Quellenattribution:**
- >50% aller Verbindungen mit Literaturquellen [1], [2], etc.
- Dokumentation: Vollständige APA-Zitate in connection.attributes.description
- Erlaubte Evidenztypen: [E] (Erfahrung), [A] (Annahme), [O] (Untersuchung)
- Keine Verbindungen ohne Quellenattribution oder mit [?]

**Messbarkeit & Beeinflussbarkeit (Skala: 0, 0.5, 1.0):**

**Messbarkeit:**
- 0 = Nicht direkt messbar (z.B. qualitative Befragung, subjektive Beobachtung ohne klare Metrik)
- 0.5 = Teilweise messbar (z.B. qualitative Daten mit Indikatoren oder Skalen)
- 1 = Direkt messbar (z.B. Kennzahlen, Anzahl, Zeitmessungen, definierte Metriken)

**Beeinflussbarkeit:**
- 0 = Schwer beeinflussbar (externe Faktoren, Randbedingungen)
- 0.5 = Teilweise beeinflussbar (nur über mittlebare Faktoren)
- 1 = Direkt beeinflussbar (konkrete Maßnahmen, Regeln, Tools)

**Anforderungen:**
- Schlüsselfaktoren: measurability ≥ 0.5 (bevorzugt 1.0) und influenceability ≥ 0.5 (bevorzugt 1.0)
- Messbare Erfolgsfaktoren: measurability = 1.0
- Erfolgsfaktoren: measurability ≥ 0 (oft niedrig), influenceability typischerweise ≤ 0.5

**Faktoren-Formulierung:**
- Alle Faktoren in "attribute-of-element"-Formulierung (z. B. "Qualität des Verständnisses von agilen Events")

### 5. **Iterative DRM-Anwendung**
Stelle sicher, dass das Modell auf der DRM basiert:
- Modelliere die aktuelle Situation (Reference Model)
- Keine sofortigen Lösungsvorschläge
- Dokumentiere explizit, welche Annahmen getroffen wurden

### 6. **Output-Format**
Generiere das Output als JSON-File im KUMU-kompatiblen Format mit Abschnitten für:
- elements – Alle Faktoren mit _id, Attributen (Name, Type, Beschreibung, Messbarkeit, Influenceability)
- connections – Alle gerichteten Verbindungen mit from, to, Polarität (++, +-, -+, --), Quellenattribution und Beschreibung

Dateiname: reference_model_[PROBLEM_AS_FILENAME].json
wobei [PROBLEM_AS_FILENAME] das Problemstatement mit Unterstrichen statt Leerzeichen ist (z. B. "Verständnis_fuer_die_agilen_Events_fehlt")

---

## Hinweise & Validierung

- **Datenquelle (KRITISCH):** Verwende NUR das Netzwerkdiagramm wirkmechanismen-main-model-blueprint.json als Quelle. Keine zusätzlichen externen Quellen ohne explizite Kennzeichnung [A].

- **Keine Extrapolationen:** Falls das Diagramm keine direkten Verbindungen für das Problem enthält, kann eine minimale logische Erweiterung basierend auf agilen Prinzipien vorgenommen werden – markiere diese als Annahmen [A].

- **Rückkopplungen (NEW):** Identifiziere und dokumentiere Rückkopplungen zwischen Einflussfaktoren, von Erfolgsfaktoren zurück zu Einflussfaktoren, und dynamische Verstärkereffekte. Das Modell sollte die dynamische Natur des Systems abbilden, nicht nur lineare Kausalketten.

- **Erklärung des Modells:** Gib eine kurze Zusammenfassung des abgeleiteten Models aus.

- **Validierung:** Stelle sicher, dass das Modell JSON-Schema-konform, topologisch korrekt, pfadvollständig, alle Faktoren integriert und quellenattributions-korrekt dokumentiert ist.

---


