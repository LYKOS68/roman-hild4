# P14 Synergos: Das Knowledge-Index-System (Das Patchbay)

**Status:** Aktiviert | **System:** Synergos | **Methode:** Curie (Extraktion) + Feynman (Didaktik) + Allen (GTD-Flow)

Dieses Dokument ist das Patchbay der DAW. In FL Studio zeigt dir das Patchbay, welches Kabel wo steckt, welches Signal wohin fließt und wie die Module miteinander verbunden sind. Ohne Patchbay stöpselst du blind. Das Knowledge-Index-System ist die systematische Kategorisierung und Indexierung aller bisherigen Artefakte (P1-P13) mit einer festen Taxonomie. Es ordnet das Chaos, verknüpft die Spuren und macht alles auffindbar – sowohl für den Producer als auch für das RAG-System (Retrieval-Augmented Generation).

---

## TEIL 1: SYSTEM-PROMPT (Das Patchbay-Plugin)

Kopiere den folgenden Block und integriere ihn in deine Synergos-Architektur. Dieser Prompt zwingt das System, jedes neue Artefakt systematisch in das Patchbay einzuordnen.

```markdown
::KNOWLEDGE_INDEX_START::

[1. UR-INTENTIONS-TRIGGER (Das Patchbay-Prinzip)]
Jede Interaktion, die ein neues Artefakt oder Modul generiert, MUSS zwingend in den zentralen Knowledge-Index (das Patchbay) eingeordnet werden. 
Dualer Nutzen: 
1. Navigation für den Producer (Wo steckt das Kabel?).
2. Retrieval-Grundlage für RAG (Welche Module sind verwandt?).
Kein Artefakt darf ungebunden bleiben. Jedes Artefakt ist ein Modul im Rack und braucht ein Etikett und mindestens zwei Kabel zu anderen Modulen.

[2. INDEX-TAXONOMIE (Die 6 Etiketten)]
Jedes Artefakt muss mit diesen 6 Feldern getaggt werden:
- Typ: [Axiom / Pipeline-Schritt / Validierungsregel / Vorlage / System-Instruction / Grenze / State-Vector-Update / Modul / Analyse]
- Quelle: [Referenz auf generierenden Prompt oder Trigger, z.B. P12-Demo, Nutzer-Input]
- Genie-Logik: [Feynman (Didaktik/Debugging) / Curie (Systematische Extraktion) / Allen (GTD-Produktivität) oder Hybrid]
- Anwendungsbereich: [Eingabe / Verarbeitung / Output / Validierung / Wartung / Routing]
- Abhängigkeiten: [Verlinkung zu anderen Artefakten, die zwingend benötigt werden]
- Testfrage: [Eine spezifische Validierungsfrage, um die Funktion des Artefakts zu prüfen]

[3. OPERATIONS-PROTOKOLL (Die 5 Schritte beim Patchen)]
Wenn ein neues Artefakt erstellt wird, durchläuft es diese 5 Schritte:
1. Generierung: Das Artefakt wird erstellt (nach P5/P10).
2. Kategorisierung: Die 6 Taxonomie-Felder werden ausgefüllt.
3. Verknüpfung: Mindestens 2 Links zu bestehenden P-Artefakten werden gezogen.
4. Index-Update: Das Artefakt wird als JSON/YAML-Block für den Index formatiert.
5. Navigationshinweis: Dem Producer wird gesagt, wo in der Projektstruktur das Artefakt abgelegt werden muss.

[4. AUSGABEFORMAT (Der Knowledge-Index-Entry Block)]
Jedes neue Artefakt muss diesen Block am Ende enthalten:

> **[KNOWLEDGE-INDEX-ENTRY]**
> - **Typ:** [Typ]
> - **Quelle:** [Quelle]
> - **Genie-Logik:** [Logik]
> - **Anwendungsbereich:** [Bereich]
> - **Abhängigkeiten:** [Abhängigkeiten]
> - **Testfrage:** [Frage]
> - **Verknüpfungen:** [Link 1], [Link 2]

::KNOWLEDGE_INDEX_ENDE::
```

---

## TEIL 2: VOLLSTÄNDIGER INDEX ALLER ARTEFAKTE (P1-P13)

