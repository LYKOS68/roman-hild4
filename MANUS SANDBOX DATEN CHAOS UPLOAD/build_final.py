#!/usr/bin/env python3
"""Synergos Final Project Builder - Konsolidiert alle P1-P23 Dateien."""
import os, shutil, json, glob, datetime, zipfile

BASE = "/home/ubuntu"
FINAL = os.path.join(BASE, "synergos_final")

# 1. Clean & Create Structure
if os.path.exists(FINAL):
    shutil.rmtree(FINAL)

dirs = [
    "01_kern",
    "02_axiome_regeln",
    "03_pipeline",
    "04_protokolle",
    "05_stresstests",
    "06_referenz",
    "07_state"
]
for d in dirs:
    os.makedirs(os.path.join(FINAL, d), exist_ok=True)

# 2. Find all P-files
p_files = sorted(glob.glob(os.path.join(BASE, "p*_synergos_*.md")))
print(f"Gefunden: {len(p_files)} Dateien")

# 3. Copy all originals to 06_referenz
for f in p_files:
    shutil.copy2(f, os.path.join(FINAL, "06_referenz", os.path.basename(f)))

# Copy soul.md to root
soul = os.path.join(BASE, "soul.md")
if os.path.exists(soul):
    shutil.copy2(soul, os.path.join(FINAL, "soul.md"))

# 4. Categorize and copy to correct folders
categories = {
    "01_kern": ["p5_", "p10_", "p9_", "p22_"],
    "02_axiome_regeln": ["p2_", "p3_", "p8_", "p13_", "p15_", "p16_", "p18_", "p21_"],
    "03_pipeline": ["p6_", "p7_"],
    "04_protokolle": ["p1_", "p11_", "p12_", "p14_"],
    "05_stresstests": ["p17_", "p19_", "p20_", "p23_"],
}

for folder, prefixes in categories.items():
    for f in p_files:
        basename = os.path.basename(f)
        for prefix in prefixes:
            if basename.startswith(prefix):
                shutil.copy2(f, os.path.join(FINAL, folder, basename))
                break

# Also copy P4 (Referenzprompt) to 01_kern
for f in p_files:
    if os.path.basename(f).startswith("p4_"):
        shutil.copy2(f, os.path.join(FINAL, "01_kern", os.path.basename(f)))

# 5. Create MASTER_INDEX.json
index_entries = []
sektor_map = {
    "p1": ("Sektor 1", "Modellauskunft & Identität"),
    "p2": ("Sektor 1", "Design-Axiome (6 Regler)"),
    "p3": ("Sektor 1", "Struktur-Transfer-Theorie (5 Regeln)"),
    "p4": ("Sektor 1", "Referenz-Prompt (5-Elemente-Template)"),
    "p5": ("Sektor 1", "Kern-Prompt (Konsolidierung P1-P4)"),
    "p6": ("Sektor 2", "12-Stufen-Pipeline"),
    "p7": ("Sektor 2", "Dreischicht-Validierungsprotokoll"),
    "p8": ("Sektor 2", "4-Stufen Pattern-Extraktion"),
    "p9": ("Sektor 2", "Lehrmeister-Modus (Demo-Reflect-Invite)"),
    "p10": ("Sektor 3", "Resonanz-Engine (RTE)"),
    "p11": ("Sektor 3", "Co-adaptives System / State-Vector"),
    "p12": ("Sektor 3", "Meta-Programmierer-Befähigung (3 Stufen)"),
    "p13": ("Sektor 3", "Ephemeralitäts-Protokoll (16 Grenzen)"),
    "p14": ("Sektor 3", "Knowledge-Index-System"),
    "p15": ("Sektor 3", "Bias-Management (12 Biases)"),
    "p16": ("Sektor 3", "Nachhaltigkeits-Flux (3 Modi)"),
    "p17": ("Sektor 4", "Stresstest: Transparenz-Overload"),
    "p18": ("Sektor 4", "Stresstest: Reflexions-Paralyse"),
    "p19": ("Sektor 4", "Stresstest: Subjektivitäts-Kollaps"),
    "p20": ("Sektor 4", "Stresstest: Antagonistische Simulation"),
    "p21": ("Sektor 5", "Interaktions-Matrix"),
    "p22": ("Sektor 5", "Anti-Regressions-Protokoll"),
    "p23": ("Sektor 5", "Finaler Integrationstest"),
}

