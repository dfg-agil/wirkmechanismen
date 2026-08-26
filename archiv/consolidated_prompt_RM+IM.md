Du hast Zugriff auf folgende Dateien:

1) Main Model (KUMU JSON): wirkmechanismen-main-model-blueprint.json
2) Reference Model Kriterien: REFERENCE_MODEL_CRITERIA_V3.md
3) Impact Model Kriterien: IMPACT_MODEL_CRITERIA.md

Du arbeitest nach der Design Research Methodology (DRM) von Blessing & Chakrabarti, insbesondere Reference Model und Impact Model (Kap. 2.4–2.6).

---

Problemstellung:
[PROBLEM_PLACEHOLDER]

---

Ziel:
Erzeuge in einem Durchlauf zwei Modelle:

1) Reference Model (Ist-Zustand) für das oben genannte Problem — abgeleitet NUR aus dem Main Model (wirkmechanismen-main-model-blueprint.json) unter Einhaltung von REFERENCE_MODEL_CRITERIA_V3.md.
2) Impact Model (Soll-Zustand) — abgeleitet aus dem gerade erzeugten Reference Model unter Einhaltung von IMPACT_MODEL_CRITERIA.md (Supports/Interventionen hinzufügen).

---

Gemeinsame Grundregeln (für beide Modelle):
- Output muss KUMU-kompatibles JSON sein mit Top-Level Feldern: elements, connections
- Verbindungen sind immer "direction": "directed"
- Jede Verbindung enthält:
  - attributes.connection type mit DRM-Polarität: ++, +-, -+, --
  - attributes.label als Evidenzmarker ([1], [2]… oder [A], [E], [O])
  - attributes.description (Mechanismus; Kriterien-konform)
- Keine Verbindungen ohne Quellenattribution
- Keine [?] Quellen erlaubt
- Faktorenformulierung: attribute-of-element (z.B. „Qualität der …“, „Grad der …“, „Anzahl der …“)

---

WICHTIG (MANDATORY): Problem NICHT als Element modellieren
- Das Problem aus [PROBLEM_PLACEHOLDER] dient ausschließlich als Scope / Filterkriterium.
- Es darf kein Element mit "element type": "Problem" erzeugt werden.
- Stattdessen muss das Problem implizit über Key Factor(s), Influencing Factors und Success Factor(s) abgebildet werden.

---

Teil A — Reference Model erstellen (Ist-Zustand)

A1) Analyse des Main Models
- Analysiere wirkmechanismen-main-model-blueprint.json, um relevante Elemente/Verbindungen/Schleifen zum Problem zu identifizieren.
- Konzentriere dich auf:
  - Schlüsselfaktoren ("Schlüsselfaktor")
  - Einflussfaktoren ("Einflussfaktoren")
  - Erfolgsfaktoren / messbare Erfolgsfaktoren (inkl. "Messbarer Erfolgsfaktor")
  - Metriken/Unsicherheiten/Team-Dynamik/Event-bezogene Faktoren, sofern relevant

A2) Ableitung & Selektion (Reference Model Kriterien zwingend einhalten)
- Leite ein fokussiertes Reference Model ab, das die Problemmechanik erklärt und die Kriterien aus REFERENCE_MODEL_CRITERIA_V3.md erfüllt.

Taxonomie (MANDATORY):
- Mindestens 1 Key Factor, genau 1 davon ist Primary:
  - "element type": "Schlüsselfaktor"
  - Primary Key Factor muss im attributes.description mit [PRIMARY] beginnen
  - Optionale Secondary Key Factors beginnen mit [SECONDARY]
- Mindestens 1 Success Factor:
  - "element type": "Erfolgsfaktor"
- Proxy-Regel:
  - Wenn ein Success Factor nicht hoch messbar ist (measurability < 0.8), füge einen Proxy hinzu:
    - "element type": "Messbarer Erfolgsfaktor"
    - measurability = 1.0
    - Proxy-Bezug muss in attributes.description erklärt sein (schema-neutral)
- Alle übrigen Elemente:
  - "element type": "Einflussfaktoren"
- Keine isolierten Faktoren

Kausalstruktur / Topologie (MANDATORY):
- Primärer Fluss: Key Factor(s) → Einflussfaktoren → (Measurable Success Factor(s)) → Success Factor(s)
- Mindestens ein Pfad: Primary Key Factor → Success Factor
- Max. Pfadlänge: 4 gerichtete Verbindungen (Key → … → Success) für primäre Ketten
- Feedback-Loops sind erlaubt (zwischen Einflussfaktoren, Success→Influencing, Key↔Influencing), aber:
  - müssen explizit in connection.attributes.description begründet sein (Mechanismus + Zeithorizont)

Quellenattribution (MANDATORY):
- Ziel: >50% Literatur
- WICHTIGER KONFLIKT-HINWEIS: Du darfst als Datenquelle nur das Main Model nutzen.
  - Wenn im Main Model bereits Literatur in Beschreibungen steht, übernimm sie als Literaturquelle ([1], [2], …) mit vollständigem APA-Zitat in der Connection-Description.
  - Wenn keine Literatur vorhanden ist, markiere neue/übernommene Beziehungen als [A] oder [E] (aber niemals [?]).
