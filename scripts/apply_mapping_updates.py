import json
from pathlib import Path
repo = Path(__file__).resolve().parents[1]
mapping_path = repo / 'mapping_result.json'
blueprint_path = repo / 'models' / 'main_model' / 'wirkmechanismen-main-model-blueprint.json'
if not mapping_path.exists():
    print('MAPPING_MISSING'); raise SystemExit(2)
if not blueprint_path.exists():
    print('BLUEPRINT_MISSING'); raise SystemExit(2)
with mapping_path.open('r', encoding='utf-8', errors='replace') as fh:
    mapping = json.load(fh)
with blueprint_path.open('r', encoding='utf-8') as fh:
    data = json.load(fh)
updates = mapping.get('updates', [])
applied = []
for upd in updates:
    eid = upd['_id']
    meas = upd.get('measurability')
    infl = upd.get('influenceability')
    for elem in data.get('elements', []):
        if elem.get('_id') == eid:
            attrs = elem.setdefault('attributes', {})
            cur_meas = attrs.get('measurability')
            cur_infl = attrs.get('influenceability')
            changed = False
            if (cur_meas is None or cur_meas == '') and meas is not None:
                attrs['measurability'] = meas
                changed = True
            if (cur_infl is None or cur_infl == '') and infl is not None:
                attrs['influenceability'] = infl
                changed = True
            if changed:
                applied.append({'_id': eid, 'measurability': attrs.get('measurability'), 'influenceability': attrs.get('influenceability')})
            break

if not applied:
    print('NO_UPDATES_APPLIED')
else:
    # write back
    with blueprint_path.open('w', encoding='utf-8') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print('APPLIED', json.dumps(applied, ensure_ascii=False))
