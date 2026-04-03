# Tiefenanalyse – Manus Sandbox /home/ubuntu
**Zeitstempel:** 2026-03-20T17:46:32.577820+00:00

Willkommen im Studio. Hier ist der Mixdown der Sandbox-Architektur – roh, direkt und ohne akademisches Gelaber. Wir schauen uns die Spuren, die Plugins und das Routing an.

## ZUSAMMENFASSUNG
Das ist unser Projekt-Status. Die nackten Zahlen des Mixes:

| Metrik | Anzahl | Beschreibung |
| :--- | :--- | :--- |
| **Total Files** | 223 | Alle Spuren im Projekt |
| **Core Files** | 31 | Die Master-Spuren (Protokolle & Main-Scripts) |
| **Boilerplate** | 6 | Die Templates & Presets |
| **Support Files** | 186 | Samples, Bounces und Hilfsdateien |
| **Python Scripts** | 13 | Unsere aktiven Effekt-Plugins |
| **Entry Points** | 11 | Die Trigger-Pads für die Automation |

## KERN-DATEIEN
Das sind die Main-Vocals und Lead-Synths. Ohne die läuft hier gar nichts.

| Pfad | Kategorie | Begründung | Größe (Bytes) |
| :--- | :--- | :--- | :--- |
| `inventory.json` | ANALYSIS_DATA | Analyse-Ergebnis der Prompt-Kette | 12073 |
| `classified_inventory.json` | ANALYSIS_DATA | Analyse-Ergebnis der Prompt-Kette | 21506 |
| `flow_analysis.json` | ANALYSIS_DATA | Analyse-Ergebnis der Prompt-Kette | 22235 |
| `action_plan.json` | ANALYSIS_DATA | Analyse-Ergebnis der Prompt-Kette | 13211 |
| `inventory_v2.json` | ANALYSIS_DATA | Analyse-Ergebnis der Prompt-Kette | 16273 |
| `soul.md` | PROTOCOL | Kern-Protokoll des Systems | 4773 |
| `universales_operationsprotokoll.md` | PROTOCOL | Kern-Protokoll des Systems | 2786 |
| `interaktionsprotokoll.md` | PROTOCOL | Kern-Protokoll des Systems | 2993 |
| `prompt-orchester.md` | PROTOCOL | Kern-Protokoll des Systems | 30847 |
| `ORCHESTRA.md` | PROTOCOL | Kern-Protokoll des Systems | 31145 |
| `classify_score.py` | SCRIPT | Ausfuehrbares Analyse-Skript | 6231 |
| `flow_detection.py` | SCRIPT | Ausfuehrbares Analyse-Skript | 9403 |
| `action_orchestrator.py` | SCRIPT | Ausfuehrbares Analyse-Skript | 9650 |
| `deep_analysis_script.py` | SCRIPT | Ausfuehrbares Analyse-Skript | 8290 |
| `skills/gws-best-practices/SKILL.md` | SKILL_DEF | Fertigkeits-Definition | 3541 |
| `skills/prompt-calibration-triggering/SKILL.md` | SKILL_DEF | Fertigkeits-Definition | 20798 |
| `skills/mapping-analysis-templates/SKILL.md` | SKILL_DEF | Fertigkeits-Definition | 5415 |
| `skills/universal-template-generator/SKILL.md` | SKILL_DEF | Fertigkeits-Definition | 8416 |
| `skills/internet-skill-finder/SKILL.md` | SKILL_DEF | Fertigkeits-Definition | 1746 |
| `skills/skill-creator/SKILL.md` | SKILL_DEF | Fertigkeits-Definition | 10326 |
| `skills/zti-delta-algorithm/SKILL.md` | SKILL_DEF | Fertigkeits-Definition | 3858 |
| `skills/prompt-engineering-system/SKILL.md` | SKILL_DEF | Fertigkeits-Definition | 4669 |
| `skills/mapping-analysis-templates/scripts/generate_schema.py` | SKILL_SCRIPT | Fertigkeits-Skript | 16505 |
| `skills/mapping-analysis-templates/scripts/validate_mapping.py` | SKILL_SCRIPT | Fertigkeits-Skript | 11521 |
| `skills/universal-template-generator/scripts/validate_template.py` | SKILL_SCRIPT | Fertigkeits-Skript | 4325 |
| `skills/universal-template-generator/scripts/fill_template.py` | SKILL_SCRIPT | Fertigkeits-Skript | 2627 |
| `skills/internet-skill-finder/scripts/fetch_skills.py` | SKILL_SCRIPT | Fertigkeits-Skript | 15538 |
| `skills/skill-creator/scripts/init_skill.py` | SKILL_SCRIPT | Fertigkeits-Skript | 10763 |
| `skills/skill-creator/scripts/quick_validate.py` | SKILL_SCRIPT | Fertigkeits-Skript | 4749 |
| `skills/zti-delta-algorithm/scripts/validate_delta.py` | SKILL_SCRIPT | Fertigkeits-Skript | 2700 |
| `skills/prompt-engineering-system/scripts/generate_prompt.py` | SKILL_SCRIPT | Fertigkeits-Skript | 1730 |

## ABHÄNGIGKEITSMATRIX
Das Routing-Board. Wer sendet an wen? Wer liest, wer schreibt?

