# Analyse: Brücke zwischen Gemini CLI (Lokal) und Manus Sandbox

Diese Dokumentation bewertet alle technisch machbaren Wege, um von einem lokalen Windows-Rechner (via Gemini CLI) direkt auf die laufende Manus Sandbox zuzugreifen. Ziel ist es, Dateien bidirektional zu synchronisieren und Befehle auszuführen.

---

## 1. MANUS REST API (/v1/files)

Die Manus Open API bietet standardisierte Endpunkte für die Interaktion mit dem System [1].

*   **Machbarkeit:** Teilweise (Nur Upload und Listen möglich, kein Download der Inhalte)
*   **API-Key Beschaffung:** Der API-Key wird in der Manus Web-App unter *Settings → Integrations → API* generiert [2]. Der in der Sandbox gefundene `sandbox_api_token` ist für interne Proxys gedacht und funktioniert **nicht** direkt mit der öffentlichen Open API.
*   **Upload-Workflow (Presigned S3):** 
    1. `POST /v1/files` aufrufen mit dem Dateinamen.
    2. Die API antwortet mit einer `upload_url` (Presigned S3 URL) und einer `file_id`.
    3. Die Datei via `PUT` Request direkt an die `upload_url` senden [3].
*   **Dateien lesen/herunterladen:** Die API bietet Endpunkte wie `GET /v1/files/{file_id}` und `GET /v1/files` an. Diese liefern jedoch nur **Metadaten** (Status, ID, Erstelldatum) zurück, keine Download-Links oder Dateiinhalte [4]. Ein direkter Download von Dateien aus der Sandbox auf den lokalen Rechner ist über die öffentliche API aktuell nicht dokumentiert.
*   **Befehlsausführung:** Befehle können nicht direkt in der Sandbox ausgeführt werden. Man kann lediglich über `POST /v1/tasks` neue Agenten-Tasks starten, die dann in ihrer eigenen Sandbox laufen [5].

**Einschränkungen:** Keine direkte Shell-Ausführung, kein Herunterladen von Dateiinhalten über die API.

---

## 2. MANUS DESKTOP APP ("My Computer" Feature)

Manus hat kürzlich die Desktop-Anwendung mit dem "My Computer"-Feature veröffentlicht [6].

*   **Machbarkeit:** Ja (Sehr empfehlenswert für diesen Use-Case)
*   **Wie es funktioniert:** Die Desktop-App holt den Manus-Agenten aus der Cloud auf die lokale Maschine. Manus kann dadurch direkt lokale Terminal-Befehle (CLI) auf dem Windows-Rechner ausführen [7].
*   **Bidirektionalität:** Ja. Wenn die Desktop-App installiert ist, kann Manus Dateien auf dem lokalen Rechner lesen, bearbeiten und verschieben. Es dient als perfekte Brücke: Der Agent kann in der Cloud arbeiten und Ergebnisse direkt lokal abspeichern oder lokale Dateien in seine Workflows integrieren [7].
*   **Was wird benötigt:** Download der Manus Desktop App für Windows und Autorisierung der gewünschten lokalen Ordner.

**Einschränkungen:** Jeder Terminal-Befehl auf dem lokalen Rechner erfordert (je nach Einstellung) eine explizite Bestätigung durch den Nutzer ("Allow Once" oder "Always Allow") [7].

---

## 3. MCP-SERVER / CUSTOM MCP

Das Model Context Protocol (MCP) wird sowohl von Manus als auch von Gemini CLI nativ unterstützt.

*   **Machbarkeit:** Ja (Als Vermittler)
*   **Architektur-Idee:** Man kann einen Custom MCP-Server lokal (z.B. in Node.js oder Python) aufsetzen [8]. 
    *   **Gemini CLI Integration:** Gemini CLI unterstützt MCP-Server nativ. In der Datei `~/.gemini/settings.json` kann der lokale MCP-Server registriert werden (z.B. via `stdio` oder `sse`) [9].
    *   **Manus Integration:** Der gleiche Server kann als "Custom MCP" in Manus registriert werden [8].
