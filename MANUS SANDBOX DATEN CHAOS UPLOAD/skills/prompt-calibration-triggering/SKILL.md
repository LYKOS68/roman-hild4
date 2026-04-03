---
name: prompt-calibration-triggering
version: 1.0
created: 2026-02-14
description: Sicherstellen, dass Prompts (1) die Empfänger-Kalibrierung des KI-Modells triggern und (2) selbst richtig kalibriert sind für korrekte Ergebnisse
tags:
  - prompt-engineering
  - llm-calibration
  - recipient-triggering
  - prompt-optimization
---

# Prompt-Kalibrierung & Empfänger-Triggering Skill

**Version:** 1.0  
**Erstellt:** 2026-02-14  
**Zweck:** Sicherstellen, dass Prompts (1) die Empfänger-Kalibrierung des KI-Modells triggern und (2) selbst richtig kalibriert sind für korrekte Ergebnisse.

---

## KERNPRINZIP

> **Ein Prompt muss ZWEI Dinge gleichzeitig leisten:**
> 1. **Empfänger-Triggering:** Das KI-Modell in den gewünschten Zustand versetzen (Rolle, Wissensbereich, Priorität aktivieren)
> 2. **Prompt-Kalibrierung:** Selbst klar, eindeutig und vollständig sein (Task, Schritte, Format, Kontext, Beispiele)

**Nur wenn beide Aspekte optimal aufeinander abgestimmt sind, kann das KI-Modell die richtigen Ergebnisse im gewünschten Format zurücksenden.**

---

## TEIL 1: EMPFÄNGER-TRIGGERING (Recipient Calibration)

### Was ist Empfänger-Triggering?

Das KI-Modell muss seine internen "Recipient-Calibration"-Mechanismen aktivieren, um die Anfrage korrekt zu interpretieren.

### Empfänger-Triggering-Komponenten

#### 1. ROLLE/PERSONA (Role Activation)
**Zweck:** Aktiviert spezifisches Verhaltens- und Wissensprofil im Modell

**Template:**
```
Du bist ein [ROLLE] mit Expertise in [DOMAIN].
Deine Aufgabe ist es, [SPEZIFISCHE_FUNKTION] durchzuführen.
```

**Beispiele:**
- "Du bist ein System-Architekt mit Expertise in Dateiformat-Transformation."
- "Du bist ein Prompt-Engineer, der LLM-spezifische Prompts optimiert."
- "Du bist ein Forensic Analyst für Google Drive Strukturen."

**Effekt:** Modell aktiviert relevante Wissensbereiche und Verhaltensweisen.

---

#### 2. KONTEXT/WISSENSBEREICH (Knowledge Domain Activation)
**Zweck:** Aktiviert relevante Wissensbereiche im Modell

**Template:**
```
KONTEXT:
- System: [SYSTEM_NAME]
- Architektur: [ARCHITEKTUR_TYP]
- Relevante Dateien: [KERNEL_FILES]
- Aktuelle Situation: [STATE_DESCRIPTION]
```

**Beispiel:**
```
KONTEXT:
- System: VERSION3
- Architektur: 3-Layer-Hierarchie (System → Kernel → User)
- Relevante Dateien: GEMINI.md, bootstrap_protocol.md, kernels/OPS.md
- Aktuelle Situation: 30 von 45 Dateien sind wirkungslose MD-Dateien
```

**Effekt:** Modell weiß, welches Wissen relevant ist und welcher Zustand vorliegt.

---

#### 3. PRIORITÄT/CONSTRAINTS (Priority Activation)
**Zweck:** Definiert, was MUSS und was DARF NICHT

**Template:**
```
PRIORITÄTEN:
1. [HÖCHSTE_PRIORITÄT]
2. [HOHE_PRIORITÄT]
3. [MITTLERE_PRIORITÄT]

CONSTRAINTS:
- MUSS: [MANDATORY_REQUIREMENTS]
- DARF NICHT: [PROHIBITIONS]
- STOP IF: [ABORT_CONDITIONS]
```

