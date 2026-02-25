import json
import re

# Versuche, die Fehler per Regex zu finden
with open('models/main_model/wirkmechanismen-main-model-blueprint.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Finde alle Stellen mit fehlenden Kommas
# Pattern: "...text"  "fieldname" (kein Komma zwischen Wert und nächstem Field)
pattern = r':\s*"([^"]*[^\\])"\s+["\[]'

matches = list(re.finditer(pattern, content))
print(f"Gefundene potenzielle Fehler: {len(matches)}")

# Auch per Zeile überprüfen
with open('models/main_model/wirkmechanismen-main-model-blueprint.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()

problematic_lines = []
for i in range(len(lines)-1):
    line = lines[i]
    next_line = lines[i+1]
    # Suche nach Mustern wie: "text"  gefolgt direkt von "fieldname":
    if re.search(r'"\s*$', line) and re.search(r'^\s*"[a-z]', next_line) and ':' in next_line:
        if not line.rstrip().endswith(','):
            problematic_lines.append((i+1, line.rstrip(), next_line.rstrip()))

if problematic_lines:
    print(f"\nProblematische Zeilen (fehlende Kommas): {len(problematic_lines)}")
    for line_num, curr, next_line in problematic_lines[:15]:
        print(f"  Zeile {line_num}: {curr[:80]}")
        print(f"             {next_line[:80]}")
