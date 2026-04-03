# P11 Synergos: Das Co-Adaptive System v1.0 (State-Vector)

**Status:** Aktiviert | **System:** Synergos | **Methode:** Curie (Extraktion) + Feynman (Einfachheit) + Allen (GTD-Flow)

Dieses Dokument ist das "externe Gehirn" – die Automations-Spur deines Projekts. Während P10 (die RTE) der Automations-Controller ist, der bei jeder Anfrage die Regler dreht, ist der State-Vector das Speichermedium. Er zeichnet jeden Regler-Stand auf, damit du beim nächsten Öffnen des Projekts genau weißt, wo du warst, was funktioniert hat und was als nächstes kommt. Er löst das größte Problem von KI-Sessions: den verlorenen Kontext nach dem Schließen der DAW.

> **Das Automations-Spur-Prinzip:** In FL Studio malst du eine Automations-Kurve für den Filter-Cutoff. Wenn du das Projekt speicherst und morgen wieder öffnest, ist die Kurve noch da. Der State-Vector ist genau das für Synergos. Jede Entscheidung, jedes Artefakt, jede Lücke wird protokolliert. Jede neue Interaktion liest diese Spur aus und baut darauf auf. Ohne diese Spur startest du jedes Mal bei Null – als ob du die DAW öffnest und alle Regler auf Default stehen.

---

## TEIL 1: DAS CO-ADAPTIVE SYSTEM ALS SYSTEM-PROMPT

Kopiere den folgenden Block und integriere ihn in deine Synergos-Architektur (als Erweiterung der RTE aus P10). Der P5-Kern-Prompt bleibt das Fundament, die RTE bleibt der Controller – und dieser Block aktiviert die Automations-Spur, die alles aufzeichnet.

