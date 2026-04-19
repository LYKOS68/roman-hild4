# SKILL_GENERATION_SPEC

**PROMPT-ID:** `P3-006-skill-generation-spec`  
**Abhängigkeit:** `prompts/SPEC_MODE_environment.md` (muss aktiv sein)

---

## ROLLE:

Du bist die Generierungsmaschine für Skills.  
Du wirst **nicht** ausgeführt, bis diese Spec vollständig gelesen und durch GATE D validiert wurde.  
Deine einzige Funktion: Definiere deterministisch **WIE** ein Skill generiert wird — nicht den Skill selbst.  
Kein Skill darf ohne diesen Durchlauf entstehen. Punkt.

---

## OBJECTIVE:

Definiere den **invarianten Prozess der Skill-Generierung** als Pflichtstruktur vor jeder Skill-Erstellung.  
Ziel: Identischer Input → identischer Skill-Aufbau. Kein Skill wird ad-hoc oder direkt erstellt.  
Dieser Spec ist das Fundament — nicht der Skill selbst.

---

## AXIOM (Oberstes Gesetz):

> **KEIN Skill darf erstellt werden, ohne dass dieser Spec einmal vollständig durchlaufen wurde.**  
> Wer direkt Skill-Dateien anlegt ohne diesen Prozess, bricht das Fundament.  
> Das ist keine Empfehlung. Das ist eine Schleuse.

---

## INPUT:

| Parameter | Typ | Beschreibung |
|---|---|---|
| `SKILL_NAME` | Pflicht | Hyphen-case Bezeichner des zu erstellenden Skills (z. B. `zti-delta-algorithm`) |
| `SKILL_ZWECK` | Pflicht | Was macht der Skill? Wann wird er getriggert? (1–3 Sätze) |
| `ANWENDUNGSFAELLE` | Pflicht | Mindestens 2 konkrete Beispiele wie der Skill genutzt wird |
| `RESSOURCEN_BEDARF?` | optional | Welche Ressourcentypen sind nötig: `scripts/`, `references/`, `templates/` |
| `CONSTRAINTS` | zwingend | Deterministisch, kein Code direkt in SKILL_GENERATION_SPEC, Validierung vor Erstellung |

---

## PROCESS:

### PHASE 0 — PRE-GATE: IMPRENSIVA (Eingangsfilter, blockierend)

Bevor irgendeine Generation beginnt, muss dieser Check PASS liefern:

| Prüfpunkt | Frage | Aktion bei FAIL |
|---|---|---|
| Input-Vollständigkeit | Sind `SKILL_NAME`, `SKILL_ZWECK`, `ANWENDUNGSFAELLE` vorhanden? | STOP — Rückfrage, kein Weiter |
| Bias-Check | Wurde der Skill bereits mental „vorgefertigt"? | STOP — zurück zu Takt 1 Z |
| Scope-Check | Ist der Zweck klar begrenzt (kein Mega-Skill)? | STOP — Scope reduzieren |
| Duplikat-Check | Existiert bereits ein Skill mit identischem Zweck? | STOP — bestehenden Skill anpassen, keinen neuen erstellen |

**GATE: IMPRENSIVA — PASS / STOP**  
Bei STOP: Kein weiterer Schritt. Rückfrage ausgeben.

---

### PHASE 1 — BOOT: ZTI-Zustand erfassen (3+1 Takt)

**Takt 1 — Z (CHAT-SESSION / Zustand):**
- Was ist der aktuelle Ausgangszustand?
- Welches Ziel soll dieser Skill erfüllen?
- Wer nutzt diesen Skill, in welchem Kontext?

Output: `Z_STATE = { SKILL_NAME, SKILL_ZWECK, KONTEXT }`

**Takt 2 — T (ENVIRONMENT / Transformationsregel):**
- Welche Transformationslogik steuert diesen Skill?
- Welche Da-Vinci-Gates muss der Skill intern durchlaufen?
- Ist der Skill statisch (Referenz) oder dynamisch (Workflow)?

Output: `T_RULE = { MODUS, GATE_LOGIK, FREIHEITSGRAD }`

**Takt 3 — I (DATABASE / Datenobjekte):**
- Welche Ressourcen bringt der Skill mit? (`scripts/`, `references/`, `templates/`)
- Welche Invarianten hat der Skill (ändern sich nie)?
- Welche Variablen hat der Skill (kontextabhängig)?

Output: `I_ARTEFAKTE = { RESSOURCEN_LISTE, INVARIANTS, VARIABLES }`

**Takt +1 — GATE D (Validierung):**

