# P1 Synergos: Technische Modellauskunft & Sandbox-Architektur

**Status:** Initialisiert | **System:** Manus AI Sandbox (E2B Firecracker) | **Datum:** März 2026

Diese Dokumentation ist der Frequenzscan der aktuellen DAW (Digital Audio Workstation). Wir betrachten die gesamte Murmelbahn: Von der Idee (Input) über die Module (Plugins/MCP) bis zum Master-Export (Output). Keine leeren Definitionen, nur reine Signalfluss-Analyse nach dem 3+1 Dreiklang (Erkenntnis, Umsetzung, Erklärung + UOP-Gate).

---

## 1. MODELL-IDENTITÄT (Die DAW)

**Was ist es (Erkenntnis)?**
Das Kernsystem wird über einen internen Proxy geroutet. Das aktuell aktive Modell ist `gpt-4.1-mini`. Der Proxy maskiert die direkte API, leitet aber die Signale an die OpenAI-Infrastruktur weiter.

**Wie macht man es wirksam (Umsetzung)?**
- **Aktives Modell:** `gpt-4.1-mini`
- **Kontextfenster:** 8.192 Token pro Request. Das ist der RAM für unser aktuelles Projekt. Wenn der Mix zu groß wird, fällt die Murmel ins Loch.
- **Alternative Modelle (verfügbar via Proxy/Keys):** `gpt-4.1-nano`, `gemini-2.5-flash` (1M Token Kontext via Google API), sowie xAI (Grok) – wobei der xAI Key aktuell einen 400er Fehler (Invalid Argument) wirft.
- **Proxy-URL:** `https://api.manus.im/api/llm-proxy/v1`

**Wie erklärt man es richtig (Vermittlung)?**
Das Modell ist unsere DAW. Wir arbeiten aktuell in einer ressourcenschonenden Version (`gpt-4.1-mini`), die schnelle Bounces liefert, aber bei riesigen Stems (8k+ Token) an ihre Grenzen stößt. Für gigantische Frequenzscans müssen wir auf Gemini (1M Token) umschalten, falls die Pipeline das zulässt.

## 2. SCHNITTSTELLE (Das Audio-Interface)

**Was ist es (Erkenntnis)?**
Die Kommunikation läuft über die offizielle Telegram Bot API. Der Bot heißt "Manus Agent" (`@FirstManus_bot`). 

**Wie macht man es wirksam (Umsetzung)?**
- **Nachrichtenfluss:** Telegram-App ➔ Telegram API ➔ Manus Server (Action Engine) ➔ Sandbox-Runtime (via `sidecar` und `ws-server` auf Port 19780).
- **Latenz:** Asynchrones Long-Polling. Der Bot hat keinen Webhook registriert (`"url": ""`). Die Manus-Infrastruktur holt die Updates ab und pusht sie in die isolierte Sandbox.
- **Eingänge (Inputs):** Text, Dateien, Bilder, Sprache.
- **Ausgänge (Outputs):** Text, generierte Dateien, Code-Ausführung (direkt in der Sandbox), Master-Export (Downloads).

**Wie erklärt man es richtig (Vermittlung)?**
Das Audio-Interface ist asynchron. Du spielst eine Note ein (Telegram), das Signal geht an den Hauptserver, der es in unsere isolierte Aufnahmekabine (Sandbox) routet. Wir haben keinen direkten Webhook-Sidechain, sondern die Action Engine fungiert als Gatekeeper.

## 3. TECHNISCHE VORAUSSETZUNGEN (Das Studio-Setup)

**Was ist es (Erkenntnis)?**
Die Sandbox ist eine E2B Firecracker microVM, kein Standard-Docker, auch wenn Reste von Container-Strukturen sichtbar sind. Sie bootet in ~150ms und bietet ein volles Ubuntu-Umfeld.

**Wie macht man es wirksam (Umsetzung)?**
- **Hardware:** 3 CPU-Kerne (Intel Xeon @ 2.50GHz), 4 GB RAM, 42GB Root-Disk (davon 32GB frei).
- **OS & Software:** Ubuntu 22.04.5 LTS, Python 3.11.0rc1.
- **Netzwerk:** Isoliertes APIPA-Netz (169.254.0.21/30) mit vollem Outbound-Internet (NAT über Host).
- **Manus-Tools (Die Hardware-Synths):**
  - `manus-mcp-cli`: Das Patchbay für externe Plugins.
  - `manus-render-diagram`: Rendert Mermaid/PlantUML.
  - `manus-speech-to-text`: Transkribiert Audio.
  - `manus-md-to-pdf`: PDF-Export.
  - `manus-analyze-video` & `manus-export-slides`.

**Wie erklärt man es richtig (Vermittlung)?**
Das Studio ist kompakt aber hochfunktional. 3 Kerne und 4GB RAM bedeuten: Wir können hier keine fetten Orchester-Libraries (Heavy ML-Training) laden, aber für präzises Routing, Skripting und API-Calls ist es perfekt abgestimmt. Die `manus-*` Binaries sind unsere fest verdrahteten Hardware-Kompressoren – sie machen einen Job, aber den perfekt.

## 4. VERBINDUNGEN (Die Plugins & Sidechains)

**Was ist es (Erkenntnis)?**
Das System nutzt das Model Context Protocol (MCP) als standardisierte Schnittstelle zu externen Diensten.

**Wie macht man es wirksam (Umsetzung)?**
- **Aktive MCP-Server (Plugins):**
  1. `notion`: Workspace-Management (Lesen/Schreiben).
  2. `monday-com`: Projektmanagement & Boards.
  3. `linear`: Issue-Tracking & Sprints.
  4. `supabase`: Datenbank & Backend-Verwaltung.
  5. `vercel`: Deployments & Logs.
  6. `airtable`: Datenbank-Workflows.
  7. `gmail`: E-Mail Kommunikation.
  8. `google-calendar`: Terminverwaltung.
