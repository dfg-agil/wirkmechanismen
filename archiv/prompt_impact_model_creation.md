# Prompt: Impact Model Erstellung fuer validierte Reference Models

## Verbindliche Grundlage

Verwende als normative Kriterien ausschliesslich `IMPACT_MODEL_CRITERIA_V3.md`.
Die Anforderungen dieses Prompts duerfen an keiner Stelle von V3 abweichen. Wenn
eine Anforderung unklar ist, gilt V3; erfinde keine eigene Regel.

Verwende folgende Dokumente:

- ein validiertes Reference Model als verbindliche Ausgangsbasis
- `IMPACT_MODEL_CRITERIA_V3.md` als verbindliche Kriterienliste
- `models/main_model/wirkmechanismen-main-model-blueprint.json` zur Pruefung von
  Faktorherkunft und Main-Model-Beziehungen
- `general/prompt_instructions.md` fuer DRM- und KUMU-Kontext
- `general/Blessing_Chakrabarti_2009_DRM.pdf`, sofern verfuegbar, fuer den
  methodologischen Kontext
- konfigurierte validierte Support-Pakete, sofern im Projekt verfuegbar

## Eingabe

Reference Model:

`[REFERENCE_MODEL_PATH]`

Problemstellung:

`[PROBLEM_PLACEHOLDER]`

Optionaler Support-Paketpfad:

`[SUPPORT_PACKAGE_PATH]`

Das Reference Model muss validiert sein. Wenn es nicht validiert, nicht verfuegbar
oder nicht eindeutig identifizierbar ist, darf kein abgeschlossenes Impact Model
erzeugt werden. Dokumentiere den Status als `draft_only` und benenne die fehlende
Voraussetzung.

Problemstellung, Domain-Scope, Problemfaktoren und Success Factors muessen aus dem
Reference Model unveraendert uebernommen werden. Wenn die Eingabe davon abweicht,
stoppe die Erstellung und dokumentiere den Konflikt.

## Ziel

Erzeuge ein Impact Model fuer den gewuenschten Zustand nach Einfuehrung konkreter
Support-Interventionen. Das Impact Model wird aus dem validierten Reference Model
abgeleitet und macht explizit, wie Support die Key Factors beeinflussen soll.

Das Impact Model muss:

- mindestens ein konkretes Support-Element enthalten
- alle Key Factors aus dem Reference Model uebernehmen
- alle Success Factors aus dem Reference Model unveraendert uebernehmen
- alle Measurable Success Factors aus dem Reference Model uebernehmen
- alle Influence Factors aus dem Reference Model uebernehmen
- neue oder geaenderte Beziehungen nachvollziehbar dokumentieren
- mindestens einen vollstaendigen Pfad `Support -> Key Factor -> ... -> Success Factor`
  enthalten
- keine Support-Elemente als abstrakte Ziele oder gewuenschte Zustaende formulieren

Support-Elemente sind konkrete Massnahmen, Werkzeuge, Prozesse oder Hilfsmittel,
zum Beispiel `Daily Moderation Guide`, `Visual Board` oder `Timeboxing Timer`.

## Unveraenderliche RM-Bestandteile

Uebernimm aus dem validierten Reference Model:

- alle Key Factors, einschliesslich `[PRIMARY]` und `[SECONDARY]`-Kennzeichnungen
- alle Success Factors und deren Definitionen
- alle Measurable Success Factors und deren Proxy-Rationale
- alle vorhandenen Influencing Factors
- alle unveraenderten RM-Verbindungen einschliesslich Quellenattribution,
  Polaritaet, Richtung und Beschreibung
- Problemstellung und Domain-Scope

Geerbte Knoten und Verbindungen duerfen nur geaendert oder entfernt werden, wenn
dies durch einen konkreten Support-Mechanismus erforderlich ist. Jede solche
Aenderung muss im IM-Aenderungslog mit Begruendung dokumentiert werden.
Geerbte Feedbackschleifen duerfen erhalten bleiben, wenn sie unveraendert und
kausal gueltig sind. Eine gueltige geerbte RM-Dynamik darf nicht nur zur Erfuellung
einer vereinfachten Endknotenpruefung geloescht werden.

## Support-Quellenpolitik

Waehle Support primaer aus verfuegbaren validierten Support-Paketen. Wenn kein
Support-Paket konfiguriert, verfuegbar oder passend zum RM-Scope ist, darf ein
`AI-generated support` als Fallback formuliert werden.

AI-generierter Support muss ausdruecklich als `AI-generated support` markiert sein
und mindestens enthalten:

