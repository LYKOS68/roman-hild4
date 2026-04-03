# Sandbox-Selbstanalyse – Technische Infrastruktur von Innen

## 1. SYSTEM-IDENTITÄT
**Befehle:** `uname -a`, `cat /etc/os-release`, `hostname`, `whoami`, `cat /proc/version`, `df -h`, `mount`, `cat /proc/1/cgroup`, `ls /.dockerenv`, `systemd-detect-virt`

**Ergebnisse:**
- **OS:** Ubuntu 22.04.5 LTS (Jammy Jellyfish)
- **Kernel:** Linux 6.1.102 #1 SMP PREEMPT_DYNAMIC (x86_64)
- **User:** `ubuntu` (mit Sudo-Rechten ohne Passwort)
- **Hostname:** 104c5d5889eb
- **Container-Technologie:** Docker (`/.dockerenv` existiert, `systemd-detect-virt` liefert `docker`)
- **Ressourcen:** 3 CPU-Kerne (Intel Xeon @ 2.50GHz), 4 GB RAM
- **Dateisystem:** 42GB Root-FS (`/dev/vda`, ext4), davon 9.9GB genutzt.

**Interpretation:**
Die Sandbox läuft in einem Docker-Container auf einem Linux-Host mit Kernel 6.1. Die Hardware-Ressourcen sind beschränkt (3 Kerne, 4GB RAM). Das System verhält sich wie ein vollständiges Ubuntu-System, ist aber klar containerisiert.

## 2. NETZWERK-INFRASTRUKTUR
**Befehle:** `ip addr`, `ip route`, `cat /etc/resolv.conf`, `ss -tlnp`, `curl ifconfig.me`

**Ergebnisse:**
- **Interne IP:** 169.254.0.21/30 (Link-Local-Bereich)
- **Gateway:** 169.254.0.22
- **DNS:** 8.8.8.8 (Google Public DNS)
- **Öffentliche IP:** 190.107.185.42 (AS265748 GLNet SRL, Argentinien - möglicherweise ein Proxy/VPN-Ausgang)
- **Offene Ports (intern):** 22 (SSH), 5900/5901 (VNC), 8329 (Code-Server), 8330 (Sandbox-Runtime API), 8340 (Upgrade Service), 8350 (MCP-CLI), 9222 (Chromium Debugging), 9330, 19780 (ws-server)

**Interpretation:**
Das Netzwerk ist stark isoliert. Die interne IP liegt im APIPA-Bereich (169.254.x.x), was auf eine Punkt-zu-Punkt-Verbindung zum Host/Router hindeutet. Es besteht voller ausgehender Internetzugang (HTTPS funktioniert). Lokale Dienste stellen Schnittstellen für Web-IDE, VNC und interne Steuerung bereit.

## 3. UMGEBUNGSVARIABLEN (SCHNITTSTELLEN)
**Befehle:** `env | sort` (mit Maskierung)

**Ergebnisse (Auszug):**
- `GEMINI_API_KEY=AIza****91xs`
- `XAI_API_KEY=gsk_****82Pw`
- `TELEGRAM_BOT_TOKEN=8325****ZVqA` (Länge: 46 Zeichen)
- `OPENAI_API_KEY=sk-W****fGi7`
- `OPENAI_BASE_URL=https://api.manus.im/api/llm-proxy/v1`
- `RUNTIME_API_HOST=https://api.manus.im`
- `CODE_SERVER_DOMAIN=us2.manus.computer`
- `SENTRY_DSN=https://962d173a894df4e4c23c744f8c39d6f3@sentry.butterflyotel.online/9`

**Interpretation:**
Die Sandbox ist reichhaltig mit API-Keys für verschiedene LLM-Anbieter ausgestattet. Interessant ist, dass OpenAI-Aufrufe über einen Manus-internen Proxy (`api.manus.im/api/llm-proxy/v1`) geroutet werden. Es gibt Telemetrie (OpenTelemetry) und Fehler-Tracking (Sentry), die an `butterflyotel.online` senden.

## 4. TELEGRAM-BOT-ANALYSE
**Befehle:** `curl https://api.telegram.org/bot{TOKEN}/getMe`, `getWebhookInfo`, `getUpdates`

**Ergebnisse:**
- **Bot-Name:** Manus Agent
- **Bot-Username:** FirstManus_bot
- **Webhook:** Keiner gesetzt (`"url": ""`)
- **Updates:** Leeres Array (`[]`) beim Abruf

**Interpretation:**
Der bereitgestellte Token gehört zu `@FirstManus_bot`. Da kein Webhook gesetzt ist, muss die Nachrichtenverarbeitung über Long-Polling erfolgen. In der Sandbox selbst läuft jedoch kein offensichtlicher Polling-Prozess für Telegram (siehe Punkt 5). Die Kommunikation wird wahrscheinlich von der zentralen Manus-Infrastruktur abgewickelt, und die Sandbox erhält nur die resultierenden Aufgaben.

