# D_VALIDATOR | Z (Zustand) · MIKRO

## SELD-Adresse
`Z.MIKRO.D`

## Gates in diesem Kontext

| Gate | Check | Rhythmus | effect_score-Schwelle |
|---|---|---|---|
| `Z.MIKRO.PRE.D` | Darf der Zyklus starten? | atomar | 0.3 |
| `Z.MIKRO.A→B.D` | Wurde A korrekt abgeschlossen? | atomar | 0.3 |
| `Z.MIKRO.B→C.D` | Ist die Transformation stabil? | atomar | 0.3 |
| `Z.MIKRO.C→END.D` | Ist die Information integriert? | atomar | 0.3 |
| `Z.MIKRO.POST.D` | Rückkopplung vollständig? | atomar | 0.3 |

## Referenz
Globales D_VALIDATOR-Protokoll: `/D_VALIDATOR.md`
SELD-0-Kern: `/KERN/SELD-0.md`

## Status
| Feld | Wert |
|---|---|
| Zustand | AKTIV |
| Letzte Prüfung | — |
| Letztes Ergebnis | — |
