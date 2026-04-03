# Template Catalog

Vollständiger Katalog aller verfügbaren Templates.

---

## Template 1: LLM-Agenten-Setup

**Anwendungsfälle:**
- Spezialisierte KI-Agenten für spezifische Aufgaben
- Chatbots mit definiertem Verhalten
- Automatisierte Assistenten

**Best Practices:**
- Temperature: 0.3-0.5 für deterministische Tasks, 0.7-0.9 für kreative Tasks
- System Prompt: Klar definierte Rolle, Kontext und Constraints
- Tools: Nur notwendige Tools hinzufügen

**Beispiele:**
- Dateiformat-Transformer
- Code-Review-Agent
- Dokumentations-Generator

---

## Template 2: Pipeline-Design

**Anwendungsfälle:**
- Datenverarbeitungs-Pipelines
- ETL (Extract, Transform, Load)
- Automatisierungs-Workflows

**Best Practices:**
- Stages: Input → Transform → Validate → Output
- Error Handling: Retry-Strategie definieren
- Idempotenz: Stages sollten wiederholbar sein

**Beispiele:**
- Log-Analyse-Pipeline
- Daten-Migrations-Pipeline
- Content-Processing-Pipeline

---

## Template 3: Architektur-Layout

**Anwendungsfälle:**
- System-Architektur-Design
- Microservices-Architekturen
- Layer-basierte Systeme

**Best Practices:**
- Layers: Klare Trennung (Presentation, Business Logic, Data)
- Dependencies: Bottom-up (höhere Layer abhängig von niedrigeren)
- Communication: Definierte Interfaces zwischen Components

**Beispiele:**
- 3-Layer-Architektur (System, Kernel, User)
- Microservices mit Event-Bus
- Monolithische Layer-Architektur

---

## Template 4: Workflow-Definition

**Anwendungsfälle:**
- Geschäftsprozesse
- Genehmigungsworkflows
- Automatisierungs-Sequenzen

**Best Practices:**
- Steps: Klar definierte Aktionen
- Conditions: Explizite Verzweigungslogik
- Validation: Checkpoints nach kritischen Steps

**Beispiele:**
- Dokumenten-Genehmigungsworkflow
- Onboarding-Prozess
- Deployment-Workflow

---

## Template 5: Prompt-Struktur

**Anwendungsfälle:**
- LLM-Prompts für spezifische Tasks
- Strukturierte Anfragen an KI-Modelle
- Wiederverwendbare Prompt-Templates

**Best Practices:**
- Empfänger-Triggering: Rolle, Kontext, Prioritäten definieren
- Prompt-Kalibrierung: Task, Schritte, Format, Beispiele
- Validierung: Output-Kriterien definieren

**Beispiele:**
- Code-Generierungs-Prompt
- Analyse-Prompt
- Transformations-Prompt

---

## Template 6: Regel-System

**Anwendungsfälle:**
- Business Rules
- Validierungs-Regeln
- Entscheidungs-Logik

**Best Practices:**
- Priority: Höchste Priorität zuerst
- Conflict Resolution: Strategie definieren
- Consistency: Regeln auf Widersprüche prüfen

**Beispiele:**
- Validierungs-Regel-System
- Pricing-Rules
- Access-Control-Rules

---

## Erweiterung: Neue Templates hinzufügen

1. Identifiziere Anwendungsfall
2. Definiere Setup, Layout, Prompt, Kontext
3. Erstelle Template mit Platzhaltern
4. Teste Template
5. Dokumentiere in diesem Katalog
6. Füge zu SKILL.md hinzu
