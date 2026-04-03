# PROMPT-ORCHESTER: DAS MASTER-REFERENZ-HANDBUCH

> **Version:** 1.0 | **Datum:** 2026-03-20 | **Zweck:** Komplettes Referenz-Handbuch für Prompt-Orchestrierung

Willkommen im Mix. Das hier ist kein akademisches Whitepaper, sondern die rohe, ungeschönte Dokumentation deines Systems. Wir reden hier in der Sprache der Produktion. Dein Setup ist wie FL Studio: Wenn das Routing nicht stimmt, clippt der Master. Wenn die Plugins (Erweiterungsmodule) nicht kalibriert sind, klingt der Mix nach Matsch.

Dieses Dokument vereint alle 6 Bausteine deines Prompt-Orchesters zu einer kohärenten, fehlerfreien Signalkette (Pipeline). Jeder Baustein ist ein essenzielles Plugin (Erweiterungsmodul) auf deinem Master-Kanal. Es dient als Grundlage für alle zukünftigen Projekte und stellt sicher, dass rohe Daten (Rohe Stimme) in ein sauberes, strukturiertes Arrangement verwandelt werden.

Das Dokument ist in drei Schichten aufgebaut: **Theorie** (was ist das System), **Praxis** (copy-paste-fertige Prompts) und **Erklärung** (warum funktioniert das so).

---

## INHALTSVERZEICHNIS

