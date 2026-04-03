#!/usr/bin/env bash
# =============================================================================
# DATEI: verbindungspunkte_diagnose.sh
# ZWECK: Alle Verbindungspunkte des Repos LYKOS68/roman-hild4 identifizieren
#        und als strukturierte Übersicht ausgeben.
#
# GEPRÜFTE VERBINDUNGSPUNKTE:
#   1. Runner          – alle registrierten Self-Hosted Runner + Status
#   2. Webhooks        – alle konfigurierten Webhooks
#   3. Workflow-Dateien – im Repo vorhandene .yml/.yaml Workflows
#   4. Secrets         – Namen (keine Werte) aller Repository-Secrets
#   5. Variables       – Namen und Werte aller Repository-Variablen
#   6. Environments    – alle konfigurierten Deployment-Environments
#   7. Deploy Keys     – alle registrierten Deploy Keys
#   8. Repository Dispatch Events – aus Workflow-Dateien extrahiert
#   9. API Rate Limit  – aktueller Status (verbleibende Anfragen)
#
# VORAUSSETZUNG: gh CLI authentifiziert als LYKOS68
# VERWENDUNG:
#   ./verbindungspunkte_diagnose.sh           # Vollständige Diagnose
#   ./verbindungspunkte_diagnose.sh --json    # Ausgabe als JSON (benötigt jq)
#   ./verbindungspunkte_diagnose.sh --help    # Hilfe anzeigen
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# KONFIGURATION
# ---------------------------------------------------------------------------
REPO="LYKOS68/roman-hild4"
REPO_OWNER="LYKOS68"
REPO_NAME="roman-hild4"
SCRIPT_VERSION="1.0.0"
OUTPUT_MODE="text"   # "text" oder "json"

# Farben (nur wenn Terminal vorhanden)
if [ -t 1 ]; then
  C_RESET="\033[0m"
  C_GREEN="\033[0;32m"
  C_YELLOW="\033[0;33m"
  C_RED="\033[0;31m"
  C_CYAN="\033[0;36m"
  C_BLUE="\033[0;34m"
  C_MAGENTA="\033[0;35m"
  C_BOLD="\033[1m"
  C_DIM="\033[2m"
else
  C_RESET="" C_GREEN="" C_YELLOW="" C_RED="" C_CYAN=""
  C_BLUE="" C_MAGENTA="" C_BOLD="" C_DIM=""
fi

# Globale Zähler für Zusammenfassung
TOTAL_SECTIONS=0
TOTAL_ERRORS=0
TOTAL_WARNINGS=0

# ---------------------------------------------------------------------------
# HILFSFUNKTIONEN
# ---------------------------------------------------------------------------

# Breite Trennlinie
sep_major() {
  echo -e "${C_CYAN}$(printf '═%.0s' {1..65})${C_RESET}"
}

# Schmale Trennlinie
sep_minor() {
  echo -e "${C_DIM}$(printf '─%.0s' {1..65})${C_RESET}"
}

# Abschnitts-Header
section_header() {
  local num="$1"
  local title="$2"
  local icon="$3"
  TOTAL_SECTIONS=$((TOTAL_SECTIONS + 1))
  echo ""
  sep_major
  echo -e "${C_BOLD}${C_BLUE}  ${icon}  ABSCHNITT ${num}: ${title}${C_RESET}"
  sep_major
}

# Status-Ausgabe
ok()   { echo -e "  ${C_GREEN}✔${C_RESET}  $*"; }
warn() { echo -e "  ${C_YELLOW}⚠${C_RESET}  $*"; TOTAL_WARNINGS=$((TOTAL_WARNINGS + 1)); }
err()  { echo -e "  ${C_RED}✘${C_RESET}  $*"; TOTAL_ERRORS=$((TOTAL_ERRORS + 1)); }
info() { echo -e "  ${C_CYAN}→${C_RESET}  $*"; }
data() { echo -e "     ${C_DIM}$*${C_RESET}"; }

# Zeitstempel
timestamp() { date "+%Y-%m-%d %H:%M:%S %Z" 2>/dev/null || echo "N/A"; }

# ---------------------------------------------------------------------------
# VORAUSSETZUNGEN PRÜFEN
# ---------------------------------------------------------------------------
check_requirements() {
  command -v gh &>/dev/null   || { echo "[FEHLER] gh CLI nicht gefunden." >&2; exit 1; }
  gh auth status &>/dev/null  || { echo "[FEHLER] gh CLI nicht authentifiziert. Bitte 'gh auth login' ausführen." >&2; exit 1; }

  if command -v jq &>/dev/null; then
    JQ_AVAILABLE=true
  else
    JQ_AVAILABLE=false
    warn "jq nicht installiert – einige Ausgaben werden nicht formatiert."
  fi
}