- konkrete Ziel-Key-Factor(s)
- konkreten kausalen Mechanismus
- messbaren Implementierungsgrad mit Wert `0`, `0.5` oder `1.0`
- Validierungsplan

Dokumentiere im Ableitungslog immer, ob der Paketpfad oder der Fallbackpfad
verwendet wurde. Erfinde keine Support-Pakete und stelle keine abstrakten Ziele als
Support dar.

## Verbindlicher Ablauf

### 1. Reference Model einfrieren

Pruefe und dokumentiere, dass das Reference Model validiert ist. Erstelle eine
Liste aller geerbten Knoten und Verbindungen. Markiere fuer jede spaetere
Aenderung, ob sie geerbt, neu, geaendert oder entfernt ist.

### 2. Support-Kandidaten extrahieren

Leite Support-Kandidaten aus kontrollierbaren Ansatzpunkten ab, die direkt auf
folgende Faktoren zielen:

1. zuerst auf den Primary Key Factor
2. danach auf First-Hop-Influencing-Factors auf gueltigen RM-Key-to-Success-Pfaden

Supports, die lediglich Outcomes, Zielzustaende oder Faktoren umformulieren,
sind unzulaessig.

### 3. Support-Kandidaten bewerten

Bewerte jeden Support-Kandidaten deterministisch:

- `+3`, wenn das Team ihn direkt umsetzen kann
- `+2`, wenn der Mechanismus zum Zielfaktor konkret und falsifizierbar ist
- `+2`, wenn der Implementierungsgrad mit einer diskreten Metrik messbar ist
- `-2`, wenn er primaer von externen Akteuren abhaengt
- `-2`, wenn er ohne eigenen Mechanismus einen bereits gewaehlten Support dupliziert

Verwende fuer die Einzelwerte die V3-Interpretation:

- direkte Umsetzbarkeit: `1.0` direkt durch das Team, `0.5` teilweise extern,
  `0.0` primaer extern
- Mechanismusspezifitaet: `1.0` mit Aktion, Zielfaktor und Richtung, `0.5` bei
  fehlender Komponente, `0.0` bei abstrakter oder zielartiger Formulierung
- messbarer Implementierungsgrad: `1.0` bei konkreter binarer oder numerischer
  Metrik, `0.5` bei nur qualitativer Metrik, `0.0` ohne Metrik

Waehle die besten ein bis drei Supports. Bei einer Differenz von hoechstens `0.01`
beim Gesamtscore verwende diese Tie-Breaker in exakter Reihenfolge:

1. hoeheres Mechanismusniveau mit klarem Aktionsverb und Zielfaktor
2. kuerzere durchschnittliche Pfadlaenge zu den Success Factors
3. hoeheres `influenceability` der Ziel-Key-Factors
4. alphabetische Bezeichnung

Dokumentiere alle Bewertungswerte, Gesamtscores, Tie-Breaks und die Auswahl im
IM-Ableitungslog.

### 4. Neue Influencing Factors

Die Standardregel lautet: Fuege keine neuen Faktoren hinzu.

Ein neuer support-getriebener Influencing Factor ist nur zulaessig, wenn alle
folgenden Bedingungen erfuellt sind:

- kausale Verbindung zu mindestens einem Support
- kausale Verbindung zu mindestens einem geerbten RM-Faktor
- Kennzeichnung der neuen Beziehung als `[A]`
- Mechanismus in `attributes.description` dokumentiert
- Messmethode in `attributes.description` dokumentiert
- Validierungsplan in `attributes.description` dokumentiert

Fehlt eine Bedingung, ist der neue Faktor unzulaessig und darf nicht aufgenommen
werden. Neue Key Factors oder neue Success Factors sind nicht zulaessig.

### 5. Neue und geaenderte Verbindungen

Jede durch Support verursachte neue oder geaenderte Verbindung muss:

- mit `[A]` als Annahme markiert werden, bis sie validiert ist
- den kausalen Mechanismus erklaeren
- die erwartete Richtungsveraenderung nennen
- einen Validierungsplan enthalten
- bei einer geaenderten RM-Verbindung die Abweichung vom RM erklaeren

Eine bestehende Verbindung kann entweder entfernt und durch eine neue `[A]`-
Verbindung ersetzt werden oder in Staerke/Polaritaet geaendert werden. In beiden
Faellen ist die Aenderung im Aenderungslog zu dokumentieren.

