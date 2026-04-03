#!/usr/bin/env python3
"""
Template Validator

Validates generated templates for:
- YAML syntax
- Placeholder completion
- Required fields
- Format correctness
"""

import sys
import yaml
import re
from pathlib import Path

def validate_yaml_syntax(file_path):
    """Validate YAML syntax"""
    try:
        with open(file_path, 'r') as f:
            yaml.safe_load(f)
        return True, "YAML syntax valid"
    except yaml.YAMLError as e:
        return False, f"YAML syntax error: {e}"

def find_placeholders(content):
    """Find all placeholders in format [PLACEHOLDER]"""
    return re.findall(r'\[([A-Z_]+(?:_[A-Z_]+)*)\]', content)

def validate_placeholders(file_path):
    """Check if placeholders are filled"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    placeholders = find_placeholders(content)
    
    if not placeholders:
        return True, "All placeholders filled"
    else:
        return False, f"Unfilled placeholders: {', '.join(set(placeholders))}"

def validate_required_fields(file_path, template_type):
    """Validate required fields based on template type"""
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    
    required_fields = {
        'agent': ['setup.name', 'setup.llm_model', 'setup.purpose'],
        'pipeline': ['setup.name', 'setup.type', 'layout.stages'],
        'architecture': ['setup.name', 'setup.architecture_type', 'layout.layers'],
        'workflow': ['setup.name', 'setup.trigger', 'layout.steps'],
        'rules': ['setup.name', 'setup.rule_engine', 'layout.rules']
    }
    
    if template_type not in required_fields:
        return True, f"Unknown template type: {template_type}, skipping field validation"
    
    missing = []
    for field_path in required_fields[template_type]:
        parts = field_path.split('.')
        current = data
        try:
            for part in parts:
                current = current[part]
        except (KeyError, TypeError):
            missing.append(field_path)
    
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"
    else:
        return True, "All required fields present"

def detect_template_type(file_path):
    """Detect template type from content"""
    with open(file_path, 'r') as f:
        content = f.read().lower()
    
    if 'llm_model' in content or '_agent' in content:
        return 'agent'
    elif 'pipeline' in content and 'stages' in content:
        return 'pipeline'
    elif 'architecture' in content and 'layers' in content:
        return 'architecture'
    elif 'workflow' in content and 'steps' in content:
        return 'workflow'
    elif 'rules' in content and 'rule_engine' in content:
        return 'rules'
    else:
        return 'unknown'

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_template.py <template_file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        sys.exit(1)
    
    print(f"🔍 Validating template: {file_path}")
    print("=" * 60)
    
    # Detect template type
    template_type = detect_template_type(file_path)
    print(f"📋 Detected template type: {template_type}")
    print()
    
    all_passed = True
    
    # Check 1: YAML Syntax
    passed, message = validate_yaml_syntax(file_path)
    status = "✅" if passed else "❌"
    print(f"{status} YAML Syntax: {message}")
    all_passed = all_passed and passed
    
    # Check 2: Placeholders
    passed, message = validate_placeholders(file_path)
    status = "✅" if passed else "⚠️"
    print(f"{status} Placeholders: {message}")
    if not passed:
        print("   Note: Unfilled placeholders are warnings, not errors")
    
    # Check 3: Required Fields
    if template_type != 'unknown':
        passed, message = validate_required_fields(file_path, template_type)
        status = "✅" if passed else "❌"
        print(f"{status} Required Fields: {message}")
        all_passed = all_passed and passed
    
    print()
    print("=" * 60)
    
    if all_passed:
        print("✅ Template validation PASSED")
        sys.exit(0)
    else:
        print("❌ Template validation FAILED")
        sys.exit(1)

if __name__ == "__main__":
    main()
