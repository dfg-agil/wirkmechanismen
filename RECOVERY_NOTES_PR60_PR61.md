# Recovery Notes: PR #60 and PR #61

## PR #60 (Media Richness connections + JSON fixes)
- Added 8 Media Richness connections between existing factors (no new influence factors).
- Fixed malformed JSON structure in the main model (duplicate keys, missing attributes, orphaned connections).
- Cleaned/realigned descriptions for three connections to avoid mixed statements.

Key connection additions (by factor):
- Grad der Mehrdeutigkeit der Aufgabe → Strukturelle Medienreichhaltigkeit [E, ++]
- Grad der Mehrdeutigkeit der Aufgabe → Wahrgenommene Medienreichhaltigkeit [A, ++]
- Grad der Mehrdeutigkeit der Aufgabe → Klarheit der Aufgabenstellung [E, --]
- Grad der Mehrdeutigkeit der Aufgabe → Konvergenz des Teamverständnisses [E, --]
- Verfügbarkeit reichhaltiger Kommunikationsmedien → Strukturelle Medienreichhaltigkeit [A, ++]
- Verfügbarkeit reichhaltiger Kommunikationsmedien → Wahrgenommene Medienreichhaltigkeit [A, ++]
- Verfügbarkeit reichhaltiger Kommunikationsmedien → Qualität des Feedbacks [A, ++]
- Ambiguität der Prozessanforderungen → Grad der Mehrdeutigkeit der Aufgabe [A, ++]

Adjusted descriptions (structured):
- Komplexität der Kommunikationsaufgabe → Konvergenz des Teamverständnisses
- Grad des Wissensaustauschs → Koordinationsaufwand
- Qualität der Struktur und Zielorientierung → Grad der Unsicherheiten im PEP

## PR #61 (Gate criteria enforcement)
- Enforced chat/agent refusal for new factors without `measurability` and `influenceability`.
- Added connectivity rule: new factors require at least 1 incoming and 1 outgoing connection.
- Consolidated additions file to avoid duplicated criteria.

## Reference
- PR #60: https://github.com/dfg-agil/wirkmechanismen/pull/60
- PR #61: https://github.com/dfg-agil/wirkmechanismen/pull/61