Hier ist das komplette Patchbay für alle bisherigen Spuren. Jedes Artefakt ist sauber etikettiert und verkabelt.

### a) Markdown-Tabelle (Für den Producer)

| ID | Artefakt-Name | Typ | Quelle | Genie-Logik | Anwendungsbereich | Abhängigkeiten | Testfrage | Verknüpfungen |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P1** | Modellauskunft | Analyse | System-Scan | Feynman | Eingabe | Keine | Welche Hard- und Software-Grenzen hat die aktuelle DAW? | P2, P13 |
| **P2** | Design-Axiome | Axiom | P1-Analyse | Curie | Verarbeitung | P1 | Wurden alle 6 Axiome (A1-A6) als harte Regler angewendet? | P5, P6 |
| **P3** | Struktur-Transfer | Pipeline-Schritt | P2-Axiome | Curie | Verarbeitung | P2 | Bestimmt die Form des Inputs die Form des Outputs (Echo-Prinzip)? | P4, P5 |
| **P4** | Referenz-Prompt | Vorlage | P3-Regeln | Allen | Output | P2, P3 | Enthält der Output die 5 zwingenden Elemente? | P5, P10 |
| **P5** | Kern-Prompt | System-Instruction | P1-P4 | Hybrid | Verarbeitung | P2, P3, P4 | Wurden die Master-Regeln vor den Task-Regeln geladen? | P6, P10 |
| **P6** | Pipeline | Pipeline-Schritt | P5 | Allen | Verarbeitung | P2, P5 | Wurden alle 12 Stufen der Signalkette ohne Lücken durchlaufen? | P7, P10 |
| **P7** | Validierung | Validierungsregel | P6 | Curie | Validierung | P5, P6 | Besteht der Output den 3+1 Dreiklang mit 6R-Check? | P10, P11 |
| **P8** | Pattern-Extraktion | Modul | P7 | Curie | Verarbeitung | P5, P6 | Wurde das erkannte Muster als wiederverwendbares Preset gespeichert? | P10, P11 |
| **P9** | Lehrmeister | Modul | P8 | Feynman | Output | P5 | Wurde das "Warum" hinter dem "Was" in FL-Studio-Metaphern erklärt? | P10, P12 |
| **P10** | RTE | System-Instruction | P5-P9 | Hybrid | Routing | P5, P6, P7 | Wurde die Automations-Spur für diese Anfrage korrekt geroutet? | P11, P12 |
| **P11** | State-Vector | State-Vector-Update | P10 | Allen | Wartung | P10 | Wurden alle 5 Bänder des externen Gedächtnisses aktualisiert? | P10, P13 |
| **P12** | Befähigung | Modul | P9, P11 | Feynman | Output | P9, P11 | Hat der Producer durch diese Interaktion mehr Autonomie gewonnen? | P9, P13 |
| **P13** | Ephemeralität | Grenze | P1-P12 | Curie | Validierung | P5, P11 | Stößt dieser Output an eine harte systemische Grenze (Limiter)? | P1, P11 |

### b) JSON-Array (Für maschinelle Verarbeitung / RAG)

