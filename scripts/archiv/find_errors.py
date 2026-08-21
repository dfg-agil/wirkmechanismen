import re

with open('models/main_model/wirkmechanismen-main-model-blueprint.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()

errors = []
for i in range(len(lines)-1):
    if '"description":' in lines[i] and '"description":' in lines[i+1] and not lines[i].rstrip().endswith(','):
        errors.append((i+1, i+2, lines[i].rstrip(), lines[i+1].rstrip()))

if errors:
    print(f'Gefunden: {len(errors)} Probleme mit doppelten description-Feldern')
    for line1, line2, curr, next_line in errors:
        print(f'  Zeile {line1}-{line2}:')
        print(f'    {curr}')
        print(f'    {next_line}')
else:
    print('Keine doppelten description-Probleme gefunden')