*   **Funktionsweise:** Der MCP-Server definiert *Tools* (z.B. `read_local_file`, `write_local_file`, `execute_sandbox_task`). Gemini CLI kann über diesen Server lokale Dateien verwalten und gleichzeitig über die Manus API Tasks in der Cloud triggern.

**Beispiel Gemini CLI `settings.json` Konfiguration [10]:**
```json
{
  "mcpServers": {
    "manus-bridge": {
      "command": "node",
      "args": ["C:/pfad/zum/mcp-server/index.js"],
      "env": {
        "MANUS_API_KEY": "sk-..."
      }
    }
  }
}
```

**Einschränkungen:** Erfordert eigenen Entwicklungsaufwand für den MCP-Server. Es ist keine "Out-of-the-box" direkte Verbindung in die *laufende* Sandbox, sondern eine Steuerung über die API.

---

## 4. CODE-SERVER & DIREKTE METHODEN (SSH / WebSocket)

Die Manus Sandbox betreibt intern verschiedene Dienste, die theoretisch für direkte Verbindungen nützlich wären.

*   **Code-Server (Port 8329):** Läuft in der Sandbox und erfordert ein Passwort (zu finden in `~/.config/code-server/config.yaml`). **Aber:** Der Port ist standardmäßig nicht öffentlich aus dem Internet erreichbar. Die Subdomains (wie `us2.manus.computer`) sind durch strikte Authentifizierung und Firewalls geschützt.
*   **SSH (Port 22):** Der SSH-Dienst läuft in der Sandbox. Die Sandbox hat jedoch nur eine interne Link-Local IP (`169.254.0.21`) und keine öffentliche IP-Adresse. Ein direkter SSH-Tunnel von außen ist nicht möglich, da das NAT/Routing von Manus dies blockiert.
*   **Interne API (Port 8330/9330):** Es gibt interne APIs für File-Uploads und Terminal-Zugriff. Diese erfordern jedoch spezifische Authentifizierungs-Token (TURN-Token, Session-Cookies), die von außen nicht ohne weiteres simuliert werden können. Der gefundene `sandbox_api_token` liefert bei direkten Aufrufen "Unauthorized".

**Machbarkeit Direkte Methoden:** Nein. Die Sandbox ist netzwerktechnisch stark isoliert.

---

## Fazit & Empfehlung

Für den Nutzer gibt es zwei sinnvolle Ansätze:

1.  **Der einfache Weg (Empfohlen):** Nutzung der **Manus Desktop App ("My Computer")**. Dies löst das Problem nativ. Manus bekommt Zugriff auf das lokale Windows-Dateisystem und kann als Brücke agieren.
2.  **Der Entwickler-Weg (Für Gemini CLI):** Einen lokalen **Custom MCP-Server** programmieren. Dieser Server bindet sich in die Gemini CLI ein (für lokale Dateioperationen) und nutzt gleichzeitig die Manus REST API, um Tasks an Manus zu delegieren.

---
**Referenzen:**
[1] Manus API Overview: https://open.manus.im/docs
[2] Manus API Quickstart: https://open.manus.im/docs/quickstart
[3] Create File API: https://open.manus.im/docs/api-reference/create-file
[4] Get File API: https://open.manus.im/docs/api-reference/get-file
[5] Create Task API: https://open.manus.im/docs/api-reference/create-task
[6] Manus Desktop App: https://manus.im/desktop
[7] Introducing My Computer: https://manus.im/blog/manus-my-computer-desktop
[8] Custom MCP Servers: https://manus.im/docs/integrations/custom-mcp
[9] Gemini CLI MCP Integration: https://github.com/google-gemini/gemini-cli
[10] MCP Servers with Gemini CLI: https://geminicli.com/docs/tools/mcp-server/