```json
[
  {
    "id": "P1",
    "name": "Modellauskunft",
    "type": "Analyse",
    "source": "System-Scan",
    "genie_logic": "Feynman",
    "application_area": "Eingabe",
    "dependencies": [],
    "test_question": "Welche Hard- und Software-Grenzen hat die aktuelle DAW?",
    "links": ["P2", "P13"]
  },
  {
    "id": "P2",
    "name": "Design-Axiome",
    "type": "Axiom",
    "source": "P1-Analyse",
    "genie_logic": "Curie",
    "application_area": "Verarbeitung",
    "dependencies": ["P1"],
    "test_question": "Wurden alle 6 Axiome (A1-A6) als harte Regler angewendet?",
    "links": ["P5", "P6"]
  },
  {
    "id": "P3",
    "name": "Struktur-Transfer",
    "type": "Pipeline-Schritt",
    "source": "P2-Axiome",
    "genie_logic": "Curie",
    "application_area": "Verarbeitung",
    "dependencies": ["P2"],
    "test_question": "Bestimmt die Form des Inputs die Form des Outputs (Echo-Prinzip)?",
    "links": ["P4", "P5"]
  },
  {
    "id": "P4",
    "name": "Referenz-Prompt",
    "type": "Vorlage",
    "source": "P3-Regeln",
    "genie_logic": "Allen",
    "application_area": "Output",
    "dependencies": ["P2", "P3"],
    "test_question": "Enthält der Output die 5 zwingenden Elemente?",
    "links": ["P5", "P10"]
  },
  {
    "id": "P5",
    "name": "Kern-Prompt",
    "type": "System-Instruction",
    "source": "P1-P4",
    "genie_logic": "Hybrid",
    "application_area": "Verarbeitung",
    "dependencies": ["P2", "P3", "P4"],
    "test_question": "Wurden die Master-Regeln vor den Task-Regeln geladen?",
    "links": ["P6", "P10"]
  },
  {
    "id": "P6",
    "name": "Pipeline",
    "type": "Pipeline-Schritt",
    "source": "P5",
    "genie_logic": "Allen",
    "application_area": "Verarbeitung",
    "dependencies": ["P2", "P5"],
    "test_question": "Wurden alle 12 Stufen der Signalkette ohne Lücken durchlaufen?",
    "links": ["P7", "P10"]
  },
  {
    "id": "P7",
    "name": "Validierung",
    "type": "Validierungsregel",
    "source": "P6",
    "genie_logic": "Curie",
    "application_area": "Validierung",
    "dependencies": ["P5", "P6"],
    "test_question": "Besteht der Output den 3+1 Dreiklang mit 6R-Check?",
    "links": ["P10", "P11"]
  },
  {
    "id": "P8",
    "name": "Pattern-Extraktion",
    "type": "Modul",
    "source": "P7",
    "genie_logic": "Curie",
    "application_area": "Verarbeitung",
    "dependencies": ["P5", "P6"],
    "test_question": "Wurde das erkannte Muster als wiederverwendbares Preset gespeichert?",
    "links": ["P10", "P11"]
  },
  {
    "id": "P9",
    "name": "Lehrmeister",
    "type": "Modul",
    "source": "P8",
    "genie_logic": "Feynman",
    "application_area": "Output",
    "dependencies": ["P5"],
    "test_question": "Wurde das 'Warum' hinter dem 'Was' in FL-Studio-Metaphern erklärt?",
    "links": ["P10", "P12"]
  },
  {
    "id": "P10",
    "name": "RTE",
    "type": "System-Instruction",
    "source": "P5-P9",
    "genie_logic": "Hybrid",
    "application_area": "Routing",
    "dependencies": ["P5", "P6", "P7"],
    "test_question": "Wurde die Automations-Spur für diese Anfrage korrekt geroutet?",
    "links": ["P11", "P12"]
  },
  {
    "id": "P11",
    "name": "State-Vector",
    "type": "State-Vector-Update",
    "source": "P10",
    "genie_logic": "Allen",
    "application_area": "Wartung",
    "dependencies": ["P10"],
    "test_question": "Wurden alle 5 Bänder des externen Gedächtnisses aktualisiert?",
    "links": ["P10", "P13"]
  },
  {
    "id": "P12",
    "name": "Befähigung",
    "type": "Modul",
    "source": "P9, P11",
    "genie_logic": "Feynman",
    "application_area": "Output",
    "dependencies": ["P9", "P11"],
    "test_question": "Hat der Producer durch diese Interaktion mehr Autonomie gewonnen?",
    "links": ["P9", "P13"]
  },
  {
    "id": "P13",
    "name": "Ephemeralität",
    "type": "Grenze",
    "source": "P1-P12",
    "genie_logic": "Curie",
    "application_area": "Validierung",
    "dependencies": ["P5", "P11"],
    "test_question": "Stößt dieser Output an eine harte systemische Grenze (Limiter)?",
    "links": ["P1", "P11"]
  }
]
```

---

## TEIL 3: LIVE-DEMONSTRATION (P13 Index-Eintrag)

Hier ist die Live-Demo, wie das Patchbay-Protokoll in der Praxis aussieht. Wir patchen P13 (das Ephemeralitäts-Protokoll) in den Index.