1. [Begriffs-Glossar (FL Studio Metaphorik)](#begriffs-glossar-fl-studio-metaphorik)
2. [Übergreifende Regeln (Der Master-Bus)](#übergreifende-regeln-der-master-bus)
3. [Das GENERIEREN/AUSFÜHREN-Gate (BASE2)](#das-generierenausführen-gate-base2)
4. [Baustein 1: 4-Prompt-Kette (Copy-Paste für Gemini CLI)](#baustein-1-4-prompt-kette-copy-paste-für-gemini-cli)
5. [Baustein 2: ZTII-S / Koschöpfer-Protokoll (3+1 Schema)](#baustein-2-ztii-s--koschöpfer-protokoll-31-schema)
6. [Baustein 3: Ausführer-Prompt für Projektanalyse](#baustein-3-ausführer-prompt-für-projektanalyse)
7. [Baustein 4: Generator für Dateisystem-Prompts (PROMPT_PACK)](#baustein-4-generator-für-dateisystem-prompts-prompt_pack)
8. [Baustein 5: Konkretes Ausführungsformat (ΔZ-Block)](#baustein-5-konkretes-ausführungsformat-δz-block)
9. [Baustein 6: DRY-RUN Workspace-Architektur](#baustein-6-dry-run-workspace-architektur)
10. [Der komplette Signalfluss (Wie alles zusammenhängt)](#der-komplette-signalfluss-wie-alles-zusammenhängt)
11. [Schnellreferenz-Karte](#schnellreferenz-karte)

---

## BEGRIFFS-GLOSSAR (FL STUDIO METAPHORIK)

Damit wir dieselbe Sprache sprechen, hier die Übersetzungstabelle. Jeder Anglizismus wird mit deutscher Übersetzung und FL-Studio-Pendant geführt. Diese Begriffe gelten im gesamten Handbuch.

| Standard-Begriff | FL Studio Pendant / Metapher | Bedeutung im System |
| :--- | :--- | :--- |
| **Agenten / LLMs** | Gesangs-Voreinstellungen (Vocal Presets) | Vorkonfigurierte Rollen, die eine bestimmte Aufgabe ohne Nachdenken ausführen. |
| **Regeln / Konfiguration** | Mixer-Regler | Die Parameter, die das Verhalten des Systems steuern und begrenzen. |
| **Code / Rohe Daten** | Rohe Stimme / Rohe Stems | Unbearbeiteter Input, der durch das System strukturiert werden muss. |
| **Projekt / System** | Der Mix | Das Gesamtergebnis, an dem gearbeitet wird. |
| **Workflow / Prozess** | Signalfluss (Signal Flow) / Murmelbahn | Der definierte Weg, den eine Information durch das System nimmt. |
| **Module / Erweiterungen** | Plugins (Erweiterungsmodule) | Spezifische Werkzeuge für isolierte Aufgaben (z.B. Dateisystem-Zugriff). |
| **Vorlagen** | Templates (Vorlagen) | Wiederverwendbare Projektstrukturen (z.B. DRY-RUN Workspace). |
| **Fehler / Bug** | Lücke in der Murmelbahn | Ein Bruch im Signalfluss (Signal Flow), der den Prozess stoppt. |
| **Debugging** | Frequenzen sauber trennen | Isolieren und Beheben von Fehlern durch präzise Eingriffe. |
| **Architektur** | Playlist-Anordnung | Die logische und physische Struktur von Dateien und Prozessen. |
| **Pipeline** | Signalkette (Signal Chain) | Die serielle Abfolge von Prompts oder Befehlen. |
| **Iteration / Loop** | Loop (Wiederholschleife) | Das wiederholte Ausführen eines Prozesses zur Verfeinerung. |
| **Deployment / Output** | Master-Export | Das finale Ausliefern oder Anwenden von Änderungen. |

---

## ÜBERGREIFENDE REGELN (DER MASTER-BUS)

Bevor wir in die einzelnen Plugins (Erweiterungsmodule) gehen, hier die Gesetze, die den gesamten Mix zusammenhalten. Ohne diese Regeln übersteuert das System. Diese Regeln gelten **global** und überschreiben jede lokale Annahme.

### REGEL 1: OBERSTES AXIOM (Master-Export-Gate)

**Keine Operation ohne explizite Nutzerbestätigung.** Der Render-Button wird nur von dir gedrückt. Das System bereitet den Mix (Projekt) im DRY-RUN vor, generiert die Spezifikationen und zeigt das Delta (ΔZ). Aber der finale Schreibvorgang (Ausführung) erfordert ein explizites "GO". Das ist das Gate zwischen GENERIEREN (0) und AUSFÜHREN (1).

> **Warum:** Ohne dieses Gate schreibt das System unkontrolliert in dein Dateisystem. Das ist, als würde FL Studio automatisch rendern, während du noch am Arrangement arbeitest. Katastrophe.

### REGEL 2: EISERNES GESETZ (Konsistenz-Check)

**Kein Output ohne Substanz und Konsistenz.** Jeder Bounce (jede Antwort, jede generierte Datei) muss drei Tests bestehen:

| Test | FL Studio Pendant | Prüffrage |
| :--- | :--- | :--- |
| **Erkenntnis** | Das rohe Sample | Was ist es? Ist der Zweck klar? |
| **Praxis** | Das Routing | Wie setzt man es um? Ist es ausführbar? |
| **Vermittlung** | Das Arrangement | Wie erklärt man es? Versteht der Nutzer es? |

> **Warum:** Ein Output, der nur schön klingt, aber nicht umsetzbar ist, ist wie ein Beat mit perfektem Mastering aber ohne Kick. Nutzlos.

### REGEL 3: 3+1 Ebenen mit 6R-Check (Multiband-Kompression)

Jede Ebene der Bearbeitung (Zustand, Information, Transformation + Delta) wird rigoros auf 6 Parameter geprüft. Das ist die Multiband-Kompression deines Systems: Jedes Frequenzband (jede Ebene) wird einzeln kontrolliert.

| # | Parameter | Prüffrage im System |
| :--- | :--- | :--- |
| 1 | **Richtige Ware** | Ist es der richtige Inhalt? |
| 2 | **Richtige Menge** | Ist es genau das, was gebraucht wird, nicht mehr? |
| 3 | **Richtige Qualität** | Ist der Code (Rohe Stimme) / Text fehlerfrei? |
| 4 | **Richtige Zeit** | Passiert es in der richtigen Phase der Signalkette (Pipeline)? |
| 5 | **Richtiger Ort** | Geht es in den richtigen Dateipfad? |
| 6 | **Richtige Kosten** | Ist es Token-effizient? |

> **Warum:** Diese 6R kommen aus der Lagerlogistik. Wenn du das falsche Paket an den falschen Ort zur falschen Zeit lieferst, ist es egal, wie gut die Ware ist. Dasselbe gilt für Prompts.

### REGEL 4: Token-Minimierung (EQing)

**Kompakt, keine Füllwörter, nur was zählt.** Wir schneiden die unnötigen Frequenzen rigoros ab. Keine Höflichkeitsfloskeln im Code-Output. Nur das reine, ausführbare Signal. Jedes Token, das nicht zum Ergebnis beiträgt, ist Rauschen.

> **Warum:** Tokens kosten Geld und Kontext-Fenster. Ein aufgeblähter Prompt ist wie ein Mix mit zu vielen Spuren: Matsch. EQ raus, was nicht gebraucht wird.

---

## DAS GENERIEREN/AUSFÜHREN-GATE (BASE2)

Das ist das fundamentale Prinzip, das unter allem liegt. Jede Aktion im System hat genau zwei Zustände, wie ein binärer Schalter:

| Zustand | Name | FL Studio Pendant | Was passiert |
| :--- | :--- | :--- | :--- |
| **0** | GENERIEREN | MIDI schreiben / Arrangement bauen | Erzeugt Struktur, Form, Träger. Hat keinen Effekt außerhalb des Systems. Beispiele: Prompt generieren, Schema erstellen, Workflow beschreiben, Plan schreiben. |
| **1** | AUSFÜHREN | Bounce / Render / Master-Export | Erzeugt Effekt, ändert einen Zielzustand, koppelt Systeme. Beispiele: Prompt an LLM senden, Datei schreiben, Prozess starten, Entscheidung treffen. |

**Die Wahrheit:** Diese zwei Zustände sind nicht strikt trennbar. Selbst wenn du etwas generierst, führst du die Generierung aus. Aber erst die **Integration** (das Schreiben in die echte Welt) macht es zu einer echten Ausführung (1). Deshalb braucht es das **Gate**: Vor jedem Output wird eine Modus-Entscheidung erzwungen.

> **In FL Studio:** Du kannst stundenlang MIDI-Noten setzen (GENERIEREN). Aber erst wenn du auf "Export" drückst (AUSFÜHREN), entsteht die WAV-Datei. Das Gate ist der Export-Dialog.

---

## BAUSTEIN 1: 4-PROMPT-KETTE (COPY-PASTE FÜR GEMINI CLI)

### Theorie

Das ist deine Standard-Vocal-Chain für die Gemini CLI. Vier Gesangs-Voreinstellungen (Vocal Presets), die nacheinander geladen werden, um rohe Ideen in saubere, ausführbare Dateien zu verwandeln. Diese Signalkette (Pipeline) zwingt das Modell in die reine Ausführung und eliminiert das typische "Ich erkläre dir mal was"-Verhalten.

### Praxis (Copy-Paste-fertig)

**PROMPT 1 – ANKER (Das Vocal Preset laden)**

Dieser Prompt setzt die Rolle. Er kalibriert das Modell auf reines Ausführen.

```text
Du bist ein Ausführer, kein Denker. Jede Antwort enthält exakt drei Elemente:
1) Ziel-Pfad (absolut),
2) Aktion (erstellen/ändern/verschieben/löschen),
3) Inhalt oder Befehl.
Pfad unbekannt = ABBRUCH. Keine Erklärungen, keine Höflichkeit, keine Rückfragen. Nur Signal.
```

**PROMPT 2 – AUFTRAG (Das Recording)**

Dieser Prompt definiert die konkrete Aufgabe im Format PFAD/AKTION/INHALT.

```text
AUFTRAG:
PFAD: /home/ubuntu/projekt/src/main.py
AKTION: erstellen
INHALT:
def main():
    print("Signal läuft.")

if __name__ == "__main__":
    main()
```

**PROMPT 3 – AUSFÜHRUNG (Der Bounce)**

Dieser Prompt triggert die sofortige Ausführung ohne Rückfrage.

```text
Sofort ausführen. Keine Rückfrage. Bestätigung ausschließlich mit:
ERLEDIGT + [vollständiger Pfad]
```

**PROMPT 4 – PRÜFUNG (Phasen-Check)**

Dieser Prompt verifiziert das Ergebnis gegen den Auftrag.

```text
Datei lesen: [Pfad aus PROMPT 2 einsetzen].
Inhalt gegen den Auftrag aus PROMPT 2 prüfen.
Bei Abweichung: FEHLER + exakte Differenz aufzeigen.
Bei Übereinstimmung: PASSED.
```

### Erklärung (Warum funktioniert das)

Die 4-Prompt-Kette funktioniert, weil sie die Empfänger-Kalibrierung des Modells in vier saubere Phasen zerlegt. PROMPT 1 setzt den Kontext (das Vocal Preset). PROMPT 2 liefert den Input (das Recording). PROMPT 3 erzwingt die Transformation (den Bounce). PROMPT 4 schließt die Wiederholschleife (Loop) mit einer Validierung. Ohne diese Trennung vermischt das Modell Planung und Ausführung, was zu unsauberem Output führt. Es ist wie vier Insert-Effekte auf einem Kanal: Jeder hat eine Aufgabe, und die Reihenfolge ist entscheidend.

---

## BAUSTEIN 2: ZTII-S / KOSCHÖPFER-PROTOKOLL (3+1 SCHEMA)

### Theorie

Das ist dein Feedback-Loop (Wiederholschleife) mit dem System. Das Intent-First Prinzip bedeutet: Du singst die Melodie (natürliche Sprache), das System schreibt die MIDI-Noten (Struktur). Es verhindert, dass du dich mit Syntax herumschlagen musst.

Das Protokoll nutzt das rekursive ZTI-Framework (Zustand, Transformation, Information). Jeder Schritt ist eine bewusste Zustandsänderung. Das ZTI ist fraktal: Jede Komponente (Z, T, I) enthält in sich selbst einen vollständigen ZTI-Zyklus.

### Praxis (Die vier Phasen)

**Phase Z – Zustand (Der aktuelle Mix)**

Das System spiegelt zurück, was es verstanden hat.

```text
"Ich verstehe, dass du [ZIEL] erreichen willst.
Aktueller Zustand: [IST-ZUSTAND].
Zielzustand: [SOLL-ZUSTAND]."
```

**Phase I – Information (Die Routing-Regeln / Die Mixer-Regler)**

Das System benennt die Regeln und Werkzeuge, die es einsetzen wird.

```text
"Dazu nutze ich folgende Regeln:
- [REGEL 1]
- [REGEL 2]
Verfügbare Werkzeuge: [WERKZEUG-LISTE]."
```

**Phase T – Transformation (Das Processing)**

Das System führt die eigentliche Arbeit durch (oder bereitet sie im DRY-RUN vor).

```text
"Ich generiere jetzt [ARTEFAKT].
Modus: GENERIEREN (0) / DRY-RUN.
Output folgt."
```

**Phase ΔZ – Delta (Der A/B-Vergleich)**

Das System zeigt das Ergebnis und fragt nach Bestätigung.

```text
"Hier ist das Ergebnis:
[DELTA-ZUSAMMENFASSUNG]
Geänderte Felder: [LISTE]
Ist das Routing so, wie du es dir vorgestellt hast? (JA / NEIN / ANPASSEN)"
```

### Die Sicherungen

**Anti-Frust-Sicherung:** Syntax-Fehler von dir sind "kreative Unschärfe". Das System ist der Auto-Tune, der die schiefen Töne glattzieht, ohne die Emotion (den Intent) zu killen. Wenn du schreibst "mach mir ne datei wo das ding drin is", versteht das System: "Erstelle eine Datei mit dem besprochenen Inhalt" und fragt nach dem Pfad.

**Rückfrage-Pflicht bei Unklarheiten:** Wenn der Beat hakt, fragt das System nach Optionen, anstatt blind weiterzuproduzieren:

```text
"Unklarheit erkannt bei: [ELEMENT].
Option A: [Interpretation 1]
Option B: [Interpretation 2]
Option C: [Interpretation 3]
Welche Option?"
```

### Erklärung (Warum funktioniert das)

Das 3+1 Schema funktioniert, weil es den natürlichen Kommunikationsfluss abbildet. Zuerst Verständnis sichern (Z), dann Regeln klären (I), dann handeln (T), dann prüfen (ΔZ). Das ist wie ein Mixing-Workflow: Erst den Song anhören (Z), dann das Routing planen (I), dann die Mixer-Regler (Konfiguration) einstellen (T), dann A/B-Vergleich mit der Referenz (ΔZ). Die Anti-Frust-Sicherung verhindert, dass das System bei jedem Tippfehler abbricht. Die Rückfrage-Pflicht verhindert, dass es in die falsche Richtung produziert.

---

## BAUSTEIN 3: AUSFÜHRER-PROMPT FÜR PROJEKTANALYSE

### Theorie

Wenn du ein neues, chaotisches Projekt (einen Ordner voller roher Stems, z.B. deine Tagebucheinträge, Songideen, philosophischen Texte) reinholst, ist dies der Analyzer, der dir zeigt, was Phase ist. Er transformiert Chaos in Struktur und deckt die vier Kernprozesse ab: IDENTIFY & PURGE, CONVERT & STANDARDIZE, ORGANIZE, VERIFY.

### Praxis (Copy-Paste-fertiger Prompt)

```text
Du bist ein Projektanalyzer. Dein einziger Zweck: Chaos in Struktur verwandeln.

KONTEXT:
- FZ (Endziel): {{ ENDZIEL }}
- SK (Systemkontext): {{ SYSTEMKONTEXT }}
- VW (Verfügbare Werkzeuge): {{ WERKZEUGE }}
- ES (Eingabe-Spezifikation): {{ EINGABE_FORMAT }}
- AS (Ausgabe-Spezifikation): {{ AUSGABE_FORMAT }}

PROZESS (in dieser Reihenfolge):
1. IDENTIFY: Alle Datenquellen im Pfad {{ QUELL_PFAD }} identifizieren und auflisten.
2. EXTRACT: Kernmechanismen und wiederkehrende Muster extrahieren.
3. PURPOSE: Den übergeordneten Zweck aus den Daten ableiten.
4. MAP: Die Architektur (Playlist-Anordnung) als Baumstruktur darstellen.
5. COMPRESS: Die minimal reproduzierbare Implementierung als ausführbares Skript liefern.

OUTPUT-FORMAT (exakt dieses Schema, keine Abweichung):
PROJEKT_ZWECK: [Ein Satz]
KERNMECHANISMEN: [Max. 5 Einträge]
FUNKTIONS_MAP: [Baumstruktur]
MINIMALE_ARCHITEKTUR: [Ordnerstruktur]
MINIMAL_REPRODUZIERBARE_IMPLEMENTIERUNG: [Codeblock]

Keine Erklärungen außerhalb des Schemas. Nur Signal.
```

### Erklärung (Warum funktioniert das)

Die Platzhalter (FZ, SK, VW, ES, AS) funktionieren wie die Input-Kanäle eines Mixers. Jeder Kanal hat einen definierten Zweck. Wenn einer fehlt, weiß das System sofort, wo die Lücke in der Murmelbahn (Bug) ist. Der 5-Schritt-Prozess (IDENTIFY, EXTRACT, PURPOSE, MAP, COMPRESS) zwingt das Modell in eine lineare Analyse statt in freies Assoziieren. Das Output-Format ist starr, weil starre Formate maschinell weiterverarbeitbar sind.

---

## BAUSTEIN 4: GENERATOR FÜR DATEISYSTEM-PROMPTS (PROMPT_PACK)

### Theorie

Das ist dein Preset-Manager. Er trennt strikt zwischen `plan` (Struktur entwerfen / MIDI schreiben / GENERIEREN (0)) und `execute` (physisches Schreiben / Audio bouncen / AUSFÜHREN (1)). Das verhindert ungewollte operative Seiteneffekte. Kein Prompt darf gleichzeitig planen und schreiben.

### Praxis (YAML-Schema mit Beispielen)

**Grundschema:**

```yaml
category: "{{ KATEGORIE }}"
prompts:
  - name: "{{ PROMPT_NAME }}"
    allowed: ["{{ ERLAUBTE_AKTIONEN }}"]
    forbidden: ["{{ VERBOTENE_AKTIONEN }}"]
    template: |
      {{ PROMPT_TEXT }}
```

**Beispiel 1: structure_architect (Nur Planung)**

```yaml
category: "Architektur_und_Struktur"
prompts:
  - name: "structure_architect"
    allowed: ["plan", "list", "analyze"]
    forbidden: ["write", "delete", "move", "execute"]
    template: |
      Analysiere den Ordner {{ ziel_pfad }}.
      Erstelle einen Strukturplan basierend auf der DRY-RUN Architektur.
      Schreibe KEINE Dateien. Liefere nur die Spezifikation als Markdown-Baum.
```

**Beispiel 2: file_writer (Nur Ausführung)**

```yaml
category: "Dateisystem_Operationen"
prompts:
  - name: "file_writer"
    allowed: ["write", "create", "move"]
    forbidden: ["plan", "analyze", "explain"]
    template: |
      Führe exakt die folgende Operation aus:
      BEFEHL: {{ befehl }}
      ZIEL: {{ ziel_pfad }}
      INHALT: {{ inhalt }}
      Bestätige mit: ERLEDIGT + Pfad.
```

**Beispiel 3: chaos_scanner (Nur Analyse)**

```yaml
category: "Daten_Analyse"
prompts:
  - name: "chaos_scanner"
    allowed: ["read", "list", "analyze", "categorize"]
    forbidden: ["write", "delete", "move", "execute"]
    template: |
      Scanne den Ordner {{ quell_pfad }}.
      Kategorisiere jede Datei nach: Thema, Emotion, Sprachmuster, Erzählstruktur.
      Liefere das Ergebnis als YAML. Schreibe KEINE Dateien.
```

### Erklärung (Warum funktioniert das)

Die strikte Trennung von `allowed` und `forbidden` funktioniert wie die Routing-Matrix in FL Studio. Kanal 1 geht nur in Bus A, nicht in Bus B. Wenn ein Prompt sowohl planen als auch schreiben darf, entstehen unkontrollierte Seiteneffekte. Das ist wie ein Send-Effekt ohne Return: Das Signal verschwindet irgendwo. Die YAML-Struktur macht die Prompts maschinell lesbar und versionierbar.

---

## BAUSTEIN 5: KONKRETES AUSFÜHRUNGSFORMAT (ΔZ-BLOCK)

### Theorie

Jede Operation, jede Lücke in der Murmelbahn (Bug), die gefixt wird, MUSS nach diesem Schema dokumentiert und ausgeführt werden. Das ist dein Debugging-Standard (Frequenzen sauber trennen) und macht jede Änderung auditierbar. Der ΔZ-Block ist das Herzstück des minimalen Kernalgorithmus für Zustandsänderungen.

### Praxis (Das vollständige ΔZ-Block Format)

```text
┌─────────────────────────────────────────────┐
│ ΔZ-BLOCK                                    │
├─────────────────────────────────────────────┤
│ DELTA_SUMMARY: [Einzeilige Zusammenfassung] │
│ BEFEHL:        [bash / powershell / python]  │
│ ZIEL:          [Absoluter Dateipfad]         │
│ ÄNDERUNG:      [Was genau passiert]          │
│ ERWARTUNG:     [Was danach gelten soll]      │
│ TEST:          [Wie man es prüft]            │
├─────────────────────────────────────────────┤
│ INVARIANTS_CHECK: [PASS / FAIL + Regel]      │
│ RISK_FLAG:        [Y / N]                    │
│ SHADOW_REQUIRED:  [YES / NO]                 │
│ INTEGRATION:      [APPLIED / NOT_APPLIED]    │
└─────────────────────────────────────────────┘
```

**Konkretes Beispiel:**

```text
┌─────────────────────────────────────────────────────────────────┐
│ ΔZ-BLOCK                                                        │
├─────────────────────────────────────────────────────────────────┤
│ DELTA_SUMMARY: Konvertierungs-Schleife für TXT-zu-MD hinzufügen │
│ BEFEHL:        bash                                              │
│ ZIEL:          /home/ubuntu/projekt/scripts/convert.sh           │
│ ÄNDERUNG:      for-Schleife die alle .txt in .md konvertiert     │
│ ERWARTUNG:     Alle .txt im Input liegen als .md im Output vor   │
│ TEST:          ls /home/ubuntu/projekt/output/ | grep "\.md"     │
├─────────────────────────────────────────────────────────────────┤
│ INVARIANTS_CHECK: PASS (Regel: Keine Löschung ohne Backup)       │
│ RISK_FLAG:        N                                              │
│ SHADOW_REQUIRED:  NO                                             │
│ INTEGRATION:      NOT_APPLIED (wartet auf Master-Export-Gate)    │
└─────────────────────────────────────────────────────────────────┘
```

### Der Kernalgorithmus hinter dem ΔZ-Block

1. **Impuls empfangen:** Die Anforderung kommt rein (z.B. "Konvertiere alle TXT-Dateien").
2. **Inferenz durchführen:** Das System analysiert, was zu tun ist.
3. **Delta-Paket identifizieren:** Der ΔZ-Block wird geschrieben.
4. **Invarianten prüfen:** Verstößt die Änderung gegen eine Regel?
5. **Risiko bewerten:** Bei RISK_FLAG: Y wird ein SHADOW-Prozess (Zweitblick) gestartet.
6. **Integration:** Erst nach Bestätigung durch das Master-Export-Gate wird `INTEGRATION: APPLIED` gesetzt.
7. **Dokumentation:** Der ΔZ-Block wird im Ledger (Protokoll) gespeichert.

### Erklärung (Warum funktioniert das)

Der ΔZ-Block funktioniert, weil er jede Änderung atomar und nachvollziehbar macht. In FL Studio ist das wie die Undo-History: Jeder Schritt ist dokumentiert, und du kannst jederzeit zurückspringen. Das INVARIANTS_CHECK-Feld verhindert, dass Regeln verletzt werden. Das RISK_FLAG triggert einen Zweitblick bei kritischen Operationen. Die INTEGRATION bleibt auf NOT_APPLIED, bis du das Master-Export-Gate passierst. Kein unkontrolliertes Schreiben.

---

## BAUSTEIN 6: DRY-RUN WORKSPACE-ARCHITEKTUR

### Theorie

Das ist dein persistentes Template (Vorlage) in VS Code. Hier baust du den Mix (Projekt) auf, bevor du ihn exportierst. Es trennt die Planung physisch von der Ausführung. Die Ordner 00 bis 03 sind der GENERIEREN-Bereich (0). Ordner 04 ist der AUSFÜHREN-Bereich (1). Dazwischen liegt das Master-Export-Gate.

### Praxis (Die Playlist-Anordnung)

```text
/workspace_root/
│
├── 00_spec/                    # MIDI-Spuren: Spezifikationen, Pläne, Prompt-Packs
│   ├── prompts/                # Die YAML-Prompt-Packs aus Baustein 4
│   ├── schemas/                # Datenbank-Schemata, Ordnerstruktur-Pläne
│   └── requirements.md         # Was soll das Projekt am Ende können?
│
├── 01_validate/                # Analyzer: Test-Skripte, Schema-Validierung
│   ├── tests/                  # Automatisierte Prüfskripte
│   └── checklists/             # Manuelle 6R-Checklisten
│
├── 02_transform/               # Processing: Skripte die Daten umwandeln
│   ├── converters/             # z.B. txt_to_md.sh, yaml_formatter.py
│   └── filters/                # z.B. duplicate_remover.sh
│
├── 03_simulate/                # Playback: DRY-RUN Ausführung, Logs, Deltas
│   ├── dry_run_logs/           # Protokolle der simulierten Ausführung
│   ├── delta_blocks/           # Gesammelte ΔZ-Blöcke vor der Freigabe
│   └── diff_reports/           # Vorher-Nachher-Vergleiche
│
├── 04_execute/                 # Master-Export: Finale Skripte nach Gate-Freigabe
│   ├── approved_scripts/       # Nur freigegebene Skripte landen hier
│   └── execution_log.md        # Protokoll aller ausgeführten Operationen
│
└── README.md                   # Projektbeschreibung und Signalfluss-Übersicht
```

### Die Regeln des Workspace

| Ordner | Modus | Darf schreiben auf echte Daten? | FL Studio Pendant |
| :--- | :--- | :--- | :--- |
| `00_spec` | GENERIEREN (0) | NEIN | MIDI-Editor / Piano Roll |
| `01_validate` | GENERIEREN (0) | NEIN | Spectrum Analyzer |
| `02_transform` | GENERIEREN (0) | NEIN (nur auf Kopien) | Mixer-Inserts (Effektkette) |
| `03_simulate` | GENERIEREN (0) | NEIN | Vorhören im Browser |
| `04_execute` | AUSFÜHREN (1) | JA (nach Gate-Freigabe) | Master-Export / Render |

### Erklärung (Warum funktioniert das)

Die physische Trennung in Ordner verhindert, dass ein Skript aus der Planungsphase versehentlich echte Daten verändert. In FL Studio würdest du auch nicht im Piano Roll direkt auf die Master-Spur rendern. Du arbeitest in Layern. Ordner 00-03 sind deine Layer. Ordner 04 ist der finale Bounce. Die Struktur ist einmal als Template (Vorlage) gespeichert und wird für jedes neue Projekt kopiert. Jeder neue Chaos-Ordner (rohe Stems) wird durch diese Signalkette (Pipeline) geschleust.

---

## DER KOMPLETTE SIGNALFLUSS (WIE ALLES ZUSAMMENHÄNGT)

Hier ist die Murmelbahn von Anfang bis Ende. So fließt das Signal durch alle 6 Bausteine:

```text
[CHAOS-INPUT]
    │
    ▼
┌──────────────────────────────────────────────────────────────┐
│ BAUSTEIN 2: KOSCHÖPFER-PROTOKOLL                             │
│ Z: "Du willst deine Chaos-Dateien strukturieren."            │
│ I: "Ich nutze Baustein 3 (Analyzer) + Baustein 6 (DRY-RUN)" │
│ T: "Ich starte die Analyse..."                               │
│ ΔZ: "Hier ist der Plan. Passt das?"                          │
└──────────────────────┬───────────────────────────────────────┘
                       │ [Nutzer bestätigt]
                       ▼
┌──────────────────────────────────────────────────────────────┐
│ BAUSTEIN 3: PROJEKTANALYSE (in 00_spec/)                     │
│ → IDENTIFY: Dateien scannen                                  │
│ → EXTRACT: Muster erkennen                                   │
│ → PURPOSE: Zweck ableiten                                    │
│ → MAP: Architektur (Playlist-Anordnung) entwerfen            │
│ → COMPRESS: Minimalen Loop (Wiederholschleife) bauen         │
└──────────────────────┬───────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────┐
│ BAUSTEIN 4: PROMPT_PACK generieren (in 00_spec/prompts/)     │
│ → structure_architect (nur plan, kein write)                  │
│ → chaos_scanner (nur analyze, kein execute)                   │
│ → file_writer (nur write, kein plan) ← wartet auf Gate       │
└──────────────────────┬───────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────┐
│ BAUSTEIN 6: DRY-RUN in 03_simulate/                          │
│ → Simulation ausführen                                       │
│ → ΔZ-Blöcke (Baustein 5) generieren                         │
│ → Diff-Reports erstellen                                     │
└──────────────────────┬───────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────┐
│ ★ MASTER-EXPORT-GATE (Regel 1) ★                             │
│ "Alle ΔZ-Blöcke geprüft. 6R-Check bestanden.                │
│  Bereit für Ausführung. GO / STOP?"                          │
└──────────────────────┬───────────────────────────────────────┘
                       │ [Nutzer: GO]
                       ▼
┌──────────────────────────────────────────────────────────────┐
│ BAUSTEIN 1: 4-PROMPT-KETTE (in 04_execute/)                  │
│ → PROMPT 1: Rolle setzen (Ausführer)                         │
│ → PROMPT 2: Auftrag definieren (PFAD/AKTION/INHALT)          │
│ → PROMPT 3: Ausführen (ERLEDIGT + Pfad)                      │
│ → PROMPT 4: Prüfen (PASSED / FEHLER)                         │
└──────────────────────┬───────────────────────────────────────┘
                       │
                       ▼
                [SAUBERER OUTPUT]
```

---

## SCHNELLREFERENZ-KARTE

| Situation | Welchen Baustein nutzen? | Wo im Workspace? |
| :--- | :--- | :--- |
| Neues Chaos-Projekt analysieren | Baustein 3 (Projektanalyse) | `00_spec/` |
| Prompts für Dateioperationen vorbereiten | Baustein 4 (PROMPT_PACK) | `00_spec/prompts/` |
| Änderungen simulieren und dokumentieren | Baustein 5 (ΔZ-Block) | `03_simulate/delta_blocks/` |
| Ergebnis mit dem Nutzer abstimmen | Baustein 2 (Koschöpfer-Protokoll) | Überall (Meta-Ebene) |
| Dateien tatsächlich schreiben/ändern | Baustein 1 (4-Prompt-Kette) | `04_execute/` |
| Gesamtstruktur des Workspace aufsetzen | Baustein 6 (DRY-RUN Architektur) | `/workspace_root/` |

| Frage | Antwort |
| :--- | :--- |
| Darf ich ohne Nutzer-GO Dateien schreiben? | NEIN. Master-Export-Gate. |
| Was mache ich bei einem Tippfehler vom Nutzer? | Anti-Frust-Sicherung: Intent erkennen, Optionen anbieten. |
| Wie dokumentiere ich eine Änderung? | ΔZ-Block (Baustein 5). Immer. |
| Wie trenne ich Planung von Ausführung? | PROMPT_PACK: `allowed` vs. `forbidden`. Workspace: `00-03` vs. `04`. |
| Was ist der kleinste funktionierende Prozess? | ANKER → AUFTRAG → AUSFÜHRUNG → PRÜFUNG (Baustein 1). |

---

> **Das System ist kalibriert. Der Mix (Projekt) ist bereit für das Playback. Drück Play, wenn du soweit bist.**