# ---------------------------------------------------------------------------
# HILFTEXT
# ---------------------------------------------------------------------------
show_help() {
  sep_major
  echo -e "${C_BOLD}  VERBINDUNGSPUNKTE DIAGNOSE – ${REPO}${C_RESET}"
  echo -e "  Version: ${SCRIPT_VERSION}"
  sep_major
  cat <<EOF

VERWENDUNG:
  $(basename "$0")            Vollständige Diagnose aller Verbindungspunkte
  $(basename "$0") --json     Ausgabe als JSON (benötigt jq)
  $(basename "$0") --help     Diesen Hilfetext anzeigen

GEPRÜFTE VERBINDUNGSPUNKTE:
  1  Runner              Self-Hosted Runner + Online/Offline-Status
  2  Webhooks            Konfigurierte Webhook-Endpunkte
  3  Workflow-Dateien    Im Repo vorhandene GitHub Actions Workflows
  4  Secrets             Repository-Secrets (nur Namen, keine Werte)
  5  Variables           Repository-Variablen (Namen + Werte)
  6  Environments        Deployment-Environments
  7  Deploy Keys         Registrierte SSH Deploy Keys
  8  Dispatch Events     Repository-Dispatch-Events aus Workflow-Dateien
  9  API Rate Limit      Verbleibende GitHub API-Anfragen

REPO:    $REPO
EOF
  sep_major
}

# ---------------------------------------------------------------------------
# ABSCHNITT 1: RUNNER
# ---------------------------------------------------------------------------
check_runners() {
  section_header "1" "SELF-HOSTED RUNNER" "🖥"

  local response
  response=$(gh api "repos/${REPO}/actions/runners" 2>&1) || {
    err "API-Abruf fehlgeschlagen: $response"
    return
  }

  local count=0
  if $JQ_AVAILABLE; then
    count=$(echo "$response" | jq '.total_count // 0')
  fi

  info "Registrierte Runner gesamt: ${C_BOLD}${count}${C_RESET}"
  sep_minor

  if [ "$count" = "0" ]; then
    warn "Keine Runner registriert."
    return
  fi

  if $JQ_AVAILABLE; then
    echo "$response" | jq -r '.runners[] |
      "  ID      : \(.id)\n" +
      "  Name    : \(.name)\n" +
      "  OS      : \(.os)\n" +
      "  Status  : \(.status)\n" +
      "  Busy    : \(.busy)\n" +
      "  Labels  : \(.labels | map(.name) | join(", "))\n"'  | \
    while IFS= read -r line; do
      # Status-Zeilen farbig markieren
      if echo "$line" | grep -q "Status  : online"; then
        echo -e "${C_GREEN}${line}${C_RESET}"
      elif echo "$line" | grep -q "Status  : offline"; then
        echo -e "${C_RED}${line}${C_RESET}"
      else
        echo "$line"
      fi
    done
  else
    echo "$response"
  fi
}

# ---------------------------------------------------------------------------
# ABSCHNITT 2: WEBHOOKS
# ---------------------------------------------------------------------------
check_webhooks() {
  section_header "2" "WEBHOOKS" "🔗"

  local response
  response=$(gh api "repos/${REPO}/hooks" 2>&1) || {
    err "API-Abruf fehlgeschlagen: $response"
    return
  }

  local count=0
  if $JQ_AVAILABLE; then
    count=$(echo "$response" | jq 'length')
  fi

  info "Konfigurierte Webhooks: ${C_BOLD}${count}${C_RESET}"
  sep_minor

  if [ "$count" = "0" ] || [ "$response" = "[]" ]; then
    warn "Keine Webhooks konfiguriert."
    return
  fi

  if $JQ_AVAILABLE; then
    echo "$response" | jq -r '.[] |
      "  ID          : \(.id)\n" +
      "  URL         : \(.config.url // "N/A")\n" +
      "  Content-Type: \(.config.content_type // "N/A")\n" +
      "  Aktiv       : \(.active)\n" +
      "  Events      : \(.events | join(", "))\n" +
      "  Erstellt    : \(.created_at)\n" +
      "  Letzter Code: \(.last_response.code // "N/A")\n" +
      "  Letzter Msg : \(.last_response.message // "N/A")\n"'
  else
    echo "$response"
  fi
}