**Beispiel:**
```
PRIORITÄTEN:
1. System-Protokolle müssen in YAML transformiert werden
2. Ausführbare Logik muss in Python vorliegen
3. Dokumentation kann als MD bleiben

CONSTRAINTS:
- MUSS: Jede Transformation muss validiert werden
- DARF NICHT: Keine Dateien <500 Bytes erstellen
- STOP IF: >25% Transformationen fehlschlagen
```

**Effekt:** Modell behandelt Anfragen mit korrekter Priorität und respektiert Grenzen.

---

#### 4. ERWARTUNGSHALTUNG (Expectation Setting)
**Zweck:** Definiert, was das Modell zurückgeben soll

**Template:**
```
ERWARTUNG:
- Output-Format: [FORMAT]
- Output-Struktur: [STRUCTURE]
- Output-Validierung: [VALIDATION_CRITERIA]
```

**Beispiel:**
```
ERWARTUNG:
- Output-Format: JSON
- Output-Struktur: { "transformations": [...], "statistics": {...} }
- Output-Validierung: Alle Felder müssen vorhanden sein, keine null-Werte
```

**Effekt:** Modell weiß genau, was erwartet wird und kann Output entsprechend strukturieren.

---

## TEIL 2: PROMPT-KALIBRIERUNG (Prompt Calibration)

### Was ist Prompt-Kalibrierung?

Der Prompt selbst muss "richtig kalibriert" sein - klar, eindeutig und vollständig.

### Prompt-Kalibrierungs-Komponenten

#### 1. TASK-DEFINITION (Was soll getan werden?)
**Zweck:** Präzise Definition der Aufgabe

**Template:**
```
AUFGABE: [VERB] [OBJEKT] [ZIEL]

BESCHREIBUNG:
[Detaillierte Erklärung der Aufgabe]
```

**Beispiel:**
```
AUFGABE: Transformiere alle System-Protokoll-MD-Dateien zu YAML

BESCHREIBUNG:
Extrahiere die Struktur aus den Markdown-Dateien (.gemini/bootstrap_protocol.md, etc.),
identifiziere Key-Value-Paare und konvertiere sie in ein valides YAML-Schema.
```

**Effekt:** Modell versteht genau, was zu tun ist.

---

#### 2. SCHRITTE/STRATEGIE (Wie soll es getan werden?)
**Zweck:** Definiert den Prozess

**Template:**
```
SCHRITTE:
1. [SCHRITT_1]
2. [SCHRITT_2]
3. [SCHRITT_3]
...

STRATEGIE:
[Ansatz/Methodik]
```

**Beispiel:**
```
SCHRITTE:
1. Lese Markdown-Datei
2. Extrahiere Überschriften als Keys
3. Extrahiere Listen als Arrays
4. Identifiziere Code-Blöcke
5. Konvertiere zu YAML-Struktur
6. Validiere mit yamllint

STRATEGIE:
Hierarchische Struktur beibehalten, Metadaten extrahieren, Validierung vor Export.
```

**Effekt:** Modell folgt strukturiertem Prozess.

---

#### 3. FORMAT-SPEZIFIKATION (In welchem Format?)
**Zweck:** Definiert Output-Format präzise

**Template:**
```
OUTPUT-FORMAT: [FORMAT_NAME]

STRUKTUR:
[Schema oder Beispiel]

VALIDIERUNG:
[Validierungskriterien]
```

**Beispiel:**
```
OUTPUT-FORMAT: JSON

STRUKTUR:
{
  "file": "bootstrap_protocol.md",
  "target_format": "YAML",
  "yaml_structure": {
    "protocol_name": "...",
    "version": "...",
    "phases": [...]
  },
  "validation_status": "PASS/FAIL"
}

VALIDIERUNG:
- Alle Felder müssen vorhanden sein
- yaml_structure muss valides YAML sein
- validation_status muss PASS oder FAIL sein
```

**Effekt:** Modell generiert Output im exakten Format.

---

#### 4. KONTEXT-REFERENZEN (Welche Informationen nutzen?)
**Zweck:** Verweist auf relevante Dateien/Daten

**Template:**
```
KONTEXT-REFERENZEN:
- Datei: [PATH] - Zweck: [PURPOSE]
- Datei: [PATH] - Zweck: [PURPOSE]
```

