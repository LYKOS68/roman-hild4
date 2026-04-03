#!/usr/bin/env python3
"""
Template Filler

Interactively fills placeholders in templates.
"""

import sys
import re
from pathlib import Path

def find_placeholders(content):
    """Find all unique placeholders in format [PLACEHOLDER]"""
    placeholders = re.findall(r'\[([A-Z_]+(?:_[A-Z_]+)*)\]', content)
    return list(dict.fromkeys(placeholders))  # Preserve order, remove duplicates

def fill_template(file_path, output_path=None):
    """Interactively fill template placeholders"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    placeholders = find_placeholders(content)
    
    if not placeholders:
        print("✅ No placeholders found in template")
        return content
    
    print(f"📝 Found {len(placeholders)} unique placeholders")
    print("=" * 60)
    print()
    
    values = {}
    for placeholder in placeholders:
        # Convert PLACEHOLDER_NAME to readable format
        readable = placeholder.replace('_', ' ').title()
        
        # Prompt user
        value = input(f"{readable} [{placeholder}]: ").strip()
        
        if not value:
            print(f"⚠️  Skipping {placeholder} (left empty)")
            continue
        
        values[placeholder] = value
    
    print()
    print("=" * 60)
    print(f"✅ Collected {len(values)} values")
    print()
    
    # Replace placeholders
    filled_content = content
    for placeholder, value in values.items():
        pattern = f'\\[{placeholder}\\]'
        filled_content = re.sub(pattern, value, filled_content)
    
    # Save filled template
    if output_path is None:
        output_path = file_path.parent / f"{file_path.stem}_filled{file_path.suffix}"
    
    with open(output_path, 'w') as f:
        f.write(filled_content)
    
    print(f"💾 Saved filled template to: {output_path}")
    
    # Check remaining placeholders
    remaining = find_placeholders(filled_content)
    if remaining:
        print(f"⚠️  {len(remaining)} placeholders still unfilled: {', '.join(remaining)}")
    else:
        print("✅ All placeholders filled!")
    
    return filled_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fill_template.py <template_file> [output_file]")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        sys.exit(1)
    
    print(f"🚀 Filling template: {file_path}")
    print()
    
    fill_template(file_path, output_path)

if __name__ == "__main__":
    main()
