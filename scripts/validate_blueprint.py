#!/usr/bin/env python3
"""
Blueprint Validation Script
Checks for inconsistencies between connections and elements in the KUMU blueprint.
"""

import json
import sys
from pathlib import Path
from collections import defaultdict


def load_blueprint(filepath):
    """Load and parse the JSON blueprint."""
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        # Handle both direct blueprint and array wrapper
        if isinstance(data, list):
            return {'elements': [], 'connections': data}
        return data


def validate_blueprint(blueprint):
    """Perform comprehensive validation checks."""
    errors = []
    warnings = []
    
    # Handle both dict and list structures
    if isinstance(blueprint, list):
        # If it's a list, assume it's elements
        elem_list = blueprint
        conn_list = []
        print("⚠️  Blueprint appears to be a list, not a standard dict structure")
    else:
        elem_list = blueprint.get('elements', [])
        conn_list = blueprint.get('connections', [])
    
    elements = {elem['_id']: elem for elem in elem_list if isinstance(elem, dict) and '_id' in elem}
    connections = [c for c in conn_list if isinstance(c, dict)]
    
    print(f"📊 Validation Report for Blueprint")
    print(f"   Elements: {len(elements)}")
    print(f"   Connections: {len(connections)}")
    print()
    
    # ===== CHECK 1: Reference Integrity =====
    print("🔗 CHECK 1: Connection Reference Integrity")
    ref_errors = []
    for conn in connections:
        conn_id = conn.get('_id', 'UNKNOWN')
        from_id = conn.get('from')
        to_id = conn.get('to')
        
        if not from_id or from_id not in elements:
            ref_errors.append(f"  ❌ {conn_id}: 'from' ({from_id}) not found or missing")
        
        if not to_id or to_id not in elements:
            ref_errors.append(f"  ❌ {conn_id}: 'to' ({to_id}) not found or missing")
    
    if ref_errors:
        errors.extend(ref_errors)
        print(f"   Found {len(ref_errors)} reference errors:")
        for err in ref_errors[:10]:
            print(err)
        if len(ref_errors) > 10:
            print(f"   ... and {len(ref_errors) - 10} more")
    else:
        print("   ✅ All connection references are valid")
    
    print()
    
    # ===== CHECK 2: Degree Metrics =====
    print("🔢 CHECK 2: Degree Metrics Consistency")
    degree_errors = []
    
    # Calculate actual degrees
    actual_indegree = defaultdict(int)
    actual_outdegree = defaultdict(int)
    actual_degree = defaultdict(int)
    
    for conn in connections:
        from_id = conn.get('from')
        to_id = conn.get('to')
        if from_id and to_id:
            actual_outdegree[from_id] += 1
            actual_indegree[to_id] += 1
    
    # Compare with stored metrics
    for elem in elem_list:
        if not isinstance(elem, dict):
            continue
        elem_id = elem.get('_id')
        if not elem_id:
            continue
        attributes = elem.get('attributes', {})
        
        stored_indegree = attributes.get('indegree', 0)
        stored_outdegree = attributes.get('outdegree', 0)
        stored_degree = attributes.get('degree', 0)
        
        actual_in = actual_indegree.get(elem_id, 0)
        actual_out = actual_outdegree.get(elem_id, 0)
        actual_deg = actual_in + actual_out
        
        if stored_indegree != actual_in:
            degree_errors.append(
                f"  ⚠️  {elem_id}: indegree mismatch (stored={stored_indegree}, actual={actual_in})"
            )
        
        if stored_outdegree != actual_out:
            degree_errors.append(
                f"  ⚠️  {elem_id}: outdegree mismatch (stored={stored_outdegree}, actual={actual_out})"
            )
        
        if stored_degree != actual_deg:
            degree_errors.append(
                f"  ⚠️  {elem_id}: degree mismatch (stored={stored_degree}, actual={actual_deg})"
            )
    
    if degree_errors:
        warnings.extend(degree_errors)
        print(f"   Found {len(degree_errors)} degree metric mismatches:")
        for warn in degree_errors[:15]:
            print(warn)
        if len(degree_errors) > 15:
            print(f"   ... and {len(degree_errors) - 15} more")
    else:
        print("   ✅ All degree metrics are consistent")
    
    print()
    
    # ===== CHECK 3: Duplicate IDs =====
    print("🔄 CHECK 3: Duplicate Element/Connection IDs")
    
    elem_ids = [e['_id'] for e in elem_list if isinstance(e, dict) and '_id' in e]
    conn_ids = [c['_id'] for c in connections if '_id' in c]
    
    dup_elem_ids = [id for id in elem_ids if elem_ids.count(id) > 1]
    dup_conn_ids = [id for id in conn_ids if conn_ids.count(id) > 1]
    
    if dup_elem_ids or dup_conn_ids:
        if dup_elem_ids:
            unique_dups = list(set(dup_elem_ids))
            errors.append(f"  ❌ Found {len(unique_dups)} duplicate element IDs: {unique_dups[:5]}")
        if dup_conn_ids:
            unique_dups = list(set(dup_conn_ids))
            errors.append(f"  ❌ Found {len(unique_dups)} duplicate connection IDs: {unique_dups[:5]}")
    else:
        print("   ✅ No duplicate IDs found")
    
    print()
    
    # ===== CHECK 4: Missing Descriptions =====
    print("📝 CHECK 4: Connection Documentation")
    missing_desc = 0
    for conn in connections:
        if not conn.get('attributes', {}).get('description'):
            missing_desc += 1
    
    if missing_desc > 0:
        warnings.append(f"  ⚠️  {missing_desc} connections lack descriptions")
        print(f"   ⚠️  {missing_desc} connections without descriptions")
    else:
        print("   ✅ All connections have descriptions")
    
    print()
    
    # ===== CHECK 5: Source Attribution (for Impact Models) =====
    print("🔬 CHECK 5: Source Attribution in Connection Labels")
    missing_source = 0
    for conn in connections:
        label = conn.get('attributes', {}).get('label', '')
        if label and label.strip() not in ['[A]', '[A?]', '[E]', '[X]', '[O]', '[?]']:
            missing_source += 1
    
    if missing_source > 0:
        warnings.append(f"  ⚠️  {missing_source} connections have non-standard source labels")
        print(f"   ⚠️  {missing_source} connections with non-standard labels (not [A], [E], [X], [O], [?])")
    else:
        print("   ✅ All connections use standard source attribution")
    
    print()
    
    # ===== SUMMARY =====
    print("=" * 60)
    print("📋 SUMMARY")
    print("=" * 60)
    print(f"Errors:   {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    
    if errors:
        print("\n🛑 ERRORS (must fix):")
        for err in errors:
            print(err)
    
    if warnings:
        print("\n⚠️  WARNINGS (should review):")
        for warn in warnings[:10]:
            print(warn)
        if len(warnings) > 10:
            print(f"   ... and {len(warnings) - 10} more warnings")
    
    return len(errors) == 0


if __name__ == '__main__':
    blueprint_path = Path(__file__).parent.parent / 'models' / 'main_model' / 'wirkmechanismen-main-model-blueprint.json'
    
    if not blueprint_path.exists():
        print(f"❌ Blueprint file not found: {blueprint_path}")
        sys.exit(1)
    
    print(f"🔍 Validating: {blueprint_path}\n")
    
    blueprint = load_blueprint(blueprint_path)
    is_valid = validate_blueprint(blueprint)
    
    sys.exit(0 if is_valid else 1)