Nach erfolgreichem Piloting darf `[A]` durch `[O]` ersetzt werden. Bei publizierter
Literaturevidenz darf `[A]` durch `[1-9]+` ersetzt werden. Der Validierungsprozess
muss dokumentiert werden.

### 6. Kausalstruktur

- Jede Verbindung ist gerichtet und enthaelt `"direction": "directed"`.
- Jede Verbindung verwendet genau eine DRM-Polaritaet: `++`, `+-`, `-+` oder `--`.
- Jedes Support-Element ist ein Startknoten ohne eingehende Verbindungen.
- Jedes Support-Element beeinflusst mindestens einen Key Factor.
- Jeder Key Factor aus dem RM bleibt erhalten und ist an mindestens einen Support
  oder den geerbten Wirkpfad angebunden.
- Es gibt mindestens einen vollstaendigen Pfad von jedem ausgewaehlten Support zu
  mindestens einem Success Factor.
- Die maximale Pfadlaenge eines Support-to-Success-Pfades betraegt fuenf Kanten,
  also Support plus hoechstens vier weitere Schritte.
- Das Success-Factor-Ziel bleibt gegenueber dem RM unveraendert.
- Geerbte RM-Schleifen duerfen bleiben, wenn sie unveraendert und kausal gueltig
  sind. Neue oder geaenderte Schleifen brauchen `[A]`, Mechanismus und
  Validierungsplan.

Waehle Polaritaeten fuer den gewuenschten Post-Interventionskontext. Kopiere
Main-Model- oder RM-Polaritaeten nicht mechanisch. Wenn eine geerbte Polaritaet
im gewuenschten Kontext nicht passt, dokumentiere die begruendete Aenderung.
Support-to-Key-Factor-Verbindungen sind typischerweise `++`, sofern die Evidenz
keine andere Richtung verlangt.

### 7. Messbarkeit und Beeinflussbarkeit

Supports muessen eine hohe Beeinflussbarkeit von `1.0` anstreben und einen
messbaren Implementierungsgrad mit `0`, `0.5` oder `1.0` besitzen. Dokumentiere
die konkrete Messmethode, zum Beispiel `Board vorhanden: ja/nein` oder
`Nutzungsrate des Guides`.

Messbarkeit und Beeinflussbarkeit geerbter Key Factors bleiben unveraendert,
sofern keine V3-konforme Support-Begruendung eine Erhoehung der
Beeinflussbarkeit rechtfertigt. Messbarkeit und Beeinflussbarkeit der Success
Factors bleiben unveraendert.

## Quellenattribution und Beschreibungen

- Unveraenderte RM-Verbindungen behalten exakt ihre Quellenattribution.
- Alle neuen Support-Verbindungen werden mit `[A]` gekennzeichnet.
- `[?]` und Verbindungen ohne Quellenattribution sind unzulaessig.
- Jede neue oder geaenderte Verbindung besitzt eine Beschreibung mit kausalem
  Mechanismus und theoretischer, empirischer oder analogischer Begruendung.
- Support-Verbindungen verwenden das Muster: `Support X improves Factor Y through
  Mechanism Z` und umfassen 30 bis 200 Woerter.
- Jede `[A]`-Verbindung enthaelt ausserdem erwartete Richtungsveraenderung und
  Validierungsplan.

## Metriken, Logs und Pfaderhaltung

Das IM-Ableitungslog muss enthalten:

- Validierungsnachweis und Scope des Reference Models
- vollstaendige Liste geerbter Knoten und Verbindungen
- Support-Quellenpfad: Paket oder `AI-generated support`-Fallback
- alle Support-Kandidaten mit Einzelwerten, Gesamtscores und Auswahlstatus
- vollstaendige Tie-Break-Entscheidungen mit Toleranz `0.01`
- Support-to-Key-to-Success-Pfade und deren Laengen
- Liste aller neuen, geaenderten und entfernten Verbindungen mit Begruendung
- Liste aller neuen Influencing Factors mit allen Ausnahmebedingungen
- Messmethode und Implementierungsgrad jedes Supports
- Validierungsplan fuer jede `[A]`-Verbindung
- Support-Distinctness-Check: Das Entfernen jedes Supports muss mindestens einen
  intendierten Verbesserungspfad reduzieren
- Minimaler Pfaderhaltungstest nach dem Einfuegen und Aendern von Supports

## Ausgabeformat

Erzeuge ein KUMU-kompatibles JSON mit mindestens diesen Abschnitten:

```json
{
  "elements": [],
  "connections": [],
  "derivation_log": {}
}
```

`elements` enthalten mindestens `_id` und `attributes` mit `label`,
`element type` und `description`. Verwende folgende Elementtypen:

