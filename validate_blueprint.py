import json

# Load blueprint
with open("models/main_model/wirkmechanismen-main-model-blueprint.json", encoding="utf-8") as f:
    data = json.load(f)

elements = data.get("elements", [])
connections = data.get("connections", [])

print("=" * 60)
print("JSON BLUEPRINT VALIDIERUNG")
print("=" * 60)

# Check for duplicate element IDs
element_ids = [e["_id"] for e in elements]
duplicates = [id for id in element_ids if element_ids.count(id) > 1]
if duplicates:
    print("\n❌ DUPLIKAT ELEMENT IDs gefunden:")
    for dup in set(duplicates):
        print(f"  - {dup}: {element_ids.count(dup)}x")
else:
    print("\n✓ Keine duplizierten Element-IDs")

# Check for invalid connections
valid_ids = set(element_ids)
invalid_connections = []
for conn in connections:
    if conn.get("from") not in valid_ids or conn.get("to") not in valid_ids:
        invalid_connections.append({
            "_id": conn.get("_id"),
            "from": conn.get("from"),
            "to": conn.get("to"),
            "valid_from": conn.get("from") in valid_ids,
            "valid_to": conn.get("to") in valid_ids
        })

if invalid_connections:
    print(f"\n❌ Ungültige Verbindungen gefunden: {len(invalid_connections)}")
    for conn in invalid_connections[:20]:  # Show first 20
        from_status = "✓" if conn['valid_from'] else "✗"
        to_status = "✓" if conn['valid_to'] else "✗"
        print(f"  - {conn['_id']}")
        print(f"    from: {conn['from']} [{from_status}]")
        print(f"    to:   {conn['to']} [{to_status}]")
else:
    print("\n✓ Alle Verbindungen sind gültig")

# Check for duplicate connection IDs
connection_ids = [c["_id"] for c in connections]
dup_connections = [id for id in connection_ids if connection_ids.count(id) > 1]
if dup_connections:
    print(f"\n❌ Duplikat Verbindungs-IDs gefunden: {len(set(dup_connections))}")
    for dup in set(dup_connections):
        print(f"  - {dup}: {connection_ids.count(dup)}x")
else:
    print("\n✓ Keine duplizierten Verbindungs-IDs")

# Check for elements without required attributes
print("\n" + "=" * 60)
print("STRUKTURELLE PRÜFUNG (Pro Element)")
print("=" * 60)

required_attrs = ["label", "element type"]
missing_attrs = []
for elem in elements:
    for attr in required_attrs:
        if attr not in elem.get("attributes", {}):
            missing_attrs.append({
                "element": elem["_id"],
                "label": elem.get("attributes", {}).get("label", "N/A"),
                "missing_attr": attr
            })

if missing_attrs:
    print(f"\n⚠️  {len(missing_attrs)} Elemente mit fehlenden Attributen:")
    for item in missing_attrs[:10]:
        print(f"  - {item['element']} ({item['label']}): fehlt '{item['missing_attr']}'")
else:
    print("\n✓ Alle Elemente haben erforderliche Attribute")

print("\n" + "=" * 60)
print("ZUSAMMENFASSUNG")
print("=" * 60)
print(f"Elemente: {len(elements)}")
print(f"Verbindungen: {len(connections)}")
print(f"Fehler gefunden: {len(duplicates) + len(invalid_connections) + len(dup_connections)}")
print("=" * 60)
