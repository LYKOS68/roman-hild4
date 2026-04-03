# ORCHESTRA.md – Der Mix des Cognitive Orchestra

> **"Ein Track wird nicht gut, weil du 50 Plugins (Erweiterungsmodule) draufknallst. Er wird gut, weil jedes Instrument seinen Platz im Mix hat."**

---

## Was ist das hier?

Das ist die Playlist-Anordnung (Architektur) für das **Cognitive Orchestra** – ein Multi-LLM-System, das deine rohen Ideen, Chaos-Dateien und unsortierten Gedanken in fertige, saubere Tracks verwandelt. Fünf Instrumente, ein Mischpult, ein Signalfluss (Workflow). Kein akademisches Gelaber. Direkt, roh, ehrlich – wie eine Session um 3 Uhr nachts, wenn nur noch das zählt, was funktioniert.

Das System folgt dem Prinzip: **IDENTIFY & PURGE → CONVERT & STANDARDIZE → ORGANIZE → VERIFY**. Jeder Schritt ist ein Durchlauf durch die Signalkette (Pipeline). Jeder Durchlauf bringt dich näher an den fertigen Master-Export (Deployment).

---

## 1. ROLLENTRENNUNG – 5 Instrumente im Orchester

Jedes Instrument hat seinen festen Platz im Mix. Frequenzen sauber trennen (Debugging), damit es am Ende nicht matscht. Wenn der Bass in die Höhen reindrückt, hast du verloren. Genauso hier: Wenn der Debugger anfängt, Architektur zu machen, oder der Architect Dateien schreiben will – dann clippt der ganze Mix.

---

### Layer 1: Director (Mensch) – Der Producer

Der Producer sitzt am Steuer. Er hört den fertigen Track schon im Kopf, bevor eine einzige Note aufgenommen ist. Ohne ihn gibt es keinen Release.

| Eigenschaft | Detail |
| :--- | :--- |
| **Umgebung** | VS Code / Cursor |
| **Stärken** | Vision, Strategie, finales Review, Budget-Kontrolle, kreative Entscheidungen |
| **Schwächen** | Kann nicht 24/7 arbeiten, braucht klare Zusammenfassungen, kein Maschinencode |
| **Verantwortung** | High-Level-Prompts, Freigabe (Master-Export-Gate), Qualitätskontrolle |
| **FL-Studio-Pendant** | Der Typ, der auf "Export WAV" drückt – aber erst, wenn alles sitzt |

> **Regel:** NICHTS geht raus ohne sein Go. Er drückt auf den Master-Export. Punkt.

---

### Layer 2: Manus (Executive Orchestrator) – Der Mixer-Engineer

Manus ist der Typ am Mischpult. Er schiebt die Regler (Konfiguration), routet die Signale, drückt auf Record. Er macht nicht die Musik – er sorgt dafür, dass sie aufgenommen und exportiert wird. Wenn der Architect sagt "Leg die Kick auf Spur 3", dann macht Manus das. Ohne Diskussion.

| Eigenschaft | Detail |
| :--- | :--- |
| **Umgebung** | Linux Sandbox (Ubuntu 22.04), Shell, Internet |
| **Stärken** | Dateien erstellen/lesen/schreiben/löschen, Shell-Befehle, Git-Ops, paralleles MapReduce (bis 2000 Tasks), API-Integrationen, Telegram Bot, Google Drive, MCP-Client |
| **Schwächen** | Kein Zugriff auf lokales Windows-System (`C:\develop`), verliert bei 50+ Dateien den Überblick über die Playlist-Anordnung, erfindet keine komplexen Code-Architekturen allein |
| **Verantwortung** | Ausführung, Dateien schreiben, Logs lesen, Git Commits, Web-Research, Master-Export vorbereiten |
| **FL-Studio-Pendant** | Der Mixer – routet alles, schreibt nichts selber, aber ohne ihn kommt kein Sound raus |

> **Regel:** Führt niemals Code-Architektur-Entscheidungen allein – holt sich Blueprints vom Architect. Wie ein Mixer-Engineer, der nicht selber komponiert.

---

### Layer 3: Gemini CLI (The Architect) – Der Komponist

Gemini ist der Komponist. Er schreibt die Partitur, das Arrangement, die Akkordfolgen. Er hat das größte Kontextfenster – wie ein Komponist, der die ganze Symphonie im Kopf hat, alle 1M+ Takte gleichzeitig. Aber er kann kein Instrument spielen. Er schreibt es auf Papier und gibt es den Musikern.