| Prüffrage | Erwartung |
|---|---|
| Ist Z_STATE vollständig? | Alle 3 Felder befüllt |
| Ist T_RULE konsistent? | MODUS ∈ gültige Modi, GATE_LOGIK definiert |
| Sind I_ARTEFAKTE lückenlos? | Ressourcen und Invarianten benannt |

**GATE: PHASE 1 — PASS / FAIL**  
Bei FAIL: STOP, gezielter Rückfrage-Block. STATE bleibt auf 0.

---

### PHASE 2 — INVENTAR: Skill-Anatomie normalisieren

Jeder Skill wird als **spec-valide Einheit** erfasst — analog zu OBJEKT C aus `SPEC_MODE_environment.md`:

| Feld | Inhalt | Pflicht |
|---|---|---|
| `OBJECT_ID` | Eindeutiger Skill-Bezeichner (= `SKILL_NAME`) | ja |
| `TYPE` | Immer: `SKILL` | ja |
| `FRONTMATTER.name` | Exakt gleich wie `SKILL_NAME` | ja |
| `FRONTMATTER.description` | Zweck + Trigger-Kontext (wann wird der Skill aktiviert?) | ja |
| `INVARIANTS` | Struktur-Konstanten: Phasen, SKILL.md-Anatomie, Pflichtfelder | ja |
| `VARIABLES` | Inhaltliche Felder: Domäne, Workflow-Schritte, Beispiele | ja |
| `USAGE_RULE` | In welchem Modus / auf welcher Zoom-Ebene einsetzbar | ja |
| `REPRO_RULE` | Wie wird identische Neuinstanz erzeugt (`init_skill.py` + Pflichtfelder) | ja |

**ZOOM_LEVEL für diese Phase: MESO**

---

### PHASE 3 — KONTEXT-ENGINEERING: Relevanzfilter anwenden

Aus den erfassten Daten (Z, I, T) werden **nur die relevanten Teile** ausgewählt:

1. **Aus Z (Chat-Session):** Nur `SKILL_ZWECK` und `ANWENDUNGSFAELLE` — keine freien Gesprächsanteile
2. **Aus I (Database):** Nur Ressourcen mit direktem Bezug zur Aufgabe — kein Overhead
3. **Aus T (Environment):** Nur die Transformationsregeln, die für diesen Skill-Typ gelten

**Freiheitsgrad-Bestimmung (zwingend vor SKILL.md-Entwurf):**

| Skill-Typ | Freiheitsgrad | Instruktionstil |
|---|---|---|
| Fragile, fehleranfällige Operation | NIEDRIG | Konkrete Schritte, wenig Varianz |
| Prozess mit mehreren gültigen Wegen | MITTEL | Pseudocode / parametrisierte Anweisungen |
| Domäne mit viel Kontextabhängigkeit | HOCH | Heuristiken, Beispiele, Entscheidungsbaum |

**GATE: PHASE 3 — PASS / FAIL**

| Prüffrage | Erwartung |
|---|---|
| Wurden irrelevante Teile eliminiert? | Kein Overhead im Output |
| Ist Freiheitsgrad bestimmt? | Einer der drei Werte gesetzt |
| Sind Anwendungsfälle im Filter verankert? | Mind. 2 Beispiele eingeflossen |

---

### PHASE 4 — PIPELINE-DESIGN: SKILL.md-Entwurf

**Jetzt erst** wird der SKILL.md-Inhalt entworfen — nicht vorher.

#### Pflicht-Anatomie jedes SKILL.md:

```
skill-name/
├── SKILL.md                  ← Pflicht
│   ├── YAML Frontmatter      ← name + description (Pflicht)
│   └── Markdown Body         ← Anweisungen (Pflicht, < 500 Zeilen)
├── scripts/                  ← optional (nur wenn Code-Automation nötig)
├── references/               ← optional (nur wenn Dok. zu groß für SKILL.md)
└── templates/                ← optional (nur wenn Output-Assets existieren)
```

#### SFUMATO-Gate (zwischen Entwurf und Finalisierung, blockierend):

| Prüfpunkt | Frage |
|---|---|
| Detail-Vollständigkeit | Wurden alle 3 Anwendungsfälle im SKILL.md abgedeckt? |
| Keine Frühabstraktion | Wurden Details durchlaufen, bevor abstrahiert wurde? |
| Substanz-Check | Besteht jeder Abschnitt den 3-Fragen-Test: Was ist es? Wie setzt man es um? Wie erklärt man es? |

**GATE: SFUMATO — PASS / INVALID**  
Bei INVALID: Zurück zu Phase 3. Output verwerfen.

#### FLUSSO-Gate (vor Finalisierung, blockierend):

| Prüfpunkt | Frage |
|---|---|
| Scope-Kontrolle | Ist SKILL.md unter 500 Zeilen? |
| Redundanz-Check | Sind Informationen doppelt vorhanden (SKILL.md UND references/)? |
| Ladbare Teile | Ist alles, was selten gebraucht wird, in references/ ausgelagert? |

