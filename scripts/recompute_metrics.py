#!/usr/bin/env python3
"""
Recompute analytics metrics (degree, indegree, outdegree, size) for all elements
based on actual connection counts. This ensures KUMU displays all connections correctly.
"""

import json
from pathlib import Path
from collections import defaultdict


def recompute_metrics(blueprint_path):
    """Load blueprint, calculate metrics, and save."""
    
    # Load blueprint
    with open(blueprint_path, 'r', encoding='utf-8-sig') as f:
        blueprint = json.load(f)
    
    elements = {elem['_id']: elem for elem in blueprint['elements']}
    connections = blueprint['connections']
    
    # Calculate actual degrees
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    
    for conn in connections:
        from_id = conn.get('from')
        to_id = conn.get('to')
        if from_id and to_id:
            outdegree[from_id] += 1
            indegree[to_id] += 1
    
    # Update metrics in elements
    updated_count = 0
    for elem_id, elem in elements.items():
        if 'attributes' not in elem:
            elem['attributes'] = {}
        
        attrs = elem['attributes']
        
        actual_in = indegree.get(elem_id, 0)
        actual_out = outdegree.get(elem_id, 0)
        actual_degree = actual_in + actual_out
        
        old_indegree = attrs.get('indegree', 0)
        old_outdegree = attrs.get('outdegree', 0)
        old_degree = attrs.get('degree', 0)
        
        # Update only if changed
        if old_indegree != actual_in or old_outdegree != actual_out or old_degree != actual_degree:
            attrs['indegree'] = actual_in
            attrs['outdegree'] = actual_out
            attrs['degree'] = actual_degree
            attrs['size'] = actual_degree + 1  # size = neighbors + self
            
            if old_indegree != actual_in or old_outdegree != actual_out:
                print(f"  ✓ {elem_id}: in({old_indegree}→{actual_in}) out({old_outdegree}→{actual_out}) deg({old_degree}→{actual_degree})")
                updated_count += 1
    
    # Save blueprint
    with open(blueprint_path, 'w', encoding='utf-8') as f:
        json.dump(blueprint, f, indent=2, ensure_ascii=False)
    
    return updated_count, len(elements)


if __name__ == '__main__':
    blueprint_path = Path(__file__).parent.parent / 'models' / 'main_model' / 'wirkmechanismen-main-model-blueprint.json'
    
    if not blueprint_path.exists():
        print(f"❌ Blueprint not found: {blueprint_path}")
        exit(1)
    
    print(f"🔄 Recomputing metrics for: {blueprint_path}\n")
    updated, total = recompute_metrics(blueprint_path)
    print(f"\n✅ Updated {updated}/{total} elements with correct metrics")
    print(f"📊 Blueprint saved successfully")
