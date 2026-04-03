#!/usr/bin/env bash
# =============================================================================
# DATEI: webhook_setup.sh
# ZWECK: Webhooks für das GitHub-Repo LYKOS68/roman-hild4 verwalten
#        - Webhook registrieren (mit URL als Parameter)
#        - Bestehende Webhooks auflisten
#        - Webhook löschen (--delete <id>)
#        - Webhook testen / ping senden (--ping <id>)
# VORAUSSETZUNG: gh CLI authentifiziert als LYKOS68 (gh auth login)
# VERWENDUNG:
#   ./webhook_setup.sh <webhook_url>          # Webhook registrieren
#   ./webhook_setup.sh --list                 # Alle Webhooks auflisten
#   ./webhook_setup.sh --delete <hook_id>     # Webhook löschen
#   ./webhook_setup.sh --ping <hook_id>       # Webhook testen (ping)
#   ./webhook_setup.sh --help                 # Hilfe anzeigen
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# KONFIGURATION
# ---------------------------------------------------------------------------
REPO="LYKOS68/roman-hild4"
REPO_ID="1200574044"
API_BASE="https://api.github.com"

# Farben für die Ausgabe (werden deaktiviert wenn kein Terminal)
if [ -t 1 ]; then
  C_RESET="\033[0m"
  C_GREEN="\033[0;32m"
  C_YELLOW="\033[0;33m"
  C_RED="\033[0;31m"
  C_CYAN="\033[0;36m"
  C_BOLD="\033[1m"
else
  C_RESET="" C_GREEN="" C_YELLOW="" C_RED="" C_CYAN="" C_BOLD=""
fi

# ---------------------------------------------------------------------------
# HILFSFUNKTIONEN
# ---------------------------------------------------------------------------

# Trennlinie ausgeben
separator() {
  echo -e "${C_CYAN}$(printf '=%.0s' {1..60})${C_RESET}"
}

# Erfolgs-Meldung
ok() { echo -e "${C_GREEN}[OK]${C_RESET} $*"; }

# Warn-Meldung
warn() { echo -e "${C_YELLOW}[WARN]${C_RESET} $*"; }

# Fehler-Meldung und Abbruch
die() { echo -e "${C_RED}[FEHLER]${C_RESET} $*" >&2; exit 1; }

# Info-Meldung
info() { echo -e "${C_CYAN}[INFO]${C_RESET} $*"; }

# ---------------------------------------------------------------------------
# VORAUSSETZUNGEN PRÜFEN
# ---------------------------------------------------------------------------
check_requirements() {
  # gh CLI verfügbar?
  command -v gh &>/dev/null || die "gh CLI nicht gefunden. Bitte installieren: https://cli.github.com"

  # gh CLI authentifiziert?
  gh auth status &>/dev/null || die "gh CLI nicht authentifiziert. Bitte 'gh auth login' ausführen."

  # jq verfügbar? (für JSON-Ausgabe)
  if ! command -v jq &>/dev/null; then
    warn "jq nicht gefunden – JSON-Ausgabe wird nicht formatiert."
    JQ_AVAILABLE=false
  else
    JQ_AVAILABLE=true
  fi
}

# ---------------------------------------------------------------------------
# HILFTEXT
# ---------------------------------------------------------------------------
show_help() {
  separator
  echo -e "${C_BOLD}WEBHOOK SETUP – LYKOS68/roman-hild4${C_RESET}"
  separator
  cat <<EOF

VERWENDUNG:
  $(basename "$0") <webhook_url>          Neuen Webhook registrieren
  $(basename "$0") --list                 Alle Webhooks auflisten
  $(basename "$0") --delete <hook_id>     Webhook löschen
  $(basename "$0") --ping   <hook_id>     Webhook testen (ping senden)
  $(basename "$0") --help                 Diesen Hilfetext anzeigen

PARAMETER:
  <webhook_url>   Vollständige HTTPS-URL des Webhook-Endpunkts
                  Beispiel: https://mein-server.de/webhook

  <hook_id>       Numerische ID des Webhooks (aus --list ermitteln)

REGISTRIERTE EVENTS (beim Erstellen):
  - push               Bei jedem Push in das Repository
  - workflow_run       Bei Start/Ende eines Workflow-Laufs
  - repository_dispatch  Bei externem API-Aufruf (workflow_dispatch via API)

BEISPIELE:
  # Webhook für lokalen ngrok-Tunnel registrieren:
  $(basename "$0") https://abc123.ngrok.io/webhook

  # Alle vorhandenen Webhooks anzeigen:
  $(basename "$0") --list

  # Webhook mit ID 12345678 löschen:
  $(basename "$0") --delete 12345678

  # Webhook mit ID 12345678 testen:
  $(basename "$0") --ping 12345678

REPO:   $REPO
EOF
  separator
}