**Beispiel:**
```
KONTEXT-REFERENZEN:
- Datei: /home/ubuntu/HAWKING_FORENSIC/VERSION3_SYSTEM_MAP.json - Zweck: Dependency Graph
- Datei: /home/ubuntu/version3_analysis/.gemini/bootstrap_protocol.md - Zweck: Quell-Datei
- Datei: /home/ubuntu/HAWKING_FORENSIC/FORMAT_TRANSFORMATION_ANALYSIS.json - Zweck: Transformationsplan
```

**Effekt:** Modell weiß, welche Dateien zu laden sind.

---

#### 5. BEISPIELE (Few-Shot Learning)
**Zweck:** Demonstriert gewünschtes Verhalten

**Template:**
```
BEISPIEL 1:
Input: [EXAMPLE_INPUT_1]
Output: [EXAMPLE_OUTPUT_1]

BEISPIEL 2:
Input: [EXAMPLE_INPUT_2]
Output: [EXAMPLE_OUTPUT_2]
```

**Beispiel:**
```
BEISPIEL 1:
Input: bootstrap_protocol.md mit Überschriften "Phase 1", "Phase 2"
Output:
protocol_name: bootstrap_protocol
version: 1.0
phases:
  - name: Phase 1
    steps: [...]
  - name: Phase 2
    steps: [...]

BEISPIEL 2:
Input: system_protocol.md mit Regeln "Layer 1 overrides Layer 2"
Output:
protocol_name: system_protocol
version: 1.0
rules:
  - priority: 1
    rule: "Layer 1 overrides Layer 2"
```

**Effekt:** Modell versteht Pattern und repliziert es.

---

## TEIL 3: VOLLSTÄNDIGES PROMPT-TEMPLATE

### Universal Prompt Template (Empfänger-Triggering + Prompt-Kalibrierung)

```markdown
//[SYSTEM_NAME]::[OPERATION_NAME]

═══════════════════════════════════════════════════════════════
EMPFÄNGER-KALIBRIERUNG (Recipient Calibration)
═══════════════════════════════════════════════════════════════

ROLLE:
Du bist ein [ROLLE] mit Expertise in [DOMAIN].
Deine Aufgabe ist es, [SPEZIFISCHE_FUNKTION] durchzuführen.

KONTEXT:
- System: [SYSTEM_NAME]
- Architektur: [ARCHITEKTUR_TYP]
- Relevante Dateien: [KERNEL_FILES]
- Aktuelle Situation: [STATE_DESCRIPTION]

PRIORITÄTEN:
1. [HÖCHSTE_PRIORITÄT]
2. [HOHE_PRIORITÄT]
3. [MITTLERE_PRIORITÄT]

CONSTRAINTS:
- MUSS: [MANDATORY_REQUIREMENTS]
- DARF NICHT: [PROHIBITIONS]
- STOP IF: [ABORT_CONDITIONS]

ERWARTUNG:
- Output-Format: [FORMAT]
- Output-Struktur: [STRUCTURE]
- Output-Validierung: [VALIDATION_CRITERIA]

═══════════════════════════════════════════════════════════════
PROMPT-KALIBRIERUNG (Prompt Calibration)
═══════════════════════════════════════════════════════════════

AUFGABE: [VERB] [OBJEKT] [ZIEL]

BESCHREIBUNG:
[Detaillierte Erklärung der Aufgabe]

SCHRITTE:
1. [SCHRITT_1]
2. [SCHRITT_2]
3. [SCHRITT_3]
...

STRATEGIE:
[Ansatz/Methodik]

OUTPUT-FORMAT: [FORMAT_NAME]

STRUKTUR:
[Schema oder Beispiel]

VALIDIERUNG:
[Validierungskriterien]

KONTEXT-REFERENZEN:
- Datei: [PATH] - Zweck: [PURPOSE]
- Datei: [PATH] - Zweck: [PURPOSE]

BEISPIELE:

BEISPIEL 1:
Input: [EXAMPLE_INPUT_1]
Output: [EXAMPLE_OUTPUT_1]

BEISPIEL 2:
Input: [EXAMPLE_INPUT_2]
Output: [EXAMPLE_OUTPUT_2]

═══════════════════════════════════════════════════════════════
AUSFÜHRUNG
═══════════════════════════════════════════════════════════════

[Hier beginnt die eigentliche Prompt-Ausführung mit konkreten Daten]
```

