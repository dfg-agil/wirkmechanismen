# KUMU-GitHub Verbindung: Praktische Anleitung

## 📋 Checkliste

### Phase 1: Lokale Vorbereitung ✅ ABGESCHLOSSEN

- [x] GitHub Actions Workflow erstellt
- [x] Python Sync-Script erstellt
- [x] Dokumentation erstellt
- [x] Dateien zum Commit vorbereitet

**Status:** Bereit für GitHub

---

## Phase 2: KUMU API-Token beschaffen (MANUELL)

**Zeitaufwand:** ~2 Minuten

### Schritt 1: Öffnen Sie KUMU

- [ ] Gehen Sie zu: https://kumu.io
- [ ] Melden Sie sich an

### Schritt 2: Navigieren Sie zu API Settings

- [ ] Klicken Sie oben rechts auf Ihr Profil
- [ ] Klicken Sie auf **"Account Settings"**
- [ ] Klicken Sie auf **"API"** (links im Menü)

### Schritt 3: Generieren Sie einen Token

- [ ] Klicken Sie auf den Button **"Generate New Token"**
- [ ] Ein Token wird generiert (z.B. `sk_live_abc123xyz...`)
- [ ] **Kopieren Sie sofort diesen Token**
- [ ] Speichern Sie ihn sicher (z.B. in einer Textdatei)

### Schritt 4: Notieren Sie Account & Project

- [ ] Öffnen Sie Ihr KUMU Projekt
- [ ] Die URL sieht aus wie: `https://kumu.io/{ACCOUNT}/{PROJECT}`
- [ ] Notieren Sie beide Slugs:
  ```
  KUMU_ACCOUNT = [Erster Teil, z.B. dfg-agil]
  KUMU_PROJECT = [Zweiter Teil, z.B. wirkmechanismen]
  ```

---

## Phase 3: GitHub Secrets konfigurieren (MANUELL)

**Zeitaufwand:** ~3 Minuten

### Schritt 1: GitHub Settings öffnen

- [ ] Gehen Sie zu: https://github.com/dfg-agil/wirkmechanismen
- [ ] Klicken Sie auf **"Settings"** Tab (oben)

### Schritt 2: Navigieren Sie zu Secrets

- [ ] Klicken Sie links im Menü auf **"Secrets and variables"**
- [ ] Klicken Sie auf **"Actions"**

### Schritt 3: Fügen Sie Secret 1 hinzu (KUMU_API_KEY)

- [ ] Klicken Sie auf **"New repository secret"** (grüner Button)
- [ ] Name: `KUMU_API_KEY`
- [ ] Value: [Fügen Sie Ihren KUMU API Token ein]
- [ ] Klicken Sie **"Add secret"**

### Schritt 4: Fügen Sie Secret 2 hinzu (KUMU_ACCOUNT)

- [ ] Klicken Sie wieder auf **"New repository secret"**
- [ ] Name: `KUMU_ACCOUNT`
- [ ] Value: [Ihr KUMU Account Slug, z.B. dfg-agil]
- [ ] Klicken Sie **"Add secret"**

### Schritt 5: Fügen Sie Secret 3 hinzu (KUMU_PROJECT)

- [ ] Klicken Sie wieder auf **"New repository secret"**
- [ ] Name: `KUMU_PROJECT`
- [ ] Value: [Ihr KUMU Project Slug, z.B. wirkmechanismen]
- [ ] Klicken Sie **"Add secret"**

### Schritt 6: Überprüfung

Nach Abschluss sollten Sie auf der Secrets-Seite sehen:
```
✓ KUMU_API_KEY       (***hidden***)
✓ KUMU_ACCOUNT       (dfg-agil)
✓ KUMU_PROJECT       (wirkmechanismen)
```

- [ ] Alle 3 Secrets sind sichtbar

---

## Phase 4: Dateien committen und pushen (TERMINAL)

**Zeitaufwand:** ~1 Minute

```bash
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

- [ ] Commit erfolgreich
- [ ] Push erfolgreich

---

## Phase 5: GitHub Actions Test (WEB)

**Zeitaufwand:** ~2 Minuten

### Schritt 1: Navigieren Sie zu GitHub Actions

- [ ] Gehen Sie zu: https://github.com/dfg-agil/wirkmechanismen/actions
- [ ] Sie sollten einen neuen Workflow Run sehen (von dem Push)

### Schritt 2: Überprüfen Sie den Workflow Status

- [ ] Klicken Sie auf den neuesten Run
- [ ] Schauen Sie sich die Logs an
- [ ] Suchen Sie nach: `✅ Successfully synced blueprint to KUMU`

### Schritt 3: Bestätigung in KUMU

- [ ] Öffnen Sie Ihr KUMU Projekt
- [ ] Überprüfen Sie, dass die Blueprint-Daten vorhanden sind
- [ ] Überprüfen Sie, dass die letzten Änderungen sichtbar sind

---

## ✅ Fertig!

Wenn alle Tests erfolgreich sind:

1. **Automatische Synchronisation ist aktiv** 🎉
2. **Jeder Push zu `main` mit Änderungen am Blueprint synchronisiert automatisch zu KUMU**
3. **GitHub bleibt die Source of Truth**
4. **KUMU wird immer aktuell gehalten**

---

## 📚 Zusätzliche Ressourcen

- GitHub Actions Workflow: `.github/workflows/sync-blueprint-to-kumu.yml`
- Python Sync Script: `scripts/sync_blueprint_to_kumu.py`
- Setup-Dokumentation: `.github/KUMU_SYNC_SETUP.md`
- Secrets-Konfiguration: `.github/KUMU_SECRETS_CONFIG.txt`

---

## ❓ Troubleshooting

### Workflow läuft nicht

**Überprüfung:**
1. Überprüfen Sie den GitHub Actions Tab
2. Suchen Sie nach dem Workflow "Sync Main Model Blueprint to KUMU"
3. Schauen Sie sich die Logs an

**Häufige Fehler:**
- `Missing required environment variables` → Secrets nicht konfiguriert
- `Authentication failed` → API Key ungültig
- `Project not found` → Account/Project Slug falsch

---

## 📝 Nächste Schritte

Nach erfolgreicher Einrichtung:

1. Machen Sie regelmäßig Änderungen am Blueprint
2. Pushen Sie zu `main` via Pull Request
3. Der Workflow synchronisiert automatisch zu KUMU
4. Überprüfen Sie gelegentlich die GitHub Actions Logs

---

**Status:** Bereit zur Konfiguration
**Zuletzt aktualisiert:** 2026-01-14
