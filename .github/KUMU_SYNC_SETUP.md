# KUMU Synchronisation via GitHub Actions

Diese Anleitung beschreibt die Einrichtung der automatischen Synchronisation zwischen GitHub und KUMU.

## 📋 Überblick

Wenn Sie Änderungen am Main Model Blueprint (`wirkmechanismen-main-model-blueprint.json`) zur `main` Branch pushen, wird automatisch ein GitHub Action ausgelöst, der:

1. ✅ Das Blueprint validiert
2. 📤 Es zu KUMU hochlädt
3. 📊 Status-Reports erstellt

## ⚙️ Konfigurationsschritte

### Schritt 1: KUMU API-Token beschaffen

1. Gehen Sie zu [kumu.io](https://kumu.io)
2. Melden Sie sich an und gehen Sie zu: **Account Settings** > **API**
3. Erstellen Sie einen neuen API Token
4. Kopieren Sie den Token (Sie werden ihn später brauchen)

### Schritt 2: GitHub Secrets konfigurieren

1. Gehen Sie zu Ihrem GitHub Repository: **wirkmechanismen**
2. Navigieren Sie zu: **Settings** > **Secrets and variables** > **Actions**
3. Klicken Sie auf **"New repository secret"**
4. Fügen Sie die folgenden Secrets hinzu:

#### Secret 1: `KUMU_API_KEY`
- **Name**: `KUMU_API_KEY`
- **Value**: Ihr KUMU API Token (aus Schritt 1)

#### Secret 2: `KUMU_ACCOUNT`
- **Name**: `KUMU_ACCOUNT`
- **Value**: Your KUMU account slug (z.B. `dfg-agil` aus `kumu.io/dfg-agil`)

#### Secret 3: `KUMU_PROJECT`
- **Name**: `KUMU_PROJECT`
- **Value**: Your KUMU project slug (z.B. `wirkmechanismen` aus `kumu.io/dfg-agil/wirkmechanismen`)

### Schritt 3: GitHub Action aktivieren

Der Workflow ist bereits unter `.github/workflows/sync-blueprint-to-kumu.yml` definiert.

**Überprüfung:**
1. Gehen Sie zu Ihrem Repository
2. Klicken Sie auf den Tab **"Actions"**
3. Sie sollten den Workflow **"Sync Main Model Blueprint to KUMU"** sehen

## 🧪 Testen des Workflows

### Test 1: Manueller Trigger (Optional)

```bash
# Sie können den Workflow manuell triggern, indem Sie die Datei ändern und pushen
git checkout -b test/kumu-sync
echo "# Test" >> README.md
git add models/main_model/wirkmechanismen-main-model-blueprint.json
git commit -m "test: trigger KUMU sync"
git push -u origin test/kumu-sync
```

### Test 2: Workflow-Status überprüfen

1. Gehen Sie zu **Actions** Tab in GitHub
2. Klicken Sie auf den neuesten Workflow-Run
3. Sie sollten die Logs sehen:
   - ✅ Blueprint validation passed
   - ✅ Successfully synced blueprint to KUMU

## 📚 KUMU API Referenz

### API Endpoints

**Blueprint Upload (empfohlen):**
```
POST https://kumu.io/api/v2/projects/{account}/{project}/elements
```

**Alternative - Über Import-URL:**
```
https://kumu.io/import?url=https://raw.githubusercontent.com/dfg-agil/wirkmechanismen/main/models/main_model/wirkmechanischen-main-model-blueprint.json
```

### Headers

```
Authorization: Bearer {KUMU_API_KEY}
Content-Type: application/json
```

### Request Body

Das Blueprint JSON (mit `elements` und `connections` arrays)

### Response Codes

- `200` / `201`: Success - Blueprint aktualisiert
- `401`: Authentifizierung fehlgeschlagen - API Key überprüfen
- `404`: Projekt nicht gefunden - Account/Project Slug überprüfen
- `400`: Invalid JSON - Blueprint-Format überprüfen

## 🔍 Troubleshooting

### Fehler: "Missing required environment variables"

**Problem**: Secrets sind nicht konfiguriert
**Lösung**: Siehe Schritt 2 oben

### Fehler: "Authentication failed: Invalid KUMU_API_KEY"

**Problem**: Der API Key ist ungültig oder abgelaufen
**Lösung**: 
1. Überprüfen Sie den API Key in KUMU Account Settings
2. Generieren Sie einen neuen Token falls nötig
3. Aktualisieren Sie das Secret in GitHub

### Fehler: "Project not found in KUMU"

**Problem**: `KUMU_ACCOUNT` oder `KUMU_PROJECT` sind falsch
**Lösung**:
1. Öffnen Sie Ihr KUMU Projekt: `kumu.io/{ACCOUNT}/{PROJECT}`
2. Überprüfen Sie die Slug-Namen exakt
3. Aktualisieren Sie die Secrets in GitHub

### Workflow läuft nicht

**Problem**: Der Workflow wird nicht bei Push ausgelöst
**Lösung**:
1. Überprüfen Sie, dass Sie Änderungen an `wirkmechanismen-main-model-blueprint.json` macht
2. Der Trigger reagiert nur auf `main` Branch
3. Überprüfen Sie den Tab **Actions** für Logs

## 📊 Workflow-Logs überprüfen

1. Gehen Sie zu **GitHub Repository** > **Actions**
2. Klicken Sie auf den neuesten Run
3. Expandieren Sie **"Sync Blueprint to KUMU"** Job
4. Schauen Sie sich die Output an

**Erfolgreicher Log-Eintrag:**
```
✓ Loaded blueprint: 156 elements, 402 connections
📤 Syncing to KUMU...
   Account: dfg-agil
   Project: wirkmechanismen
✅ Successfully synced blueprint to KUMU
```

## 🔐 Sicherheit

- API Keys sind als **encrypted secrets** gespeichert in GitHub
- Sie sind nicht im Repository Code sichtbar
- Sie werden nur zur Laufzeit injiziert
- Logs zeigen den API Key nicht

## 📝 Workflow-Datei Struktur

```
.github/
└── workflows/
    └── sync-blueprint-to-kumu.yml
```

**Triggers:**
- `push` events auf `main` branch
- Nur wenn Datei `models/main_model/wirkmechanismen-main-model-blueprint.json` geändert wird

**Jobs:**
1. Checkout Repository
2. Setup Python Environment
3. Validate Blueprint (lint_blueprint.py)
4. Sync to KUMU (sync_blueprint_to_kumu.py)
5. Report Status

## 🚀 Nächste Schritte

1. ✅ Configure Secrets in GitHub (Schritt 2)
2. ✅ Test the workflow (Schritt 3)
3. ✅ Make changes to the blueprint and push to main
4. ✅ Watch the automatic sync happen in GitHub Actions

## ❓ Fragen?

Wenn Sie Probleme mit der Einrichtung haben:

1. Überprüfen Sie die Logs im GitHub Actions Tab
2. Validieren Sie Ihre KUMU API-Token
3. Überprüfen Sie die `KUMU_ACCOUNT` und `KUMU_PROJECT` Werte in den Secrets

---

**Status**: Workflow ist konfiguriert und bereit zur Verwendung.
**Letzte Aktualisierung**: 2026-01-14
