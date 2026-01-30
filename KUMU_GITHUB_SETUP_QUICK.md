# 🔗 KUMU-GitHub Setup: Schritt-für-Schritt Anleitung

## ✅ Status: Lokale Vorbereitung ABGESCHLOSSEN

```
✓ GitHub Actions Workflow erstellt
✓ Python Sync-Script erstellt  
✓ Alle Dokumentationen erstellt
✓ Dateien für Commit vorbereitet
```

---

## 📋 Sie müssen jetzt 2 Dinge tun:

### 1️⃣ KUMU Konfiguration (Web)
### 2️⃣ GitHub Secrets (Web)

Nach diesen beiden Schritten ist die Automatisierung aktiv!

---

## 🔑 KUMU API-Token beschaffen

**Zeitaufwand:** 2 Minuten

### Öffnen Sie KUMU:
```
Gehen Sie zu: https://kumu.io
Melden Sie sich an
```

### Finden Sie die API Settings:
```
1. Klick auf Ihr Profil (oben rechts)
2. Klick auf "Account Settings"
3. Klick auf "API" (linkes Menü)
```

### Generieren Sie einen Token:
```
1. Klick auf Button: "Generate New Token"
2. Ein Token wird angezeigt (z.B. sk_live_abc123xyz...)
3. KOPIEREN Sie sofort diesen Token
4. SPEICHERN Sie ihn sicher (z.B. Textdatei)
```

### Merken Sie sich diese Information:
```
Von Ihrer KUMU URL: https://kumu.io/{ACCOUNT}/{PROJECT}

Beispiel: https://kumu.io/dfg-agil/wirkmechanismen
          ├─ KUMU_ACCOUNT = dfg-agil
          └─ KUMU_PROJECT = wirkmechanismen
```

---

## 🔐 GitHub Secrets konfigurieren

**Zeitaufwand:** 3 Minuten

### Öffnen Sie GitHub Settings:
```
Gehen Sie zu: https://github.com/dfg-agil/wirkmechanismen/settings/secrets/actions
```

### Oder manuell navigieren:
```
1. GitHub: https://github.com/dfg-agil/wirkmechanismen
2. Klick auf "Settings" Tab
3. Linkes Menü: "Secrets and variables" > "Actions"
```

### Fügen Sie 3 Secrets hinzu:

#### ⚙️ Secret 1: KUMU_API_KEY
```
1. Klick "New repository secret"
2. Name:  KUMU_API_KEY
3. Value: [Ihr KUMU API Token, den Sie oben kopiert haben]
4. Klick "Add secret"
```

#### ⚙️ Secret 2: KUMU_ACCOUNT
```
1. Klick "New repository secret"
2. Name:  KUMU_ACCOUNT
3. Value: [Z.B. dfg-agil]
4. Klick "Add secret"
```

#### ⚙️ Secret 3: KUMU_PROJECT
```
1. Klick "New repository secret"
2. Name:  KUMU_PROJECT
3. Value: [Z.B. wirkmechanismen]
4. Klick "Add secret"
```

### Überprüfung:
Nach den 3 Secrets sollten Sie sehen:
```
✓ KUMU_API_KEY      (***hidden***)
✓ KUMU_ACCOUNT      (dfg-agil)
✓ KUMU_PROJECT      (wirkmechanismen)
```

---

## 💾 Dateien committen und pushen

**Zeitaufwand:** 1 Minute

Öffnen Sie PowerShell/Terminal im Repository:

### Führen Sie folgende Befehle aus:

```powershell
# 1. Überprüfen Sie den Status
git status

# 2. Committen Sie die neuen Dateien
git commit -m "feat: add KUMU GitHub Actions workflow for automatic synchronisation

- Add GitHub Actions workflow for automatic Blueprint-to-KUMU sync
- Add Python sync script with KUMU API integration  
- Add setup documentation and configuration guide
- Trigger: push to main branch with changes to main model blueprint

The workflow validates the blueprint and automatically syncs it to KUMU
after merge, ensuring GitHub remains the source of truth while keeping
KUMU updated."

# 3. Pushen Sie zu GitHub
git push origin main
```

**Erwartete Ausgabe:**
```
[main xxxxxxx] feat: add KUMU GitHub Actions workflow...
 6 files changed, 400 insertions(+)
...
To https://github.com/dfg-agil/wirkmechanismen.git
   xxxxxxx..yyyyyyy  main -> main
```

---

## 🧪 Test des Workflows

**Zeitaufwand:** 2 Minuten

