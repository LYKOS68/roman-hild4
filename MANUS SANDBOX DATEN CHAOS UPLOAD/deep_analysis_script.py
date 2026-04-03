import os, json, datetime, re

base = '/home/ubuntu'

# 1. Alle Dateien sammeln (ohne hidden)
files = []
for root, dirs, fnames in os.walk(base):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for f in fnames:
        fp = os.path.join(root, f)
        try:
            stat = os.stat(fp)
            if stat.st_size > 0:
                rel = os.path.relpath(fp, base)
                files.append({
                    'path': rel,
                    'abs': fp,
                    'size': stat.st_size,
                    'ext': os.path.splitext(f)[1],
                    'dir': os.path.relpath(root, base),
                    'name': f
                })
        except:
            pass

# 2. Klassifizierung: Kern vs Boilerplate
core_files = []
boilerplate_files = []
support_files = []

for f in files:
    p = f['path']
    ext = f['ext']
    if f['dir'] == '.' and ext in ['.md', '.py', '.json']:
        if f['name'] in ['soul.md', 'ORCHESTRA.md', 'universales_operationsprotokoll.md', 'interaktionsprotokoll.md', 'prompt-orchester.md']:
            core_files.append({**f, 'category': 'PROTOCOL', 'reason': 'Kern-Protokoll des Systems'})
        elif ext == '.py':
            core_files.append({**f, 'category': 'SCRIPT', 'reason': 'Ausfuehrbares Analyse-Skript'})
        elif ext == '.json' and ('inventory' in f['name'] or 'classified' in f['name'] or 'flow' in f['name'] or 'action' in f['name']):
            core_files.append({**f, 'category': 'ANALYSIS_DATA', 'reason': 'Analyse-Ergebnis der Prompt-Kette'})
        else:
            support_files.append({**f, 'category': 'SUPPORT', 'reason': 'Unterstuetzende Datei'})
    elif 'skills/' in p and f['name'] == 'SKILL.md':
        core_files.append({**f, 'category': 'SKILL_DEF', 'reason': 'Fertigkeits-Definition'})
    elif 'skills/' in p and ext == '.py':
        core_files.append({**f, 'category': 'SKILL_SCRIPT', 'reason': 'Fertigkeits-Skript'})
    elif 'skills/' in p and 'templates' in p:
        boilerplate_files.append({**f, 'category': 'TEMPLATE', 'reason': 'Wiederverwendbare Vorlage'})
    elif 'skills/' in p:
        support_files.append({**f, 'category': 'SKILL_SUPPORT', 'reason': 'Referenz/Lizenz/Daten'})
    else:
        support_files.append({**f, 'category': 'OTHER', 'reason': 'Nicht eindeutig zuordenbar'})

# 3. Abhaengigkeitsmatrix aus Python-Imports
dependencies = {}
for f in files:
    if f['ext'] == '.py':
        try:
            with open(f['abs']) as fh:
                content = fh.read()
            imports = re.findall(r'^(?:import|from)\s+(\S+)', content, re.MULTILINE)
            deps_internal = []
            deps_external = []
            for imp in imports:
                mod = imp.split('.')[0]
                internal = any(ff['name'].replace('.py','') == mod for ff in files if ff['ext'] == '.py')
                if internal:
                    deps_internal.append(mod)
                else:
                    deps_external.append(mod)
            dependencies[f['path']] = {
                'internal': list(set(deps_internal)),
                'external': list(set(deps_external)),
                'has_main': '__main__' in content or 'if __name__' in content,
                'reads_files': bool(re.search(r'open\(|json\.load|read\(\)', content)),
                'writes_files': bool(re.search(r'json\.dump|write\(|open\(.+["\']w', content))
            }
        except:
            pass

# 4. Datenfluss bestimmen
data_flow = []
data_flow.append({'source': 'soul.md', 'target': 'ALL', 'type': 'CONFIGURES', 'desc': 'Master-Preset, definiert Kommunikationsstil und Regeln'})
data_flow.append({'source': 'universales_operationsprotokoll.md', 'target': 'ALL', 'type': 'GOVERNS', 'desc': 'UOP-Gate, keine Operation ohne Bestaetigung'})
data_flow.append({'source': 'interaktionsprotokoll.md', 'target': 'ALL', 'type': 'GOVERNS', 'desc': '3+1 Ebenen mit 6R-Check'})
data_flow.append({'source': 'ORCHESTRA.md', 'target': 'ALL', 'type': 'ORCHESTRATES', 'desc': 'Rollentrennung, Aufgabenzuordnung, Kommunikation'})

