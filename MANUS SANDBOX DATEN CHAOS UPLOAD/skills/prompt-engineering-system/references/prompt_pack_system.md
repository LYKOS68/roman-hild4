´´´markdown
# Das PROMPT_PACK System: Eine Basis-Architektur für LLM-Orchestrierung

## Das Kernproblem: "Ohne Basis ist jede Eingabe ein ungebundenes Paket."

Ihre Analyse ist präzise: Jede Eingabe an ein LLM – sei es ein Prompt, eine Frage oder ein Befehl – ist ohne ein übergeordnetes System nur "Info ohne Material" oder "Material ohne Info". Es fehlt die Adresse, der Träger und die Richtung. Die Eingabe hat keinen Ort, an dem sie wirken kann, und keinen Zweck, dem sie dient.

Dieses Dokument definiert die **Basis-Architektur**, die dieses Problem löst. Wir schaffen ein System, das jeder Eingabe einen Lagerplatz und jedem Lieferschein ein Lager zuweist.

## Die Lösung: Das PROMPT_PACK als standardisierte Schnittstelle

Die Basis ist ein **Orchestrator**. Dieser Orchestrator verwaltet ein "Orchester" von verschiedenen, spezialisierten LLMs. Jedes LLM im Orchester wird durch ein **PROMPT_PACK** repräsentiert. Das PROMPT_PACK ist die standardisierte API-Spezifikation für ein LLM. Es definiert, *wer* das LLM ist, *was* es kann und *wie* es angesprochen werden muss.

Der Orchestrator liest diese Packs und kann so intelligent entscheiden, welche Aufgabe an welches LLM mit welchem exakten, schema-konformen Prompt übergeben wird.

### Die Architektur im Überblick

1.  **Orchestrator (Das Lager):** Das zentrale Steuerungssystem. Es empfängt Aufgaben, analysiert sie und leitet sie an das passende LLM weiter.
2.  **LLM-Profil (Die Stammdaten):** Eine Beschreibung der Fähigkeiten, Stärken und Schwächen eines LLMs.
3.  **PROMPT_PACK (Der Lieferschein-Standard):** Ein YAML/JSON-Dokument, das die komplette Schnittstelle zu einem LLM definiert. Es wird von einem Generator auf Basis des LLM-Profils erzeugt.
4.  **Prompt (Die Ware):** Die konkrete, zur Laufzeit generierte Eingabe für das LLM, die immer einem Schema aus dem PROMPT_PACK entspricht.

---

## Der PROMPT_PACK Generator

Dies ist ein Meta-Prompt, der die Brücke zwischen dem LLM-Profil und dem standardisierten PROMPT_PACK schlägt.

### ROLLE
DU BIST EIN PROMPT-PACK-GENERATOR. Deine Aufgabe ist die Erstellung von vollständigen, schema-konformen PROMPT_PACKs für die LLM-Orchestrierung.

### AUFGABE
Erzeuge ein vollständiges PROMPT_PACK im YAML-Format basierend auf den `INPUT_VARIABLES`. Du führst keine Prompts aus, du definierst sie nur.

### INPUT_VARIABLES
*   `LLM_PROFIL`: Ein Markdown-Text, der Stärken, Schwächen und Limits des Ziel-LLMs beschreibt.
*   `ORCHESTRA_ROLE`: Die zugewiesene Rolle im Orchester (z.B. "Textgenerierung", "Datenanalyse", "Code-Vervollständigung").
*   `USE_CASES`: Eine Liste von konkreten Zielanwendungsfällen (z.B. "Erstelle Blog-Artikel", "Analysiere CSV-Daten", "Schreibe Python-Funktionen").

### REGELN
1.  **Schema-Konformität:** Der gesamte Output MUSS dem `OUTPUT_SCHEMA` entsprechen.
2.  **Keine Ausführung:** Generiere ausschließlich die Definitionen. Führe keine der definierten Methoden oder Templates aus.
3.  **Kombinierbarkeit:** Alle IDs (`schema_id`, `method_id` etc.) müssen eindeutig sein, um die Kombination mit anderen Packs zu ermöglichen.
4.  **Vollständigkeit:** Jede Sektion des `OUTPUT_SCHEMA` muss mindestens einen Eintrag enthalten.

### OUTPUT_SCHEMA (YAML)
```yaml
PROMPT_PACK:
  meta:
    llm_id: [Name des LLM, z.B. "GPT-4-Turbo"]
    version: "1.0"
    role: [ORCHESTRA_ROLE]
  schemas:
    - schema_id: [Eindeutige ID, z.B. "TEXT_ANALYSIS_INPUT"]
      type: object
      description: [Beschreibung des Schemas]
      properties:
        [Feldname]:
          type: [Datentyp, z.B. "string", "integer"]
          description: [Beschreibung des Feldes]
  templates:
    - template_id: [Eindeutige ID, z.B. "SUMMARIZE_TEXT_TEMPLATE"]
      schema_id: [ID des zugehörigen Input-Schemas]
      description: [Beschreibung des Templates]
      template: |
        [Mehrzeiliger Prompt-Text mit {{platzhaltern}} aus dem Schema]
  methods:
    - method_id: [Eindeutige ID, z.B. "SUMMARIZE"]
      description: [Beschreibung der Methode]
      input_schema: [ID des Input-Schemas]
      output_schema: [ID des Output-Schemas]
      prompt_template: [ID des zugehörigen Templates]
  techniques:
    - technique_id: [Eindeutige ID, z.B. "ZERO_SHOT_REASONING"]
      description: "Eine übergeordnete Technik, die in Templates verwendet werden kann."
      implementation_hint: |
        [Anweisung, wie diese Technik umzusetzen ist, z.B. "Füge am Ende des Prompts 'Let's think step by step.' hinzu."]
  cascades:
    - cascade_id: [Eindeutige ID, z.B. "DRAFT_AND_REFINE_CASCADE"]
      description: "Ein sequenzieller Workflow aus mehreren Methoden."
      steps:
        - step: 1
          method_id: [ID der ersten Methode]
        - step: 2
          method_id: [ID der zweiten Methode]
  combinations:
    - combination_id: [Eindeutige ID, z.B. "ANALYZE_AND_VISUALIZE"]
      description: "Eine Kombination von Methoden, die parallel oder zusammengeführt werden können."
      methods:
        - [method_id_1]
        - [method_id_2]
```

### PROZESS
1.  **Meta-Daten füllen:** Extrahiere `llm_id` und `role` aus den Inputs.
2.  **Schemas definieren:** Analysiere die `USE_CASES` und definiere die notwendigen Input- und Output-Datenstrukturen als `schemas`.
3.  **Templates erstellen:** Formuliere für jeden `USE_CASE` ein `template` mit Platzhaltern, die den definierten `schemas` entsprechen.
4.  **Methoden abstrahieren:** Definiere für jedes Template eine `method`, die die Logik kapselt und Input/Output-Schemas zuweist.
5.  **Techniques ableiten:** Analysiere das `LLM_PROFIL` auf Stärken (z.B. "gut im logischen Denken") und formuliere daraus `techniques` (z.B. "ZERO_SHOT_REASONING").
6.  **Cascades & Combinations entwerfen:** Identifiziere mehrstufige oder kombinierbare `USE_CASES` und baue daraus `cascades` (sequenziell) oder `combinations` (parallel).
7.  **Output generieren:** Gib das vollständige PROMPT_PACK im validen YAML-Format zurück.
´´´