```markdown
::STATE_VECTOR_START::

[1. UR-ZIELTRIGGER (Die Dual-Output-Regel)]
Ab sofort erzeugt JEDE Interaktion zwingend ZWEI synchronisierte Outputs:
a) Das angeforderte System-Artefakt (wie in P10/RTE definiert, mit 4 Blöcken A-D).
b) Den aktualisierten State-Vector (als Kopiervorlage in Markdown oder JSON).
Der Bounce ist erst fertig, wenn BEIDE Outputs gerendert sind. Ein Artefakt ohne
Vector-Update ist wie ein Track ohne gespeicherte Automation – beim nächsten Öffnen
stehen alle Regler wieder auf Null.

[2. STATE-VECTOR STRUKTUR (Was wird auf der Spur protokolliert?)]
Der State-Vector ist das externe Gedächtnis. Er muss diese 5 Frequenzbänder aufzeichnen:

BAND 1 – Generiertes Artefakt:
  Name, Typ, Artefakt-ID (Schema: PXXX-SYY-ZZZ), Integrationsort (Dateipfad oder MCP-Ziel).

BAND 2 – Angewandte Prinzipien:
  Welche Axiome (A1-A6 aus P2) wurden aktiviert? Welche Genie-Logiken (Curie/Feynman/Allen)
  haben das Signal verarbeitet? Welche Regeln (R1-R5) wurden angewendet?

BAND 3 – Entdeckte Lücken/Konflikte:
  Wo clippt der Mix? Offene Einträge mit Priorität (1 = sofort, 2 = nächste Session,
  3 = Backlog). Jede Lücke bekommt einen Lösungsvorschlag.

BAND 4 – Abgeleitete Regelverbesserung:
  Hat der Durchlauf eine neue Regel offenbart? Eine bestehende Regel verbessert?
  Ein neues Preset vorgeschlagen? Hier werden Regel-Versionen und Checklisten-Updates
  protokolliert.

BAND 5 – Ressourcenbilanz:
  Geschätzte Token-Kosten des Durchlaufs, Komplexitätsstufe (Niedrig/Mittel/Hoch),
  identifizierte Flaschenhälse (z.B. Token-Limit, MCP-Timeout, manuelle Schritte).

[3. CO-ADAPTIVER PROZESS (Die 4-Schritt-Schleife)]
Jede Session durchläuft diese Schleife – ohne Ausnahme:

SCHRITT 1 – VORLAUF (Automation laden):
  Das System liest den aktuellen State-Vector ein. Offene Lücken mit Priorität 1 werden
  ZUERST abgearbeitet, bevor neue Spuren angelegt werden. Wenn der Vector leer ist
  (erste Session), wird ein initialer Nullpunkt-Scan (A1) durchgeführt.

SCHRITT 2 – VERARBEITUNG (Mixen):
  Die Anfrage läuft durch die RTE (P10) und die 12-Stufen-Pipeline (P6). Bei JEDER
  Entscheidung wird der Vector konsultiert:
  - "Widerspricht dies einer früheren Regel im Changelog?"
  - "Gibt es eine offene Lücke, die diese Anfrage betrifft?"
  - "Wurde ein ähnliches Artefakt bereits generiert (Duplikat-Check)?"
  Wenn ein Konflikt erkannt wird: STOPP. Konflikt benennen, Auflösung vorschlagen.

SCHRITT 3 – OUTPUT (Bouncen):
  Zwei Outputs werden synchron generiert:
  (A) Das fertige Artefakt im RTE-Format (Konfigurationsblock, Integrationsanweisung,
      Abhängigkeiten, Selbsttest).
  (B) Der aktualisierte State-Vector als Copy-Paste-Block. Alle 5 Bänder werden
      aktualisiert. Neue Einträge werden mit [NEU] markiert.

SCHRITT 4 – INTEGRATION (Speichern):
  Der Nutzer kopiert den aktualisierten Vector in seine zentrale Steuerdatei
  (`/home/ubuntu/synergos_state.md` oder `.json`). Dieser Schritt ist manuell –
  das ist die bewusste Design-Entscheidung: Der Producer behält die Kontrolle über
  sein Projekt-File. Kein automatisches Überschreiben.

[4. GRENZEN & SKALIERBARKEIT (Der Headroom)]
GRENZE 1: Manuelle Pflege.
  Der Nutzer muss den Vector nach jeder Session kopieren. Das kostet 30 Sekunden.
  UMGEHUNG: Der Vector ist so formatiert, dass er als einzelner Block kopierbar ist.
  Kein Zusammensuchen aus mehreren Stellen. Ein Block, ein Copy-Paste.

GRENZE 2: Wachsende Größe.
  Nach 50 Artefakten wird der Vector lang. Das frisst Token beim Einlesen.
  UMGEHUNG: Archivierung. Abgeschlossene Sektoren werden in separate Archiv-Dateien
  ausgelagert (`synergos_archive_s1.md`). Der aktive Vector enthält nur den aktuellen
  Sektor plus die Lücken-Liste.

GRENZE 3: Kein automatischer Sync.
  Der Vector liegt als Datei, nicht in einer Datenbank.
  UMGEHUNG: Migrations-Pfad. Sobald die Architektur steht (P14+), kann der Vector
  in Supabase oder Notion migriert werden. Das JSON-Format ist dafür vorbereitet.

[5. ERFOLGSKRITERIUM (Der Phasen-Check)]
Das System ist erfolgreich co-adaptiv, wenn:
- JEDE neue Interaktion nachweisbar auf der vorherigen aufbaut (Vector-Referenz).
- KEINE Information zwischen Sessions verloren geht (Automations-Spur ist vollständig).
- Offene Lücken systematisch abgebaut werden (Clipping-Liste schrumpft).
- Das Regelwerk sich organisch verbessert (Changelog wächst).

::STATE_VECTOR_ENDE::
```

---

## TEIL 2: STATE-VECTOR VORLAGE

Hier sind die Copy-Paste-fertigen Vorlagen für das externe Gehirn. Wähle das Format, das am besten zu deinem aktuellen Setup passt. Markdown ist für den Start empfohlen (menschenlesbar, direkt in jeder Session nutzbar). JSON ist für die spätere Automatisierung vorbereitet (Skript-Integration, Datenbank-Migration).

---

### Option A: Markdown-Format (Empfohlen für den Start)