chain = [
    ('inventory.json', 'classify_score.py', 'FEEDS', 'Inventar wird klassifiziert'),
    ('classify_score.py', 'classified_inventory.json', 'PRODUCES', 'Erzeugt Klassifizierung'),
    ('classified_inventory.json', 'flow_detection.py', 'FEEDS', 'Klassifizierung wird analysiert'),
    ('flow_detection.py', 'flow_analysis.json', 'PRODUCES', 'Erzeugt Signalfluss-Analyse'),
    ('flow_analysis.json', 'action_orchestrator.py', 'FEEDS', 'Signalfluss wird in Aktionsplan umgesetzt'),
    ('action_orchestrator.py', 'action_plan.json', 'PRODUCES', 'Erzeugt Aktionsplan'),
]
for src, tgt, typ, desc in chain:
    data_flow.append({'source': src, 'target': tgt, 'type': typ, 'desc': desc})

# 5. Minimale Kernmechanismen
minimal_core = {
    'protocols': [f['path'] for f in core_files if f['category'] == 'PROTOCOL'],
    'analysis_chain': {
        'scripts': [f['path'] for f in core_files if f['category'] == 'SCRIPT'],
        'data': [f['path'] for f in core_files if f['category'] == 'ANALYSIS_DATA'],
        'required_libraries': ['os', 'json', 'datetime', 're'],
        'entry_point': 'classify_score.py (startet die Analyse-Kette)'
    },
    'skills': {
        'definitions': [f['path'] for f in core_files if f['category'] == 'SKILL_DEF'],
        'scripts': [f['path'] for f in core_files if f['category'] == 'SKILL_SCRIPT']
    }
}

# 6. Ergebnis zusammenbauen
result = {
    'analysis_type': 'DEEP_CORE_EXTRACTION',
    'timestamp': datetime.datetime.now(tz=datetime.timezone.utc).isoformat(),
    'summary': {
        'total_files': len(files),
        'core': len(core_files),
        'boilerplate': len(boilerplate_files),
        'support': len(support_files),
        'python_scripts': len(dependencies),
        'entry_points': [k for k,v in dependencies.items() if v.get('has_main')]
    },
    'core_files': [{
        'path': f['path'],
        'category': f['category'],
        'reason': f['reason'],
        'size_bytes': f['size']
    } for f in core_files],
    'boilerplate_files': [{
        'path': f['path'],
        'category': f['category'],
        'reason': f['reason'],
        'size_bytes': f['size']
    } for f in boilerplate_files],
    'dependency_matrix': dependencies,
    'data_flow': data_flow,
    'primary_data_flow_chain': 'inventory.json -> classify_score.py -> classified_inventory.json -> flow_detection.py -> flow_analysis.json -> action_orchestrator.py -> action_plan.json',
    'minimal_core_mechanisms': minimal_core,
    'chain_of_thought': [
        'SCHRITT 1: soul.md ist das Master-Preset - ohne diese Datei verliert das System seine Identitaet und Kommunikationsregeln',
        'SCHRITT 2: UOP + Interaktionsprotokoll sind die Mixer-Regler - sie steuern WIE interagiert wird (Bestaetigungspflicht, 3+1, 6R)',
        'SCHRITT 3: ORCHESTRA.md definiert WER was macht - Rollentrennung zwischen Director, Manus, Gemini, Claude, GPT-4o',
        'SCHRITT 4: Die Analyse-Kette (Inventar -> Klassifizierung -> Signalfluss -> Aktionsplan) ist der operative Signalfluss - die Murmelbahn',
        'SCHRITT 5: Die 8 Fertigkeiten (Skills) sind die Plugins - sie erweitern die Grundfunktionalitaet',
        'SCHRITT 6: Ohne die 4 Protokolle + die Analyse-Kette ist das System tot. Alles andere ist Support oder Vorlage.'
    ]
}

with open('deep_analysis.json', 'w') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print('=== TIEFENANALYSE ABGESCHLOSSEN ===')
print(f'Gesamt: {len(files)} Dateien')
print(f'Kern: {len(core_files)} | Vorlagen: {len(boilerplate_files)} | Unterstuetzung: {len(support_files)}')
print(f'Python-Skripte: {len(dependencies)}')
print(f'Einstiegspunkte: {[k for k,v in dependencies.items() if v.get("has_main")]}')
print()
print('PRIMAERER DATENFLUSS:')
print('inventory.json -> classify_score.py -> classified_inventory.json -> flow_detection.py -> flow_analysis.json -> action_orchestrator.py -> action_plan.json')
print()
print('MINIMALER KERN (ohne diese stirbt das System):')
for p in minimal_core['protocols']:
    print(f'  [PROTOKOLL] {p}')
for p in minimal_core['analysis_chain']['scripts']:
    print(f'  [SKRIPT]    {p}')
print()
print(f'BENOETIGTE BIBLIOTHEKEN: {minimal_core["analysis_chain"]["required_libraries"]}')