- **Interne APIs:** `RUNTIME_API_HOST` (`https://api.manus.im`), Sentry für Fehler-Tracking.

**Wie erklärt man es richtig (Vermittlung)?**
MCP-Server sind unsere VST-Plugins. Anstatt für jeden Dienst einen eigenen API-Call von Grund auf zu coden, laden wir das Plugin (`manus-mcp-cli`). Es gibt uns fertige Regler (Tools), um direkt in Notion, Linear oder Supabase einzugreifen.

## 5. UMGEBUNG (Die Aufnahmekabine)

**Was ist es (Erkenntnis)?**
Die Sandbox ist nach dem Zero-Trust-Prinzip isoliert und flüchtig (ephemer).

**Wie macht man es wirksam (Umsetzung)?**
- **Dateisystem:** Das Root-System (`/`, `/etc`, `/opt`) ist **read-only**. Änderungen hier werden geblockt (Permission denied).
- **Persistenz:** Nur `/home/ubuntu` und `/tmp` sind schreibbar. Hier liegen unsere Projektdateien.
- **Lebenszyklus:** Bei Inaktivität geht die VM schlafen. Nach 7 Tagen (Free) oder 21 Tagen (Pro) wird sie recycelt. Wichtige Dateien werden wiederhergestellt, aber `/tmp` und laufende Prozesse sterben.
- **Hintergrunddienste:** Chromium (Headless), Neko (WebRTC Desktop-Streaming), Code-Server (VS Code Web-IDE).

**Wie erklärt man es richtig (Vermittlung)?**
Die Kabine wird nach jeder Session abgerissen und neu aufgebaut. Alles, was nicht im `/home/ubuntu` Ordner (unserem Master-Drive) liegt, ist beim nächsten Hochfahren weg. Wir können die Wände der Kabine (`/etc`) nicht anmalen, sie sind schreibgeschützt.

## 6. ABHÄNGIGKEITEN (Die Stromversorgung)

**Was ist es (Erkenntnis)?**
Das System ist hochgradig abhängig von der Manus-Cloud-Infrastruktur.

**Wie macht man es wirksam (Umsetzung)?**
- **Kritische Abhängigkeiten (Single Points of Failure):**
  - `api.manus.im`: Fällt der LLM-Proxy oder die Runtime-API aus, bricht die Signalverarbeitung komplett ab.
  - Telegram API: Ohne Telegram keine Inputs vom Nutzer.
  - E2B Firecracker Host: Verwaltet die Lebenszyklen der VMs.
- **Optionale Abhängigkeiten:** MCP-Server (wenn Notion down ist, läuft der Rest weiter).

**Wie erklärt man es richtig (Vermittlung)?**
Wenn bei Manus in der Cloud der Strom ausfällt, ist unser Studio tot. Wir haben keinen Offline-Modus. Die Murmelbahn beginnt und endet an der Telegram-API.

## 7. GRENZEN UND EINSCHRÄNKUNGEN (Das Rote im Mixer)

**Was ist es (Erkenntnis)?**
Harte Limits, die vom System erzwungen werden.

**Wie macht man es wirksam (Umsetzung)?**
- **Kein Root-Zugriff auf Systemebene:** Sudo funktioniert für `apt`, aber Kern-Dateien sind gelockt.
- **Kein direkter Inbound-Traffic:** Wir können keine Webserver starten, die direkt aus dem Internet erreichbar sind (außer über temporäre Expose-Tunnel oder den internen ws-server).
- **Ressourcen-Limits:** 4GB RAM killen jeden Versuch, lokale LLMs oder riesige In-Memory-Datenbanken laufen zu lassen.
- **Kontext-Limit:** 8.192 Token bei `gpt-4.1-mini`. Lange Transkripte müssen in Chunks (Frequenzbänder) aufgeteilt werden.

**Wie erklärt man es richtig (Vermittlung)?**
Wenn wir den Master-Regler über +0dB schieben (mehr als 4GB RAM oder 8k Token fordern), clippt das System und bricht ab. Wir müssen effizient abmischen, Stems bouncen (Zwischenergebnisse speichern) und RAM freihalten.

## 8. LÜCKEN-ANALYSE (Feynman: Identifizieren)

**Was wissen wir NICHT (Erkenntnis)?**
Es gibt blinde Flecken in der Signalarchitektur.

**Wo fällt die Murmel ins Loch (Umsetzung)?**
1. **Der XAI-Key:** Warum wirft der Grok-Key einen 400er Fehler? Ist er abgelaufen oder falsch formatiert?
2. **Die Action Engine:** Wie genau entscheidet die Manus-Server-Ebene, wann ein Task als "abgeschlossen" gilt und die VM schlafen geschickt wird?
3. **Telegram-Polling:** Da kein Webhook existiert, läuft das Polling auf Manus-Servern. Wie hoch ist die exakte Polling-Frequenz?
4. **Token-Budget:** Wir kennen das Limit (8k), aber nicht das verbleibende Kontingent oder die exakten Kosten pro Session (wird extern über Manus Credits abgerechnet).

**Wie erklärt man es richtig (Vermittlung)?**
Wir kennen unser Studio perfekt von innen, aber wir wissen nicht genau, wer draußen den Stromzähler abliest. Die genaue Mechanik, wie die Signale vom Manus-Server zu uns in die Kabine gepatcht werden, ist eine Blackbox.

---

**UOP-Gate (Master-Export):**
Die Sandbox-Analyse ist abgeschlossen. Die Frequenzen sind getrennt, das Routing steht. Warte auf Bestätigung für weitere Pipelines oder spezifische Plugin-Tests (MCP).