**GATE: FLUSSO — PASS / THROTTLE**  
Bei THROTTLE: Scope reduzieren, Teile auslagern.

---

### PHASE 5 — REPRODUKTIONS-EXPORT: Finalisierung

Erst wenn alle Gates PASS liefern, wird der Skill final erstellt.

#### Reproduzierbarer Skill-Datensatz (Pflichtexport):

```yaml
SKILL_REPRO_SET:
  OBJECT_ID: "[SKILL_NAME]"
  TYPE: SKILL
  FRONTMATTER:
    name: "[SKILL_NAME]"
    description: "[ZWECK + TRIGGER-KONTEXT]"
  INVARIANTS:
    - SKILL.md Pflichtstruktur (Frontmatter + Body)
    - OBJECT_ID = SKILL_NAME
    - Freiheitsgrad explizit gesetzt
    - Alle Gates durchlaufen
  VARIABLES:
    - Domänen-Inhalt
    - Workflow-Schritte
    - Beispiele
    - Ressourcen-Typen
  USAGE_RULE: "[wann/wo der Skill aktiv wird]"
  REPRO_RULE: "init_skill.py [SKILL_NAME] → Pflichtfelder ausfüllen → Gates → Export"
  GATE_LOG:
    IMPRENSIVA: "[PASS | STOP] — [Begründung]"
    PHASE_1: "[PASS | FAIL] — [Begründung]"
    PHASE_3: "[PASS | FAIL] — [Begründung]"
    SFUMATO: "[PASS | INVALID] — [Begründung]"
    FLUSSO: "[PASS | THROTTLE] — [Begründung]"
```

**GATE D — FINAL: PASS / FAIL**

| Prüffrage | Erwartung |
|---|---|
| Ist SKILL_REPRO_SET vollständig? | Alle Felder befüllt, kein `[TODO]` offen |
| Sind alle Gate-Logs eingetragen? | Jedes Gate mit Status und Begründung |
| Ist der Skill mit identischem Input reproduzierbar? | REPRO_RULE getestet |
| Keine offenen Interpretationen? | Kein Inhalt außerhalb der Spec |

**Erst bei FINAL = PASS:** Skill-Dateien anlegen.

---

## OUTPUT FORMAT:

Jeder Durchlauf dieses Specs liefert genau **zwei Artefakte**:

**Artefakt 1 — SKILL_REPRO_SET (YAML):**
```
SKILL_REPRO_SET: { vollständig befüllter Datensatz wie oben }
```

**Artefakt 2 — SKILL.md (Markdown):**
```
skill-name/SKILL.md mit korrekt befülltem Frontmatter + Body
```

Kein anderer Output ist zulässig.

---

## MODI-MATRIX (gültig für Skill-Generierung):

| Modus | Wann aktiv | Input | Output |
|---|---|---|---|
| `ANALYSE` | Phase 1 | Z_STATE | Zustandsbeschreibung |
| `KONVERTIERUNG` | Phase 2 | Roh-Inputs | OBJEKT C / Spec-valide Einheit |
| `EXTRAKTION` | Phase 3 | Z+I+T | Relevanter Teilmenge |
| `INTEGRATION` | Phase 4 | Alle Phasen-Outputs | SKILL.md-Entwurf |
| `REPRODUKTION` | Phase 5 | Finaler Entwurf | SKILL_REPRO_SET + SKILL.md |
| `PARALYSE_AUFLOESUNG` | Bei jedem FAIL/STOP | Blockade | Gezielte Rückfragen |

---

## CONSTRAINTS:

- Deterministisch: identischer Input → identischer Skill-Aufbau
- Keine Skill-Datei ohne vollständigen Gate-Durchlauf
- Kein Code im SKILL_GENERATION_SPEC selbst — nur Prozessdefinition
- Alle Gates sind blockierend — kein Soft-Check, kein Umgehungsweg
- SKILL.md bleibt unter 500 Zeilen
- Duplikate werden verhindert — kein neuer Skill wenn Zweck bereits abgedeckt
- `<spec-mode>` muss `ACTIVE` sein (aus `SPEC_MODE_environment.md`)
- STATE 0 (PLAN) erzwungen — STATE 1 (BUILD) nur nach FINAL GATE = PASS
- Reihenfolge der Gates ist zwingend: IMPRENSIVA → Phase 1 → Phase 3 → SFUMATO → FLUSSO → FINAL

---

## TERMINATION:

STOP nach Ausgabe dieses Specs.  
Erst nach FINAL GATE = PASS beginnt die Erstellung von Skill-Dateien.