# ---------------------------------------------------------------------------
# WEBHOOKS AUFLISTEN
# ---------------------------------------------------------------------------
list_webhooks() {
  separator
  info "Bestehende Webhooks für ${C_BOLD}${REPO}${C_RESET} abrufen..."
  separator

  # Webhooks über gh API abrufen
  local response
  response=$(gh api "repos/${REPO}/hooks" 2>&1) || die "API-Abruf fehlgeschlagen: $response"

  # Anzahl prüfen
  local count
  if $JQ_AVAILABLE; then
    count=$(echo "$response" | jq 'length')
  else
    count=$(echo "$response" | grep -c '"id"' || echo "?")
  fi

  if [ "$count" = "0" ] || [ "$response" = "[]" ]; then
    warn "Keine Webhooks gefunden."
    return 0
  fi

  info "Gefundene Webhooks: ${C_BOLD}${count}${C_RESET}"
  echo ""

  if $JQ_AVAILABLE; then
    # Formatierte Ausgabe mit jq
    echo "$response" | jq -r '.[] | 
      "ID      : \(.id)\n" +
      "URL     : \(.config.url // "N/A")\n" +
      "Aktiv   : \(.active)\n" +
      "Events  : \(.events | join(", "))\n" +
      "Erstellt: \(.created_at)\n" +
      "Letzter Ping: \(.last_response.code // "N/A") \(.last_response.status // "")\n" +
      "---"'
  else
    # Rohe JSON-Ausgabe ohne jq
    echo "$response"
  fi

  separator
}