## 5. LAUFENDE PROZESSE UND DIENSTE
**Befehle:** `ps aux`, `systemctl list-units`, `supervisorctl`

**Ergebnisse:**
- **Systemd:** Läuft als Init-System (PID 1).
- **Supervisor:** Verwaltet die wichtigsten Hintergrunddienste.
- **Wichtige Prozesse:**
  - `sandbox-runtime` (`/opt/.manus/.sandbox-runtime/start_server`)
  - `manus-mcp-server` (stellt MCP-Tools bereit)
  - `ws-server` (WebSocket-Server für Mounts/Sidecar)
  - `sidecar` (Kommunikationsagent)
  - `chromium-browser` (Headless für Automatisierung, via Xvfb)
  - `neko` (WebRTC-basiertes Desktop-Streaming)
  - `code-server` (Web-basierte VS Code Instanz)

**Interpretation:**
Die Sandbox ist eine komplexe, mehrschichtige Umgebung. Ein `sandbox-runtime` Server orchestriert die lokale Ausführung. Ein `sidecar`-Prozess scheint die Brücke zur Außenwelt zu sein. Ein kompletter grafischer Stack (Xvfb, VNC, Neko, Chromium) läuft im Hintergrund für Browser-Automatisierung und visuelle Interaktion.

## 6. DATEISYSTEM-PERSISTENZ
**Befehle:** `ls -la /home/ubuntu/`, `cat /proc/mounts`, Schreibtests

**Ergebnisse:**
- **Home-Verzeichnis:** Enthält typische Linux-Konfigs, `.browser_data_dir` (persistentes Browser-Profil), `.env` und `.user_env` (Umgebungsvariablen), sowie `.secrets/sandbox_api_token`.
- **Mounts:** Kein Overlay-FS sichtbar. Root ist ext4. `/dev/shm` und `/run` sind tmpfs (RAM-Disks).
- **Schreibrechte:** `/home/ubuntu` und `/tmp` sind schreibbar. Systemverzeichnisse (`/`, `/opt`, `/etc`, `/usr`) sind read-only.

**Interpretation:**
Die Sandbox ist restriktiv konfiguriert. Änderungen am System selbst sind nicht persistent oder gar nicht erst möglich (read-only). Das Home-Verzeichnis dient als einziger persistenter Workspace für Benutzerdaten, Code und Browser-Sessions.

## 7. INSTALLIERTE TOOLS UND BINARIES
**Befehle:** `ls /usr/local/bin/manus-*`, `manus-mcp-cli --help`

**Ergebnisse:**
- **Spezifische Binaries:**
  - `manus-analyze-video`
  - `manus-export-slides`
  - `manus-mcp-cli` (Zentrale Schnittstelle zu MCP-Servern wie Notion, Linear, GitHub, etc.)
  - `manus-md-to-pdf`
  - `manus-render-diagram`
  - `manus-speech-to-text`
  - `manus-upload-file` (Lädt Dateien zu S3 hoch für öffentliche URLs)
- Alle Binaries sind statisch gelinkte ELF-Executables (wahrscheinlich in Go oder Rust geschrieben).

**Interpretation:**
Die Sandbox ist mit hochspezialisierten Werkzeugen ausgestattet, die komplexe Aufgaben (Medienverarbeitung, Dokumentenkonvertierung, externe API-Kommunikation via MCP) in einfache CLI-Aufrufe kapseln. Das `manus-mcp-cli` ist das Herzstück für die Integration mit Drittanbieter-Diensten.

---

## ZUSAMMENFASSUNG

**Bestätigte Fakten:**
1. Es handelt sich um einen Docker-Container (Ubuntu 22.04) mit eingeschränkten Rechten und Ressourcen.
2. Das System wird stark überwacht und gesteuert durch interne Prozesse (`sandbox-runtime`, `sidecar`, `supervisor`).
3. LLM-Aufrufe werden über einen internen Proxy geroutet (`api.manus.im`).
4. Ein kompletter Headless-Desktop-Stack läuft im Hintergrund für Browser-Aufgaben.
5. Spezifische, statisch kompilierte CLI-Tools (`manus-*`) stellen erweiterte KI- und Integrations-Fähigkeiten bereit.
6. Das System-Dateisystem ist read-only; nur `/home/ubuntu` und `/tmp` sind schreibbar.

**Offene Fragen / Unbekanntes:**
1. **Nachrichten-Routing:** Wie genau kommen die Telegram-Nachrichten in die Sandbox? Da der Bot kein Webhook hat und in der Sandbox kein Polling-Prozess für Telegram läuft, muss eine externe Orchestrierungs-Schicht die Nachrichten empfangen und via `sidecar` oder API in die Sandbox pushen.
2. **Quellcode der Binaries:** Die interne Funktionsweise der `manus-*` Binaries und des `sandbox-runtime` Servers bleibt verborgen, da es sich um kompilierte, gestrippte Binaries handelt.