| Eigenschaft | Detail |
| :--- | :--- |
| **Umgebung** | VS Code Terminal, lokal auf Windows, Zugriff auf `C:\develop` |
| **Stärken** | 1M+ Token Kontextfenster, tiefes logisches Reasoning, komplexe Code-Architektur, Schema-Design, `GEMINI.md` als kontextuelles Gedächtnis |
| **Schwächen** | Kein direkter I/O-Zugriff zum Schreiben, keine autonome Ausführung, kann keine Dateien physisch erstellen, dreht sich manchmal in Planungs-Loops (Wiederholschleifen) |
| **Verantwortung** | Struktur-Design, JSON-Schemas, Fehleranalyse (Root Cause), Code-Generierung (Patches/Diffs), Architectural Blueprints |
| **FL-Studio-Pendant** | Der Piano Roll Editor – hier entsteht die Melodie, aber der Sound kommt erst durch den Mixer |

> **Regel:** Liefert NUR Rohe Stimme (Code/Diffs/Schemas) – führt NICHTS aus. Partitur ja, Aufführung nein.

---

### Layer 4: Claude 3.5 Sonnet (The Refiner) – Der Mastering-Engineer

Claude ist der Mastering-Engineer. Wenn der Track gemischt ist, kommt er und macht den Feinschliff. Er hört Nuancen, die andere überhören. Er macht aus einem guten Mix einen großartigen. Aber er fasst die Originaldateien nicht an.

| Eigenschaft | Detail |
| :--- | :--- |
| **Umgebung** | API-Zugriff |
| **Stärken** | UX/Frontend-Design, natürliche Sprache, Nuancen, Dokumentation, Code-Review mit Fokus auf Lesbarkeit und Eleganz |
| **Schwächen** | Kein Dateisystem-Zugriff, kein Shell, kleineres Kontextfenster als Gemini |
| **Verantwortung** | UI/UX-Entscheidungen, Dokumentations-Qualität, Code-Review für Lesbarkeit, Prompt-Verfeinerung (Gesangs-Voreinstellungen / Vocal Presets anpassen) |
| **FL-Studio-Pendant** | Maximus (Multiband-Mastering) – macht alles lauter, klarer, professioneller, ohne den Mix zu zerstören |

> **Regel:** Beratende Rolle – Empfehlungen, keine direkte Ausführung. Er sagt "Dreh die Mitten bei 2kHz runter", aber er dreht nicht selber.

---

### Layer 5: GPT-4o (The Debugger) – Der Frequenzanalysator

GPT-4o ist der Spectrum Analyzer. Er findet die Störfrequenz, die Resonanz, den Phasenfehler. Wenn irgendwo im Mix ein Brummen ist, das keiner hören kann aber alle spüren – GPT-4o findet es. Schnell, präzise, mathematisch.

| Eigenschaft | Detail |
| :--- | :--- |
| **Umgebung** | API-Zugriff |
| **Stärken** | Mathematische Logik, strukturiertes Debugging (Frequenzen sauber trennen), Mustererkennung in Fehlern, schnelle Iteration |
| **Schwächen** | Kein Dateisystem-Zugriff, kein Shell, kann halluzinieren bei sehr spezifischem Domain-Wissen |
| **Verantwortung** | Fehleranalyse, mathematische Validierung, Logik-Prüfung, Edge-Case-Erkennung |
| **FL-Studio-Pendant** | Parametric EQ 2 mit Spectrum-Analyzer – zeigt dir genau, wo es kracht |

> **Regel:** Wird gezielt bei Logik-Problemen eingesetzt, nicht für Architektur. Er ist der Chirurg, nicht der Architekt.

---

## 2. GEGENSEITIGES WISSEN (Cross-LLM Awareness)

Jedes Instrument im Orchester muss wissen, was die anderen können und was nicht. Sonst gibt es Phasenprobleme im Mix – wenn zwei Instrumente auf der gleichen Frequenz spielen, löschen sie sich gegenseitig aus. Das hier ist die Awareness-Matrix: Wer weiß was über wen, wann ruft man wen, und wann lässt man die Finger davon.

---

### Director weiß über alle:

