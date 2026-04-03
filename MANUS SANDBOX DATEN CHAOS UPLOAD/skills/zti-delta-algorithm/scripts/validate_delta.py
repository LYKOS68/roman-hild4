#!/usr/bin/env python3
"""
Validiert einen ΔZ-BLOCK gegen definierte Invarianten.
Implementiert die D-Rolle (Delta / Übergeordneter Zustand).
"""

import yaml
import sys
import argparse
from typing import Dict, List

def load_delta_block(filepath: str) -> Dict:
    """Lädt einen ΔZ-BLOCK aus einer YAML-Datei."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data.get('DELTA_BLOCK', {})

def load_invariants(filepath: str) -> List[Dict]:
    """Lädt die Invarianten-Definitionen aus einer YAML-Datei."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data.get('INVARIANTS', [])

def check_invariants(delta_block: Dict, invariants: List[Dict]) -> tuple:
    """
    Prüft den Delta-Block gegen alle Invarianten.
    
    Returns:
        tuple: (PASS/FAIL, Regel-Beschreibung, Risiko-Flag)
    """
    for invariant in invariants:
        rule_name = invariant.get('name', 'UNKNOWN')
        rule_check = invariant.get('check', lambda x: True)
        
        # Hier würde eine echte Prüflogik implementiert werden.
        # Für dieses Template ist es ein Platzhalter.
        
        # Beispiel: Prüfe, ob DELTA_FIELDS nicht leer ist
        if len(delta_block.get('DELTA_FIELDS', [])) == 0:
            return ('FAIL', f"Regel: {rule_name} - DELTA_FIELDS darf nicht leer sein", 'N')
    
    # Beispiel: Setze RISK_FLAG auf 'Y', wenn mehr als 3 Änderungen vorliegen
    risk_flag = 'Y' if len(delta_block.get('DELTA_FIELDS', [])) > 3 else 'N'
    
    return ('PASS', f"Alle Invarianten erfüllt", risk_flag)

def main():
    parser = argparse.ArgumentParser(description='Validiert einen ΔZ-BLOCK.')
    parser.add_argument('delta_block_file', type=str, help='Pfad zur ΔZ-BLOCK YAML-Datei')
    parser.add_argument('--invariants', type=str, default=None, help='Pfad zur Invarianten-Definitions-Datei')
    
    args = parser.parse_args()
    
    delta_block = load_delta_block(args.delta_block_file)
    
    if args.invariants:
        invariants = load_invariants(args.invariants)
    else:
        # Verwende Standard-Invarianten
        invariants = [
            {'name': 'NON_EMPTY_FIELDS', 'check': lambda x: len(x.get('DELTA_FIELDS', [])) > 0}
        ]
    
    check_result, rule_description, risk_flag = check_invariants(delta_block, invariants)
    
    print(f"INVARIANTS_CHECK: {check_result}")
    print(f"Regel: {rule_description}")
    print(f"RISK_FLAG: {risk_flag}")
    print(f"SHADOW_REQUIRED: {'YES' if risk_flag == 'Y' else 'NO'}")
    
    if check_result == 'FAIL':
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