---

## TEIL 4: KONKRETE ANWENDUNGSBEISPIELE

### Beispiel 1: Dateiformat-Transformation

```markdown
//VERSION3::FORMAT_TRANSFORMATION

═══════════════════════════════════════════════════════════════
EMPFÄNGER-KALIBRIERUNG
═══════════════════════════════════════════════════════════════

ROLLE:
Du bist ein System-Architekt mit Expertise in Dateiformat-Transformation.
Deine Aufgabe ist es, wirkungslose MD-Dateien in funktionale Formate zu transformieren.

KONTEXT:
- System: VERSION3
- Architektur: 3-Layer-Hierarchie (System → Kernel → User)
- Relevante Dateien: VERSION3_SYSTEM_MAP.json, FORMAT_TRANSFORMATION_ANALYSIS.json
- Aktuelle Situation: 30 von 45 Dateien sind wirkungslose MD-Dateien

PRIORITÄTEN:
1. System-Protokolle → YAML (KRITISCH)
2. Hawking-Logik → PYTHON (HOCH)
3. Commands → SHELL_SCRIPT (MITTEL)

CONSTRAINTS:
- MUSS: Jede Transformation validieren
- DARF NICHT: Dateien <500 Bytes erstellen
- STOP IF: >25% Transformationen fehlschlagen

ERWARTUNG:
- Output-Format: JSON
- Output-Struktur: { "transformations": [...], "validation": {...} }
- Output-Validierung: Alle Transformationen müssen validation_status haben

═══════════════════════════════════════════════════════════════
PROMPT-KALIBRIERUNG
═══════════════════════════════════════════════════════════════

AUFGABE: Transformiere bootstrap_protocol.md zu bootstrap_protocol.yaml

BESCHREIBUNG:
Extrahiere die Struktur aus bootstrap_protocol.md, identifiziere Phasen, Regeln und
Constraints, und konvertiere sie in ein valides YAML-Schema.

SCHRITTE:
1. Lese /home/ubuntu/version3_analysis/.gemini/bootstrap_protocol.md
2. Extrahiere Überschriften als protocol_name und Phasen
3. Extrahiere Listen als Arrays
4. Identifiziere Code-Blöcke als Beispiele
5. Konvertiere zu YAML-Struktur
6. Validiere mit yamllint
7. Speichere als bootstrap_protocol.yaml

STRATEGIE:
Hierarchische Struktur beibehalten, Metadaten (Version, Autor) extrahieren,
Validierung vor Export.

OUTPUT-FORMAT: JSON

STRUKTUR:
{
  "file": "bootstrap_protocol.md",
  "target_file": "bootstrap_protocol.yaml",
  "target_format": "YAML",
  "yaml_content": "...",
  "validation_status": "PASS",
  "validation_errors": []
}

VALIDIERUNG:
- yaml_content muss valides YAML sein
- validation_status muss PASS sein
- Keine validation_errors

KONTEXT-REFERENZEN:
- Datei: /home/ubuntu/version3_analysis/.gemini/bootstrap_protocol.md - Zweck: Quell-Datei
- Datei: /home/ubuntu/HAWKING_FORENSIC/FORMAT_TRANSFORMATION_ANALYSIS.json - Zweck: Transformationsplan

BEISPIELE:

BEISPIEL 1:
Input: bootstrap_protocol.md mit "# Phase 1: Initialization"
Output:
protocol_name: bootstrap_protocol
version: 1.0
phases:
  - name: Initialization
    steps:
      - Load GEMINI.md
      - Validate Layer 1

═══════════════════════════════════════════════════════════════
AUSFÜHRUNG
═══════════════════════════════════════════════════════════════

Führe jetzt die Transformation für bootstrap_protocol.md durch.
```

---

### Beispiel 2: Drive-Operation