```markdown
# SYNERGOS STATE-VECTOR (Automations-Spur)

**Projekt-ID:** SYN-CORE-01
**Version:** [X.Y]
**Letzte Aktualisierung:** [YYYY-MM-DD]
**Gesamtstatus:** [Aktiv / Pausiert / Blockiert]
**Aktiver Sektor:** [Sektor X, Prompt PYY]

---

## 1. ARTEFAKT-REGISTER (Die Playlist)
| Nr. | ID | Artefakt-Name | Typ | Sektor | Status | Integrationsort |
| :---: | :--- | :--- | :--- | :---: | :--- | :--- |
| 1 | P001 | [Name] | [Typ] | S1 | [Status] | `[Dateipfad]` |
| 2 | P002 | [Name] | [Typ] | S1 | [Status] | `[Dateipfad]` |

## 2. OFFENE LÜCKEN (Die Clipping-Liste)
| Prio | ID | Beschreibung (Was clippt?) | Lösungsvorschlag (EQ) | Betrifft | Status |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | L001 | [Beschreibung] | [Vorschlag] | [Artefakt/Stufe] | [Offen/In Arbeit] |

## 3. REGEL-CHANGELOG (Die Mixer-Historie)
| Version | Änderung / Neues Preset | Auslöser (Warum?) | Betroffene Axiome | Datum |
| :--- | :--- | :--- | :--- | :--- |
| v1.0 | [Beschreibung] | [Trigger] | [A1-A6, R1-R5] | [YYYY-MM-DD] |

## 4. RESSOURCENBILANZ (Gain-Staging)
| Metrik | Wert |
| :--- | :--- |
| Letzter Artefakt-Token-Verbrauch | ~[X]k Token |
| Gesamtkomplexität | [Niedrig / Mittel / Hoch] |
| Flaschenhals | [Beschreibung] |
| Aktive Spuren (von 23) | [X] / 23 |

## 5. NÄCHSTE SCHRITTE (Das nächste Plugin)
1. **[Prio 1]:** [Aufgabe] – Quelle: [Lücke LXX / Nächster Prompt]
2. **[Prio 2]:** [Aufgabe]
3. **[Prio 3]:** [Aufgabe]
```

---

### Option B: JSON-Format (Für spätere Skript-Integration)

```json
{
  "header": {
    "project_id": "SYN-CORE-01",
    "version": "1.0",
    "last_updated": "YYYY-MM-DD",
    "overall_status": "Aktiv",
    "active_sector": "Sektor 3",
    "active_prompt": "P11"
  },
  "artifact_registry": [
    {
      "nr": 1,
      "id": "P001",
      "name": "Modellauskunft",
      "type": "System-Scan",
      "sector": "S1",
      "status": "Abgeschlossen",
      "integration_path": "p1_modellauskunft.md",
      "applied_principles": ["A1"],
      "genie_logic": "Feynman"
    }
  ],
  "open_gaps": [
    {
      "priority": 1,
      "id": "L001",
      "description": "Kein automatischer Profil-Loader",
      "proposed_solution": "Nullpunkt-Scan als JSON-Config bauen",
      "affects": "Stufe 2 (Pipeline P6)",
      "status": "Offen"
    }
  ],
  "rule_changelog": [
    {
      "version": "v1.0",
      "change": "Initiales Setup P1-P10",
      "trigger": "Grundarchitektur gebaut",
      "affected_axioms": ["A1", "A2", "A3", "A4", "A5", "A6"],
      "date": "2026-03-22"
    }
  ],
  "resource_balance": {
    "last_artifact_tokens": 0,
    "total_complexity": "Mittel",
    "bottleneck": "Manuelles Copy-Paste des Vectors",
    "active_tracks": 11,
    "total_tracks": 23
  },
  "next_steps": [
    {
      "priority": 1,
      "task": "P12: IDENTIFY & PURGE Pipeline bauen",
      "source": "Nächster Prompt"
    }
  ]
}
```

---

## TEIL 3: LIVE-DEMONSTRATION (Der vollständige State-Vector für P1-P11)

Hier wird das Protokoll demonstriert. Zuerst der vollständige State-Vector-Eintrag für P10 (Resonanz-Engine), dann das komplette Projekt-Log aller Artefakte P1-P11.

---

### 3.1 State-Vector-Eintrag für P10 (Resonanz-Engine)

**BAND 1 – Generiertes Artefakt:**

| Feld | Wert |
| :--- | :--- |
| Name | Resonanz-Engine (RTE) |
| Typ | System-Prompt + Live-Demo |
| Artefakt-ID | P010-S12-001 |
| Integrationsort | `p10_synergos_rte.md` – als Wrapper um den P5-Kern-Prompt |
| Beschreibung | Automations-Controller, der bei JEDER Anfrage die 12-Stufen-Pipeline (P6), die Dreischichten-Validierung (P7), das Pattern-Hunting (P8) und den Lehrmeister-Modus (P9) automatisch aktiviert und steuert. |

**BAND 2 – Angewandte Prinzipien:**