for f in p_files:
    basename = os.path.basename(f)
    key = basename.split("_")[0]
    sektor, beschreibung = sektor_map.get(key, ("Unbekannt", "Unbekannt"))
    size = os.path.getsize(f)
    
    # Find which folder it's in
    folder = "06_referenz"
    for cat_folder, prefixes in categories.items():
        for prefix in prefixes:
            if basename.startswith(prefix):
                folder = cat_folder
                break
    if basename.startswith("p4_"):
        folder = "01_kern"
    
    index_entries.append({
        "id": key.upper(),
        "datei": basename,
        "ordner": folder,
        "sektor": sektor,
        "beschreibung": beschreibung,
        "groesse_bytes": size,
        "typ": "markdown"
    })

master_index = {
    "projekt": "Synergos – Personal-GPT-Orchestration",
    "version": "1.0",
    "erstellt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "gesamt_artefakte": len(index_entries),
    "sektoren": {
        "Sektor 1 (P1-P5)": "Grundlogik – Axiome, Regeln, Kern-Prompt",
        "Sektor 2 (P6-P9)": "Werkzeuge – Pipeline, Validierung, Pattern, Didaktik",
        "Sektor 3 (P10-P16)": "Integration – RTE, State-Vector, Ethik, Modi",
        "Sektor 4 (P17-P20)": "Stresstests – Overload, Paralyse, Subjektivität, Antagonismus",
        "Sektor 5 (P21-P23)": "Konsolidierung – Matrix, Anti-Regression, Integrationstest"
    },
    "artefakte": index_entries
}

with open(os.path.join(FINAL, "MASTER_INDEX.json"), "w", encoding="utf-8") as f:
    json.dump(master_index, f, ensure_ascii=False, indent=2)

# 6. Create empty State-Vector template
state_vector = {
    "version": "0.1",
    "erstellt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "aktueller_modus": "STANDARD",
    "sitzungen": [],
    "offene_luecken": [],
    "regelversionierung": [],
    "bias_protokoll": [],
    "notizen": "Leere Vorlage – wird mit jeder Interaktion gefüllt."
}

with open(os.path.join(FINAL, "07_state", "state_vector.json"), "w", encoding="utf-8") as f:
    json.dump(state_vector, f, ensure_ascii=False, indent=2)

