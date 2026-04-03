import json, os
from datetime import datetime, timezone

# Lade Inputs
with open('/home/ubuntu/classified_inventory.json') as f:
    cls = json.load(f)
with open('/home/ubuntu/flow_analysis.json') as f:
    flow = json.load(f)
with open('/home/ubuntu/inventory.json') as f:
    inv = json.load(f)

# Konfiguration
config = {
    "archive_threshold_days": 365,
    "review_threshold_days": 180,
    "delete_after_days": 730,
    "min_file_size_bytes": 50,
    "exempt_patterns": [".git", "README", "LICENSE", ".keep"],
    "backup_location": "./archive/",
    "worm_chain_protection": True
}

now = datetime.now(tz=timezone.utc)

# Lookup-Maps
cls_by_path = {item["filepath"]: item for item in cls["classified_files"]}
inv_by_path = {item["filepath"]: item for item in inv["inventory"]}

# Entry Points als Set
entry_point_files = set(ep["filepath"] for ep in flow["entry_points"])

# Abhängigkeits-Map: Welche Dateien werden von Core benötigt?
dependency_files = set()
for dep in flow["dependency_matrix"]:
    if dep["file"] in entry_point_files or cls_by_path.get(dep["file"], {}).get("category") == "core":
        for d in dep["depends_on"]:
            dependency_files.add(d)
    for u in dep["used_by"]:
        dependency_files.add(dep["file"])

# Datenfluss: Welche Dateien sind Quellen/Ziele?
flow_connected = set()
for f in flow["data_flow"]["primary"]:
    flow_connected.add(f["source"])
    flow_connected.add(f["target"])

# WORM-Chain geschützte Pfade
worm_analysis = flow["worm_chain_analysis"]
protected_paths = set()
if worm_analysis["detected"]:
    for bf in worm_analysis.get("block_files", []):
        protected_paths.add(bf)
    if worm_analysis.get("worm_log"):
        protected_paths.add(worm_analysis["worm_log"])

# Manifest-Dateien schützen
for mf, info in flow["manifest_references"].items():
    if info["status"] == "found":
        protected_paths.add(info.get("filepath", mf))

# Exempt-Patterns
def is_exempt(filepath):
    for pat in config["exempt_patterns"]:
        if pat.lower() in filepath.lower():
            return True
    return False

# Aktionsplan erstellen
actions = []
summary = {
    "total_essential": 0,
    "total_dependencies": 0,
    "total_archive": 0,
    "total_review": 0,
    "total_delete": 0,
    "total_protected": 0
}
archive_files = []