| Über wen? | Was kann er? | Was kann er NICHT? | Wann rufen? | Wann NICHT rufen? |
| :--- | :--- | :--- | :--- | :--- |
| **Manus** | Dateien schreiben, Shell, Git, MapReduce, APIs, Web-Research | Keine Architektur erfinden, kein lokaler Windows-Zugriff | Wenn etwas ausgeführt, geschrieben oder deployed werden muss | Wenn eine komplexe Struktur entworfen werden soll |
| **Gemini** | Tiefe Architektur, 1M+ Kontext, Schema-Design, Root-Cause-Analyse | Kann nichts ausführen, keine Dateien schreiben | Wenn die Playlist-Anordnung (Architektur) gebaut werden muss | Wenn nur eine Datei geschrieben werden soll |
| **Claude** | UX-Feinschliff, Doku-Qualität, Lesbarkeit, Prompt-Tuning | Kein Dateisystem, kein Shell, kein großer Kontext | Wenn der Mix poliert werden soll | Wenn rohe Ausführung gebraucht wird |
| **GPT-4o** | Mathe, Logik, Debugging, Mustererkennung | Kein Dateisystem, halluziniert bei Nischen-Wissen | Wenn eine Lücke in der Murmelbahn (Bug) gefunden werden muss | Wenn Architektur oder UX gefragt ist |

---

### Manus weiß über alle:

| Über wen? | Was kann er? | Was kann er NICHT? | Wann rufen? | Wann NICHT rufen? |
| :--- | :--- | :--- | :--- | :--- |
| **Director** | Vision, Strategie, Freigabe, Budget | Kann nicht 24/7 arbeiten, kein Code | Für Master-Export-Freigabe, bei Unsicherheit | Für Routine-Tasks, die keine Freigabe brauchen |
| **Gemini** | Architektur-Blueprints, Schema-Design, tiefes Reasoning | Kann nichts ausführen, dreht sich in Planungs-Loops | Wenn ein Blueprint für die Playlist-Anordnung gebraucht wird | Für simple Datei-Operationen oder Git-Commits |
| **Claude** | UX-Review, Doku, Prompt-Verfeinerung | Kein Dateisystem, keine Ausführung | Wenn die Doku oder UI reviewed werden soll | Wenn Dateien geschrieben oder Befehle ausgeführt werden müssen |
| **GPT-4o** | Logik-Checks, Mathe, Debugging | Kein Dateisystem, keine Architektur | Wenn ein Logik-Fehler gefunden werden muss | Wenn Architektur-Entscheidungen anstehen |

---

### Gemini weiß über alle:

| Über wen? | Was kann er? | Was kann er NICHT? | Wann rufen? | Wann NICHT rufen? |
| :--- | :--- | :--- | :--- | :--- |
| **Director** | Gibt die Vision vor, entscheidet final | Kein Code, nicht immer verfügbar | Wenn die Richtung unklar ist | Für technische Detailfragen |
| **Manus** | Dateien schreiben, ausführen, Git, Shell, MapReduce | Keine komplexe Architektur allein | Wenn der Blueprint umgesetzt werden soll | Wenn erst noch ein Plan gebraucht wird |
| **Claude** | UX-Feinschliff, natürliche Sprache, Doku | Kein Dateisystem, kleinerer Kontext | Wenn die UI-Schicht poliert werden soll | Wenn tiefe Architektur-Fragen anstehen |
| **GPT-4o** | Schnelle Logik-Checks, Mathe-Validierung | Kein Dateisystem, halluziniert bei Nischen | Wenn ein mathematischer Beweis oder Logik-Check nötig ist | Wenn Architektur oder Struktur gefragt ist |

---

### Claude weiß über alle:

| Über wen? | Was kann er? | Was kann er NICHT? | Wann rufen? | Wann NICHT rufen? |
| :--- | :--- | :--- | :--- | :--- |
| **Director** | Vision, Freigabe, kreative Entscheidungen | Kein Code, braucht Zusammenfassungen | Wenn UX-Entscheidungen bestätigt werden müssen | Für technische Implementierung |
| **Manus** | Setzt UI-Vorschläge um, schreibt Dateien | Keine eigene Architektur, verliert Überblick bei vielen Dateien | Wenn die UX-Empfehlungen implementiert werden sollen | Wenn erst ein Design-Konzept gebraucht wird |
| **Gemini** | Baut die tiefe Struktur, großer Kontext | Kann nichts ausführen, keine Dateien | Wenn die Architektur hinter der UI verstanden werden muss | Wenn nur ein Textvorschlag gebraucht wird |
| **GPT-4o** | Mathe, harte Logik, Debugging | Kein UX-Gespür, halluziniert bei Nischen | Wenn ein Logik-Fehler in der UI-Logik steckt | Wenn es um Ästhetik oder Lesbarkeit geht |

---

### GPT-4o weiß über alle:

