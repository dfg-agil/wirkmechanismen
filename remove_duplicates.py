import json

# Load blueprint
with open('models/main_model/wirkmechanismen-main-model-blueprint.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

connections = data.get("connections", [])

print(f"Vor Bereinigung: {len(connections)} Verbindungen")

# Dedupliziere: Behalte die erste Instanz, entferne Duplikate
seen = {}
unique_connections = []

for conn in connections:
    conn_id = conn.get("_id")
    if conn_id not in seen:
        seen[conn_id] = True
        unique_connections.append(conn)
    else:
        print(f"Duplikat entfernt: {conn_id}")

data["connections"] = unique_connections

print(f"Nach Bereinigung: {len(unique_connections)} Verbindungen")
print(f"Removed: {len(connections) - len(unique_connections)} Duplikate")

# Save
with open('models/main_model/wirkmechanismen-main-model-blueprint.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nDatei aktualisiert!")