for item in cls["classified_files"]:
    fp = item["filepath"]
    cat = item["category"]
    score = item["score"]
    heuristics = item["heuristics"]
    age_days = heuristics["age_days"]
    size = inv_by_path.get(fp, {}).get("size_bytes", 0)
    
    action_entry = {
        "filepath": fp,
        "action": None,
        "priority": 5,
        "reason": "",
        "verification_required": False,
        "backup_before_action": False
    }
    
    # 1. PROTECTED: WORM-Chain und Manifeste
    if fp in protected_paths:
        action_entry["action"] = "PROTECTED"
        action_entry["priority"] = 0
        action_entry["reason"] = "WORM-Chain oder Manifest-Datei – unveränderlich geschützt"
        summary["total_protected"] += 1
    
    # 2. KEEP_ESSENTIAL: Core + Entry Points
    elif fp in entry_point_files:
        action_entry["action"] = "KEEP_ESSENTIAL"
        action_entry["priority"] = 1
        action_entry["reason"] = f"Aktiver Einstiegspunkt (Konfidenz: {next((ep['confidence'] for ep in flow['entry_points'] if ep['filepath'] == fp), 'N/A')})"
        summary["total_essential"] += 1
    
    elif cat == "core" and score >= 0.80:
        action_entry["action"] = "KEEP_ESSENTIAL"
        action_entry["priority"] = 1
        action_entry["reason"] = f"Kern-Datei mit hohem Score ({score}). {'; '.join(item['reasons'])}"
        summary["total_essential"] += 1
    
    elif cat == "core" and fp in flow_connected:
        action_entry["action"] = "KEEP_ESSENTIAL"
        action_entry["priority"] = 1
        action_entry["reason"] = f"Kern-Datei im aktiven Signalfluss. {'; '.join(item['reasons'])}"
        summary["total_essential"] += 1
    
    # 3. KEEP_DEPENDENCY: Von Core benötigte Dateien
    elif fp in dependency_files:
        action_entry["action"] = "KEEP_DEPENDENCY"
        action_entry["priority"] = 2
        action_entry["reason"] = f"Wird von Kern-Dateien benötigt (Abhängigkeit)"
        summary["total_dependencies"] += 1
    
    elif cat == "support" and fp in flow_connected:
        action_entry["action"] = "KEEP_DEPENDENCY"
        action_entry["priority"] = 2
        action_entry["reason"] = f"Unterstützungsdatei im aktiven Signalfluss"
        summary["total_dependencies"] += 1
    
    # 4. Exempt-Dateien
    elif is_exempt(fp):
        action_entry["action"] = "KEEP_DEPENDENCY"
        action_entry["priority"] = 2
        action_entry["reason"] = f"Ausgenommen durch Exempt-Pattern"
        summary["total_dependencies"] += 1
    
    # 5. ARCHIVE: Alte Boilerplate, ungenutzte Support
    elif cat == "boilerplate" and age_days > config["archive_threshold_days"]:
        action_entry["action"] = "ARCHIVE"
        action_entry["priority"] = 3
        action_entry["reason"] = f"Vorlage, {age_days} Tage alt, ungenutzt"
        action_entry["backup_before_action"] = True
        action_entry["archive_path"] = f"archive/{fp}"
        archive_files.append({"filepath": fp, "size": size})
        summary["total_archive"] += 1
    
    elif cat == "support" and age_days > config["archive_threshold_days"] and fp not in flow_connected:
        action_entry["action"] = "ARCHIVE"
        action_entry["priority"] = 3
        action_entry["reason"] = f"Unterstützungsdatei, {age_days} Tage alt, nicht im Signalfluss"
        action_entry["backup_before_action"] = True
        action_entry["archive_path"] = f"archive/{fp}"
        archive_files.append({"filepath": fp, "size": size})
        summary["total_archive"] += 1
    
    # 6. DELETE_CANDIDATE: Isoliert, alt, temporär
    elif heuristics["is_temporal"] and age_days > config["review_threshold_days"]:
        action_entry["action"] = "DELETE_CANDIDATE"
        action_entry["priority"] = 5
        action_entry["reason"] = f"Temporäre Datei, {age_days} Tage alt"
        action_entry["verification_required"] = True
        summary["total_delete"] += 1
    
    elif size < config["min_file_size_bytes"] and cat != "core" and fp not in flow_connected:
        action_entry["action"] = "DELETE_CANDIDATE"
        action_entry["priority"] = 5
        action_entry["reason"] = f"Unter Mindestgröße ({size} Bytes), nicht im Signalfluss"
        action_entry["verification_required"] = True
        summary["total_delete"] += 1
    
    elif age_days > config["delete_after_days"] and fp not in flow_connected and cat not in ["core"]:
        action_entry["action"] = "DELETE_CANDIDATE"
        action_entry["priority"] = 5
        action_entry["reason"] = f"Über {config['delete_after_days']} Tage alt, isoliert"
        action_entry["verification_required"] = True
        summary["total_delete"] += 1
    
    # 7. REVIEW: Unknown oder Grenzfälle
    elif cat == "unknown":
        action_entry["action"] = "REVIEW"
        action_entry["priority"] = 4
        action_entry["reason"] = f"Nicht klassifizierbar – manuelle Prüfung nötig. {'; '.join(item['reasons'])}"
        action_entry["verification_required"] = True
        summary["total_review"] += 1
    
    # 8. Alles andere: KEEP basierend auf Kategorie
    elif cat == "core":
        action_entry["action"] = "KEEP_ESSENTIAL"
        action_entry["priority"] = 1
        action_entry["reason"] = f"Kern-Datei. {'; '.join(item['reasons'])}"
        summary["total_essential"] += 1
    
    elif cat == "support":
        action_entry["action"] = "KEEP_DEPENDENCY"
        action_entry["priority"] = 2
        action_entry["reason"] = f"Aktive Unterstützungsdatei. {'; '.join(item['reasons'])}"
        summary["total_dependencies"] += 1
    
    elif cat == "boilerplate":
        action_entry["action"] = "KEEP_DEPENDENCY"
        action_entry["priority"] = 2
        action_entry["reason"] = f"Aktive Vorlage (unter Archiv-Schwelle). {'; '.join(item['reasons'])}"
        summary["total_dependencies"] += 1
    
    else:
        action_entry["action"] = "REVIEW"
        action_entry["priority"] = 4
        action_entry["reason"] = "Keine klare Zuordnung möglich"
        action_entry["verification_required"] = True
        summary["total_review"] += 1
    
    actions.append(action_entry)

# Sortiere nach Priorität
actions.sort(key=lambda x: (x["priority"], x["filepath"]))

# Ergebnis
result = {
    "actions": actions,
    "summary": summary,
    "archive_plan": {
        "target_directory": config["backup_location"],
        "estimated_size_bytes": sum(af["size"] for af in archive_files),
        "file_count": len(archive_files)
    },
    "protected_paths": list(protected_paths) if protected_paths else ["Keine WORM-Chain oder Manifeste im Workspace erkannt"]
}

with open("/home/ubuntu/action_plan.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"\n=== AKTIONSPLAN ===")
print(f"KEEP_ESSENTIAL:  {summary['total_essential']}")
print(f"KEEP_DEPENDENCY: {summary['total_dependencies']}")
print(f"ARCHIVE:         {summary['total_archive']}")
print(f"REVIEW:          {summary['total_review']}")
print(f"DELETE_CANDIDATE: {summary['total_delete']}")
print(f"PROTECTED:       {summary['total_protected']}")
print(f"GESAMT:          {sum(summary.values())}")
print(f"\nArchiv-Plan: {len(archive_files)} Dateien, {sum(af['size'] for af in archive_files)} Bytes")
print(f"\nTop-5 Aktionen:")
for a in actions[:5]:
    print(f"  [{a['action']}] {a['filepath']} – {a['reason'][:60]}")