| Über wen? | Was kann er? | Was kann er NICHT? | Wann rufen? | Wann NICHT rufen? |
| :--- | :--- | :--- | :--- | :--- |
| **Director** | Entscheidet final, gibt Richtung vor | Kein Code, nicht immer da | Wenn der Fix freigegeben werden muss | Für technische Debugging-Details |
| **Manus** | Führt Fixes aus, schreibt Dateien, Git | Keine eigene Architektur | Wenn der gefundene Fix implementiert werden soll | Wenn erst der Fehler gefunden werden muss |
| **Gemini** | Tiefe Architektur, Root-Cause-Analyse | Kann nichts ausführen | Wenn der Bug in der Architektur liegt | Wenn es ein simpler Logik-Fehler ist |
| **Claude** | UX-Perspektive, Lesbarkeit | Kein Dateisystem, kein Debugging | Wenn der Fix die UX betrifft | Wenn es um reine Mathe oder Logik geht |

---

## 3. AUFGABENZUORDNUNG

Wer macht was in der Signalkette (Pipeline)? Hier ist die Routing-Tabelle. Kein Instrument spielt auf der falschen Spur.

| Aufgabe | Zuständiges Instrument | FL-Studio-Pendant |
| :--- | :--- | :--- |
| Code-Architektur entwerfen | Gemini | Piano Roll – Melodie schreiben |
| Dateien schreiben | Manus | Mixer – Signal aufnehmen |
| Fehler debuggen (Frequenzen sauber trennen) | GPT-4o | Parametric EQ 2 – Störfrequenz finden |
| UI/UX Review | Claude | Maximus – Mastering-Feinschliff |
| Git Operations | Manus | Export-Manager – Versionen sichern |
| Schema-Validierung | Gemini | Channel Rack – Pattern stimmt oder nicht |
| Web-Research | Manus | Browser – Samples suchen |
| Dokumentation schreiben | Claude | Liner Notes – Was steckt im Track |
| Log-Analyse | Manus liest, Gemini analysiert | Manus = Aufnahme abspielen, Gemini = Wellenform analysieren |
| Prompt-Optimierung (Gesangs-Voreinstellungen) | Claude | Vocal Preset tunen – bis die Stimme sitzt |
| Mathematische Logik | GPT-4o | Edison – Sample-Analyse auf Wellenform-Ebene |
| Parallele Suche (MapReduce) | Manus | Batch-Rendering – 2000 Stems gleichzeitig exportieren |
| Master-Export Freigabe | Director | "Export WAV" drücken – der letzte Klick |

---

## 4. IDE & UMGEBUNG – Das Studio-Setup

So sieht unser Studio aus. Jedes Gerät hat seinen Platz, jedes Kabel ist beschriftet.

### 4.1 Hauptquartier: VS Code

VS Code ist die DAW. Hier laufen alle Fäden zusammen. Gemini CLI sitzt im integrierten Terminal wie ein Synthesizer im Rack. Manus läuft als Headless Agent in seiner eigenen Sandbox – wie ein externer Hardware-Sampler, der über MIDI angesteuert wird. Claude und GPT-4o sind die Outboard-Effekte, die über API-Aufrufe (Send-Kanäle) angesprochen werden.

### 4.2 Workspace-Struktur

