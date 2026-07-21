import json

with open('models/main_model/wirkmechanismen-main-model-blueprint.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

connections = data.get("connections", [])

# Finde Duplikate
connection_ids = {}
duplicates = {}

for conn in connections:
    conn_id = conn.get("_id")
    if conn_id in connection_ids:
        if conn_id not in duplicates:
            duplicates[conn_id] = []
        duplicates[conn_id].append({
            "index": len(connection_ids[conn_id]),
            "from": conn.get("from"),
            "to": conn.get("to")
        })
    else:
        connection_ids[conn_id] = [conn]
        
    if conn_id in connection_ids and len(connection_ids[conn_id]) < len([c for c in connections if c.get("_id") == conn_id]):
        pass
    else:
        if conn_id not in connection_ids:
            connection_ids[conn_id] = []
        connection_ids[conn_id].append(conn)

# Neu zählen
dup_info = {}
for conn in connections:
    conn_id = conn.get("_id")
    if conn_id not in dup_info:
        dup_info[conn_id] = {"count": 0, "instances": []}
    dup_info[conn_id]["count"] += 1
    dup_info[conn_id]["instances"].append({
        "from": conn.get("from"),
        "to": conn.get("to")
    })

duplicates = {k: v for k, v in dup_info.items() if v["count"] > 1}

print("Duplikat-Verbindungen:")
for dup_id, info in duplicates.items():
    print(f"\n{dup_id} ({info['count']}x):")
    for i, inst in enumerate(info["instances"]):
        print(f"  [{i}] {inst['from']} -> {inst['to']}")
