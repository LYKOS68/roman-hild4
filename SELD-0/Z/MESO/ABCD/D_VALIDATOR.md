# D_VALIDATOR | Z (Zustand) · MESO

## SELD-Adresse
`Z.MESO.D`

## Gates in diesem Kontext

| Gate | Check | Rhythmus | effect_score-Schwelle |
|---|---|---|---|
| `Z.MESO.PRE.D` | Darf der Zyklus starten? | operativ | 0.5 |
| `Z.MESO.A→B.D` | Wurde A korrekt abgeschlossen? | operativ | 0.5 |
| `Z.MESO.B→C.D` | Ist die Transformation stabil? | operativ | 0.5 |
| `Z.MESO.C→END.D` | Ist die Information integriert? | operativ | 0.5 |
| `Z.MESO.POST.D` | Rückkopplung vollständig? | operativ | 0.5 |

## Referenz
Globales D_VALIDATOR-Protokoll: `/D_VALIDATOR.md`
SELD-0-Kern: `/KERN/SELD-0.md`

## Status
| Feld | Wert |
|---|---|
| Zustand | AKTIV |
| Letzte Prüfung | — |
| Letztes Ergebnis | — |
