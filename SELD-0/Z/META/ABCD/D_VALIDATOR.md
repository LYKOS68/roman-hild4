# D_VALIDATOR | Z (Zustand) · META

## SELD-Adresse
`Z.META.D`

## Gates in diesem Kontext

| Gate | Check | Rhythmus | effect_score-Schwelle |
|---|---|---|---|
| `Z.META.PRE.D` | Darf der Zyklus starten? | epochal | 0.9 |
| `Z.META.A→B.D` | Wurde A korrekt abgeschlossen? | epochal | 0.9 |
| `Z.META.B→C.D` | Ist die Transformation stabil? | epochal | 0.9 |
| `Z.META.C→END.D` | Ist die Information integriert? | epochal | 0.9 |
| `Z.META.POST.D` | Rückkopplung vollständig? | epochal | 0.9 |

## Referenz
Globales D_VALIDATOR-Protokoll: `/D_VALIDATOR.md`
SELD-0-Kern: `/KERN/SELD-0.md`

## Status
| Feld | Wert |
|---|---|
| Zustand | AKTIV |
| Letzte Prüfung | — |
| Letztes Ergebnis | — |