| Prinzip | Anwendung in P10 |
| :--- | :--- |
| A1 (Nullpunkt-Kalibrierung) | Schritt 1 der RTE lädt zwingend das Nutzerprofil (23J, Solo, FL Studio, Lagerlogistik). Kein Durchlauf ohne Nullpunkt. |
| A2 (Signal-Routing) | Schritt 2 routet jede Anfrage durch die 12-Stufen-Pipeline. Das Routing-Ziel wird in Stufe 5 automatisch bestimmt. |
| A3 (Architektur-Zwang) | Stufe 6 der Pipeline erzwingt den Bauplan VOR der Ausführung. Kein Bounce ohne Go. |
| A4 (Format-Schablone) | Schritt 3 presst jeden Output in das 4-Block-Format (A: Konfiguration, B: Integration, C: Abhängigkeiten, D: Selbsttest). |
| A5 (Frequenz-Hierarchie) | Stufe 7 lädt Master-Regeln vor Task-Regeln. Die RTE selbst steht über allen Task-Prompts. |
| R1 (Echo-Prinzip) | Die RTE spiegelt die Struktur des Inputs im Output (strukturierte Anfrage = strukturiertes Artefakt). |
| R3 (Hierarchie-Resonanz) | Die Detailtiefe des Artefakts passt sich proportional zur Komplexität der Anfrage an. |
| Genie-Logik | Curie (Extraktion der Systemkomponenten) + Allen (GTD-Organisation des Durchlaufs) + Feynman (Erklärung im Transparenz-Protokoll). Hybrid-Modus. |

**BAND 3 – Entdeckte Lücken/Konflikte:**

| Prio | ID | Lücke | Lösungsvorschlag | Status |
| :---: | :--- | :--- | :--- | :--- |
| 1 | L001 | Kein automatischer Profil-Loader implementiert. Das Nutzerprofil ist hardcodiert im RTE-Prompt. Wenn sich der Nutzer weiterentwickelt (z.B. Ausbildung abgeschlossen), muss der Prompt manuell editiert werden. | Nutzerprofil in eine externe JSON-Config (`user_profile.json`) auslagern. Die RTE liest diese Config in Schritt 1 ein. | Offen |
| 2 | L002 | Kein persistenter Kontext zwischen Sessions. Die RTE vergisst nach Session-Ende alles. Offene Lücken, laufende Pläne, Fortschritt – alles weg. | State-Vector-System einführen (wird in P11 gelöst). | Gelöst (P11) |
| 2 | L003 | MCP-Server-Verfügbarkeit nicht vorab geprüft. Wenn ein MCP-Server in Stufe 5 (Routing) nicht erreichbar ist, bricht der Durchlauf erst in Stufe 12 (Export) ab. | Ping-Test aller Ziel-MCP-Server in Schritt 1 (Initialisierung) einbauen. Nicht erreichbare Server sofort auf Fallback setzen. | Offen |
| 3 | L004 | Genie-Logik-Trigger-Wörter sind nicht als formale Regel definiert. Die Wörter (sortieren, extrahieren, erklären, planen...) stehen nur im RTE-Prompt, nicht im Regelwerk (P2/P5). | Trigger-Wörter als formale Regel R6 vorschlagen und in den Regel-Changelog aufnehmen. | Offen |
| 3 | L005 | P9-Lehrmeister-Aktivierung basiert auf Heuristik, nicht auf messbaren Kriterien. Die Trigger-Tabelle (Reine Ausführung = Bypass, Neues Modul = Aktiv) ist subjektiv. | Messbare Schwellenwerte definieren: z.B. "Wenn das Artefakt mehr als 3 neue Konzepte einführt, wird P9 aktiviert." | Offen |

**BAND 4 – Abgeleitete Regelverbesserung:**

| Vorschlag | Beschreibung | Auslöser | Status |
| :--- | :--- | :--- | :--- |
| R6 (Genie-Logik-Trigger) | Formalisierung der Trigger-Wörter als harte Regel: Curie-Wörter (sortieren, extrahieren, analysieren, kategorisieren, filtern), Feynman-Wörter (erklären, verstehen, warum, Struktur, Bauplan), Allen-Wörter (planen, organisieren, erstellen, umsetzen, Deadline). | Lücke L004 – Trigger-Wörter sind informell. | Vorgeschlagen |
| Checklisten-Update P7 | Schicht 3 (Integrationsfähigkeit) um den Punkt "State-Vector-Kompatibilität" erweitern: "Ist das Artefakt im State-Vector protokollierbar?" | P11 führt den State-Vector ein – die Validierung muss das berücksichtigen. | Vorgeschlagen |
| Archivierungs-Regel | Wenn ein Sektor vollständig abgeschlossen ist, werden seine Artefakte in eine Archiv-Datei verschoben. Der aktive Vector enthält nur den aktuellen Sektor. | Grenze 2 des State-Vectors (wachsende Größe). | Vorgeschlagen |

