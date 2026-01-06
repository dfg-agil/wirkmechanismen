import json
from pathlib import Path
repo = Path(__file__).resolve().parents[1]
blueprint_path = repo / 'models' / 'main_model' / 'wirkmechanismen-main-model-blueprint.json'
mapping_path = repo / 'mapping_result.json'
if not mapping_path.exists():
    print('MAPPING_MISSING')
    raise SystemExit(2)
with mapping_path.open('r', encoding='utf-8', errors='replace') as fh:
    mapping = json.load(fh)
with blueprint_path.open('r', encoding='utf-8') as fh:
    lines = fh.readlines()

updates = mapping.get('updates', [])
patch_parts = []
for upd in updates:
    eid = upd['_id']
    meas = upd.get('measurability')
    infl = upd.get('influenceability')
    # find the block for this element by searching for the id line
    id_line = f'      "_id": "{eid}",\n'
    try:
        idx = lines.index(id_line)
    except ValueError:
        # fallback: search any line containing the id
        idx = None
        for i,l in enumerate(lines):
            if f'"_id": "{eid}"' in l:
                idx = i
                break
        if idx is None:
            print('ID_NOT_FOUND', eid)
            continue
    # we want to find the lines within the attributes block where micmac exposure and measurability occur
    # search forward from idx for the sequence '"micmac exposure"'
    mi = None
    for j in range(idx, idx+80):
        if j < len(lines) and '"micmac exposure"' in lines[j]:
            mi = j
            break
    if mi is None:
        print('MICMAC_NOT_FOUND', eid)
        continue
    # assume lines mi, mi+1, mi+2 correspond to micmac exposure, measurability, influenceability
    old_block = ''.join(lines[mi:mi+3])
    new_block = f'        "micmac exposure": 0,\n        "measurability": {meas if meas is not None else "null"},\n        "influenceability": {infl if infl is not None else "null"}\n'
    # context: include 3 lines before and after
    pre_ctx = ''.join(lines[max(0, mi-3):mi])
    post_ctx = lines[mi+3] if mi+3 < len(lines) else ''
    part = f"@@\n{pre_ctx}-{old_block}+{new_block}{post_ctx}\n"
    patch_parts.append(part)

# assemble full patch
patch = ['*** Begin Patch\n', f'*** Update File: {str(blueprint_path)}\n']
for p in patch_parts:
    patch.append(p)
patch.append('\n*** End Patch\n')
out = repo / 'generated_patch.txt'
with out.open('w', encoding='utf-8') as fh:
    fh.write(''.join(patch))
print('WROTE', out)
