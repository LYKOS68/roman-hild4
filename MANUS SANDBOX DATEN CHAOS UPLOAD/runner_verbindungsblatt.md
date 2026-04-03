# RUNNER VERBINDUNGSBLATT – LYKOS68/roman-hild4

## 1. REPO-IDENTITÄT

| Feld | Wert |
|---|---|
| Repo | LYKOS68/roman-hild4 |
| Repo ID | 1200574044 |
| Node ID | R_kgDOR49OXA |
| URL | https://github.com/LYKOS68/roman-hild4 |
| Sichtbarkeit | public |
| Default Branch | main |

## 2. RUNNER-IDENTITÄT

| Feld | Wert |
|---|---|
| Name | manus-sandbox |
| Agent ID | 2 |
| Pool | Default (ID: 1) |
| Labels | manus, linux, sandbox, self-hosted, Linux, X64 |
| Arbeitsverzeichnis | /home/ubuntu/actions-runner/_work |
| Version | 2.333.1 |

## 3. VERBINDUNGSENDPUNKTE

| Dienst | URL |
|---|---|
| Pipeline Server | https://pipelinesghubeus7.actions.githubusercontent.com/iRmfjmBzgBI00lATT1gKjM5wwKL8jmaroCfNBt74zMaSuPIDZv/ |
| Broker (V2) | https://broker.actions.githubusercontent.com/ |
| Token-Auth | https://tokenghub.actions.githubusercontent.com/_apis/oauth2/token/37e3d41f-d209-4fb2-904f-2f658b481813 |
| OAuth Client ID | 6c6d44dc-ab49-4c4e-bacf-611a26a683c8 |

## 4. API-ENDPUNKTE (GitHub REST API v3)

Alle Endpunkte erfordern Authentication (Personal Access Token mit `repo` Scope) außer die als "public" markierten.

### Repo-Basis (public)
```
GET https://api.github.com/repos/LYKOS68/roman-hild4
```

### Actions Runners (auth required)
```
GET  https://api.github.com/repos/LYKOS68/roman-hild4/actions/runners
     → Liste aller registrierten Runner
GET  https://api.github.com/repos/LYKOS68/roman-hild4/actions/runners/{runner_id}
     → Details eines Runners (runner_id = 2 für manus-sandbox)
DELETE https://api.github.com/repos/LYKOS68/roman-hild4/actions/runners/{runner_id}
     → Runner entfernen
```

### Actions Workflows (public für öffentliche Repos)
```
GET  https://api.github.com/repos/LYKOS68/roman-hild4/actions/workflows
     → Liste aller Workflows
GET  https://api.github.com/repos/LYKOS68/roman-hild4/actions/runs
     → Liste aller Workflow-Runs
```

### Repository Dispatch (auth required) – FERNSTEUERUNG
```
POST https://api.github.com/repos/LYKOS68/roman-hild4/dispatches
Header: Authorization: Bearer <PAT>
Body: {"event_type": "trigger-name", "client_payload": {"key": "value"}}
```
→ Löst einen `repository_dispatch` Event aus. Damit kann JEDES System (Telegram Bot, Manus, Gemini, externes Script) einen Workflow triggern.

### Webhooks (auth required)
```
GET    https://api.github.com/repos/LYKOS68/roman-hild4/hooks
POST   https://api.github.com/repos/LYKOS68/roman-hild4/hooks
       Body: {"config": {"url": "https://dein-endpoint.com/webhook", "content_type": "json"}, "events": ["push", "workflow_run"]}
DELETE https://api.github.com/repos/LYKOS68/roman-hild4/hooks/{hook_id}
```
→ Webhooks senden HTTP POST an eine URL deiner Wahl wenn Events passieren (Push, PR, Workflow-Run, etc.)

## 5. WEBHOOK-SETUP (Schritt für Schritt)

Webhooks brauchen einen öffentlich erreichbaren HTTP-Endpunkt. Optionen:

| Option | Beschreibung |
|---|---|
| Supabase Edge Function | Serverless Funktion die Webhook-Payloads empfängt und verarbeitet |
| Telegram Bot API | Webhook → Supabase → Telegram sendMessage |
| Manus Scheduled Task | Polling statt Webhook (kein öffentlicher Endpunkt nötig) |
| ngrok / smee.io | Temporärer Tunnel für Entwicklung |

## 6. WORKFLOW-TRIGGER (wie man den Runner ansteuert)

### Via Push (automatisch)
```yaml
# .github/workflows/deploy.yml
on: push
jobs:
  deploy:
    runs-on: [self-hosted, manus]
    steps:
      - uses: actions/checkout@v4
      - run: echo "Läuft auf manus-sandbox"
```

### Via Repository Dispatch (ferngesteuert)
```yaml
on:
  repository_dispatch:
    types: [sync-state, deploy, validate]
jobs:
  handle:
    runs-on: [self-hosted, manus]
    steps:
      - run: echo "Event: ${{ github.event.action }}"
      - run: echo "Payload: ${{ toJSON(github.event.client_payload) }}"
```
Trigger per curl:
```bash
curl -X POST \
  -H "Authorization: Bearer <PAT>" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/LYKOS68/roman-hild4/dispatches \
  -d '{"event_type":"sync-state","client_payload":{"action":"validate"}}'
```

### Via Cron (zeitgesteuert)
```yaml
on:
  schedule:
    - cron: '0 */6 * * *'  # alle 6 Stunden
```

### Via Manual (GitHub UI)
```yaml
on:
  workflow_dispatch:
    inputs:
      action:
        description: 'Was soll passieren?'
        required: true
        type: choice
        options: [validate, deploy, sync]
```

## 7. STEUERUNGSBEFEHLE (Sandbox-lokal)

```bash
# Status
tail -5 /home/ubuntu/runner.log

# Prozess prüfen
ps aux | grep Runner.Listener | grep -v grep

# Stoppen
pkill -f "Runner.Listener"

# Neu starten
pkill -f "Runner.Listener" 2>/dev/null; sleep 2; cd /home/ubuntu/actions-runner && nohup ./run.sh > /home/ubuntu/runner.log 2>&1 &

# Log live
tail -f /home/ubuntu/runner.log

# Deregistrieren (braucht neuen Token)
cd /home/ubuntu/actions-runner && ./config.sh remove --token <TOKEN>

# Schnelldiagnose
echo "=== PROZESS ===" && ps aux | grep Runner.Listener | grep -v grep && echo "=== LOG ===" && tail -3 /home/ubuntu/runner.log && echo "=== UPTIME ===" && uptime
```