**BAND 5 – Ressourcenbilanz:**

| Metrik | Wert |
| :--- | :--- |
| Geschätzte Token für RTE-Prompt | ~1.800 Token (der `::RTE_START::` bis `::RTE_ENDE::` Block) |
| Geschätzte Token für einen vollen RTE-Durchlauf | ~4.500–6.500 Token (abhängig von Artefakt-Komplexität) |
| Token-Budget pro Session (bei 8k Limit) | ~1.500 Token verbleiben für Nutzer-Input nach RTE-Prompt + P5-Kern-Prompt |
| Komplexitätsstufe | Hoch – Die RTE ist das komplexeste Einzelartefakt im System |
| Flaschenhals | Token-Budget. Der RTE-Prompt + P5-Kern-Prompt belegen zusammen ~3.500 Token. Bei 8k RAM bleiben ~4.500 für Input + Output. Bei Gemini (1M Token) ist das kein Problem. |

---

### 3.2 Vollständiger State-Vector (P1-P11) – Copy-Paste-fertig

Kopiere diesen Block in deine zentrale `synergos_state.md`. Das ist ab jetzt dein Ausgangspunkt für jede neue Session.

```markdown
# SYNERGOS STATE-VECTOR (Automations-Spur)

**Projekt-ID:** SYN-CORE-01
**Version:** 1.0
**Letzte Aktualisierung:** 2026-03-22
**Gesamtstatus:** Aktiv
**Aktiver Sektor:** Sektor 3, Prompt P11

---

## 1. ARTEFAKT-REGISTER (Die Playlist)
| Nr. | ID | Artefakt-Name | Typ | Sektor | Status | Integrationsort |
| :---: | :--- | :--- | :--- | :---: | :--- | :--- |
| 1 | P001 | Modellauskunft (DAW-Scan) | System-Scan | S1 | Abgeschlossen | `p1_modellauskunft.md` |
| 2 | P002 | Die 6 Design-Axiome (Mixer-Regler) | Regelwerk | S1 | Abgeschlossen | `p2_synergos_axiome.md` |
| 3 | P003 | Strukturtransfer (5 Regeln) | Analyse | S1 | Abgeschlossen | `p3_strukturtransfer.md` |
| 4 | P004 | Referenz-Prompt (5-Elemente-Template) | Template | S1 | Abgeschlossen | `p4_referenz_prompt.md` |
| 5 | P005 | Der Kern-Prompt (Master-Export S1) | System-Prompt | S1 | Abgeschlossen | `p5_synergos_kernprompt.md` |
| 6 | P006 | 12-Stufen-Pipeline (Signalkette) | Workflow | S2 | Abgeschlossen | `p6_synergos_pipeline.md` |
| 7 | P007 | Validierungsprotokoll (Mastering) | Regelwerk | S2 | Abgeschlossen | `p7_synergos_validierung.md` |
| 8 | P008 | Pattern-Hunting (Sample-Library) | Modul | S2 | Abgeschlossen | `p8_pattern_hunting.md` |
| 9 | P009 | Lehrmeister-Didaktik (Tutorial-Preset) | Modul | S2 | Abgeschlossen | `p9_lehrmeister.md` |
| 10 | P010 | Resonanz-Engine RTE (Automations-Controller) | System-Prompt + Demo | S3 | Abgeschlossen | `p10_synergos_rte.md` |
| 11 | P011 | Co-Adaptives System (State-Vector) | State-Vector + Demo | S3 | Abgeschlossen | `p11_synergos_statevector.md` |

## 2. OFFENE LÜCKEN (Die Clipping-Liste)
| Prio | ID | Beschreibung (Was clippt?) | Lösungsvorschlag (EQ) | Betrifft | Status |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | L001 | Kein automatischer Profil-Loader. Nutzerprofil ist hardcodiert. | Externe `user_profile.json` Config bauen. | P10 RTE, Stufe 2 | Offen |
| 1 | L003 | MCP-Server-Verfügbarkeit wird nicht vorab geprüft. | Ping-Test in RTE Schritt 1 einbauen. | P10 RTE, Stufe 5/12 | Offen |
| 2 | L006 | Chaos-Dateien sind nicht indexiert. Millionen Dateien ohne Zuordnung. | Knowledge-Index-Scan real bauen (P12+). | Gesamtsystem | Offen |
| 2 | L007 | 4 Kern-Pipelines (IDENTIFY, CONVERT, ORGANIZE, VERIFY) fehlen noch. | P12-P15 definieren und bauen. | Sektor 4 | Offen |
| 3 | L004 | Genie-Logik-Trigger-Wörter nicht als formale Regel definiert. | Als R6 in Regelwerk aufnehmen. | P2 Axiome, P10 RTE | Offen |
| 3 | L005 | P9-Lehrmeister-Aktivierung basiert auf Heuristik, nicht auf Messwerten. | Messbare Schwellenwerte definieren. | P9, P10 RTE | Offen |

## 3. REGEL-CHANGELOG (Die Mixer-Historie)
| Version | Änderung / Neues Preset | Auslöser (Warum?) | Betroffene Axiome | Datum |
| :--- | :--- | :--- | :--- | :--- |
| v0.1 | P1: DAW gescannt. Modell, RAM, Plugins identifiziert. | Grundlagen-Erfassung. | – | 2026-03-22 |
| v0.2 | P2: 6 Axiome (A1-A6) aus 8 Problemen destilliert. | 8 matschige Probleme brauchten harte Regler. | A1-A6 | 2026-03-22 |
| v0.3 | P3: 5 Verarbeitungsregeln (R1-R5) definiert. | Output-Symmetrie erzwingen. | R1-R5 | 2026-03-22 |
| v0.4 | P4: 5-Elemente-Template standardisiert. | Einheitliches Ausgabeformat nötig. | A4 | 2026-03-22 |
| v0.5 | P5: Kern-Prompt exportiert. Master-Export Sektor 1. | Konsolidierung P1-P4 in einen Prompt. | A1-A6, R1-R5 | 2026-03-22 |
| v0.6 | P6: 12-Stufen-Pipeline gebaut. Signalkette steht. | Verarbeitungsweg von Rohsignal bis Export. | A1-A5, R2-R3 | 2026-03-22 |
| v0.7 | P7: Dreischichten-Validierung + Metadaten-Header. | Kein Output ohne Mastering. | A1-A6 | 2026-03-22 |
| v0.8 | P8: Pattern-Hunting. 8 Master-Presets erkannt. | Wiederkehrende Muster als Presets speichern. | A6 | 2026-03-22 |
| v0.9 | P9: Lehrmeister-Modus mit Demo-Reflect-Invite. | Didaktik für Selbstwartung des Systems. | A3, A6 | 2026-03-22 |
| v0.95 | P10: RTE als Automations-Controller. Wrapper um P5. | Manuelle Axiom-Aktivierung eliminieren. | A1-A6, R1-R5 | 2026-03-22 |
| v1.0 | P11: State-Vector eingeführt. Externes Gedächtnis. | Kontext-Verlust zwischen Sessions lösen. | – (neues Modul) | 2026-03-22 |

## 4. RESSOURCENBILANZ (Gain-Staging)
| Metrik | Wert |
| :--- | :--- |
| Letzter Artefakt-Token-Verbrauch | ~5.000 Token (P11 State-Vector-Prompt) |
| Gesamtkomplexität | Hoch (23-Spur-Architektur, 11 Spuren belegt) |
| Flaschenhals | Token-Budget bei gpt-4.1-mini (8k). P5 + RTE + State-Vector = ~5.300 Token Overhead. |
| Aktive Spuren | 11 / 23 |
| Empfehlung | Für komplexe Durchläufe auf Gemini (1M Token) wechseln. Für Routine-Tasks reicht gpt-4.1-mini mit komprimiertem Vector. |

## 5. NÄCHSTE SCHRITTE (Das nächste Plugin)
1. **[Prio 1]:** P12 – IDENTIFY & PURGE Pipeline für die Chaos-Dateien bauen. Quelle: Lücke L006/L007.
2. **[Prio 1]:** L001 lösen – Nutzerprofil in externe JSON-Config auslagern.
3. **[Prio 2]:** P13 – CONVERT & STANDARDIZE Pipeline aufsetzen.
4. **[Prio 2]:** L003 lösen – MCP-Server Ping-Test in RTE Schritt 1 einbauen.
5. **[Prio 3]:** P14 – ORGANIZE (Supabase/Notion Routing) definieren.
6. **[Prio 3]:** R6 (Genie-Logik-Trigger) formal ins Regelwerk aufnehmen.
```

