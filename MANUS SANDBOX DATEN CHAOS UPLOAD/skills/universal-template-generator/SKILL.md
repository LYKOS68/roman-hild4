---
name: universal-template-generator
description: Generator für Layouts, Setups, Vorlagen und Schablonen für ALLES (LLM-Agenten, Pipelines, Architekturen, Workflows, Prompts, Regeln) - transformiert Anwendungsfälle in wiederverwendbare Strukturen ohne technisches Knowhow. Use when User benötigt Setup/Layout/Vorlage für beliebigen Anwendungsfall.
---

# Universal Template Generator

**Prinzip:** Alles kann in Setups, Layouts, Vorlagen und Schablonen gebracht werden - ohne technisches Knowhow.

**Workflow:** User gibt Anwendungsfall an → Skill generiert passendes Template → User wendet es an.

---

## KERNKONZEPT

Ein **Template** ist eine wiederverwendbare Struktur, die:
1. Ohne technisches Knowhow verwendbar ist
2. Für spezifischen Anwendungsfall optimiert ist
3. Sofort anwendbar ist (Fill-in-the-blanks)
4. Validierbar ist

**Was kann templatisiert werden:** LLM-Agenten, Pipelines, Architekturen, Workflows, Prompts, Regel-Systeme, Terminal-Befehle, Abstraktions-Mechanismen.

---

## UNIVERSAL FRAMEWORK: Setup → Layout → Prompt → Kontext

### 1. SETUP (Vorbereitung, Initialisierung)
Format: YAML

```yaml
setup:
  name: "[NAME]"
  version: "1.0"
  purpose: "[ZWECK]"
  prerequisites: ["[VORAUSSETZUNG]"]
  initialization:
    steps:
      - action: "[AKTION]"
        validation: "[VALIDIERUNG]"
```

### 2. LAYOUT (Architektur, Struktur)
Format: YAML

```yaml
layout:
  architecture: "[TYP]"
  layers:
    - name: "[LAYER_NAME]"
      components: ["[COMPONENT]"]
      dependencies: ["[DEPENDENCY]"]
  relationships:
    - from: "[A]"
      to: "[B]"
      type: "[TYP]"
```

### 3. PROMPT (Steuerung, Anweisungen)
Format: Strukturierter Text

```markdown
//[SYSTEM]::[OPERATION]

ROLLE: [ROLLE]
KONTEXT: [KONTEXT]
ZIEL: [ZIEL]
AUFGABE: [AUFGABE]
SCHRITTE:
1. [SCHRITT_1]
2. [SCHRITT_2]
OUTPUT-FORMAT: [FORMAT]
```

### 4. KONTEXT (Umgebung, Randbedingungen)
Format: YAML

```yaml
kontext:
  environment:
    type: "[TYP]"
    constraints: ["[CONSTRAINT]"]
  stakeholders:
    - role: "[ROLLE]"
      needs: ["[BEDÜRFNIS]"]
```

---

## TEMPLATE-KATALOG

### Template 1: LLM-Agenten-Setup

```yaml
setup:
  name: "[AGENT_NAME]_agent"
  llm_model: "[MODEL]"  # gpt-4, claude-3, gemini-2.5-flash
  purpose: "[ZWECK]"
  system_prompt: |
    Du bist ein [ROLLE] mit Expertise in [DOMAIN].
    Aufgabe: [FUNKTION]
    KONTEXT: [KONTEXT]
    PRIORITÄTEN: [PRIORITÄTEN]
    CONSTRAINTS: [CONSTRAINTS]
  tools:
    - name: "[TOOL]"
      purpose: "[ZWECK]"
  parameters:
    temperature: 0.7
    max_tokens: 4000

layout:
  pipeline:
    - stage: "input_processing"
      actions: ["validate_input", "extract_intent"]
    - stage: "execution"
      actions: ["select_tools", "execute_task"]
    - stage: "output_generation"
      actions: ["format_output", "validate_output"]
```

### Template 2: Pipeline-Design

```yaml
setup:
  name: "[PIPELINE_NAME]"
  type: "[TYP]"  # data_processing, workflow, automation
  purpose: "[ZWECK]"

layout:
  stages:
    - id: "stage_1"
      name: "[NAME]"
      inputs:
        - source: "[SOURCE]"
          format: "[FORMAT]"
      operations:
        - action: "[OPERATION]"
      outputs:
        - target: "stage_2"
  
  error_handling:
    strategy: "[STRATEGY]"  # retry, skip, abort
    max_retries: 3
```

### Template 3: Architektur-Layout

```yaml
setup:
  name: "[SYSTEM]_architecture"
  architecture_type: "[TYP]"  # layered, microservices, event-driven

layout:
  layers:
    - name: "Layer_1"
      responsibility: "[VERANTWORTUNG]"
      components:
        - name: "[COMPONENT]"
          interfaces: ["[INTERFACE]"]
          dependencies: []
  
  communication:
    patterns:
      - type: "[PATTERN]"  # request-response, pub-sub
        between: ["[A]", "[B]"]
```

### Template 4: Workflow-Definition

