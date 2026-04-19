# D_VALIDATOR | I (Information_Integration) · MAKRO

## SELD-Adresse
`I.MAKRO.D`

## Gates in diesem Kontext

| Gate | Check | Rhythmus | effect_score-Schwelle |
|---|---|---|---|
| `I.MAKRO.PRE.D` | Darf der Zyklus starten? | zyklisch | 0.7 |
| `I.MAKRO.A→B.D` | Wurde A korrekt abgeschlossen? | zyklisch | 0.7 |
| `I.MAKRO.B→C.D` | Ist die Transformation stabil? | zyklisch | 0.7 |
| `I.MAKRO.C→END.D` | Ist die Information integriert? | zyklisch | 0.7 |
| `I.MAKRO.POST.D` | Rückkopplung vollständig? | zyklisch | 0.7 |

## Referenz
Globales D_VALIDATOR-Protokoll: `/D_VALIDATOR.md`
SELD-0-Kern: `/KERN/SELD-0.md`

## Status
| Feld | Wert |
|---|---|
| Zustand | AKTIV |
| Letzte Prüfung | — |
| Letztes Ergebnis | — |
