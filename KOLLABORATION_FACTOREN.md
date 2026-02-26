# Neue Faktoren: Grad & Effektivität der Kollaboration

## Element 1: Grad der Kollaboration
```json
{
  "_id": "elem-gradKollaboration",
  "attributes": {
    "label": "Grad der Kollaboration",
    "element type": "Schlüsselfaktor",
    "tags": ["Teamdynamik", "Zusammenarbeit", "Kollaboration"],
    "description": "Ausmaß, in dem Arbeit gemeinsam und ko-kreativ statt nur arbeitsteilig/kooperativ erfolgt. Unterscheidung zwischen echter Kollaboration (gemeinsame Artefakt-Erstellung, gemeinsame Entscheidungen) und reiner Kooperation (parallel, mit Handoff) bis hin zu 'Dienst nach Vorschrift' (minimale Abstimmung).",
    "measurability": 0.5,
    "influenceability": 0.5
  }
}
```

## Element 2: Effektivität der Kollaboration
```json
{
  "_id": "elem-effektivitaetKollaboration",
  "attributes": {
    "label": "Effektivität der Kollaboration",
    "element type": "Messbarer Erfolgsfaktor",
    "tags": ["Teamdynamik", "Zusammenarbeit", "Erfolg", "Messung"],
    "description": "Ergebniswirksamkeit der Zusammenarbeit im Team. Messbar über Reduktion von Rework durch Hand-offs, Schnelligkeit von Entscheidungsfindung, Koordinationseffzienz, Fehlerquoten bei gemeinsamen Aufgaben und Stakeholder-Zufriedenheit mit Collaboration-Prozessen.",
    "measurability": 1,
    "influenceability": 1
  }
}
```

## Connections
1. `elem-1oLVNA94` (Team Partizipation) → `elem-gradKollaboration` `[A], "++"`
2. `elem-kpdrF0zk` (Teamdynamik) → `elem-gradKollaboration` `[A], "++"`
3. `elem-gradKollaboration` → `elem-effektivitaetKollaboration` `[A], "++"`
4. `elem-gemeinsamVerstaendnis` (Gemeinsames Verständnis) → `elem-effektivitaetKollaboration` `[A], "++"`
