# PROJECT_CHARTA — PROTOKOLL-SELD-0

## VERFASSUNGSRANG

Diese Charta ist das oberste Regelwerk des Systems. Kein Tool, kein Operator, kein Prozess darf ihr widersprechen.

## IDENTITÄT

| Feld | Wert |
|---|---|
| System | PROTOKOLL-SELD-0 |
| Producer | Roman |
| Version | SELD-0 v1.0 |
| Erstellt | 2026-04-19 |
| Status | AKTIV |

## DAS OBERSTЕ AXIOM

> Keine Operation (Generieren, Suchen, Erstellen, Bearbeiten, Löschen) darf ohne explizite Nutzerbestätigung ausgeführt werden. Der Producer hat immer das letzte Wort.

## DIE VIER ACHSEN (SELD)

```
S = Säule   (Z · T · I · S)
E = Ebene   (META · MAKRO · MESO · MIKRO)
L = Layer   (A · B · C · D)
D = Delta   (3+1-Validator)

SELD-0 = S × E × L × D
```

### S — Säulen

| Symbol | Name | Funktion |
|---|---|---|
| **Z** | Zustand | Was ist? — Ausgangspunkt, Beobachtung |
| **T** | Transformation | Was passiert? — Veränderung, Herstellung |
| **I** | Information / Integration | Was bedeutet es? Wie passt es ins Ganze? |
| **S** | Stabilität / Synthese | Lokale Effizienz + globale Stabilität |

### E — Ebenen

| Symbol | Name | Funktion |
|---|---|---|
| **META** | Prinzipien | FULL/KOMPLETT. Erst wenn Meta steht, kann operiert werden. |
| **MAKRO** | Strategie | Sequenzielle Einheit — 5 Sequenzen × 4er Prompt-Ketten |
| **MESO** | Struktur | Geteilte Einheit — Base-2 |
| **MIKRO** | Aufgabe | Einzelner Schritt |

> **NANO** ist die Ausführungsebene innerhalb MIKRO. Sie ist keine eigene Ebene in der SELD-Matrix, aber ein gültiger Zoom-Zustand.

### L — Layer (ABCD-Operatoren)

| Symbol | Operator | Bereich | Aktion |
|---|---|---|---|
| **A** | Alpha | Zustand | Beobachten, verstehen |
| **B** | Bravo | Transformation | Umsetzen, herstellen |
| **C** | Charlie | Information + Integration | Prüfen, kritisieren |
| **D** | Delta | Interferenz + Kernalgo | Integrieren, rückkoppeln |

### D — Delta (3+1-Validator)

D ist **nicht** der vierte Schritt. D ist **Meta-Validator**, Gate, Lock und Flow-Controller.

```
A → [D] → B → [D] → C → [D] → Abschluss[D]
```

D liegt:
- **zwischen** jedem ABC-Schritt (Gate)
- **über** jedem ABC-Zyklus (Meta-Lock)
- **unter** jedem Schritt (Interferenz-Fundament)

## 0-KERN

> Der Kern ist die Kreuzung aller vier Achsen.  
> Das System wächst von innen nach außen — nicht von oben nach unten.

Der Kern ist offiziell Teil dieser Verfassung.  
Referenz: `/KERN/SELD-0.md`

## DA-VINCI-GATES (BLOCKIEREND)

Kein Umgehungsweg. Reihenfolge zwingend.

| Gate | Position | Check | Aktion bei Fail |
|---|---|---|---|
| **IMPRENSIVA** | VOR Analyse | Input auf Vorbelastung prüfen | STOP |
| **SFUMATO** | ZWISCHEN Analyse & Ausführung | Detailschritt durchlaufen? | INVALID |
| **FLUSSO** | VOR Ausführung | Fluss-Kapazität überschritten? | THROTTLE |

## PERSISTENZ-DREIKLANG

| Datei | Funktion | Regel |
|---|---|---|
| `state.json` | Canonical JSON, SHA256-verifiziert | WORM |
| `ledger.log` | Append-only Audit-Log | Kein Überschreiben |
| `ANWEISUNG.md` | Master-Anweisung | Kein Überschreiben ohne Freigabe |

## OPERATIONSSTRUKTUR vs. EBENENSTRUKTUR

| Typ | Inhalt | Nicht verwechseln mit |
|---|---|---|
| **Ebenenstruktur** | META · MAKRO · MESO · MIKRO | Zoom-Tiefe |
| **Operationsstruktur (3+1)** | D-Validator-Ebene | Teil des ABCD-Flows, NICHT eine E-Ebene |

## PFLICHTEN JEDES TOOLS

Jedes Tool, das in diesem System operiert, muss:

1. Die SELD-Adresse des aktuellen Schritts kennen (`S.E.L.D`)
2. Den D-Gate-Status vor jedem Layer-Übergang prüfen
3. Keinen Output ohne adressierbare Quelle produzieren
4. Den Zustand nach jeder Mutation in `state.json` spiegeln
5. Jede Mutation in `ledger.log` einzeilig protokollieren

## VERSIONIERUNG

| Version | Änderung |
|---|---|
| ZTIIS_v2 | Ursprungssystem — Säulen, Ebenen, Operatoren |
| SELD-0 v1.0 | Vier Achsen zu einem operativen Kern verschmolzen. 0-KERN offiziell. D als Meta-Validator definiert. |
