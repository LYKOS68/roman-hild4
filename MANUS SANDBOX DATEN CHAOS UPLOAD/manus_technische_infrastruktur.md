# Technische Infrastruktur der Manus-Plattform (manus.im)

Dieser Bericht fasst offizielle, verifizierbare technische Informationen zur KI-Plattform Manus in den Bereichen Telegram-Anbindung, Sandbox-Infrastruktur sowie Zugriff und Bearbeitung zusammen.

## 1. Telegram-Anbindung

Die Telegram-Integration von Manus dient als vollwertiges Execution Layer und nicht nur als einfacher Chatbot. Manus nutzt für die Kommunikation die offizielle Telegram Bot API. Benutzer verbinden ihren Manus-Account mit Telegram, indem sie im Manus-Workspace einen QR-Code scannen oder einen Link anklicken, der sie direkt zum offiziellen Bot führt [1].

Es handelt sich um einen Standard-Telegram-Bot, der über die Telegram Bot API kommuniziert und als privater Chat-Partner für den Nutzer agiert. Wenn ein Nutzer eine Nachricht an den Manus-Bot in Telegram sendet, hat der Bot ausschließlich Zugriff auf diesen privaten Chat. Er kann keine anderen Chats, Gruppen oder Kontakte des Nutzers lesen [2].

Die Eingaben, welche Text, Sprache, Bilder oder Dateien umfassen können, werden von Telegram an die Manus-Server weitergeleitet. Dort analysiert die Manus Action Engine die Anfrage und führt sie in einer sicheren, isolierten Cloud-VM aus [2]. Das Ergebnis wird anschließend über die Telegram Bot API zurück in den Chat gesendet. Die Einrichtung und Nutzung ist im offiziellen Manus Help Center detailliert dokumentiert [1].

## 2. Sandbox-Infrastruktur

Die Sandbox ist das Kernstück der Handlungsfähigkeit von Manus und wird offiziell als realer Cloud-Computer beschrieben. Manus nutzt für seine Sandbox-Infrastruktur die Plattform E2B, welche auf Firecracker microVMs basiert. Diese ursprünglich von AWS entwickelten, leichtgewichtigen und ephemeren virtuellen Maschinen bieten eine hardwarenahe Isolierung [3].

Während der Entwicklungsphase testete das Manus-Team Docker-Container, verwarf diese jedoch. Docker bot nicht die volle Funktionalität eines Betriebssystems, beispielsweise für die Installation bestimmter Pakete, und war mit 10 bis 20 Sekunden Startzeit zu langsam. Die Firecracker microVMs von E2B starten hingegen in etwa 150 Millisekunden und bieten ein vollständiges Ubuntu-Linux-Umfeld [3].

Das Dateisystem in der Sandbox ist persistent. Dateien, die der Nutzer hochlädt, sowie Artefakte, die Manus generiert, bleiben erhalten [4]. Bei Inaktivität geht die Sandbox in einen Sleep-Modus über. Wenn der Nutzer die Aufgabe fortsetzt, wacht sie auf, wobei der Zustand erhalten bleibt.

Wenn eine Sandbox über einen längeren Zeitraum inaktiv ist, wird sie recycelt. Diese Frist beträgt 7 Tage für Free-Nutzer und 21 Tage für Pro-Nutzer. Wenn die Aufgabe danach wieder geöffnet wird, erstellt Manus eine neue Sandbox und stellt wichtige Dateien wie hochgeladene Anhänge und Manus-Artefakte automatisch wieder her. Temporäre Dateien und Zwischencode gehen dabei jedoch verloren [4].

## 3. Zugriff und Bearbeitung

Die Manus-Sandbox ist nach dem Zero-Trust-Prinzip isoliert [4]. Der Zugriff von außen ist stark reglementiert und erfolgt über definierte Schnittstellen. Es gibt keinen offiziellen, direkten SSH-Zugriff oder eine direkte API-Schnittstelle in die laufende Sandbox-VM für Endnutzer. Die Sandbox ist eine geschlossene Umgebung, die nur durch den Manus-Agenten oder die offiziellen Plattform-Schnittstellen gesteuert wird [4].

| Zugriffsmethode | Beschreibung |
| :--- | :--- |
| **Web-Interface & Telegram** | Nutzer können Dateien direkt über den Chat im Web-Interface oder in Telegram hochladen. Generierte Artefakte können über das Web-Interface heruntergeladen werden, oder Nutzer weisen Manus an, Dateien zu zippen und einen Download-Link bereitzustellen [4]. |
| **Manus API** | Entwickler können über den `/v1/files` Endpunkt der Manus REST API Dateien hochladen. Die API generiert eine presigned S3-URL, über die die Datei per PUT-Request hochgeladen wird. Anschließend kann sie an einen Task angehängt werden [5]. |
| **Manus Desktop App** | Mit der Desktop-App und dem My Computer Feature kann Manus direkt auf lokale Dateien des Nutzers zugreifen und Workflows lokal ausführen [6]. |
| **MCP-Server** | Das Model Context Protocol (MCP) spielt eine zentrale Rolle bei der Integration externer Daten. MCP-Connectors ermöglichen es dem Manus-Agenten, aus der Sandbox heraus authentifiziert auf externe Dateien und Systeme wie Google Drive oder Notion zuzugreifen, ohne dass die Dateien manuell in die Sandbox hochgeladen werden müssen [7]. Nutzer können auch eigene Custom MCP-Server hosten [8]. |

---

### Referenzen

[1] Manus Help Center: [How do I set up and use Manus Agents in Telegram?](http://help.manus.im/en/articles/14033617-how-do-i-set-up-and-use-manus-agents-in-telegram)
[2] Manus Help Center: [Is my data safe when using Manus Agents in Telegram?](https://help.manus.im/en/articles/14033996-is-my-data-safe-when-using-manus-agents-in-telegram)
[3] E2B Blog: [How Manus Uses E2B to Provide Agents With Virtual Computers](https://e2b.dev/blog/how-manus-uses-e2b-to-provide-agents-with-virtual-computers)
[4] Manus Blog: [Understanding Manus sandbox](https://manus.im/blog/manus-sandbox)
[5] Manus API Docs: [Create File](https://open.manus.im/docs/api-reference/create-file)
[6] Manus Help Center: [How to download the Manus Desktop App?](http://help.manus.im/en/articles/14089011-how-to-download-the-manus-desktop-app)
[7] Manus Docs: [MCP Connectors](https://manus.im/docs/integrations/mcp-connectors)
[8] Manus Docs: [Custom MCP Servers](https://manus.im/docs/integrations/custom-mcp)
