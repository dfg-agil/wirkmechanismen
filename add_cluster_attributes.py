#!/usr/bin/env python3
"""
Script to add cluster attributes to blueprint elements.
Modifies the Henrike blueprint to mark elements as part of the "Mensch" cluster.
"""

import json

# List of element IDs to add to "Mensch" cluster
MENSCH_CLUSTER_ELEMENTS = [
    "elem-raumnaeheTeam",
    "elem-informelleBegegnungen",
    "elem-VzcqeqTN",
    "elem-teamLeadSozialkompetenz",
    "elem-wDnzlLwI",
    "elem-psychSicherheit",
    "elem-informelleKommunikationQualitaet",
    "elem-akzeptanzMedium",
    "elem-68KZOQXM",
    "elem-GzVWvit5",
    "elem-U5tPKB1A",
    "elem-lKD0abzp",
    "elem-8DovrrfU",
    "elem-kTvnvfVI",
    "elem-xGnKBSH9",
    "elem-SVQRqUSA",
    "elem-97NjDQTs",
    "elem-5kn48AvH",
    "elem-Tc7Rjavq",
    "elem-transpFahig01",
    "elem-gradKollaboration",
    "elem-effektivitaetKollaboration"
]

BLUEPRINT_FILE = "models/main_model/wirkmechanismen-main-model-blueprint-Henrike.json"


def add_cluster_attributes():
    """Load blueprint, add cluster attributes to specified elements, and save."""
    
    # Load the blueprint
    with open(BLUEPRINT_FILE, 'r', encoding='utf-8') as f:
        blueprint = json.load(f)
    
    # Counter for tracking changes
    modified_count = 0
    not_found = []
    
    # Iterate through elements and add cluster attribute
    for element in blueprint.get('elements', []):
        elem_id = element.get('_id')
        
        if elem_id in MENSCH_CLUSTER_ELEMENTS:
            # Add cluster attribute
            element['attributes']['cluster'] = "Mensch"
            modified_count += 1
        
        # Track elements not found
        if elem_id in MENSCH_CLUSTER_ELEMENTS:
            MENSCH_CLUSTER_ELEMENTS.remove(elem_id)
    
    # Check for elements that weren't found
    if MENSCH_CLUSTER_ELEMENTS:
        not_found = MENSCH_CLUSTER_ELEMENTS
    
    # Save the modified blueprint
    with open(BLUEPRINT_FILE, 'w', encoding='utf-8') as f:
        json.dump(blueprint, f, indent=2, ensure_ascii=False)
    
    # Print results
    print(f"✅ Modified {modified_count} elements")
    print(f"✅ Blueprint saved to: {BLUEPRINT_FILE}")
    
    if not_found:
        print(f"⚠️  Warning: {len(not_found)} elements not found:")
        for elem_id in not_found:
            print(f"   - {elem_id}")
    
    return modified_count == 22


if __name__ == "__main__":
    success = add_cluster_attributes()
    exit(0 if success else 1)