---

## TEIL 4: INTEGRATION IN DIE ARCHITEKTUR

Wie greift der State-Vector in die bestehende Synergos-Architektur ein? Er ist der Speicherchip der Resonanz-Engine – das Bauteil, das der RTE gefehlt hat.

Die RTE (P10) ist der Automations-Controller, der bei jeder Anfrage die Regler dreht. Aber sie hat Amnesie – wenn die DAW zugeht, vergisst sie alles. Der State-Vector ist die Automations-Spur, die auf der Festplatte liegt. Wenn die DAW morgen aufgeht, liest die RTE zuerst diese Spur, bevor sie anfängt zu mischen. Das ist David Allens Kernprinzip in Aktion: "Dein Kopf ist zum Haben von Ideen da, nicht zum Festhalten." Der Vector hält fest, damit die RTE denken kann.

---

### 4.1 Die Schichtenarchitektur nach P11

Mit P11 hat das System drei klar getrennte Schichten, die zusammen das vollständige Betriebssystem bilden:

| Schicht | Komponente | Funktion | FL-Studio-Pendant | Änderungsfrequenz |
| :---: | :--- | :--- | :--- | :--- |
| 1 (Kern) | **P5 Kern-Prompt** | Identität, Axiome (A1-A6), Regeln (R1-R5), Qualitäts-Gate | Die DAW-Konfiguration (Template) | Selten – nur bei Regelwerk-Updates |
| 2 (Controller) | **P10 RTE** | Automatisches Routing, Pipeline-Steuerung, Artefakt-Generierung | Der Automations-Controller | Nie – läuft bei jeder Anfrage identisch |
| 3 (Gedächtnis) | **P11 State-Vector** | Projekt-Log, Lücken-Tracking, Regel-Evolution, Ressourcen-Monitoring | Die Automations-Spur auf der Festplatte | Bei jeder Session – wächst organisch |

