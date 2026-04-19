# D_VALIDATOR — VALIDATOR-META-EBENE

## DEFINITION

Der D_VALIDATOR ist die operative Meta-Ebene des 3+1-Systems.  
Er ist **kein** Teil der Ebenenstruktur (E.ME.NA).  
Er ist **Teil der Operationsstruktur** — das Gate, das ABC überhaupt erst erlaubt.

## POSITION IM ABLAUF

```
START
  │
  ▼
[D_VALIDATOR: PRE-CYCLE-GATE]
  │  Darf der Zyklus starten?
  │  PASS → weiter │ FAIL → STOP
  ▼
  A  (Alpha: Beobachten, verstehen)
  │
  ▼
[D_VALIDATOR: A→B-GATE]
  │  Wurde A korrekt abgeschlossen?
  │  PASS → weiter │ FAIL → zurück zu A
  ▼
  B  (Bravo: Umsetzen, herstellen)
  │
  ▼
[D_VALIDATOR: B→C-GATE]
  │  Ist die Transformation stabil?
  │  PASS → weiter │ FAIL → zurück zu B
  ▼
  C  (Charlie: Prüfen, kritisieren)
  │
  ▼
[D_VALIDATOR: C→ABSCHLUSS-GATE]
  │  Ist die Information integriert?
  │  PASS → weiter │ FAIL → zurück zu C
  ▼
ABSCHLUSS [D_VALIDATOR: POST-CYCLE-LOCK]
  │  Rückkopplung vollständig?
  │  PASS → State-Update │ FAIL → Zyklus wiederholen
  ▼
END
```

## GATE-FELDER (6-FELDER-MODELL)

Jeder D_VALIDATOR-Check verwendet folgende 6 Felder:

| Feld | Beschreibung | Pflicht |
|---|---|---|
| `boundary` | Wo im Zyklus bin ich? (`PRE` / `A→B` / `B→C` / `C→END` / `POST`) | ja |
| `candidate` | Welcher Output will das Gate passieren? | ja |
| `decision` | PASS oder FAIL | ja |
| `delta_rhythm` | epochal / zyklisch / operativ / kontinuierlich / atomar | ja |
| `delta_level` | META / MAKRO / MESO / MIKRO | ja |
| `effect_score` | 0.0 – 1.0 normalisiert (Auswirkung der Entscheidung) | ja |

## GATE-LOGIK

| Bedingung | Reaktion |
|---|---|
| `decision = PASS` | Nächster Schritt freigegeben |
| `decision = FAIL` | Aktueller Schritt wiederholen. Kein Vorwärtsgehen. |
| `effect_score > 0.8` | Automatisch an Producer eskalieren |
| `boundary = PRE` und FAIL | Gesamter Zyklus gesperrt. STOP. |
| `boundary = POST` und FAIL | Rückkopplungsschleife. Zyklus neu starten. |

## SELD-ADRESSE

Jeder D_VALIDATOR-Check ist einer SELD-Adresse zugeordnet:

```
Format: S.E.L.D
Beispiel: Z.META.A→B.D
          T.MESO.B→C.D
          I.MAKRO.POST.D
```

## D_VALIDATOR PRO EBENE

Jede Ebene (META / MAKRO / MESO / MIKRO) hat ihren eigenen D_VALIDATOR-Kontext:

| Ebene | Delta-Rhythmus | Typische effect_score-Schwelle |
|---|---|---|
| META | epochal | 0.9 |
| MAKRO | zyklisch | 0.7 |
| MESO | operativ | 0.5 |
| MIKRO | atomar | 0.3 |

## INTERFERENZ-RÜCKKOPPLUNG

Nach jedem vollständigen ABC-Zyklus (POST-Gate) führt der D_VALIDATOR eine Interferenz-Prüfung durch:

```
Interferenz = Δ(Zustand_nach_Zyklus) − Δ(Zustand_vor_Zyklus)
```

Wenn `|Interferenz| < Schwellwert` → Zyklus war stabil.  
Wenn `|Interferenz| ≥ Schwellwert` → Rückkopplung: Zyklus wiederholen oder Producer-Freigabe.

## VERHÄLTNIS ZU DA-VINCI-GATES

| Gate | Relation zu D_VALIDATOR |
|---|---|
| IMPRENSIVA | Vorgelagert — prüft den Input, bevor D_VALIDATOR aktiv wird |
| SFUMATO | Kooperativ — prüft, ob D_VALIDATOR den Detailschritt wirklich ausgeführt hat |
| FLUSSO | Übergeordnet — kann D_VALIDATOR-Zyklen drosseln |

## STATUS

| Feld | Wert |
|---|---|
| Version | D_VALIDATOR v1.0 |
| Erstellt | 2026-04-19 |
| Träger | `/D_VALIDATOR.md` |
| Zustand | AKTIV |
| Besitzer | Roman (Producer) |
| Referenz Kern | `/KERN/SELD-0.md` |
