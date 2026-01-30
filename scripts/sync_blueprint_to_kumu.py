#!/usr/bin/env python3
"""
Sync KUMU Blueprint to KUMU API

This script synchronizes the Main Model Blueprint JSON to KUMU.io
by uploading it via the KUMU API.

Environment variables required:
- KUMU_API_KEY: Your KUMU API token
- KUMU_ACCOUNT: Your KUMU account slug
- KUMU_PROJECT: Your KUMU project slug
"""

import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests library not installed. Install with: pip install requests")
    sys.exit(1)


def get_credentials():
    """Get KUMU API credentials from environment variables."""
    api_key = os.getenv("KUMU_API_KEY")
    account = os.getenv("KUMU_ACCOUNT")
    project = os.getenv("KUMU_PROJECT")
    
    if not all([api_key, account, project]):
        missing = []
        if not api_key:
            missing.append("KUMU_API_KEY")
        if not account:
            missing.append("KUMU_ACCOUNT")
        if not project:
            missing.append("KUMU_PROJECT")
        
        print(f"ERROR: Missing required environment variables: {', '.join(missing)}")
        print("\nPlease set these as GitHub Secrets in your repository settings:")
        print("1. Go to Settings > Secrets and variables > Actions")
        print("2. Add the following secrets:")
        print("   - KUMU_API_KEY: Your KUMU API token")
        print("   - KUMU_ACCOUNT: Your KUMU account slug (from kumu.io/account-name)")
        print("   - KUMU_PROJECT: Your KUMU project slug (from kumu.io/account-name/project-slug)")
        sys.exit(1)
    
    return api_key, account, project


def load_blueprint(blueprint_path):
    """Load and validate the blueprint JSON file."""
    if not blueprint_path.exists():
        print(f"ERROR: Blueprint file not found: {blueprint_path}")
        sys.exit(1)
    
    try:
        with open(blueprint_path, 'r', encoding='utf-8') as f:
            blueprint = json.load(f)
        
        # Validate structure
        if not isinstance(blueprint, dict):
            print("ERROR: Blueprint is not a JSON object")
            sys.exit(1)
        
        if "elements" not in blueprint or "connections" not in blueprint:
            print("ERROR: Blueprint must contain 'elements' and 'connections' arrays")
            sys.exit(1)
        
        print(f"✓ Loaded blueprint: {len(blueprint['elements'])} elements, {len(blueprint['connections'])} connections")
        return blueprint
    
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in blueprint: {e}")
        sys.exit(1)


def sync_to_kumu(api_key, account, project, blueprint):
    """Upload blueprint to KUMU via API."""
    
    # KUMU API endpoint for updating a project's blueprint
    url = f"https://kumu.io/api/v2/projects/{account}/{project}/elements"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    print(f"\n📤 Syncing to KUMU...")
    print(f"   Account: {account}")
    print(f"   Project: {project}")
    print(f"   API Endpoint: {url}")
    
    try:
        # Method 1: Upload entire blueprint as replacement
        # This is the most reliable method
        response = requests.post(
            url,
            headers=headers,
            json=blueprint,
            timeout=30
        )
        
        if response.status_code == 200:
            print("✅ Successfully synced blueprint to KUMU")
            print(f"   Response: {response.status_code}")
            return True
        
        elif response.status_code == 201:
            print("✅ Successfully created/updated blueprint in KUMU")
            print(f"   Response: {response.status_code}")
            return True
        
        elif response.status_code == 401:
            print("❌ Authentication failed: Invalid KUMU_API_KEY")
            print(f"   Response: {response.status_code}")
            print(f"   Details: {response.text}")
            return False
        
        elif response.status_code == 404:
            print("❌ Project not found in KUMU")
            print(f"   Account: {account}")
            print(f"   Project: {project}")
            print(f"   Response: {response.status_code}")
            print(f"   Details: {response.text}")
            return False
        
        else:
            print(f"❌ Failed to sync blueprint to KUMU")
            print(f"   Status Code: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    
    except requests.exceptions.Timeout:
        print("❌ Request timeout: KUMU API took too long to respond")
        return False
    
    except requests.exceptions.ConnectionError:
        print("❌ Connection error: Cannot reach KUMU API")
        print("   Check your internet connection and KUMU_ACCOUNT/KUMU_PROJECT values")
        return False
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def main():
    """Main synchronization workflow."""
    print("🔄 KUMU Blueprint Synchronization")
    print("=" * 50)
    
    # Get credentials
    api_key, account, project = get_credentials()
    
    # Load blueprint
    repo_root = Path(__file__).resolve().parents[1]
    blueprint_path = repo_root / "models" / "main_model" / "wirkmechanismen-main-model-blueprint.json"
    
    print(f"\n📂 Loading blueprint from: {blueprint_path}")
    blueprint = load_blueprint(blueprint_path)
    
    # Sync to KUMU
    success = sync_to_kumu(api_key, account, project, blueprint)
    
    if not success:
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("✅ Synchronization complete!")


if __name__ == "__main__":
    main()