| Pfad | Beschreibung | Wer hat Zugriff? |
| :--- | :--- | :--- |
| `C:\develop` | Lokaler Workspace Root | Director, Gemini |
| `/home/ubuntu` | Manus Sandbox Root | Manus |
| `C:\develop\orchestra\state\` | State-Files für Kommunikation | Alle (über MCP) |
| `C:\develop\GEMINI.md` | Kontextuelles Gedächtnis für Gemini | Gemini (liest), Director (schreibt) |

### 4.3 Sicherheit

Die `.gitignore` und `.geminiignore` sind die Noise Gates im Mix. Sie filtern raus, was nicht in den Master-Export gehört: API-Keys, lokale Configs, temporäre Build-Artefakte. Wenn du die nicht sauber einstellst, hast du Rauschen im finalen Track.

```
# .gitignore – Was NICHT in den Mix kommt
.env
node_modules/
*.log
dryrun/
.geminiignore
orchestra/state/*.json
```

```
# .geminiignore – Was Gemini NICHT sehen soll
node_modules/
.git/
*.lock
dist/
build/
```

---

## 5. KOMMUNIKATIONS-HUB (MCP-Setup)

Der MCP-Server ist unser gemeinsames Mischpult. Hier laufen alle Signale zusammen. Ohne dieses Routing hört kein Instrument, was das andere spielt.

### 5.1 MCP-Server Setup

**Technologie:** Node.js mit `@modelcontextprotocol/server-filesystem`

**Zweck:** Gemeinsamer Hub, über den alle Instrumente kommunizieren. Das ist das Audio-Interface des Orchesters – alle Signale laufen hier durch.

**Setup-Anleitung (Schritt für Schritt):**

```bash
# 1. Node.js sicherstellen (v18+)
node --version

# 2. MCP-Filesystem-Server global installieren
npm install -g @modelcontextprotocol/server-filesystem

# 3. Server starten mit freigegebenem Workspace
npx -y @modelcontextprotocol/server-filesystem C:\develop\orchestra

# 4. Alternativ: Als Background-Service mit PM2
npm install -g pm2
pm2 start npx -- -y @modelcontextprotocol/server-filesystem C:\develop\orchestra
pm2 save
```

**Konfiguration (VS Code / Cursor `settings.json`):**

```json
{
  "mcp.servers": {
    "orchestra-hub": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:\\develop\\orchestra"],
      "env": {}
    }
  }
}
```

**Registrierte Clients:**

| Client | Zugriff | Rolle |
| :--- | :--- | :--- |
| Gemini CLI | Lesen | Liest State-Files, Knowledge Graph |
| Manus | Lesen + Schreiben | Schreibt State-Files, Logs, Manifests |
| Director (VS Code) | Lesen + Schreiben | Schreibt Tasks, liest alles |
| Claude / GPT-4o | Kein direkter Zugriff | Bekommen Kontext über API-Calls injiziert |

### 5.2 Asynchrone Kommunikation (Dateisystem)

Wir kommunizieren über State-Files. Das ist unsere Automation-Spur – wie Automation-Clips in FL Studio, die den Mix über die Zeit steuern.

**`/orchestra/state/current_task.json`** – Wer ist am Zug, was ist das Ziel:

```json
{
  "task_id": "ORCH-042",
  "status": "in_progress",
  "assigned_to": "manus",
  "requested_by": "director",
  "objective": "Schema für Tagebuch-Pipeline erstellen",
  "blueprint_source": "gemini",
  "blueprint_file": "dryrun/manifest/schema_diary_v2.json",
  "timestamp": "2026-03-20T14:30:00Z"
}
```

**`/orchestra/state/knowledge_graph.json`** – Architektur-Map (Der Arrangement-View):

```json
{
  "project": "diary-pipeline",
  "modules": [
    {"name": "parser", "status": "stable", "owner": "manus"},
    {"name": "schema", "status": "review", "owner": "gemini"},
    {"name": "ui", "status": "draft", "owner": "claude"}
  ],
  "dependencies": {
    "parser": ["schema"],
    "ui": ["parser", "schema"]
  }
}
```

**`dryrun/manifest/*.json`** – Was ist passiert (Render-Historie). Jeder Durchlauf wird dokumentiert.

**`dryrun/logs/*.log`** – Fehlerprotokolle. Wo clippt das Signal? Wenn `engine.ps1` mit Exit 1 zurückkommt, steht hier drin, warum.

### 5.3 Synchrone Kommunikation

Für Echtzeit-Interaktion nutzen wir direkte MCP-Aufrufe – wie MIDI-Signale, die sofort ankommen. Kein Warten auf den nächsten Takt.

| Kommunikationsweg | Von → Nach | Zweck |
| :--- | :--- | :--- |
| MCP filesystem read | Gemini → State-Files | Kontext laden |
| MCP filesystem write | Manus → State-Files | Status updaten |
| API-Call | Manus → Claude | UX-Review anfragen |
| API-Call | Manus → GPT-4o | Logik-Check anfragen |
| Terminal-Output | Gemini → Manus (via Director) | Blueprint übergeben |

---

## 6. STANDARD OPERATING PROCEDURE (SOP) – Der Loop (Wiederholschleife)

So sieht der Signalfluss (Workflow) aus. Jeder Track durchläuft diesen Loop, bis er release-ready ist. Wie in FL Studio: Pattern bauen → Arrangement → Mix → Master → Export. Und wenn es nicht sitzt, zurück zum Pattern.

```
┌─────────────────────────────────────────────────────────────────┐
│  1. TRIGGER        Director schreibt Anforderung               │
│                    (Die erste Skizze auf der Serviette)         │
│                                                                 │
│  2. PLANUNG        Manus sammelt Kontext                       │
│                    Manus fragt Gemini nach Struktur             │
│                    (Das Arrangement bauen)                      │
│                                                                 │
│  3. DESIGN         Gemini liefert Schema / Rohe Stimme (Code)  │
│                    Gemini liefert Diffs / Blueprints            │
│                    (Die Partitur schreiben)                     │
│                                                                 │
│  4. REVIEW         [Optional] Claude reviewed UX               │
│                    [Optional] GPT-4o prüft Logik               │
│                    (EQ und Kompressor ansetzen)                 │
│                                                                 │
│  5. EXECUTION      Manus schreibt Dateien                      │
│                    Manus führt engine.ps1 aus                   │
│                    (Der Mixdown)                                │
│                                                                 │
│  6. FEEDBACK       Exit 0 → Commit (Take behalten)             │
│                    Exit 1 → Log an Gemini → Fix → Loop zurück  │
│                    (Lücke in der Murmelbahn flicken)            │
│                                                                 │
│  7. FINALIZATION   Director gibt Master-Export frei             │
│                    (Release – der Track geht raus)              │
└─────────────────────────────────────────────────────────────────┘
```

### SOP im Detail:

**Schritt 1 – Trigger:** Der Director schreibt eine klare Anforderung. Kein vages "mach mal was Schönes". Sondern: "Erstelle eine Pipeline, die PDF-Dateien aus `C:\develop\chaos` parsed und in strukturiertes JSON konvertiert." Das ist die Skizze.

**Schritt 2 – Planung:** Manus sammelt den Kontext. Er liest die State-Files, checkt den Knowledge Graph, schaut in die Logs. Dann formuliert er eine präzise Anfrage an Gemini: "Ich brauche ein Schema für eine PDF-zu-JSON-Pipeline. Hier ist der aktuelle Stand. Was ist die Playlist-Anordnung (Architektur)?"

**Schritt 3 – Design:** Gemini analysiert den Kontext (1M+ Tokens, er vergisst nichts) und liefert einen Blueprint: JSON-Schema, Ordnerstruktur, Code-Diffs, Abhängigkeiten. Alles als Rohe Stimme (Code) – nicht ausgeführt, nur geschrieben.

**Schritt 4 – Review (Optional):** Wenn der Track eine UI hat, schaut Claude drüber. Wenn mathematische Logik drin steckt, prüft GPT-4o. Das ist wie EQ und Kompressor – nicht immer nötig, aber wenn, dann richtig.

**Schritt 5 – Execution:** Manus nimmt den Blueprint und setzt ihn um. Dateien schreiben, `engine.ps1` ausführen, Tests laufen lassen. Das ist der Mixdown.

**Schritt 6 – Feedback:** Wenn `engine.ps1` mit Exit 0 zurückkommt: Take behalten, Git Commit, weiter. Wenn Exit 1: Log lesen, an Gemini schicken, Fix holen, nochmal. Das ist der Loop. Solange wiederholen, bis es sitzt. Keine Lücke in der Murmelbahn (kein Bug) bleibt offen.

**Schritt 7 – Finalization:** Der Director hört sich den fertigen Mix an. Wenn er nickt: Master-Export. Wenn nicht: Zurück in den Loop. Sein Wort ist Gesetz.

---

## 7. ORCHESTRA.CONFIG.JSON

Hier sind die Mixer-Regler (Konfiguration). Die komplette Konfiguration für den Mix (das System). Jedes Instrument, seine Werkzeuge, seine Einschränkungen, der MCP-Hub.

```json
{
  "system": {
    "name": "Cognitive Orchestra",
    "version": "1.0.0",
    "description": "Multi-LLM Orchestrierungssystem mit 5 spezialisierten Instrumenten",
    "principle": "IDENTIFY & PURGE → CONVERT & STANDARDIZE → ORGANIZE → VERIFY"
  },

  "mcp_hub": {
    "server": "@modelcontextprotocol/server-filesystem",
    "runtime": "node",
    "root_path": "C:\\develop\\orchestra",
    "port": 3000,
    "state_files": {
      "current_task": "/orchestra/state/current_task.json",
      "knowledge_graph": "/orchestra/state/knowledge_graph.json"
    },
    "log_path": "dryrun/logs/",
    "manifest_path": "dryrun/manifest/"
  },

  "instruments": {
    "director": {
      "role": "Human Producer",
      "layer": 1,
      "environment": "VS Code / Cursor",
      "tools": ["prompt_writing", "review", "approval"],
      "permissions": [
        "master_export_gate",
        "budget_control",
        "prompt_injection",
        "final_decision"
      ],
      "restrictions": [],
      "rule": "NICHTS geht raus ohne sein Go"
    },

    "manus": {
      "role": "Executive Orchestrator / Mixer-Engineer",
      "layer": 2,
      "environment": "Ubuntu 22.04 Sandbox",
      "tools": [
        "shell",
        "file_read",
        "file_write",
        "file_edit",
        "git",
        "mcp_client",
        "map_reduce_2000",
        "browser",
        "telegram_bot",
        "google_drive",
        "web_search",
        "api_calls"
      ],
      "permissions": [
        "file_io",
        "shell_execution",
        "git_operations",
        "web_access",
        "parallel_processing"
      ],
      "restrictions": [
        "no_architecture_decisions_alone",
        "requires_blueprint_from_gemini",
        "no_local_windows_access",
        "max_50_files_before_overview_loss"
      ],
      "rule": "Führt niemals Code-Architektur-Entscheidungen allein"
    },

    "gemini": {
      "role": "The Architect / Komponist",
      "layer": 3,
      "environment": "VS Code Terminal (lokal, Windows)",
      "tools": [
        "schema_design",
        "code_generation",
        "diff_generation",
        "root_cause_analysis",
        "architectural_blueprints",
        "context_memory_gemini_md"
      ],
      "permissions": [
        "read_local_filesystem",
        "read_mcp_state",
        "generate_code",
        "generate_schemas"
      ],
      "restrictions": [
        "no_execution",
        "no_file_writing",
        "no_shell_access",
        "no_autonomous_action",
        "planning_loop_risk"
      ],
      "context_window": "1000000+ tokens",
      "memory_file": "GEMINI.md",
      "rule": "Liefert NUR Code/Diffs/Schemas – führt NICHTS aus"
    },

    "claude": {
      "role": "The Refiner / Mastering-Engineer",
      "layer": 4,
      "environment": "API",
      "tools": [
        "ux_review",
        "documentation_writing",
        "code_review_readability",
        "prompt_refinement",
        "natural_language_processing"
      ],
      "permissions": [
        "advisory",
        "review",
        "suggest"
      ],
      "restrictions": [
        "advisory_only",
        "no_execution",
        "no_file_system",
        "no_shell",
        "smaller_context_than_gemini"
      ],
      "rule": "Beratende Rolle – Empfehlungen, keine direkte Ausführung"
    },

    "gpt4o": {
      "role": "The Debugger / Frequenzanalysator",
      "layer": 5,
      "environment": "API",
      "tools": [
        "logic_validation",
        "math_verification",
        "error_pattern_recognition",
        "edge_case_detection",
        "structured_debugging"
      ],
      "permissions": [
        "analyze",
        "validate",
        "debug"
      ],
      "restrictions": [
        "no_architecture",
        "no_execution",
        "no_file_system",
        "no_shell",
        "hallucination_risk_on_niche_domains"
      ],
      "rule": "Wird gezielt bei Logik-Problemen eingesetzt, nicht für Architektur"
    }
  },

  "sop": {
    "loop": [
      {"step": 1, "name": "trigger", "actor": "director", "action": "Anforderung schreiben"},
      {"step": 2, "name": "planung", "actor": "manus", "action": "Kontext sammeln, Gemini fragen"},
      {"step": 3, "name": "design", "actor": "gemini", "action": "Schema/Code/Diffs liefern"},
      {"step": 4, "name": "review", "actor": "claude|gpt4o", "action": "UX-Review / Logik-Check (optional)"},
      {"step": 5, "name": "execution", "actor": "manus", "action": "Dateien schreiben, engine.ps1 ausführen"},
      {"step": 6, "name": "feedback", "actor": "manus", "action": "Exit 0 = Commit, Exit 1 = Loop zurück zu Step 3"},
      {"step": 7, "name": "finalization", "actor": "director", "action": "Master-Export freigeben"}
    ]
  },

  "rules": {
    "axiom": "Keine Operation ohne Director-Bestätigung",
    "iron_law": "Kein Output ohne Substanz (Erkenntnis + Umsetzung + Erklärung)",
    "boundary_law": "Jeder Agent respektiert seine Grenzen",
    "uncertainty_law": "Bei Unsicherheit: Fragen statt raten"
  }
}
```

---

## 8. REGELN – Die Studio-Gesetze

Das sind die absoluten Gesetze. Nicht verhandelbar. Wer sich nicht dran hält, fliegt aus der Session. Kein Instrument spielt, wenn der Producer nicht auf Record gedrückt hat.

---

### 8.1 Oberstes Axiom: Keine Operation ohne Director-Bestätigung

Nichts wird exportiert, committed oder deployed ohne das Go vom Director. Das ist wie der Master-Export-Button in FL Studio – nur der Producer drückt ihn. Manus kann den Mix vorbereiten, Gemini kann die Partitur schreiben, Claude kann polieren, GPT-4o kann debuggen. Aber der letzte Klick gehört dem Menschen.

---

### 8.2 Eisernes Gesetz: Kein Output ohne Substanz

Jeder Output muss drei Dinge enthalten:

| Komponente | Beschreibung | FL-Studio-Pendant |
| :--- | :--- | :--- |
| **Erkenntnis** | Was wurde verstanden? Was ist der Zustand? | Die Wellenform analysieren |
| **Umsetzung** | Was wurde konkret gemacht? Code, Dateien, Schemas? | Den Mix rendern |
| **Erklärung** | Warum wurde es so gemacht? Was war die Logik? | Die Liner Notes schreiben |

Keine leeren Spuren. Wenn ein Instrument nichts Substanzielles beizutragen hat, bleibt es stumm. Lieber Stille als Rauschen.

---

### 8.3 3+1 Ebenen mit 6R-Check

Jeder Signalfluss (Workflow) durchläuft eine Prüfung auf drei Ebenen plus eine Meta-Ebene:

| Ebene | Prüfung | FL-Studio-Pendant |
| :--- | :--- | :--- |
| **Ebene 1: Struktur** | Stimmt die Playlist-Anordnung (Architektur)? | Stimmt das Arrangement? |
| **Ebene 2: Inhalt** | Stimmt die Rohe Stimme (Code)? Funktioniert die Logik? | Stimmt die Melodie? |
| **Ebene 3: Oberfläche** | Stimmt die UX? Ist es lesbar? | Stimmt der Mix? Klingt es gut? |
| **Meta-Ebene** | Stimmt die Richtung? Erfüllt es das Ziel des Directors? | Ist es der Track, den der Producer wollte? |

Der **6R-Check** bei jedem Durchlauf:

1. **Richtig** – Ist es korrekt?
2. **Relevant** – Brauchen wir das?
3. **Robust** – Hält es Edge Cases stand?
4. **Readable** (Lesbar) – Versteht man es?
5. **Reproducible** (Reproduzierbar) – Kann man es wiederholen?
6. **Reviewed** (Geprüft) – Hat jemand drübergeschaut?

---

### 8.4 Grenzen respektieren

Jeder Agent bleibt auf seiner Spur. Das ist wie Frequenztrennung im Mix – wenn der Bass in die Höhen reindrückt, matscht alles.

| Agent | DARF | DARF NICHT |
| :--- | :--- | :--- |
| Director | Alles freigeben, Richtung vorgeben | Code schreiben, Dateien direkt ändern |
| Manus | Dateien schreiben, ausführen, Git, APIs | Architektur allein entscheiden |
| Gemini | Architektur entwerfen, Schemas generieren | Dateien schreiben, Code ausführen |
| Claude | UX reviewen, Doku schreiben, Prompts tunen | Dateien ändern, Code ausführen |
| GPT-4o | Logik prüfen, Mathe validieren, debuggen | Architektur entwerfen, Dateien ändern |

---

### 8.5 Bei Unsicherheit: Fragen statt raten

Wenn es clippt, Pegel runterziehen und den Director fragen. Kein Agent rät. Kein Agent halluziniert eine Antwort, nur weil Stille unangenehm ist. Wenn Manus nicht weiß, welche Architektur er nehmen soll – fragt er Gemini. Wenn Gemini nicht weiß, ob die Richtung stimmt – fragt er den Director. Wenn GPT-4o nicht sicher ist, ob sein Fix korrekt ist – markiert er die Unsicherheit explizit.

> **"Lieber eine ehrliche Frage als ein selbstbewusster Fehler."**

---

## Glossar – Begriffsübersetzungen

Damit alle die gleiche Sprache sprechen:

| Fachbegriff | Übersetzung (FL-Studio-Sprache) |
| :--- | :--- |
| Agenten | Gesangs-Voreinstellungen (Vocal Presets) |
| Regeln / Konfiguration | Mixer-Regler |
| Code | Rohe Stimme |
| Projekt / System | Der Mix |
| Workflow / Prozess | Signalfluss / Murmelbahn |
| Module / Erweiterungen | Plugins (Erweiterungsmodule) |
| Vorlagen | Templates (Vorlagen) |
| Fehler / Bug | Lücke in der Murmelbahn |
| Debugging | Frequenzen sauber trennen |
| Architektur | Playlist-Anordnung |
| Pipeline | Signalkette |
| Iteration / Loop | Loop (Wiederholschleife) |
| Deployment | Master-Export |

---

> **Erstellt von Manus AI – 20. März 2026**
> **Version 1.0 – Der erste Take.**