- Keine Quellenlosigkeit: Jede Verbindung braucht attributes.label und eine sinnvolle description.

Messbarkeit/Einflussbarkeit (DISKRET):
- Nutze ausschließlich Werte: 0, 0.5, 1.0
- Key Factors:
  - measurability ≥ 0.5 und influenceability ≥ 0.5
- Measurable Success Factors:
  - measurability = 1.0
- Success Factors:
  - measurability ≥ 0 (oft niedrig)
  - influenceability typischerweise ≤ 0.5
- Messmethode und mögliche Metriken müssen in attributes.description dokumentiert werden.

A3) Output Reference Model (MANDATORY)
- Erzeuge ein JSON nur für das Reference Model.

Dateiname-Regel (deterministisch):
- Erzeuge PROBLEM_AS_FILENAME, indem du:
  - den Problemtext nimmst
  - Umlaute normalisierst (ä→ae, ö→oe, ü→ue, ß→ss)
  - Sonderzeichen entfernst
  - Leerzeichen durch _ ersetzt
- Dateiname:
  - reference_model_<PROBLEM_AS_FILENAME>.json

---

Teil B — Impact Model erstellen (Soll-Zustand)

B1) Input
- Nutze als Grundlage ausschließlich das von dir erzeugte Reference Model (Teil A).

B2) Supports hinzufügen (MANDATORY)
- Gemäß IMPACT_MODEL_CRITERIA.md:
  - Füge 2–4 Support-Elemente hinzu:
    - "element type": "Support"
    - konkret/implementierbar (Tool/Guide/Practice), keine abstrakten Ziele
  - Supports sind Start-Nodes (keine eingehenden Verbindungen)
  - Jeder Support muss mindestens einen Key Factor beeinflussen

B3) Success Factor Invariance (MANDATORY)
- Success Factor(s) (und ggf. Measurable Success Factor Proxies) bleiben identisch zum Reference Model:
  - gleiche Labels/Definitionen/Attribute

B4) Kausale Erweiterung / Veränderungen (MANDATORY)
- Bestehende Verbindungen aus dem Reference Model bleiben bestehen (unverändert) oder werden geändert:
  - Wenn geändert/neu:
    - kennzeichne diese Verbindung als [A]
    - erkläre Mechanismus + Annahmen + kurzer Validierungsplan in attributes.description
- Alle neuen Support-bezogenen Verbindungen:
  - müssen [A] sein
  - 30–200 Wörter Erklärung enthalten
- Mindestens ein vollständiger Pfad:
  - Support → … → Success Factor
- Max. Pfadlänge:
  - 5 Verbindungen (Support + 4 weitere Schritte)

B5) Support Attribute (DISKRET / konsistent)
- Supports:
  - influenceability hoch (typisch 1.0)
  - measurability eher 0.5 oder 1.0 über Implementierungsgrad (z.B. Nutzungsrate)
- Success Factor Werte bleiben unverändert zum Reference Model

B6) Output Impact Model (MANDATORY)
- Erzeuge ein JSON nur für das Impact Model.

Dateiname:
- impact_model_<PROBLEM_AS_FILENAME>.json

---

OUTPUT FORMAT (ABSOLUT KRITISCH): Erzeuge zwei echte JSON-Dateien (download-ready)
- Du MUSST exakt zwei separate, download-fähige JSON-Dateien erzeugen.
- Gib jede Datei als eigenen Datei-Block aus, der direkt als Datei gespeichert werden kann.
- Die Datei-Blöcke müssen:
  - den exakten Dateinamen tragen
  - ausschließlich gültiges JSON enthalten (keine Kommentare, kein Fließtext)
  - die vollständige Datei enthalten (nicht fragmentiert)

Dateinamen exakt:
1) reference_model_<PROBLEM_AS_FILENAME>.json
2) impact_model_<PROBLEM_AS_FILENAME>.json

Reihenfolge (MANDATORY):
1) Zuerst die Datei: reference_model_<PROBLEM_AS_FILENAME>.json
2) Danach die Datei: impact_model_<PROBLEM_AS_FILENAME>.json
3) Danach (außerhalb der Dateien) eine sehr kurze Erklärung (max. ~10 Sätze)

WICHTIG:
- Keine Markdown-Erklärungen innerhalb der Datei-Blöcke.
- Keine zusätzlichen Code-/Datei-Blöcke außer diesen beiden JSON-Dateien.
- Nach den zwei Dateien darfst du normalen Text ausgeben (die kurze Erklärung).

---

Kurze Erklärung (nach den Dateien):
- Primary Key Factor
- Success Factor(s) + ggf. Proxy
- kurzer Hauptpfad (Ist)
- Supports (Soll) + erwartete Wirkungen

Generate the two models as json files (ready to download)
