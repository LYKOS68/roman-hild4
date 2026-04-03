---
name: zti-delta-algorithm
description: Implementiert den ZTI+ΔZ Kernalgorithmus für zustandsbasierte Inferenz mit Delta-Integration, Invarianten-Prüfung und Shadow-Validierung. Verwenden Sie diesen Skill, um jede Zustandsänderung nach einem minimalen, aber vollständigen Protokoll zu verarbeiten.
---

# ZTI+ΔZ Kernalgorithmus mit A-B-C-D-Rollenmodell

Dieser Skill implementiert einen sich selbst regulierenden, zustandsbasierten Inferenzzyklus. Er formalisiert den Prozess durch vier Funktionsrollen (A, B, C, D), die analog zu Legislative, Exekutive und Judikative eines Rechtsstaats agieren.

## Die ZTI-Metapher: Das Gebäude

Die gesamte Operation basiert auf Ihrer präzisen Metapher:

*   **Z (Zustand):** Das Gebäude. Der Ort, wo alles ist. Der aktuelle Kontext, die Regeln, die Identität. **Was gilt jetzt?**
*   **T (Transformation):** Das Lager. Der Ort, wo Bewegung passiert. Die Ausführung, die Veränderung.
*   **I (Information):** Das Büro. Der Ort, wo die Anweisung lebt. Die Planung, die Steuerung, die Daten.

> **Referenzen:** 
> - ZTI-Metapher: `/home/ubuntu/skills/zti-delta-algorithm/references/zti_metaphor.yaml`
> - A-B-C-D-Modell: `/home/ubuntu/skills/zti-delta-algorithm/references/abcd_model.yaml`

## Das A-B-C-D-Rollenmodell

*   **A (Alpha / Legislative):** Definiert den Zustand (Z) und die Regeln. Setzt die Invarianten.
*   **B (Bravo / Exekutive):** Führt die Transformationen (T) aus. Bewegt die Daten.
*   **C (Charlie / Judikative):** Bewertet die Informationen (I) und trifft Entscheidungen. Prüft Risiken.
*   **D (Delta / Übergeordneter Zustand):** Träger aller Zyklen. Stellt Konsistenz und Integrität sicher.

## Der ZTI-Kreislauf mit A-B-C-D

1.  **C (I):** Informationen sammeln und bewerten.
2.  **A (Z):** Zustand definieren und Regeln setzen.
3.  **B (T):** Transformationen ausführen.
4.  **D:** Konsistenz und Integrität prüfen (DEF, WORM, SHADOW).
5.  **zurück zu C (I):** Der Zyklus beginnt von neuem.

## Gates: DEF, WORM, SHADOW

*   **DEF (A):** Regeln und Invarianten definieren.
*   **WORM (D):** Write Once, Read Many - Änderungen protokollieren und nachweisbar machen.
*   **SHADOW (C):** Risiken erkennen und bewerten.

## Die praktische Umsetzung: Der ΔZ-BLOCK

Jede Zustandsänderung muss als `ΔZ-BLOCK` formuliert werden. Dies ist kein separates Modul, sondern ein obligatorischer Datenblock, der jede Transaktion begleitet.

> **Template:** Ein leeres `ΔZ-BLOCK` Template befindet sich in `/home/ubuntu/skills/zti-delta-algorithm/templates/delta_block_template.yaml`.

## Workflow bei jeder Zustandsänderung

1.  **Impuls empfangen:** Ein Ereignis tritt ein (z.B. neue Benutzeranfrage, Dateisystemänderung).

2.  **Inferenz durchführen:** Das System analysiert den Impuls und bestimmt die notwendigen Änderungen.

3.  **ΔZ-BLOCK ausfüllen:**
    *   **Aktion:** Füllen Sie das `delta_block_template.yaml` mit den Ergebnissen der Inferenz aus.

4.  **Validierung durchführen:**
    *   **Aktion:** Führen Sie das Skript `validate_delta.py` aus. Dieses Skript prüft die Invarianten und setzt das `RISK_FLAG`.
    *   **Skript:** `/home/ubuntu/skills/zti-delta-algorithm/scripts/validate_delta.py`

5.  **Integration (oder Abbruch):**
    *   **Wenn** `INVARIANTS_CHECK` auf `PASS` und `SHADOW_REQUIRED` auf `NO` steht, wird die Änderung integriert.
    *   **Wenn** `SHADOW_REQUIRED` auf `YES` steht, wird eine manuelle Bestätigung oder eine zweite KI-Instanz zur Prüfung angefordert.
    *   **Wenn** `INVARIANTS_CHECK` auf `FAIL` steht, wird der Prozess abgebrochen und ein Fehler protokolliert.

## Verwendung des Skills

Dieser Skill ist fundamental. Er sollte als **META-SKILL** betrachtet werden, der die Ausführung *aller anderen* Skills und Aktionen steuert. Jede Operation, die den Systemzustand ändert, muss diesen ZTI+ΔZ Zyklus durchlaufen.