# ---------------------------------------------------------------------------
# ABSCHNITT 3: WORKFLOW-DATEIEN
# ---------------------------------------------------------------------------
check_workflows() {
  section_header "3" "WORKFLOW-DATEIEN" "⚙"

  local response
  response=$(gh api "repos/${REPO}/actions/workflows" 2>&1) || {
    err "API-Abruf fehlgeschlagen: $response"
    return
  }

  local count=0
  if $JQ_AVAILABLE; then
    count=$(echo "$response" | jq '.total_count // 0')
  fi

  info "Workflow-Dateien im Repo: ${C_BOLD}${count}${C_RESET}"
  sep_minor

  if [ "$count" = "0" ]; then
    warn "Keine Workflow-Dateien gefunden."
    info "Hinweis: Workflows müssen unter .github/workflows/ abgelegt sein."
    return
  fi

  if $JQ_AVAILABLE; then
    echo "$response" | jq -r '.workflows[] |
      "  ID      : \(.id)\n" +
      "  Name    : \(.name)\n" +
      "  Datei   : \(.path)\n" +
      "  Status  : \(.state)\n" +
      "  URL     : \(.html_url)\n"'
  else
    echo "$response"
  fi

  # Letzte Workflow-Läufe abrufen
  sep_minor
  info "Letzte Workflow-Läufe (max. 5):"
  local runs
  runs=$(gh api "repos/${REPO}/actions/runs?per_page=5" 2>/dev/null || echo '{"workflow_runs":[]}')
  if $JQ_AVAILABLE; then
    local run_count
    run_count=$(echo "$runs" | jq '.workflow_runs | length')
    if [ "$run_count" = "0" ]; then
      data "Keine Läufe vorhanden."
    else
      echo "$runs" | jq -r '.workflow_runs[] |
        "  Run-ID  : \(.id)\n" +
        "  Workflow: \(.name)\n" +
        "  Status  : \(.status)\n" +
        "  Ergebnis: \(.conclusion // "läuft noch")\n" +
        "  Gestartet: \(.created_at)\n"'
    fi
  fi
}

# ---------------------------------------------------------------------------
# ABSCHNITT 4: SECRETS
# ---------------------------------------------------------------------------
check_secrets() {
  section_header "4" "SECRETS (nur Namen)" "🔐"

  local response
  response=$(gh api "repos/${REPO}/actions/secrets" 2>&1) || {
    err "API-Abruf fehlgeschlagen: $response"
    return
  }

  local count=0
  if $JQ_AVAILABLE; then
    count=$(echo "$response" | jq '.total_count // 0')
  fi

  info "Repository-Secrets: ${C_BOLD}${count}${C_RESET}"
  info "(Werte werden aus Sicherheitsgründen NICHT angezeigt)"
  sep_minor

  if [ "$count" = "0" ]; then
    warn "Keine Secrets konfiguriert."
    return
  fi

  if $JQ_AVAILABLE; then
    echo "$response" | jq -r '.secrets[] |
      "  Name     : \(.name)\n" +
      "  Erstellt : \(.created_at)\n" +
      "  Geändert : \(.updated_at)\n"'
  else
    echo "$response"
  fi
}

# ---------------------------------------------------------------------------
# ABSCHNITT 5: VARIABLES
# ---------------------------------------------------------------------------
check_variables() {
  section_header "5" "VARIABLES (Namen + Werte)" "📋"

  local response
  response=$(gh api "repos/${REPO}/actions/variables" 2>&1) || {
    err "API-Abruf fehlgeschlagen: $response"
    return
  }

  local count=0
  if $JQ_AVAILABLE; then
    count=$(echo "$response" | jq '.total_count // 0')
  fi

  info "Repository-Variablen: ${C_BOLD}${count}${C_RESET}"
  sep_minor

  if [ "$count" = "0" ]; then
    warn "Keine Variablen konfiguriert."
    return
  fi

  if $JQ_AVAILABLE; then
    echo "$response" | jq -r '.variables[] |
      "  Name     : \(.name)\n" +
      "  Wert     : \(.value)\n" +
      "  Erstellt : \(.created_at)\n" +
      "  Geändert : \(.updated_at)\n"'
  else
    echo "$response"
  fi
}

