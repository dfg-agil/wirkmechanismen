import json
import sys
from pathlib import Path
import unicodedata

repo = Path(__file__).resolve().parents[1]
excel = repo / 'scripts' / 'factors_measurability_proposals_RO_green.xlsx'
blueprint = repo / 'models' / 'main_model' / 'wirkmechanismen-main-model-blueprint.json'

if not excel.exists():
    print('MISSING_EXCEL')
    sys.exit(2)
if not blueprint.exists():
    print('MISSING_BLUEPRINT')
    sys.exit(2)

# simple xlsx reader using zip/xml
import zipfile
import xml.etree.ElementTree as ET
z = zipfile.ZipFile(str(excel))
shared = []
if 'xl/sharedStrings.xml' in z.namelist():
    with z.open('xl/sharedStrings.xml') as fh:
        tree = ET.parse(fh)
        root = tree.getroot()
        for si in root.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si'):
            texts = []
            for t in si.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t'):
                texts.append(t.text or '')
            shared.append(''.join(texts))

candidates = [n for n in z.namelist() if n.startswith('xl/worksheets/sheet') and n.endswith('.xml')]
if not candidates:
    print('NO_SHEET')
    sys.exit(3)
sheet = sorted(candidates)[0]
with z.open(sheet) as fh:
    tree = ET.parse(fh)
    root = tree.getroot()
    ns = {'d': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    rows = []
    for row in root.findall('.//d:sheetData/d:row', ns):
        cells = {}
        max_col = 0
        for c in row.findall('d:c', ns):
            ref = c.get('r')
            col = ''.join([ch for ch in ref if ch.isalpha()])
            idx = 0
            for ch in col:
                idx = idx * 26 + (ord(ch.upper()) - ord('A') + 1)
            if idx > max_col:
                max_col = idx
            cell_type = c.get('t')
            v = c.find('d:v', ns)
            value = ''
            if v is not None and v.text is not None:
                if cell_type == 's':
                    try:
                        si = int(v.text)
                        value = shared[si] if si < len(shared) else ''
                    except Exception:
                        value = v.text
                else:
                    value = v.text
            else:
                is_node = c.find('d:is', ns)
                if is_node is not None:
                    t = is_node.find('.//d:t', ns)
                    if t is not None and t.text:
                        value = t.text
            cells[idx - 1] = value
        row_list = [cells.get(i, '') for i in range(max_col)]
        rows.append(row_list)

# Expect header in first row, columns label;measurability;influenceability or similar
headers = [h.strip() for h in rows[0]] if rows else []
# find indices
def find_col(name):
    name = name.lower()
    for i,h in enumerate(headers):
        if h and name in h.lower():
            return i
    return None

col_label = find_col('label')
col_meas = find_col('measurability')
col_infl = find_col('influenceability')
if col_label is None or col_meas is None or col_infl is None:
    print('COLUMNS_NOT_FOUND', headers)
    sys.exit(4)

entries = []
for r in rows[1:]:
    label = r[col_label].strip() if col_label < len(r) else ''
    meas = r[col_meas].strip() if col_meas < len(r) else ''
    infl = r[col_infl].strip() if col_infl < len(r) else ''
    if label:
        entries.append((label, meas, infl))

# load blueprint
with blueprint.open('r', encoding='utf-8') as fh:
    data = json.load(fh)

# build mapping from normalized label to element id
def normalize(s):
    s = s or ''
    s = s.strip().lower()
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    # remove non-alnum
    s = ''.join(ch for ch in s if ch.isalnum())
    return s

label_to_id = {}
for e in data.get('elements', []):
    attrs = e.get('attributes', {})
    lab = attrs.get('label', '')
    n = normalize(lab)
    if n:
        label_to_id[n] = e.get('_id')

updates = []
not_found = []
for label, meas, infl in entries:
    n = normalize(label)
    if n in label_to_id:
        eid = label_to_id[n]
        # find element
        elem = next((x for x in data['elements'] if x.get('_id') == eid), None)
        if elem is None:
            not_found.append(label)
            continue
        attrs = elem.get('attributes', {})
        cur_meas = attrs.get('measurability')
        cur_infl = attrs.get('influenceability')
        # convert meas/infl to float if possible
        try:
            new_meas = float(meas) if meas not in ('', None) else None
        except:
            new_meas = None
        try:
            new_infl = float(infl) if infl not in ('', None) else None
        except:
            new_infl = None
        change = {}
        if (cur_meas is None or cur_meas == '') and new_meas is not None:
            change['measurability'] = new_meas
        if (cur_infl is None or cur_infl == '') and new_infl is not None:
            change['influenceability'] = new_infl
        if change:
            updates.append({'_id': eid, 'label': label, **change})
    else:
        not_found.append(label)

# output results as JSON
print(json.dumps({'updates': updates, 'not_found': not_found}, ensure_ascii=False, indent=2))