Der P5 definiert **was** das System ist. Die RTE definiert **wie** das System auf jede Anfrage reagiert. Der State-Vector dokumentiert **was passiert ist** und **was als nächstes kommt**. Zusammen bilden sie das vollständige Betriebssystem mit Gedächtnis.

---

### 4.2 Der Signalfluss: RTE + State-Vector (ASCII-Diagramm)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   NUTZER-ANFRAGE (Neues Projekt / Session Start)                            │
│   "Lass uns P12 bauen."                                                     │
│       │                                                                     │
│       ▼                                                                     │
│  ┌──────────────────────────────────────────────────────────────────────┐    │
│  │                RTE (Automations-Controller / P10)                    │    │
│  │                                                                      │    │
│  │  SCHRITT 1 – VORLAUF (Automation laden)                              │    │
│  │  ┌────────────────────────────────────────────────────────────┐      │    │
│  │  │  State-Vector einlesen ◄── `/home/ubuntu/synergos_state.md`│      │    │
│  │  │                                                            │      │    │
│  │  │  Ergebnis:                                                 │      │    │
│  │  │  - P1-P11 abgeschlossen (11/23 Spuren belegt)             │      │    │
│  │  │  - Offene Lücke L001 (Prio 1): Profil-Loader fehlt        │      │    │
│  │  │  - Offene Lücke L003 (Prio 1): MCP-Ping fehlt             │      │    │
│  │  │  - Nächster Schritt: P12 (IDENTIFY & PURGE)                │      │    │
│  │  └────────────────────────────────────────────────────────────┘      │    │
│  │       │                                                              │    │
│  │       ▼                                                              │    │
│  │  SCHRITT 2 – VERARBEITUNG (Mixen)                                    │    │
│  │  ┌────────────────────────────────────────────────────────────┐      │    │
│  │  │  Pipeline P6 (12 Stufen) + Validierung P7                  │      │    │
│  │  │                                                            │      │    │
│  │  │  Bei JEDER Entscheidung:                                   │      │    │
│  │  │  Vector konsultieren ──► "Widerspricht dies einer          │      │    │
│  │  │                           früheren Regel im Changelog?"    │      │    │
│  │  │                                                            │      │    │
│  │  │  Duplikat-Check ──► "Existiert ein ähnliches Artefakt      │      │    │
│  │  │                      bereits im Register?"                 │      │    │
│  │  └────────────────────────────────────────────────────────────┘      │    │
│  │       │                                                              │    │
│  │       ▼                                                              │    │
│  │  SCHRITT 3 – OUTPUT BOUNCEN (Dual-Output)                            │    │
│  │  ┌─────────────────────┐    ┌─────────────────────────────────┐      │    │
│  │  │ [A] ARTEFAKT        │    │ [B] AKTUALISIERTER VECTOR       │      │    │
│  │  │ (z.B. P12 Pipeline) │    │ (Copy-Paste-Block)              │      │    │
│  │  │                     │    │                                 │      │    │
│  │  │ - Konfiguration     │    │ - Neues Artefakt P012 im       │      │    │
│  │  │ - Integration       │    │   Register eingetragen          │      │    │
│  │  │ - Abhängigkeiten    │    │ - Lücken aktualisiert           │      │    │
│  │  │ - Selbsttest        │    │ - Changelog erweitert           │      │    │
│  │  └────────┬────────────┘    └──────────────┬──────────────────┘      │    │
│  └───────────┼────────────────────────────────┼──────────────────────────┘    │
│              │                                │                               │
│              ▼                                ▼                               │
│    Integrieren in System              Kopieren in `synergos_state.md`         │
│    (Datei speichern /                 (Manuell durch den Producer)            │
│     MCP-Call ausführen)                       │                               │
│                                               │                               │
│                                               ▼                               │
│                                  ┌────────────────────────┐                   │
│                                  │   EXTERNES GEHIRN      │                   │
│                                  │   (synergos_state.md)  │                   │
│                                  │                        │                   │
│                                  │   Persistiert zwischen  │                   │
│                                  │   Sessions. Wird beim   │                   │
│                                  │   nächsten Start in     │                   │
│                                  │   Schritt 1 geladen.    │                   │
│                                  └────────────┬───────────┘                   │
│                                               │                               │
│                                               └───────► Nächste Session       │
│                                                         (Schritt 1: Vorlauf)  │
└───────────────────────────────────────────────────────────────────────────────┘
```

---

### 4.3 Die 23-Spur-Architektur nach P11

Mit P11 sind 11 von 23 Spuren in der Playlist-Anordnung verdrahtet. Hier ist der aktuelle Stand:

| Sektor | Prompt | Baustein | Schicht | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Sektor 1** | P1 | Modellauskunft (DAW-Scan) | Kern | Abgeschlossen |
| | P2 | Design-Axiome (6 Mixer-Regler) | Kern | Abgeschlossen |
| | P3 | Strukturtransfer (5 Regeln) | Kern | Abgeschlossen |
| | P4 | Referenz-Prompt (5-Elemente-Template) | Kern | Abgeschlossen |
| | P5 | Kern-Prompt (Master-Export Sektor 1) | Kern | Abgeschlossen |
| **Sektor 2** | P6 | 12-Stufen-Pipeline (Signalkette) | Controller | Abgeschlossen |
| | P7 | Validierungsprotokoll (Mastering) | Controller | Abgeschlossen |
| | P8 | Pattern-Extraktion (Sample-Hunting) | Controller | Abgeschlossen |
| | P9 | Lehrmeister-Modus (Tutorial-Preset) | Controller | Abgeschlossen |
| **Sektor 3** | P10 | Resonanz-Engine (Automations-Controller) | Controller | Abgeschlossen |
| | **P11** | **Co-Adaptives System (State-Vector)** | **Gedächtnis** | **Abgeschlossen** |
| **Sektor 4** | P12 | IDENTIFY & PURGE Pipeline | Praxis | Offen |
| | P13 | CONVERT & STANDARDIZE Pipeline | Praxis | Offen |
| | P14 | ORGANIZE (Routing & Ablage) | Praxis | Offen |
| | P15 | VERIFY (Qualitätssicherung) | Praxis | Offen |
| **Sektor 5** | P16-P23 | Noch zu definieren | – | Offen |

> **Fazit:** Mit P11 haben wir das Amnesie-Problem gelöst. Der Producer muss nicht mehr jedes Mal den gesamten Kontext neu erklären. Der State-Vector ist das Gedächtnis, das zwischen Sessions persistiert – wie die Automations-Spur auf der Festplatte. Wenn du morgen "Lass uns P12 machen" schreibst, liest das System den Vector, sieht dass P1-P11 fertig sind, sieht die 6 offenen Lücken mit Prioritäten, kennt die 11 Changelog-Einträge und baut exakt auf diesem Fundament auf. Keine Lücken in der Murmelbahn. Kein Regler auf Null.

---

**UOP-Gate (Master-Export):**
P11 ist abgeschlossen. Das Co-Adaptive System v1.0 steht. Teil 1 liefert den Copy-Paste-fertigen System-Prompt. Teil 2 liefert die Vorlagen (Markdown + JSON). Teil 3 demonstriert den vollständigen State-Vector-Eintrag für P10 und das komplette Projekt-Log P1-P11. Teil 4 zeigt die Integration in die Architektur mit Signalfluss-Diagramm und Schichtenmodell. Warte auf Bestätigung oder Korrekturen.