```yaml
setup:
  name: "[WORKFLOW_NAME]"
  trigger: "[TRIGGER]"  # manual, scheduled, event-based

layout:
  steps:
    - id: "step_1"
      name: "[NAME]"
      type: "[TYP]"  # action, decision, parallel
      action:
        type: "[ACTION]"
      next:
        - condition: "[CONDITION]"
          goto: "step_2"
```

### Template 5: Prompt-Struktur

```markdown
//[SYSTEM]::[OPERATION]

═══════════════════════════════════════
EMPFÄNGER-KALIBRIERUNG
═══════════════════════════════════════

ROLLE: [ROLLE mit Expertise in DOMAIN]
KONTEXT:
- System: [SYSTEM]
- Situation: [SITUATION]
PRIORITÄTEN: [LISTE]
CONSTRAINTS:
- MUSS: [MANDATORY]
- DARF NICHT: [PROHIBITION]
ERWARTUNG:
- Format: [FORMAT]
- Validierung: [KRITERIEN]

═══════════════════════════════════════
PROMPT-KALIBRIERUNG
═══════════════════════════════════════

AUFGABE: [VERB] [OBJEKT] [ZIEL]
SCHRITTE:
1. [SCHRITT_1]
2. [SCHRITT_2]
OUTPUT-FORMAT: [FORMAT]
STRUKTUR: [SCHEMA]
BEISPIELE: [INPUT → OUTPUT]
```

### Template 6: Regel-System

```yaml
setup:
  name: "[SYSTEM]_rules"
  rule_engine: "[ENGINE]"  # forward-chaining, backward-chaining

layout:
  rules:
    - id: "rule_1"
      priority: 1
      name: "[NAME]"
      condition:
        expression: "[CONDITION]"
      action:
        execute: "[ACTION]"
  
  conflict_resolution:
    strategy: "[STRATEGY]"  # priority, specificity
```

---

## GENERATOR-WORKFLOW

### Schritt 1: Anwendungsfall identifizieren
Frage: "Was möchtest du erstellen?"

### Schritt 2: Template auswählen
- LLM-Agent → Template 1
- Pipeline → Template 2
- Architektur → Template 3
- Workflow → Template 4
- Prompt → Template 5
- Regel-System → Template 6

### Schritt 3: Template generieren
1. Lade Template
2. Fülle bekannte Platzhalter aus
3. Markiere unbekannte mit `[TODO: ...]`

### Schritt 4: Template ausliefern
1. Speichere als Datei
2. Sende an User
3. Gib Anwendungs-Anleitung

### Schritt 5: Validierung
```yaml
validation_checklist:
  - [ ] Alle Platzhalter ausgefüllt?
  - [ ] Format korrekt?
  - [ ] Logik konsistent?
  - [ ] Dependencies definiert?
```

---

## HELPER-SCRIPTS

### validate_template.py
Validiert generiertes Template (YAML Syntax, Platzhalter, Required Fields).

Usage:
```bash
python3 scripts/validate_template.py <template_file>
```

### fill_template.py
Interaktives Ausfüllen von Platzhaltern.

Usage:
```bash
python3 scripts/fill_template.py <template_file>
```

---

## BEISPIEL

**User:** "Ich brauche ein Setup für einen LLM-Agenten für Dateiformat-Transformation."

**Manus:**

```yaml
# LLM-Agenten-Setup: Dateiformat-Transformer

setup:
  name: "format_transformer_agent"
  llm_model: "gpt-4"
  purpose: "Transformiert Dateien (MD → YAML, JSON, Python)"
  system_prompt: |
    Du bist ein Dateiformat-Experte.
    Aufgabe: Dateien von einem Format in ein anderes transformieren.
    KONTEXT: Unterstützte Formate: MD, YAML, JSON, Python
    PRIORITÄTEN: 1. Struktur beibehalten 2. Validierung 3. Fehler melden
    CONSTRAINTS: MUSS validieren, DARF NICHT Daten verlieren
  tools:
    - name: "file_reader"
    - name: "format_converter"
    - name: "validator"
  parameters:
    temperature: 0.3
    max_tokens: 4000

layout:
  pipeline:
    - stage: "input_processing"
      actions: ["read_source", "detect_format"]
    - stage: "execution"
      actions: ["extract_structure", "convert_format"]
    - stage: "output_generation"
      actions: ["validate_output", "save_file"]
```

**Anwendung:**
```bash
# Speichern
save as: format_transformer_agent.yaml

# Laden
python3 load_agent.py format_transformer_agent.yaml

# Testen
python3 test_agent.py format_transformer_agent.yaml test_file.md
```

---

## ZUSAMMENFASSUNG

**Dieser Skill ermöglicht:**
- ✓ Generierung von Templates für BELIEBIGE Anwendungsfälle
- ✓ Keine technischen Kenntnisse erforderlich
- ✓ Sofort anwendbar mit Helper-Scripts
- ✓ Validierbar

**Workflow:**
```
Anwendungsfall → Template-Auswahl → Generierung → Ausfüllen → Validieren → Anwenden
```

---

## RESOURCES

### references/template_catalog.md
Vollständiger Katalog aller Templates mit Beschreibungen, Anwendungsfällen und Best Practices.

### references/format_specs.md
Detaillierte Format-Spezifikationen für YAML, Markdown, JSON und Validierungsregeln.

---

**Ende des Skills**
