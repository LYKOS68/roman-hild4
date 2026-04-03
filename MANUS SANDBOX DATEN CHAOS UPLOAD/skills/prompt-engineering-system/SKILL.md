---
name: prompt-engineering-system
description: Ein umfassendes System zur Erstellung, Verwaltung, Archivierung und Orchestrierung von Prompts für LLMs. Verwenden Sie diesen Skill, um Prompt-Packs zu erstellen, Prompts zu kalibrieren, Workflows zu definieren und die Zusammenarbeit mit LLMs zu systematisieren.
---

# Comprehensive Prompt Engineering and Management System

Dieser Skill implementiert ein vollständiges Ökosystem für professionelles Prompt Engineering. Er bietet die Werkzeuge und Strukturen, um die Zusammenarbeit mit LLMs von einer Kunst in eine Ingenieursdisziplin zu verwandeln.

## Systemstruktur

Das System besteht aus fünf Kernkomponenten, die als separate, aber integrierte Module fungieren:

1.  **Prompt-Generator:** Erstellt Prompts basierend auf Anforderungen.
2.  **Prompt-Manager:** Verwaltet Prompts und erzwingt Regeln (Chunking, Modalitätsgrenzen, Abbruchregeln).
3.  **Prompt-Archiv:** Speichert und versioniert Prompts.
4.  **Orchestrierer:** Steuert die Ausführung von Prompts und komplexen Workflows.
5.  **Prompt-Bibliothek:** Stellt wiederverwendbare Prompt-Techniken und -Templates zur Verfügung.

## Kernprinzip: Der META-KERN-PROMPT

Jeder Prompt, der dieses System durchläuft, wird zuerst durch den **META-KERN-PROMPT** validiert. Dieser stellt sicher, dass jede Eingabe ein "gebundenes Paket" ist und eine definierte **Basis**, **Adresse**, **Träger** und **Richtung** besitzt.

> **Referenz:** Lesen Sie `/home/ubuntu/skills/prompt-engineering-system/references/meta_kern_prompt.md` für die vollständige Spezifikation.

## Workflow: Von der Anforderung zum kalibrierten Prompt

1.  **Anforderung definieren:** Der Benutzer spezifiziert eine Anforderung (z.B. "Erstelle einen Prompt, der Blog-Artikel schreibt").

2.  **PROMPT_PACK erstellen:**
    *   **Aktion:** Verwenden Sie den **PROMPT_PACK-Generator**, um ein vollständiges, schema-konformes PROMPT_PACK für das Ziel-LLM zu erstellen.
    *   **Referenz:** `/home/ubuntu/skills/prompt-engineering-system/references/prompt_pack_system.md`

3.  **Prompt kalibrieren:**
    *   **Aktion:** Nutzen Sie den **Prompt-Kalibrierungs-Generator**, um einen hochspezifischen, kontextuellen Prompt zu erzeugen, der die Empfänger-Kalibrierung des LLMs triggert.
    *   **Referenz:** `/home/ubuntu/skills/prompt-engineering-system/references/prompt_kalibrierungs_generator.md`

4.  **Prompt ausführen:**
    *   **Aktion:** Der **Orchestrierer** validiert den kalibrierten Prompt mit dem **META-KERN-PROMPT** und sendet ihn an das Ziel-LLM.

## Komponenten im Detail

### 1. Prompt-Generator

Der Generator ist ein Meta-Prompt, der operative Prompts erzeugt. Er nutzt die Schemata und Templates aus dem PROMPT_PACK.

*   **Skript:** `/home/ubuntu/skills/prompt-engineering-system/scripts/generate_prompt.py`
    *   **Funktion:** Nimmt eine `method_id` und `input_data` entgegen und generiert einen ausführbaren, kalibrierten Prompt.

### 2. Prompt-Manager

Der Manager ist eine konzeptionelle Komponente, die durch den Orchestrator implementiert wird. Er achtet auf:

*   **Chunking:** Große Aufgaben werden in kleinere Prompts aufgeteilt (siehe `Decomposition Generator` im Prompt-Pack-System).
*   **Modalitätsgrenzen:** Der Orchestrator wählt das richtige LLM für die jeweilige Modalität (Text, Bild, Code).
*   **Abbruchregeln:** Jeder Prompt enthält eine `VALIDIERUNG`-Sektion, die als Abbruchbedingung dient.

### 3. Prompt-Archiv

Das Archiv ist ein versioniertes Verzeichnis, in dem alle generierten PROMPT_PACKs und kalibrierten Prompts gespeichert werden.

*   **Struktur:**
    ```
    /prompt_archive/
    ├── /packs/         # Alle PROMPT_PACKs
    │   └── gpt-4-muse_v1.0.yaml
    └── /prompts/       # Alle kalibrierten Prompts
        └── 2026-02-14_summarize_text.md
    ```

### 4. Orchestrator

Der Orchestrator ist die zentrale Steuerungseinheit. Seine Logik ist in der Systemintegration beschrieben.

*   **Referenz:** `/home/ubuntu/skills/prompt-engineering-system/references/system_integration.md`

### 5. Prompt-Bibliothek

Die Bibliothek ist eine Sammlung von wiederverwendbaren `techniques` und `templates`, die in den PROMPT_PACKs definiert sind.

## Verwendung des Skills

1.  **Initialisieren:** Stellen Sie sicher, dass alle Referenzdokumente im Verzeichnis `/home/ubuntu/skills/prompt-engineering-system/references/` vorhanden sind.
2.  **PROMPT_PACK erstellen:** Rufen Sie den PROMPT_PACK-Generator auf, um ein neues LLM in das Orchester aufzunehmen.
3.  **Prompt generieren & ausführen:** Verwenden Sie das Skript `generate_prompt.py`, um einen kalibrierten Prompt zu erzeugen und auszuführen.
