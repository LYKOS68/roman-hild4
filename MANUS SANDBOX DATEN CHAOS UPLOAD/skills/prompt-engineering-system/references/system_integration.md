´´´markdown
# Systemintegration: Das vollständige Kalibrierungs-Ökosystem

## Der Gesamtprozess: Von Chaos zu kalibrierten Ergebnissen

Dieses Dokument beschreibt, wie alle Komponenten – das **4-Phasen-Framework**, die **3-Layer-Architektur**, das **PROMPT_PACK-System** und der **Prompt-Kalibrierungs-Generator** – zu einem einzigen, kohärenten Arbeitsökosystem verschmelzen.

## Die Architektur im Überblick

```
┌─────────────────────────────────────────────────────────────────┐
│                         ORCHESTRATOR                             │
│  (Zentrale Steuerung, Aufgabenverteilung, Feedback-Management)  │
└───────────────────────┬─────────────────────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
┌───────────────────┐         ┌───────────────────┐
│  CHAOS-DATEIEN    │         │  PROMPT_PACK      │
│  (Sender-Profil)  │         │  (Modell-Kontext) │
└─────────┬─────────┘         └─────────┬─────────┘
          │                             │
          └──────────┬──────────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │ PROMPT-KALIBRIERUNGS-      │
        │ GENERATOR                  │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │ KALIBRIERTER PROMPT        │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │ ZIEL-LLM                   │
        │ (Empfänger-Kalibrierung    │
        │  wird getriggert)          │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │ ERGEBNIS                   │
        │ (Entspricht den            │
        │  Erwartungen des Senders)  │
        └────────────────────────────┘
```

## Der Workflow Schritt für Schritt

### Phase 0: Setup (Einmalig pro Projekt)

1.  **Layer-Architektur aufsetzen:**
    *   Erstellen Sie die `.gemini/`, `kernels/` und `user_kernels/` Verzeichnisse.
    *   Füllen Sie die Templates mit projektspezifischen Informationen.

2.  **PROMPT_PACKs erstellen:**
    *   Für jedes LLM, das Sie im Orchester nutzen möchten, erstellen Sie ein PROMPT_PACK mit dem **PROMPT_PACK-Generator**.

3.  **Orchestrator konfigurieren:**
    *   Weisen Sie jedem PROMPT_PACK eine Rolle zu (z.B. "Kreativ-Autor", "Daten-Analyst").

### Phase 1: IDENTIFY & PURGE (Sender-Profil-Extraktion)

1.  **Chaos-Dateien analysieren:**
    *   Der Orchestrator nutzt einen spezialisierten Prompt (basierend auf dem **Instruction Generator** aus dem 8-Generator-Pack), um Ihre Tagebücher, Notizen und Ideen zu analysieren.
    *   **Ziel:** Extraktion von `ziele`, `kontext`, `regeln` und `erfolgs_beispiele`.

2.  **Sender-Profil generieren:**
    *   Die extrahierten Informationen werden in ein strukturiertes `sender_profile.json` geschrieben.

### Phase 2: CONVERT & STANDARDIZE (Modell-Kontext-Analyse)

1.  **Aufgabe empfangen:**
    *   Sie stellen eine Anfrage (z.B. "Schreibe einen philosophischen Text über die Vergänglichkeit").

2.  **LLM-Auswahl:**
    *   Der Orchestrator analysiert die Anfrage und wählt das passende LLM aus dem Orchester (z.B. das "Kreativ-Autor"-LLM).

3.  **PROMPT_PACK laden:**
    *   Der Orchestrator liest das PROMPT_PACK des gewählten LLMs und extrahiert `meta` und `techniques`.

### Phase 3: ORGANIZE (Prompt-Kalibrierung)

1.  **Kalibrierungs-Generator aufrufen:**
    *   Der Orchestrator übergibt das `sender_profile.json`, den `Modell-Kontext` und Ihre Anfrage (`TASK_INPUT`) an den **Prompt-Kalibrierungs-Generator**.

2.  **Kalibrierter Prompt wird erzeugt:**
    *   Der Generator konstruiert einen hochspezifischen, kontextuellen Prompt mit integriertem Feedback-Loop (siehe `VALIDIERUNG`-Sektion).

### Phase 4: VERIFY (Ausführung & Feedback)

1.  **Prompt an Ziel-LLM senden:**
    *   Der kalibrierte Prompt wird an das gewählte LLM gesendet.

2.  **Empfänger-Kalibrierung wird getriggert:**
    *   Das LLM verarbeitet den Prompt. Die `VALIDIERUNG`-Sektion zwingt es zur Selbst-Reflexion und Anpassung *vor* der Ausgabe.

3.  **Ergebnis empfangen:**
    *   Das LLM sendet das Ergebnis zurück. Es entspricht den Erwartungen des Senders, weil die Kalibrierung erfolgreich war.

4.  **Feedback-Loop (Optional):**
    *   Der Orchestrator kann das Ergebnis mit dem `sender_profile.json` abgleichen. Bei Abweichungen wird das `sender_profile.json` aktualisiert (Lernen) und der Prozess wiederholt (Iteration).

## Die Rolle der 10 Prompt-Gesetze

Die **10 Prompt-Gesetze** sind die Compliance-Schicht. Sie stellen sicher, dass jeder generierte Prompt – egal ob vom **PROMPT_PACK-Generator**, vom **Kalibrierungs-Generator** oder von einem der 8 Generatoren – den definierten Standards entspricht. Der Orchestrator prüft jeden Prompt vor der Ausführung gegen diese Gesetze.

## Das Ergebnis: Ein selbstlernendes, kalibriertes System

Durch die Integration aller Komponenten entsteht ein System, das:

*   **Ihre impliziten Anforderungen explizit macht** (Sender-Profil-Extraktion).
*   **Die Fähigkeiten der LLMs kennt und nutzt** (PROMPT_PACKs).
*   **Prompts erzeugt, die die Empfänger-Kalibrierung garantiert triggern** (Kalibrierungs-Generator mit Feedback-Loop).
*   **Aus Fehlern lernt und sich verbessert** (Feedback-Loop & Sender-Profil-Update).

> **Das Scheitern der Kalibrierung ist eliminiert. Das System ist die Basis, die jeder Eingabe Adresse, Träger und Richtung gibt.**
´´´
