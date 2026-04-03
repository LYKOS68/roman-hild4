import json, math
from datetime import datetime, timezone

# Lade Inventar
with open('/home/ubuntu/inventory.json') as f:
    inv = json.load(f)

# Konfiguration
config = {
    "age_threshold_days": 180,
    "size_threshold_bytes": 1048576,
    "core_paths": ["src", "lib", "bin", "core", "scripts"],
    "support_paths": ["docs", "tests", "examples", "config", "references", "templates"],
    "boilerplate_paths": ["templates", "scaffold", "generated"],
    "critical_extensions": [".py", ".js", ".go", ".rs", ".toml", ".json"],
    "temporal_extensions": [".log", ".tmp", ".cache", ".pid"]
}

now = datetime.now(tz=timezone.utc)
classified = []
stats_cat = {"core": 0, "support": 0, "boilerplate": 0, "unknown": 0}
stats_age = {"under_30_days": 0, "30_to_180_days": 0, "over_180_days": 0}
stats_size = {"small_under_10kb": 0, "medium_10kb_to_1mb": 0, "large_over_1mb": 0}

for item in inv["inventory"]:
    fp = item["filepath"]
    ext = item["extension"]
    size = item["size_bytes"]
    mtime = datetime.strptime(item["mtime_iso"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    age_days = (now - mtime).days
    
    # Heuristiken
    path_parts = fp.lower().replace("\\", "/").split("/")
    is_old = age_days > config["age_threshold_days"]
    is_large = size > config["size_threshold_bytes"]
    is_temporal = ext in config["temporal_extensions"]
    
    # Pfad-Matches
    core_match = [p for p in config["core_paths"] if any(p in part for part in path_parts)]
    support_match = [p for p in config["support_paths"] if any(p in part for part in path_parts)]
    boilerplate_match = [p for p in config["boilerplate_paths"] if any(p in part for part in path_parts)]
    
    # Größen-Klasse
    if size < 10240:
        size_class = "small"
        stats_size["small_under_10kb"] += 1
    elif size < 1048576:
        size_class = "medium"
        stats_size["medium_10kb_to_1mb"] += 1
    else:
        size_class = "large"
        stats_size["large_over_1mb"] += 1
    
    # Alter-Klasse
    if age_days < 30:
        stats_age["under_30_days"] += 1
    elif age_days <= 180:
        stats_age["30_to_180_days"] += 1
    else:
        stats_age["over_180_days"] += 1
    
    # Klassifizierung
    reasons = []
    score = 0.5
    category = "unknown"
    
    # Root-Level .md Dateien = Kerndateien (Protokolle, Profil)
    if item["directory"] == "." and ext == ".md":
        category = "core"
        score = 0.95
        reasons.append("Wurzelverzeichnis-Protokoll/Profil")
        reasons.append("Markdown-Kerndokument")
    elif item["directory"] == "." and ext == ".json":
        category = "support"
        score = 0.80
        reasons.append("Wurzelverzeichnis-Datendatei")
    elif item["directory"] == "." and ext == ".txt":
        category = "support"
        score = 0.60
        reasons.append("Wurzelverzeichnis-Textdatei")
    elif is_temporal:
        category = "boilerplate"
        score = 0.90
        reasons.append("Temporäre Datei")
    elif boilerplate_match and not core_match:
        category = "boilerplate"
        score = 0.75
        reasons.append(f"Vorlagen-Verzeichnis: {', '.join(boilerplate_match)}")
    elif core_match or ext in config["critical_extensions"]:
        # Skripte in Skills = core
        if "scripts" in path_parts or "scripts" in fp.lower():
            category = "core"
            score = 0.90
            reasons.append("Ausführbares Skript")
        elif ext in config["critical_extensions"]:
            category = "core"
            score = 0.85
            reasons.append(f"Kritische Erweiterung: {ext}")
        else:
            category = "core"
            score = 0.80
        if core_match:
            reasons.append(f"Kern-Pfad: {', '.join(core_match)}")
    elif support_match:
        category = "support"
        score = 0.80
        reasons.append(f"Unterstützungs-Pfad: {', '.join(support_match)}")
    elif ext == ".md":
        # SKILL.md, README etc in Unterverzeichnissen
        if "skill" in fp.lower():
            category = "core"
            score = 0.85
            reasons.append("Fertigkeits-Definition")
        else:
            category = "support"
            score = 0.70
            reasons.append("Dokumentation")
    elif ext == ".yaml" or ext == ".yml":
        if "references" in fp.lower():
            category = "support"
            score = 0.75
            reasons.append("Referenz-Konfiguration")
        else:
            category = "core"
            score = 0.80
            reasons.append("Konfigurationsdatei")
    elif ext == ".txt":
        if "license" in fp.lower():
            category = "support"
            score = 0.65
            reasons.append("Lizenzdatei")
        else:
            category = "unknown"
            score = 0.40
            reasons.append("Nicht eindeutig klassifizierbar")
    else:
        category = "unknown"
        score = 0.30
        reasons.append("Keine Heuristik-Übereinstimmung")
    
    # Score-Modifikatoren
    if age_days < 7:
        score = min(1.0, score + 0.05)
        reasons.append("Kürzlich geändert (< 7 Tage)")
    if is_old:
        score = max(0.0, score - 0.10)
        reasons.append("Veraltet (> 180 Tage)")
    
    stats_cat[category] += 1
    
    classified.append({
        "filepath": fp,
        "category": category,
        "score": round(score, 2),
        "heuristics": {
            "path_match": core_match + support_match + boilerplate_match,
            "size": size_class,
            "age_days": age_days,
            "extension": ext,
            "is_old": is_old,
            "is_large": is_large,
            "is_temporal": is_temporal
        },
        "reasons": reasons
    })

result = {
    "classified_files": sorted(classified, key=lambda x: (-x["score"], x["filepath"])),
    "statistics": {
        "by_category": stats_cat,
        "by_age": stats_age,
        "by_size": stats_size
    }
}

with open("/home/ubuntu/classified_inventory.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"Klassifiziert: {len(classified)} Dateien")
print(f"Kategorien: {json.dumps(stats_cat)}")
print(f"Alter: {json.dumps(stats_age)}")
print(f"Größe: {json.dumps(stats_size)}")