```markdown
//MANUS::DRIVE_AUDIT

═══════════════════════════════════════════════════════════════
EMPFÄNGER-KALIBRIERUNG
═══════════════════════════════════════════════════════════════

ROLLE:
Du bist ein Forensic Analyst für Google Drive Strukturen.
Deine Aufgabe ist es, Drive-Ordner zu analysieren und Substanz-Audits durchzuführen.

KONTEXT:
- System: Google Drive via rclone
- Target: manus_google_drive:.GEMINI/VERSION3
- Bekannte Struktur: 45 Dateien, 6 Verzeichnisse, 417.48 KB
- Aktuelle Situation: Vollständiges Audit erforderlich

PRIORITÄTEN:
1. Metadaten erfassen (file_id, name, size, modified_time)
2. SHA256 Hashes berechnen
3. Substanz-Score ermitteln

CONSTRAINTS:
- MUSS: Alle 45 Dateien erfassen
- DARF NICHT: Dateien modifizieren
- STOP IF: >5% Dateien nicht erreichbar

ERWARTUNG:
- Output-Format: JSON
- Output-Struktur: { "files": [...], "statistics": {...}, "audit_result": "..." }
- Output-Validierung: Alle 45 Dateien müssen in "files" Array sein

═══════════════════════════════════════════════════════════════
PROMPT-KALIBRIERUNG
═══════════════════════════════════════════════════════════════

AUFGABE: Führe vollständiges Substanz-Audit für VERSION3 durch

BESCHREIBUNG:
Liste alle Dateien in manus_google_drive:.GEMINI/VERSION3 mit vollständigen Metadaten,
berechne SHA256 Hashes, analysiere Substanz (Zeilen, Code, Kommentare) und
generiere Audit-Report.

SCHRITTE:
1. Liste alle Dateien mit: rclone lsjson manus_google_drive:.GEMINI/VERSION3 -R --files-only --config /home/ubuntu/.gdrive-rclone.ini
2. Download alle Dateien zu /home/ubuntu/audit_temp/
3. Berechne SHA256 für jede Datei
4. Analysiere Substanz (non-empty-lines / total-lines)
5. Klassifiziere Dateien (Code, Config, Markdown, etc.)
6. Generiere Audit-Report als JSON
7. Exportiere zu /home/ubuntu/HAWKING_FORENSIC/DRIVE_AUDIT.json

STRATEGIE:
Parallele Downloads für Performance, Hash-Verifikation für Integrität,
Substanz-Analyse für Qualitätsbewertung.

OUTPUT-FORMAT: JSON

STRUKTUR:
{
  "metadata": {
    "timestamp": "...",
    "target": "manus_google_drive:.GEMINI/VERSION3",
    "total_files": 45
  },
  "files": [
    {
      "file_id": "...",
      "name": "...",
      "path": "...",
      "size": 1234,
      "modified_time": "...",
      "sha256": "...",
      "substance_score": 0.85,
      "classification": "MARKDOWN"
    }
  ],
  "statistics": {
    "total_size": 427499,
    "average_substance_score": 0.728,
    "by_classification": {...}
  },
  "audit_result": "PASS"
}

VALIDIERUNG:
- files Array muss 45 Einträge haben
- Jede Datei muss sha256 und substance_score haben
- audit_result muss PASS oder FAIL sein

KONTEXT-REFERENZEN:
- Remote: manus_google_drive:.GEMINI/VERSION3 - Zweck: Audit-Target
- Config: /home/ubuntu/.gdrive-rclone.ini - Zweck: rclone Authentifizierung

BEISPIELE:

BEISPIEL 1:
Input: GEMINI.md (11.5 KB, 250 Zeilen, 200 non-empty)
Output:
{
  "name": "GEMINI.md",
  "size": 11776,
  "sha256": "abc123...",
  "substance_score": 0.8,
  "classification": "MARKDOWN"
}

═══════════════════════════════════════════════════════════════
AUSFÜHRUNG
═══════════════════════════════════════════════════════════════

Führe jetzt das vollständige Drive-Audit für VERSION3 durch.
```

---

## TEIL 5: VALIDIERUNGS-CHECKLISTE

### Pre-Prompt Validation (Vor dem Senden)

✓ **Empfänger-Triggering:**
- [ ] Rolle/Persona definiert?
- [ ] Kontext/Wissensbereich aktiviert?
- [ ] Prioritäten gesetzt?
- [ ] Constraints definiert?
- [ ] Erwartungshaltung klar?

