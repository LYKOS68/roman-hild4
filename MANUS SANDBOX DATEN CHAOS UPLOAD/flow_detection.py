import json, os, re
from datetime import datetime, timezone

# Lade Inputs
with open('/home/ubuntu/inventory.json') as f:
    inv = json.load(f)
with open('/home/ubuntu/classified_inventory.json') as f:
    cls = json.load(f)

# Konfiguration
config = {
    "entry_patterns": ["main", "cli", "index", "start", "run", "cmd", "execute", "bin", "init"],
    "script_extensions": [".py", ".sh", ".ps1", ".bat", ".js"],
    "config_extensions": [".toml", ".json", ".yaml", ".ini", ".conf", ".yml"],
    "data_extensions": [".csv", ".json", ".db", ".sqlite", ".log"],
    "worm_chain_paths": ["blocks", "worm.log", "chain"],
    "manifest_files": ["manifest.toml", "pattern_db.json", "state.json"]
}

base = "/home/ubuntu"
files_by_path = {item["filepath"]: item for item in inv["inventory"]}
cls_by_path = {item["filepath"]: item for item in cls["classified_files"]}

# --- 1. EINSTIEGSPUNKTE ---
entry_points = []
for fp, item in files_by_path.items():
    ext = item["extension"]
    fname = item["filename"].lower()
    fname_no_ext = os.path.splitext(fname)[0]
    
    if ext not in config["script_extensions"]:
        continue
    
    matched_patterns = []
    for pat in config["entry_patterns"]:
        if pat in fname_no_ext or pat in fp.lower():
            matched_patterns.append(pat)
    
    # Typ bestimmen
    type_map = {
        ".py": "python_module",
        ".sh": "shell_script",
        ".ps1": "powershell_script",
        ".bat": "batch_script",
        ".js": "javascript_module"
    }
    ftype = type_map.get(ext, "unknown_script")
    
    # Confidence berechnen
    confidence = 0.50
    if matched_patterns:
        confidence += 0.15 * len(matched_patterns)
    if ext == ".py":
        confidence += 0.10
    # Prüfe ob Datei tatsächlich ausführbar aussieht
    full_path = os.path.join(base, fp)
    if os.path.exists(full_path):
        try:
            with open(full_path, 'r', errors='ignore') as f:
                content = f.read(2000)
            if 'if __name__' in content or '#!/' in content or 'def main' in content:
                confidence += 0.15
                matched_patterns.append("main_guard")
            if 'import ' in content or 'from ' in content:
                confidence += 0.05
            if 'argparse' in content or 'sys.argv' in content or 'click' in content:
                confidence += 0.10
                matched_patterns.append("cli_args")
        except:
            pass
    
    confidence = min(1.0, round(confidence, 2))
    
    if confidence >= 0.50:
        entry_points.append({
            "filepath": fp,
            "type": ftype,
            "confidence": confidence,
            "detected_patterns": list(set(matched_patterns))
        })

entry_points.sort(key=lambda x: -x["confidence"])

# --- 2. DATENFLÜSSE ---
data_flows = []
# Analysiere Python-Dateien auf imports und Datei-Operationen
py_files = [fp for fp in files_by_path if fp.endswith('.py')]
import_map = {}  # file -> list of imported modules

for fp in py_files:
    full_path = os.path.join(base, fp)
    if not os.path.exists(full_path):
        continue
    try:
        with open(full_path, 'r', errors='ignore') as f:
            content = f.read()
    except:
        continue
    
    imports = []
    # from X import Y / import X
    for m in re.finditer(r'(?:from\s+(\S+)\s+import|import\s+(\S+))', content):
        mod = m.group(1) or m.group(2)
        imports.append(mod)
    
    import_map[fp] = imports
    
    # Datei-Operationen erkennen
    file_ops = []
    if re.search(r'open\s*\(', content):
        file_ops.append("file_io")
    if re.search(r'json\.(dump|load)', content):
        file_ops.append("json_io")
    if re.search(r'(Path|os\.path|pathlib)', content):
        file_ops.append("path_ops")
    if re.search(r'(write|append|create)', content, re.I):
        file_ops.append("write_ops")
    if re.search(r'(read|load|parse)', content, re.I):
        file_ops.append("read_ops")
    
    # Finde referenzierte Dateien
    for ref_fp in files_by_path:
        ref_name = os.path.splitext(files_by_path[ref_fp]["filename"])[0]
        if ref_fp != fp and ref_name in content and len(ref_name) > 3:
            flow_type = "reference"
            if any(op in ["write_ops", "json_io"] for op in file_ops):
                flow_type = "read_write"
            elif "read_ops" in file_ops:
                flow_type = "read"
            data_flows.append({
                "source": fp,
                "target": ref_fp,
                "type": flow_type,
                "frequency": "medium"
            })