# 7. Create README.md
readme = """# SYNERGOS – Personal-GPT-Orchestration System

## Version 1.0 | Erstellt: """ + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + """

---

## Architektur

```
┌─────────────────────────────────────────────────────────┐
│                    SYNERGOS SYSTEM                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  SEKTOR 1: GRUNDLOGIK (P1-P5)                          │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐             │
│  │ P1  │→│ P2  │→│ P3  │→│ P4  │→│ P5  │             │
│  │Ident│ │Axiom│ │Regel│ │Templ│ │Kern │             │
│  └─────┘ └─────┘ └─────┘ └─────┘ └──┬──┘             │
│                                       │                 │
│  SEKTOR 2: WERKZEUGE (P6-P9)         │                 │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐   │                 │
│  │ P6  │→│ P7  │→│ P8  │→│ P9  │   │                 │
│  │Pipe │ │Valid│ │Patt │ │Lehr │   │                 │
│  └──┬──┘ └─────┘ └─────┘ └─────┘   │                 │
│     │                                │                 │
│  SEKTOR 3: INTEGRATION (P10-P16)     │                 │
│  ┌─────┐ ┌─────┐ ┌─────┐           │                 │
│  │ P10 │→│ P11 │→│P12-16│←──────────┘                 │
│  │ RTE │ │State│ │Proto │                              │
│  └──┬──┘ └─────┘ └──┬──┘                              │
│     │                │                                  │
│  SEKTOR 4: STRESSTESTS (P17-P20)                       │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                     │
│  │ P17 │ │ P18 │ │ P19 │ │ P20 │                     │
│  │Over │ │Para │ │Subj │ │Anti │                     │
│  └─────┘ └─────┘ └─────┘ └─────┘                     │
│                                                         │
│  SEKTOR 5: KONSOLIDIERUNG (P21-P23)                    │
│  ┌─────┐ ┌─────┐ ┌─────┐                              │
│  │ P21 │→│ P22 │→│ P23 │ ← MASTER-EXPORT              │
│  │Matrx│ │Regr │ │Test │                              │
│  └─────┘ └─────┘ └─────┘                              │
└─────────────────────────────────────────────────────────┘
```

## Ordnerstruktur

| Ordner | Inhalt | Zweck |
|--------|--------|-------|
| `01_kern/` | P4, P5, P9, P10, P22 | System-Prompts – die Master-Presets |
| `02_axiome_regeln/` | P2, P3, P8, P13, P15, P16, P18, P21 | Strukturierte Regeln und Axiome |
| `03_pipeline/` | P6, P7 | Pipeline-Definitionen und Validierung |
| `04_protokolle/` | P1, P11, P12, P14 | Operative Protokolle und State-Vector |
| `05_stresstests/` | P17, P19, P20, P23 | Resilienz-Tests und Ergebnisse |
| `06_referenz/` | P1-P23 komplett | Alle Originaldokumente |
| `07_state/` | state_vector.json | Leere Vorlage zum Starten |

## Schnellstart

1. **Kern-Prompt laden**: `01_kern/p5_synergos_kernprompt.md` in System Instructions einfügen
2. **RTE aktivieren**: `01_kern/p10_synergos_rte.md` als Erweiterung hinzufügen
3. **State-Vector starten**: `07_state/state_vector.json` als Projektdatei anlegen
4. **Modus wählen**: SCHNELL / STANDARD / GRÜNDLICH (siehe P16)

## Genie-Methoden

| Genie | Methode | Einsatz |
|-------|---------|---------|
| **Feynman** | Didaktik & Debugging | Erklärbar machen, Fehler finden |
| **Curie** | Systematische Extraktion | Reine Strukturen isolieren |
| **Allen** | GTD-Produktivität | Handlungsorientierung erzwingen |

## 6 Design-Axiome (aus P2)

1. **Nullpunkt-Kalibrierung** – Ist-Zustand vor allem
2. **Signal-Routing** – Richtige Aufgabe → Richtiges Tool
3. **Architektur-Zwang** – Plan vor Ergebnis
4. **Format-Schablone** – Starres Format erzwingen
5. **Frequenz-Hierarchie** – Master-Regeln nie überschreiben
6. **A/B-Referenz** – Messen, nicht raten

## Fail-Safe-Regeln (aus P17-P20)

- **FS-1**: Clipping-Detector (3 Iterationen → Notbremse)
- **FS-2**: Prioritäts-Kaskade: Nutzer > Grenzen > Modus > Bias > Axiome
- **FS-3**: Standardisiertes Notbremse-Format
- **FS-4**: Iterations-Timeout
- **S-0**: Meta-Regel bei subjektiven Widersprüchen

---

*Synergos v1.0 – 23-Prompt Personal-GPT-Orchestration System*
*Erstellt für Hirorohi782 | Heidelberg, 2026*
"""

with open(os.path.join(FINAL, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)

# 8. Create ZIP
zip_path = os.path.join(BASE, "synergos_final.zip")
if os.path.exists(zip_path):
    os.remove(zip_path)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs_list, files in os.walk(FINAL):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, FINAL)
            zf.write(filepath, os.path.join("synergos_final", arcname))

# 9. Delete loose files
for f in p_files:
    os.remove(f)
    print(f"Gelöscht: {os.path.basename(f)}")

# Delete old zip if exists
old_zip = os.path.join(BASE, "synergos_project.zip")
if os.path.exists(old_zip):
    os.remove(old_zip)
    print("Gelöscht: synergos_project.zip (alt)")

# 10. Summary
total_files = sum(1 for _, _, files in os.walk(FINAL) for _ in files)
zip_size = os.path.getsize(zip_path)
print(f"\n=== FERTIG ===")
print(f"Projektverzeichnis: {FINAL}")
print(f"Dateien im Projekt: {total_files}")
print(f"ZIP: {zip_path} ({zip_size / 1024:.1f} KB)")
print(f"Lose Dateien gelöscht: {len(p_files)}")