| Skript | Externe Libs | Interne Libs | Entry Point (Main) | Liest Dateien | Schreibt Dateien |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `classify_score.py` | datetime, json | - | Nein | Ja | Ja |
| `flow_detection.py` | datetime, json | - | Ja | Ja | Ja |
| `action_orchestrator.py` | datetime, json | - | Nein | Ja | Ja |
| `deep_analysis_script.py` | os | - | Ja | Ja | Ja |
| `skills/mapping-analysis-templates/scripts/generate_schema.py` | json, sys, typing | - | Ja | Ja | Ja |
| `skills/mapping-analysis-templates/scripts/validate_mapping.py` | json, sys, typing | - | Ja | Ja | Nein |
| `skills/universal-template-generator/scripts/validate_template.py` | re, sys, pathlib, yaml | - | Ja | Ja | Nein |
| `skills/universal-template-generator/scripts/fill_template.py` | re, sys, pathlib | - | Ja | Ja | Ja |
| `skills/internet-skill-finder/scripts/fetch_skills.py` | json, re, sys, subprocess, pathlib, urllib, os, base64 | - | Ja | Ja | Ja |
| `skills/skill-creator/scripts/init_skill.py` | sys, pathlib | - | Ja | Nein | Nein |
| `skills/skill-creator/scripts/quick_validate.py` | re, sys, pathlib, yaml | - | Ja | Nein | Nein |
| `skills/zti-delta-algorithm/scripts/validate_delta.py` | typing, sys, argparse, yaml | - | Ja | Ja | Nein |
| `skills/prompt-engineering-system/scripts/generate_prompt.py` | json, argparse | - | Ja | Ja | Nein |

## PRIMÄRER DATENFLUSS
Die Signalkette – das ist die Murmelbahn, durch die unser Audio-Signal fließt.

```text
[ inventory.json ]
       |
       v
( classify_score.py )  <-- Signal Processing
       |
       v
[ classified_inventory.json ]
       |
       v
( flow_detection.py )  <-- Signal Routing
       |
       v
[ flow_analysis.json ]
       |
       v
( action_orchestrator.py ) <-- Master Bus
       |
       v
[ action_plan.json ]   <-- Final Bounce
```

### Die Master-Controller (Protokolle)
Diese 4 Protokolle steuern das gesamte Setup:
1. `soul.md` -> Master-Preset, definiert den Vibe (Kommunikationsstil & Regeln).
2. `universales_operationsprotokoll.md` -> UOP-Gate, der Limiter. Keine Operation ohne Bestätigung.
3. `interaktionsprotokoll.md` -> Der EQ. 3+1 Ebenen mit 6R-Check für saubere Frequenzen.
4. `ORCHESTRA.md` -> Der Sequencer. Rollentrennung, Aufgabenzuordnung, Kommunikation.

## VORLAGEN (BOILERPLATE)
Die Presets und Templates, damit wir nicht jedes Mal bei Null anfangen.

| Pfad | Kategorie | Begründung | Größe (Bytes) |
| :--- | :--- | :--- | :--- |
| `skills/mapping-analysis-templates/references/analysis_prompts.md` | TEMPLATE | Wiederverwendbare Vorlage | 15060 |
| `skills/mapping-analysis-templates/references/best_practices.md` | TEMPLATE | Wiederverwendbare Vorlage | 10203 |
| `skills/mapping-analysis-templates/templates/data_mapping_template.md` | TEMPLATE | Wiederverwendbare Vorlage | 2360 |
| `skills/mapping-analysis-templates/templates/process_mapping_template.md` | TEMPLATE | Wiederverwendbare Vorlage | 3937 |
| `skills/mapping-analysis-templates/templates/system_mapping_template.md` | TEMPLATE | Wiederverwendbare Vorlage | 7981 |
| `skills/zti-delta-algorithm/templates/delta_block_template.yaml` | TEMPLATE | Wiederverwendbare Vorlage | 131 |

## MINIMALER KERN
Was das System MINDESTENS braucht, um einen Ton rauszubringen. Wenn du das hier löschst, crasht die DAW.

**Protokolle (Die Core-Engine):**
- `soul.md`
- `universales_operationsprotokoll.md`
- `interaktionsprotokoll.md`
- `prompt-orchester.md`
- `ORCHESTRA.md`

**Analyse-Kette (Die Murmelbahn):**
- **Einstiegspunkt:** `classify_score.py` (startet die Analyse-Kette)
- **Skripte:** `classify_score.py`, `flow_detection.py`, `action_orchestrator.py`, `deep_analysis_script.py`
- **Daten:** `inventory.json`, `classified_inventory.json`, `flow_analysis.json`, `action_plan.json`, `inventory_v2.json`
- **Libs:** `os`, `json`, `datetime`, `re`

**Skills (Die Essential-Plugins):**
Die 8 Core-Skills und ihre zugehörigen Scripts (z.B. `generate_schema.py`, `validate_mapping.py`, etc.).

## GEDANKENKETTE
So bauen wir den Track auf. Die 6 Schritte zum perfekten Mix:

1. **SCHRITT 1:** `soul.md` ist das Master-Preset - ohne diese Datei verliert das System seine Identität und Kommunikationsregeln.
2. **SCHRITT 2:** UOP + Interaktionsprotokoll sind die Mixer-Regler - sie steuern WIE interagiert wird (Bestätigungspflicht, 3+1, 6R).
3. **SCHRITT 3:** `ORCHESTRA.md` definiert WER was macht - Rollentrennung zwischen Director, Manus, Gemini, Claude, GPT-4o.
4. **SCHRITT 4:** Die Analyse-Kette (Inventar -> Klassifizierung -> Signalfluss -> Aktionsplan) ist der operative Signalfluss - die Murmelbahn.
5. **SCHRITT 5:** Die 8 Fertigkeiten (Skills) sind die Plugins - sie erweitern die Grundfunktionalität.
6. **SCHRITT 6:** Ohne die 4 Protokolle + die Analyse-Kette ist das System tot. Alles andere ist Support oder Vorlage.
