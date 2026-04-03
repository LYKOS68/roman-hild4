# SYNERGOS – Personal-GPT-Orchestration System

## Version 1.0 | Erstellt: 2026-03-22 18:08

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