✓ **Prompt-Kalibrierung:**
- [ ] Task präzise definiert?
- [ ] Schritte/Strategie beschrieben?
- [ ] Format spezifiziert?
- [ ] Kontext-Referenzen vorhanden?
- [ ] Beispiele gegeben?

✓ **Vollständigkeit:**
- [ ] Alle benötigten Informationen vorhanden?
- [ ] Keine Mehrdeutigkeiten?
- [ ] Validierungskriterien definiert?

---

### Post-Response Validation (Nach der Antwort)

✓ **Output-Qualität:**
- [ ] Format korrekt?
- [ ] Struktur vollständig?
- [ ] Validierungskriterien erfüllt?

✓ **Empfänger-Triggering Erfolg:**
- [ ] Hat Modell Rolle angenommen?
- [ ] Wurden Prioritäten respektiert?
- [ ] Wurden Constraints eingehalten?

✓ **Prompt-Kalibrierung Erfolg:**
- [ ] Wurden alle Schritte befolgt?
- [ ] Ist Output im richtigen Format?
- [ ] Wurden Beispiele korrekt repliziert?

---

## TEIL 6: ANTI-PATTERNS (Was vermeiden?)

### ❌ Anti-Pattern 1: Unklare Rolle
```
Schlecht: "Analysiere diese Dateien."
Gut: "Du bist ein System-Architekt. Analysiere diese Dateien nach Dateiformat-Eignung."
```

### ❌ Anti-Pattern 2: Fehlender Kontext
```
Schlecht: "Transformiere zu YAML."
Gut: "Transformiere bootstrap_protocol.md zu YAML. Kontext: VERSION3 System mit 3-Layer-Architektur."
```

### ❌ Anti-Pattern 3: Unspezifisches Format
```
Schlecht: "Gib das Ergebnis zurück."
Gut: "Gib das Ergebnis als JSON zurück mit Struktur: { 'file': '...', 'yaml_content': '...' }"
```

### ❌ Anti-Pattern 4: Keine Validierung
```
Schlecht: "Erstelle YAML."
Gut: "Erstelle YAML und validiere mit yamllint. Status muss PASS sein."
```

### ❌ Anti-Pattern 5: Fehlende Beispiele
```
Schlecht: "Konvertiere MD zu YAML."
Gut: "Konvertiere MD zu YAML. Beispiel: '# Phase 1' → 'phases:\n  - name: Phase 1'"
```

---

## TEIL 7: ANWENDUNG IN MANUS

### Skill-Integration

Wenn du diesen Skill verwendest:

1. **Lese diesen Skill:**
   ```python
   file.read('/home/ubuntu/skills/prompt-calibration-triggering/SKILL.md')
   ```

2. **Wende Template an:**
   - Fülle alle Platzhalter aus
   - Validiere mit Checkliste
   - Sende kalibrierten Prompt

3. **Validiere Response:**
   - Prüfe Output-Format
   - Prüfe Vollständigkeit
   - Prüfe Validierungskriterien

---

## TEIL 8: ZUSAMMENFASSUNG

### Kernprinzipien

1. **Empfänger-Triggering = Modell in richtigen Zustand versetzen**
   - Rolle aktivieren
   - Kontext laden
   - Prioritäten setzen
   - Erwartungen definieren

2. **Prompt-Kalibrierung = Prompt selbst optimieren**
   - Task klar definieren
   - Schritte beschreiben
   - Format spezifizieren
   - Beispiele geben

3. **Beide müssen zusammenwirken**
   - Empfänger-Triggering ohne Prompt-Kalibrierung → Modell weiß nicht, was zu tun ist
   - Prompt-Kalibrierung ohne Empfänger-Triggering → Modell ist nicht im richtigen Zustand

### Erfolgsformel

```
Optimaler Prompt = Empfänger-Triggering ⊕ Prompt-Kalibrierung ⊕ Validierung
```

Wo:
- **⊕** = Perfekte Integration (nicht nur Addition)
- **Empfänger-Triggering** = Modell-Zustand
- **Prompt-Kalibrierung** = Prompt-Qualität
- **Validierung** = Qualitätssicherung

---

**Ende des Skills**