# Skill-interne Flows: SKILL.md -> scripts -> references -> templates
skill_dirs = set()
for fp in files_by_path:
    parts = fp.split("/")
    if len(parts) >= 2 and parts[0] == "skills":
        skill_dirs.add(parts[1])

for skill in skill_dirs:
    skill_files = [fp for fp in files_by_path if fp.startswith(f"skills/{skill}/")]
    skill_md = [fp for fp in skill_files if fp.endswith("SKILL.md")]
    scripts = [fp for fp in skill_files if "/scripts/" in fp]
    refs = [fp for fp in skill_files if "/references/" in fp]
    templates = [fp for fp in skill_files if "/templates/" in fp]
    
    # SKILL.md definiert -> scripts führen aus
    for sm in skill_md:
        for sc in scripts:
            data_flows.append({
                "source": sm,
                "target": sc,
                "type": "defines",
                "frequency": "high"
            })
    # Scripts nutzen references
    for sc in scripts:
        for ref in refs:
            data_flows.append({
                "source": sc,
                "target": ref,
                "type": "reads",
                "frequency": "medium"
            })
    # Scripts nutzen templates
    for sc in scripts:
        for tpl in templates:
            data_flows.append({
                "source": sc,
                "target": tpl,
                "type": "loads_template",
                "frequency": "medium"
            })

# Root-Dokument-Flows
root_docs = [fp for fp in files_by_path if files_by_path[fp]["directory"] == "." and fp.endswith(".md")]
if len(root_docs) > 1:
    # soul.md ist das Master-Preset, andere referenzieren es
    if "soul.md" in root_docs:
        for doc in root_docs:
            if doc != "soul.md":
                data_flows.append({
                    "source": "soul.md",
                    "target": doc,
                    "type": "configures",
                    "frequency": "high"
                })

# Dedupliziere Flows
seen_flows = set()
unique_flows = []
for flow in data_flows:
    key = f"{flow['source']}|{flow['target']}|{flow['type']}"
    if key not in seen_flows:
        seen_flows.add(key)
        unique_flows.append(flow)

# --- 3. WORM-CHAIN ANALYSE ---
worm_detected = False
worm_files = []
for fp in files_by_path:
    for wpath in config["worm_chain_paths"]:
        if wpath in fp.lower():
            worm_detected = True
            worm_files.append(fp)

worm_analysis = {
    "detected": worm_detected,
    "worm_log": worm_files[0] if worm_files else None,
    "block_files": worm_files,
    "integrity_indicators": ["none_found"] if not worm_detected else ["hash_chain", "timestamp_sequence"]
}

# --- 4. ABHÄNGIGKEITSMATRIX ---
dep_matrix = []
all_scripts = [fp for fp in files_by_path if files_by_path[fp]["extension"] in config["script_extensions"]]

for fp in all_scripts:
    depends_on = []
    used_by = []
    
    for flow in unique_flows:
        if flow["source"] == fp:
            depends_on.append(flow["target"])
        if flow["target"] == fp:
            used_by.append(flow["source"])
    
    dep_matrix.append({
        "file": fp,
        "depends_on": list(set(depends_on)),
        "used_by": list(set(used_by))
    })

# Auch für Kerndokumente
for fp in root_docs:
    depends_on = []
    used_by = []
    for flow in unique_flows:
        if flow["source"] == fp:
            depends_on.append(flow["target"])
        if flow["target"] == fp:
            used_by.append(flow["source"])
    dep_matrix.append({
        "file": fp,
        "depends_on": list(set(depends_on)),
        "used_by": list(set(used_by))
    })

# --- 5. MANIFEST-REFERENZEN ---
manifest_refs = {}
for mf in config["manifest_files"]:
    found = [fp for fp in files_by_path if files_by_path[fp]["filename"] == mf]
    if found:
        manifest_refs[mf] = {
            "status": "found",
            "filepath": found[0],
            "last_updated": files_by_path[found[0]]["mtime_iso"]
        }
    else:
        manifest_refs[mf] = {"status": "not_found"}

# --- ERGEBNIS ---
result = {
    "entry_points": entry_points,
    "data_flow": {
        "primary": unique_flows
    },
    "worm_chain_analysis": worm_analysis,
    "dependency_matrix": dep_matrix,
    "manifest_references": manifest_refs
}

with open("/home/ubuntu/flow_analysis.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"Einstiegspunkte: {len(entry_points)}")
print(f"Datenflüsse: {len(unique_flows)}")
print(f"WORM-Chain: {'Erkannt' if worm_detected else 'Nicht erkannt'}")
print(f"Abhängigkeiten: {len(dep_matrix)} Einträge")
print(f"Manifeste: {sum(1 for v in manifest_refs.values() if v['status']=='found')}/{len(manifest_refs)} gefunden")

for ep in entry_points[:5]:
    print(f"  -> {ep['filepath']} ({ep['type']}, {ep['confidence']})")