# ---------------------------------------------------------------------------
# WEBHOOK REGISTRIEREN
# ---------------------------------------------------------------------------
register_webhook() {
  local webhook_url="$1"

  # URL-Format prüfen
  [[ "$webhook_url" =~ ^https?:// ]] || die "Ungültige URL: '$webhook_url'. Muss mit https:// oder http:// beginnen."

  separator
  info "Webhook-Registrierung für ${C_BOLD}${REPO}${C_RESET}"
  info "Ziel-URL: ${C_BOLD}${webhook_url}${C_RESET}"
  separator

  # Prüfen ob bereits ein Webhook mit dieser URL existiert
  info "Prüfe ob Webhook bereits existiert..."
  local existing
  existing=$(gh api "repos/${REPO}/hooks" 2>/dev/null || echo "[]")

  if $JQ_AVAILABLE; then
    local existing_id
    existing_id=$(echo "$existing" | jq -r --arg url "$webhook_url" '.[] | select(.config.url == $url) | .id' | head -1)
    if [ -n "$existing_id" ]; then
      warn "Webhook mit dieser URL existiert bereits (ID: ${existing_id})."
      warn "Verwende '--delete ${existing_id}' zum Löschen, dann erneut registrieren."
      list_webhooks
      exit 0
    fi
  fi

  # Webhook-Payload zusammenstellen
  local payload
  payload=$(cat <<EOF
{
  "name": "web",
  "active": true,
  "events": [
    "push",
    "workflow_run",
    "repository_dispatch"
  ],
  "config": {
    "url": "${webhook_url}",
    "content_type": "json",
    "insecure_ssl": "0"
  }
}
EOF
)

  # Webhook über gh API erstellen
  info "Erstelle Webhook..."
  local result
  result=$(echo "$payload" | gh api "repos/${REPO}/hooks" \
    --method POST \
    --input - 2>&1) || die "Webhook-Erstellung fehlgeschlagen:\n$result"

  ok "Webhook erfolgreich registriert!"
  echo ""

  if $JQ_AVAILABLE; then
    local hook_id
    hook_id=$(echo "$result" | jq -r '.id')
    info "Webhook-ID  : ${C_BOLD}${hook_id}${C_RESET}"
    info "URL         : $(echo "$result" | jq -r '.config.url')"
    info "Events      : $(echo "$result" | jq -r '.events | join(", ")')"
    info "Aktiv       : $(echo "$result" | jq -r '.active')"
    echo ""
    info "Zum Testen  : $(basename "$0") --ping ${hook_id}"
    info "Zum Löschen : $(basename "$0") --delete ${hook_id}"
  else
    echo "$result"
  fi

  separator
}

# ---------------------------------------------------------------------------
# WEBHOOK LÖSCHEN
# ---------------------------------------------------------------------------
delete_webhook() {
  local hook_id="$1"

  # ID muss numerisch sein
  [[ "$hook_id" =~ ^[0-9]+$ ]] || die "Ungültige Hook-ID: '$hook_id'. Muss eine Zahl sein."

  separator
  info "Lösche Webhook ID ${C_BOLD}${hook_id}${C_RESET} aus ${REPO}..."

  # Webhook-Details vor dem Löschen abrufen
  local details
  details=$(gh api "repos/${REPO}/hooks/${hook_id}" 2>&1) || {
    die "Webhook ID ${hook_id} nicht gefunden oder kein Zugriff."
  }

  if $JQ_AVAILABLE; then
    info "Webhook-URL : $(echo "$details" | jq -r '.config.url // "N/A"')"
    info "Events      : $(echo "$details" | jq -r '.events | join(", ")')"
  fi

  # Sicherheitsabfrage
  echo ""
  read -r -p "$(echo -e "${C_YELLOW}Wirklich löschen? [j/N]:${C_RESET} ")" confirm
  if [[ ! "$confirm" =~ ^[jJyY]$ ]]; then
    info "Abgebrochen."
    exit 0
  fi

  # Löschen
  gh api "repos/${REPO}/hooks/${hook_id}" --method DELETE 2>&1 || \
    die "Löschen fehlgeschlagen."

  ok "Webhook ${hook_id} erfolgreich gelöscht."
  separator
}

# ---------------------------------------------------------------------------
# WEBHOOK TESTEN (PING)
# ---------------------------------------------------------------------------
ping_webhook() {
  local hook_id="$1"

  # ID muss numerisch sein
  [[ "$hook_id" =~ ^[0-9]+$ ]] || die "Ungültige Hook-ID: '$hook_id'. Muss eine Zahl sein."

  separator
  info "Sende Ping an Webhook ID ${C_BOLD}${hook_id}${C_RESET}..."

  # Ping senden
  local result
  result=$(gh api "repos/${REPO}/hooks/${hook_id}/pings" --method POST 2>&1) || {
    die "Ping fehlgeschlagen: $result"
  }

  ok "Ping erfolgreich gesendet an Webhook ${hook_id}."
  info "Der Webhook-Endpunkt sollte eine Anfrage mit dem Header 'X-GitHub-Event: ping' erhalten haben."

  # Letzten Ping-Status abrufen
  sleep 2
  info "Rufe letzten Ping-Status ab..."
  local status
  status=$(gh api "repos/${REPO}/hooks/${hook_id}" 2>/dev/null || echo "{}")
  if $JQ_AVAILABLE; then
    local code
    code=$(echo "$status" | jq -r '.last_response.code // "N/A"')
    local msg
    msg=$(echo "$status" | jq -r '.last_response.status // "N/A"')
    info "Letzter HTTP-Status: ${C_BOLD}${code}${C_RESET} – ${msg}"
  fi

  separator
}

# ---------------------------------------------------------------------------
# HAUPTPROGRAMM
# ---------------------------------------------------------------------------
main() {
  # Keine Argumente → Hilfe anzeigen
  if [ $# -eq 0 ]; then
    show_help
    exit 0
  fi

  # Voraussetzungen prüfen
  check_requirements

  # Argumente auswerten
  case "$1" in
    --help|-h)
      show_help
      ;;

    --list|-l)
      list_webhooks
      ;;

    --delete|-d)
      [ $# -ge 2 ] || die "--delete benötigt eine Hook-ID als zweites Argument."
      delete_webhook "$2"
      ;;

    --ping|-p)
      [ $# -ge 2 ] || die "--ping benötigt eine Hook-ID als zweites Argument."
      ping_webhook "$2"
      ;;

    --*)
      die "Unbekannte Option: '$1'. Verwende --help für Hilfe."
      ;;

    *)
      # Erster Parameter ist die Webhook-URL
      register_webhook "$1"
      ;;
  esac
}

main "$@"
