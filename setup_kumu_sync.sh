#!/bin/bash
# KUMU-GitHub Verbindung Setup-Script
# Dieses Script bereitet das Repository für die KUMU-Synchronisation vor

set -e

echo "🔗 KUMU-GitHub Verbindung - Setup"
echo "=================================="
echo ""

# Schritt 1: Änderungen überprüfen
echo "✓ Schritt 1: Lokale Änderungen überprüfen"
git status
echo ""

# Schritt 2: Neue Dateien hinzufügen
echo "✓ Schritt 2: Neue Setup-Dateien vorbereiten"
echo "  - .github/workflows/sync-blueprint-to-kumu.yml"
echo "  - scripts/sync_blueprint_to_kumu.py"
echo "  - .github/KUMU_SYNC_SETUP.md"

git add .github/workflows/sync-blueprint-to-kumu.yml
git add .github/KUMU_SYNC_SETUP.md
git add scripts/sync_blueprint_to_kumu.py

echo ""

# Schritt 3: Workflow-Validierung
echo "✓ Schritt 3: Blueprint validieren"
python3 scripts/lint_blueprint.py models/main_model/wirkmechanismen-main-model-blueprint.json
echo "  ✅ Blueprint ist gültig"
echo ""

# Schritt 4: Info zu manuellen Schritten
echo "✓ Schritt 4: Manuelle Konfiguration erforderlich"
echo ""
echo "Die folgenden Schritte MÜSSEN manuell durchgeführt werden:"
echo ""
echo "A) KUMU API-Token beschaffen:"
echo "   1. Öffnen Sie https://kumu.io"
echo "   2. Gehen Sie zu: Account Settings > API"
echo "   3. Klicken Sie: Generate New Token"
echo "   4. Kopieren Sie den Token"
echo ""
echo "B) GitHub Secrets konfigurieren:"
echo "   1. Öffnen Sie: https://github.com/dfg-agil/wirkmechanismen"
echo "   2. Gehen Sie zu: Settings > Secrets and variables > Actions"
echo "   3. Klicken Sie: New repository secret"
echo "   4. Fügen Sie folgende Secrets hinzu:"
echo ""
echo "      Secret 1:"
echo "      Name:  KUMU_API_KEY"
echo "      Value: [Ihr KUMU API Token]"
echo ""
echo "      Secret 2:"
echo "      Name:  KUMU_ACCOUNT"
echo "      Value: [Ihr Account Slug, z.B. 'dfg-agil']"
echo ""
echo "      Secret 3:"
echo "      Name:  KUMU_PROJECT"
echo "      Value: [Ihr Project Slug, z.B. 'wirkmechanismen']"
echo ""

# Schritt 5: Commit-Vorbereitung
echo "✓ Schritt 5: Commit vorbereiten"
echo ""
echo "Die folgenden Dateien sind bereit zu committen:"
git diff --cached --name-only
echo ""

# Schritt 6: Anleitung zum Fortfahren
echo "📋 Nächste Schritte:"
echo ""
echo "1. Führen Sie die manuellen Schritte A und B durch (siehe oben)"
echo ""
echo "2. Committen Sie die neuen Dateien:"
echo "   git commit -m 'feat: add KUMU GitHub Actions workflow for automatic synchronisation'"
echo ""
echo "3. Pushen Sie zu GitHub:"
echo "   git push origin main"
echo ""
echo "4. Überprüfen Sie GitHub Actions:"
echo "   https://github.com/dfg-agil/wirkmechanismen/actions"
echo ""
echo "5. Der Workflow wird automatisch beim nächsten Push ausgelöst"
echo ""

echo "✅ Lokale Vorbereitung abgeschlossen!"