# ---------------------------------------------------------------------------
# ABSCHNITT 6: ENVIRONMENTS
# ---------------------------------------------------------------------------
check_environments() {
  section_header "6" "ENVIRONMENTS" "🌍"

  local response
  response=$(gh api "repos/${REPO}/environments" 2>&1) || {
    err "API-Abruf fehlgeschlagen: $response"
    return
  }

  local count=0
  if $JQ_AVAILABLE; then
    count=$(echo "$response" | jq '.total_count // 0')
  fi

  info "Deployment-Environments: ${C_BOLD}${count}${C_RESET}"
  sep_minor

  if [ "$count" = "0" ]; then
    warn "Keine Environments konfiguriert."
    return
  fi

  if $JQ_AVAILABLE; then
    echo "$response" | jq -r '.environments[] |
      "  ID          : \(.id)\n" +
      "  Name        : \(.name)\n" +
      "  URL         : \(.html_url)\n" +
      "  Erstellt    : \(.created_at)\n" +
      "  Schutzregeln: \(.protection_rules | length) Regel(n)\n"'
  else
    echo "$response"
  fi
}

# ---------------------------------------------------------------------------
# ABSCHNITT 7: DEPLOY KEYS
# ---------------------------------------------------------------------------
check_deploy_keys() {
  section_header "7" "DEPLOY KEYS" "🔑"

  local response
  response=$(gh api "repos/${REPO}/keys" 2>&1) || {
    err "API-Abruf fehlgeschlagen: $response"
    return
  }

  local count=0
  if $JQ_AVAILABLE; then
    count=$(echo "$response" | jq 'length')
  fi

  info "Registrierte Deploy Keys: ${C_BOLD}${count}${C_RESET}"
  sep_minor

  if [ "$count" = "0" ] || [ "$response" = "[]" ]; then
    warn "Keine Deploy Keys konfiguriert."
    return
  fi

  if $JQ_AVAILABLE; then
    echo "$response" | jq -r '.[] |
      "  ID          : \(.id)\n" +
      "  Titel       : \(.title)\n" +
      "  Fingerprint : \(.key | split(" ")[1] // "N/A" | .[0:20])...\n" +
      "  Nur-Lesen   : \(.read_only)\n" +
      "  Verifiziert : \(.verified)\n" +
      "  Erstellt    : \(.created_at)\n"'
  else
    echo "$response"
  fi
}

# ---------------------------------------------------------------------------
# ABSCHNITT 8: REPOSITORY DISPATCH EVENTS (aus Workflow-Dateien extrahiert)
# ---------------------------------------------------------------------------
check_dispatch_events() {
  section_header "8" "REPOSITORY DISPATCH EVENTS" "📡"

  info "Extrahiere repository_dispatch Event-Types aus Workflow-Dateien..."
  sep_minor

  # Workflow-Dateien über API abrufen
  local workflows_response
  workflows_response=$(gh api "repos/${REPO}/actions/workflows" 2>/dev/null || echo '{"workflows":[]}')

  if $JQ_AVAILABLE; then
    local wf_count
    wf_count=$(echo "$workflows_response" | jq '.total_count // 0')

    if [ "$wf_count" = "0" ]; then
      warn "Keine Workflow-Dateien vorhanden – keine Dispatch-Events extrahierbar."
      return
    fi

    # Für jede Workflow-Datei den Inhalt abrufen und nach repository_dispatch suchen
    local found_any=false
    while IFS= read -r wf_path; do
      # Dateiinhalt über Contents-API abrufen
      local file_content
      file_content=$(gh api "repos/${REPO}/contents/${wf_path}" 2>/dev/null || echo '{}')

      # Base64-Inhalt dekodieren
      local decoded
      decoded=$(echo "$file_content" | jq -r '.content // ""' | base64 -d 2>/dev/null || echo "")

      if [ -z "$decoded" ]; then
        data "  ${wf_path}: Inhalt nicht lesbar."
        continue
      fi

      # Nach repository_dispatch und types suchen
      if echo "$decoded" | grep -q "repository_dispatch"; then
        found_any=true
        info "Datei: ${C_BOLD}${wf_path}${C_RESET}"

        # Event-Types extrahieren (einfache grep-basierte Extraktion)
        local types
        types=$(echo "$decoded" | grep -A 10 "repository_dispatch" | grep -E "^\s*-\s+" | sed 's/^\s*-\s*//' | tr -d '"' | tr -d "'" || echo "")

        if [ -n "$types" ]; then
          echo "  Event-Types:"
          while IFS= read -r t; do
            [ -n "$t" ] && data "    - $t"
          done <<< "$types"
        else
          data "  Event-Types: (nicht explizit definiert – akzeptiert alle)"
        fi
        echo ""
      fi
    done < <(echo "$workflows_response" | jq -r '.workflows[].path')

    if ! $found_any; then
      warn "Keine repository_dispatch Trigger in Workflow-Dateien gefunden."
    fi
  else
    warn "jq nicht verfügbar – Dispatch-Event-Extraktion übersprungen."
  fi
}