### Navigieren Sie zu GitHub Actions:
```
https://github.com/dfg-agil/wirkmechanismen/actions
```

### Sie sollten einen neuen Run sehen:
```
"Sync Main Model Blueprint to KUMU" 
Status: In Progress (dann Completed)
```

### Klicken Sie auf den Run um Details zu sehen:

**Erfolgreicher Test zeigt:**
```
✅ Checkout repository
✅ Set up Python
✅ Validate Blueprint JSON
   → ✅ Blueprint validation passed
✅ Sync Blueprint to KUMU
   → ✅ Successfully synced blueprint to KUMU
✅ Report Status
```

**Fehler würde zeigen:**
```
❌ Failed to sync blueprint to KUMU
   Please check KUMU API credentials and connection
```

Wenn Fehler erscheinen → Siehe Troubleshooting unten

### Überprüfung in KUMU:
```
1. Öffnen Sie Ihr KUMU Projekt
2. Überprüfen Sie, dass die Blueprint-Daten vorhanden sind
3. Überprüfen Sie, dass die Factoren noch da sind
```

---

## 🎉 Fertig!

Wenn alle Tests erfolgreich sind:

✅ **Automatische Synchronisation ist aktiv**

Ab jetzt:
- Jeder Push zu `main` mit Änderungen am Blueprint synchronisiert automatisch zu KUMU
- GitHub bleibt die Source of Truth
- KUMU wird immer aktuell gehalten
- Der Status ist im GitHub Actions Log nachverfolgbar

---

## ⚠️ Troubleshooting

### Problem: Workflow läuft nicht / zeigt Fehler

**Überprüfung 1: Secrets kontrollieren**
```
GitHub > Settings > Secrets and variables > Actions
Überprüfen Sie, dass alle 3 Secrets vorhanden sind:
✓ KUMU_API_KEY
✓ KUMU_ACCOUNT  
✓ KUMU_PROJECT
```

**Überprüfung 2: API Key testen**
```
Überprüfen Sie in KUMU:
- Account Settings > API
- Ist der Token noch gültig?
- Falls nicht: Generieren Sie einen neuen und aktualisieren Sie den Secret
```

**Überprüfung 3: Account/Project Slug**
```
Öffnen Sie Ihr KUMU Projekt
URL Format: https://kumu.io/{ACCOUNT}/{PROJECT}
Überprüfen Sie die exakten Slugs in den Secrets
```

**Überprüfung 4: GitHub Actions Logs**
```
GitHub > Actions > "Sync Main Model Blueprint to KUMU" 
Klicken Sie auf den fehlgeschlagenen Run
Expandieren Sie die Logs und suchen Sie nach Fehlermeldungen
```

### Problem: Fehler "Authentication failed"

**Lösung:**
1. KUMU API Key überprüfen
2. Neuen Token in KUMU generieren
3. Secret `KUMU_API_KEY` in GitHub aktualisieren
4. Workflow erneut testen

### Problem: Fehler "Project not found"

**Lösung:**
1. Öffnen Sie Ihr KUMU Projekt: https://kumu.io/...
2. Überprüfen Sie die genauen Slugs in der URL
3. Aktualisieren Sie die Secrets `KUMU_ACCOUNT` und `KUMU_PROJECT`
4. Workflow erneut testen

---

## 📚 Dokumentation

Die folgenden Dateien wurden erstellt/aktualisiert:

```
.github/
├── workflows/
│   └── sync-blueprint-to-kumu.yml          (GitHub Actions Workflow)
├── KUMU_SYNC_SETUP.md                      (Setup-Dokumentation)
├── KUMU_SECRETS_CONFIG.txt                 (Secrets-Referenz)
└── ...

scripts/
└── sync_blueprint_to_kumu.py              (Python Sync-Script)

Root:
└── KUMU_GITHUB_SETUP.md                    (Diese Datei)
```

---

## ✅ Zusammenfassung der nächsten Schritte

- [ ] KUMU API-Token generieren
- [ ] KUMU Account & Project Slug notieren
- [ ] 3 GitHub Secrets konfigurieren
- [ ] Dateien committen (`git commit`)
- [ ] Zu main pushen (`git push origin main`)
- [ ] GitHub Actions Log überprüfen
- [ ] Test erfolgreich bestätigt ✓

---

**Status:** Bereit zum Setup
**Letzte Aktualisierung:** 2026-01-14
**Nächster Schritt:** KUMU Konfiguration (siehe oben)