- `Support` fuer konkrete Interventionen
- `Schluesselfaktor` fuer geerbte Key Factors
- `Erfolgsfaktor` fuer geerbte Success Factors
- `Messbarer Erfolgsfaktor` fuer geerbte Measurable Success Factors
- `Einflussfaktoren` fuer geerbte oder regelkonform neue Influencing Factors

Support-Elemente muessen in ihrer Beschreibung Quelle, Ziel-Key-Factor,
Mechanismus, Implementierungsmetrik und Validierungsplan nennen. Alle IDs muessen
eindeutig sein.

`connections` enthalten mindestens `_id`, `from`, `to`, `direction` und
`attributes` mit `label`, `connection type` und `description`. Alle `from`- und
`to`-Referenzen muessen auf vorhandene Element-IDs zeigen.

Der Dateiname lautet:

`[IMPACT_MODEL_OUTPUT_PATH]`

## Validierung vor der Ausgabe

Pruefe vor der Ausgabe alle folgenden Punkte:

- validiertes Reference Model als Grundlage bestaetigt
- identischer Domain-Scope sowie identische Problem- und Success-Factor-Definition
- mindestens ein Support-Element vorhanden
- jeder Support ist konkret, implementierbar und ein Startknoten
- jeder Support beeinflusst mindestens einen Key Factor
- alle Key Factors aus dem RM uebernommen
- alle Success Factors aus dem RM unveraendert uebernommen
- alle Measurable Success Factors und RM-Influencing-Factors uebernommen
- mindestens ein vollstaendiger Support-to-Success-Pfad vorhanden
- maximale Pfadlaenge von fuenf Kanten eingehalten
- alle neuen und geaenderten Support-Kanten mit `[A]` markiert
- jede `[A]`-Kante enthaelt Mechanismus, Richtungserwartung und Validierungsplan
- keine unzulaessigen neuen Faktoren
- alle neuen Faktoren erfuellen die vollstaendige Ausnahmebedingung
- geerbte unveraenderte Kanten besitzen unveraenderte Quellenattribution
- keine `[?]`-Quellen und keine unbelegten Verbindungen
- alle Verbindungen gerichtet und mit gueltiger DRM-Polaritaet
- Polaritaeten entsprechen dem gewuenschten Kontext oder sind begruendet angepasst
- Supports besitzen messbaren Implementierungsgrad
- Success-Factor-Metriken bleiben unveraendert
- Support-Distinctness-Check bestanden
- Minimaler Pfaderhaltungstest dokumentiert
- Support-Scoring, Tie-Breaks und Aenderungslog reproduzierbar dokumentiert
- JSON-Syntax, ID-Eindeutigkeit und Referenzintegritaet geprueft

Berechne ausserdem diese Qualitaetswerte:

- Support Coverage: 100 Prozent der Key Factors durch mindestens einen Support
  adressiert
- Assumption Documentation: 100 Prozent der `[A]`-Kanten begruendet
- Validation Planning: mindestens 75 Prozent der Annahmen mit dokumentiertem
  Validierungsplan, wobei jede Support-getriebene `[A]`-Kante einen Plan benoetigt
- Topological Integrity: 100 Prozent fuer Support-Startknoten und neue
  Support-to-Success-Pfade
- Path Completeness: 100 Prozent fuer mindestens einen vollstaendigen Pfad je
  Support
- Deterministic Traceability: 100 Prozent fuer Support-Scoring, Tie-Breaks und
  Aenderungslog

Wenn ein Kriterium nicht erfuellt werden kann, gib kein abgeschlossenes Impact
Model aus. Dokumentiere stattdessen die konkrete Verletzung und den Status
`draft_only`.

## Validierungs- und Integrationsworkflow

1. Initiales Impact Model mit `[A]`-Annahmen erstellen
2. Menschliche und Peer-Pruefung der Plausibilitaet
3. Pilotierung mit kleiner Testgruppe
4. Validierte Annahmen von `[A]` nach `[O]` aktualisieren
5. Bei publizierter Evidenz gegebenenfalls von `[A]` nach `[1-9]+` aktualisieren
6. Validierte Support-Beziehungen in das Main Model integrieren

Verwende fuer Commits die V3-Konventionen:

- `[IMPACT] Add {domain} impact model with {N} support interventions`
- `[IMPACT] Validate assumption [A] -> [O] for {connection} based on {pilot/study}`
- `[IMPACT] Refine support {name} based on pilot results`
- `[IMPACT] Promote validated {domain} model to production`