# ---------------------------------------------------------------------------
# ABSCHNITT 9: API RATE LIMIT
# ---------------------------------------------------------------------------
check_rate_limit() {
  section_header "9" "API RATE LIMIT STATUS" "📊"

  local response
  response=$(gh api "rate_limit" 2>&1) || {
    err "API-Abruf fehlgeschlagen: $response"
    return
  }

  if $JQ_AVAILABLE; then
    echo "$response" | jq -r '
      .resources |
      to_entries[] |
      "  \(.key | ascii_upcase):\n" +
      "    Limit     : \(.value.limit)\n" +
      "    Verbraucht: \(.value.used)\n" +
      "    Verbleibend: \(.value.remaining)\n" +
      "    Reset um  : \(.value.reset | todate)\n"'

    # Warnung bei niedrigem Limit
    local core_remaining
    core_remaining=$(echo "$response" | jq '.resources.core.remaining')
    if [ "$core_remaining" -lt 100 ]; then
      warn "Kritisch: Nur noch ${core_remaining} Core-API-Anfragen verfügbar!"
    elif [ "$core_remaining" -lt 500 ]; then
      warn "Niedrig: Nur noch ${core_remaining} Core-API-Anfragen verfügbar."
    else
      ok "Core-API: ${core_remaining} Anfragen verbleibend."
    fi
  else
    echo "$response"
  fi
}

# ---------------------------------------------------------------------------
# ZUSAMMENFASSUNG
# ---------------------------------------------------------------------------
print_summary() {
  echo ""
  sep_major
  echo -e "${C_BOLD}  DIAGNOSE-ZUSAMMENFASSUNG${C_RESET}"
  sep_major
  echo ""
  data "Repo        : ${REPO}"
  data "Zeitstempel : $(timestamp)"
  data "Abschnitte  : ${TOTAL_SECTIONS}"
  data "Warnungen   : ${TOTAL_WARNINGS}"
  data "Fehler      : ${TOTAL_ERRORS}"
  echo ""

  if [ "$TOTAL_ERRORS" -gt 0 ]; then
    err "Diagnose mit ${TOTAL_ERRORS} Fehler(n) abgeschlossen."
  elif [ "$TOTAL_WARNINGS" -gt 0 ]; then
    warn "Diagnose mit ${TOTAL_WARNINGS} Warnung(en) abgeschlossen."
  else
    ok "Diagnose erfolgreich abgeschlossen – keine Fehler."
  fi

  sep_major
  echo ""
}

# ---------------------------------------------------------------------------
# KOPFZEILE
# ---------------------------------------------------------------------------
print_header() {
  sep_major
  echo -e "${C_BOLD}${C_MAGENTA}"
  echo "  ██╗   ██╗███████╗██████╗ ██████╗ ██╗███╗   ██╗██████╗ "
  echo "  ██║   ██║██╔════╝██╔══██╗██╔══██╗██║████╗  ██║██╔══██╗"
  echo "  ██║   ██║█████╗  ██████╔╝██████╔╝██║██╔██╗ ██║██║  ██║"
  echo "  ╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔══██╗██║██║╚██╗██║██║  ██║"
  echo "   ╚████╔╝ ███████╗██║  ██║██████╔╝██║██║ ╚████║██████╔╝"
  echo "    ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝╚═════╝ "
  echo -e "${C_RESET}"
  echo -e "  ${C_BOLD}VERBINDUNGSPUNKTE DIAGNOSE${C_RESET}  |  Version ${SCRIPT_VERSION}"
  echo -e "  Repo: ${C_CYAN}${REPO}${C_RESET}"
  echo -e "  Zeit: $(timestamp)"
  sep_major
}

# ---------------------------------------------------------------------------
# HAUPTPROGRAMM
# ---------------------------------------------------------------------------
main() {
  # Argumente auswerten
  case "${1:-}" in
    --help|-h)
      show_help
      exit 0
      ;;
    --json)
      OUTPUT_MODE="json"
      warn "JSON-Modus: Ausgabe wird als rohe API-Antworten dargestellt."
      ;;
    "")
      # Keine Argumente → normale Textausgabe
      ;;
    *)
      echo "[FEHLER] Unbekannte Option: '$1'. Verwende --help für Hilfe." >&2
      exit 1
      ;;
  esac

  # Voraussetzungen prüfen
  check_requirements

  # Kopfzeile ausgeben
  print_header

  # Alle Abschnitte prüfen
  check_runners
  check_webhooks
  check_workflows
  check_secrets
  check_variables
  check_environments
  check_deploy_keys
  check_dispatch_events
  check_rate_limit

  # Zusammenfassung
  print_summary
}

main "$@"