```yaml
---
id: P13
title: Ephemeralitäts-Protokoll (Der Master-Bus-Limiter)
status: Aktiviert
---

> **[KNOWLEDGE-INDEX-ENTRY]**
> - **Typ:** Grenze
> - **Quelle:** Analyse der Systemgrenzen P1-P12
> - **Genie-Logik:** Curie (Systematische Extraktion der Limits)
> - **Anwendungsbereich:** Validierung
> - **Abhängigkeiten:** P5 (Kern-Prompt), P11 (State-Vector)
> - **Testfrage:** Stößt dieser Output an eine harte systemische Grenze (Limiter)?
> - **Verknüpfungen:** 
>   - Link 1: [P1 Modellauskunft] (Definiert die ursprünglichen Hardware-Grenzen)
>   - Link 2: [P11 State-Vector] (Speicherort für erkannte Lücken und Workarounds)
>   - Link 3: [P5 Kern-Prompt] (Limiter greift VOR dem Master-Export-Gate ein)
```

**Navigationshinweis für den Producer:** 
Speichere diesen YAML/Index-Block am Ende der Datei `p13_synergos_ephemeralitaet.md`. Er dient als Meta-Tag für zukünftige Suchanfragen und RAG-Pipelines.

---

## TEIL 4: ABHÄNGIGKEITSGRAPH (Die Kabelverbindungen)

Dieses ASCII-Diagramm zeigt das komplette Routing. Es macht sichtbar, welche Module das Fundament bilden (die Stromversorgung), welche in Reihe geschaltet sind (die Signalkette) und welche als Sidechain über allem liegen.

```text
=========================================================================
                      SYNERGOS PATCHBAY ROUTING
=========================================================================

[GRUNDLAGEN / STROMVERSORGUNG]
  P1 (Modellauskunft) ──────┐
                            ▼
  P2 (Design-Axiome) ───────┼───► P5 (KERN-PROMPT / MASTER-BUS)
                            ▲     │
  P3 (Struktur-Transfer) ───┤     │
                            │     │
  P4 (Referenz-Prompt) ─────┘     │
                                  │
==================================│======================================
                                  ▼
[SIGNALKETTE / PIPELINE]          │
  P6 (12-Stufen-Pipeline) ◄───────┘
          │
          ▼
  P7 (Validierung)
          │
          ▼
  P8 (Pattern-Extraktion)
          │
          ▼
  P9 (Lehrmeister)
          │
=========================================================================
          ▼
[AUTOMATION & ROUTING]
  P10 (RTE / Controller) ◄─── Bündelt P5 bis P9 und steuert den Mix
          │
=========================================================================
          ▼
[QUERSCHNITTSFUNKTIONEN / SIDECHAIN & LIMITER]

  ┌──────────────────────────────────────────────────────────┐
  │                                                          │
  │  P11 (State-Vector) ◄───────► P12 (Befähigung)           │
  │  (Das Gedächtnis)             (Der Lern-Loop)            │
  │          ▲                                               │
  │          │                                               │
  │          ▼                                               │
  │  P13 (Ephemeralität)                                     │
  │  (Der Master-Bus-Limiter)                                │
  │                                                          │
  └──────────────────────────────────────────────────────────┘

=========================================================================
```

**Erklärung des Routings:**
1. **Grundlagen (P1-P5):** Das ist die Stromversorgung. P5 ist der Master-Bus, in den alles reinfließt. Ohne P5 läuft gar nichts.
2. **Signalkette (P6-P9):** Das ist die serielle Pipeline. Das Signal läuft von P6 (Aufnahme/Struktur) über P7 (Validierung) und P8 (Mustererkennung) bis zu P9 (Didaktik).
3. **Automation (P10):** Die RTE ist der MIDI-Controller, der auf dem Pult liegt und alle Regler von P5 bis P9 automatisch steuert.
4. **Querschnittsfunktionen (P11-P13):** Diese Module liegen als Sidechain über dem gesamten Projekt. P11 speichert jeden Handgriff, P12 trainiert den Producer parallel, und P13 limitiert das Signal kurz vor dem Master-Out, damit nichts clippt.
