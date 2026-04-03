---
name: mapping-analysis-templates
description: Stellt Vorlagen, Skripte und Best Practices für die Erstellung und Analyse von Daten-, Prozess- und System-Mappings bereit. Verwenden Sie diesen Skill, um strukturierte Mapping-Dokumente zu erstellen, Analysen durchzuführen und die Qualität von Mapping-Artefakten sicherzustellen.
---

# Mapping und Analyse Skill

Dieser Skill bietet eine umfassende Sammlung von Werkzeugen zur Erstellung, Validierung und Analyse von Daten-, Prozess- und System-Mappings. Er ist darauf ausgelegt, strukturierte, konsistente und qualitativ hochwertige Mapping-Dokumente zu erstellen, die als "Single Source of Truth" dienen.

Der Skill folgt dem Prinzip "Dokumentation als Code". Mappings werden in strukturierten Formaten erstellt, die versioniert, validiert und automatisiert verarbeitet werden können.

## Kernkomponenten

- **`templates/`**: Markdown-Vorlagen für verschiedene Mapping-Typen.
- **`scripts/`**: Python-Skripte zur Generierung von Schemas und zur Validierung von Mapping-Dokumenten.
- **`references/`**: Best Practices und eine Sammlung von Analyse-Prompts.

## Workflow

Folgen Sie diesem Workflow, um ein Mapping- oder Analyse-Dokument zu erstellen:

### 1. Vorlage auswählen

Wählen Sie basierend auf der Anforderung eine der folgenden Vorlagen aus dem `templates/`-Verzeichnis:

| Vorlage | Anwendungsfall |
|---|---|
| `data_mapping_template.md` | Für das Mapping von Datenfeldern zwischen zwei Systemen, inklusive Transformationen und Validierungsregeln. |
| `process_mapping_template.md` | Zur Dokumentation von Geschäftsprozessen, inklusive Schritten, Verantwortlichkeiten, KPIs und Risiken. |
| `system_mapping_template.md` | Zur Beschreibung von Systemlandschaften, inklusive Komponenten, Schnittstellen, Abhängigkeiten und Sicherheitsaspekten. |

Kopieren Sie die ausgewählte Vorlage in Ihr Arbeitsverzeichnis und benennen Sie sie entsprechend (z.B. `order_to_invoice_data_mapping.md`).

### 2. Mapping-Dokument erstellen

Füllen Sie die Markdown-Vorlage mit den spezifischen Informationen für das Mapping aus. Halten Sie sich dabei an die Struktur der Vorlage.

### 3. Analyse durchführen (optional)

Wenn die Aufgabe eine tiefere Analyse erfordert, konsultieren Sie die Referenzdatei `references/analysis_prompts.md`. Sie enthält detaillierte Prompt-Vorlagen für verschiedene Szenarien, wie z.B.:

- Explorative Datenanalyse
- Root-Cause-Analyse
- Architektur-Review
- Kosten-Nutzen-Analyse

Verwenden Sie diese Prompts, um eine detaillierte Analyse mit einem LLM durchzuführen und die Ergebnisse in Ihr Dokument zu integrieren.

### 4. Schema generieren und Mapping validieren

Um die strukturelle Integrität sicherzustellen, sollten Sie Ihr Mapping-Dokument validieren. Der empfohlene Weg ist, das Markdown-Dokument in ein strukturiertes JSON-Format zu überführen und dieses dann zu validieren.

**Schritt 4.1: Schema generieren**

Verwenden Sie das Skript `scripts/generate_schema.py`, um ein JSON-Schema für Ihren Mapping-Typ zu erstellen. Dies dient als Vorlage für die JSON-Struktur.

```bash
# Beispiel für ein Daten-Mapping
python3.11 /home/ubuntu/skills/mapping-analysis-templates/scripts/generate_schema.py data_mapping > data_mapping_schema.json
```

**Schritt 4.2: Mapping nach JSON konvertieren**

Überführen Sie die Inhalte Ihres ausgefüllten Markdown-Dokuments in eine JSON-Datei, die dem generierten Schema entspricht. Speichern Sie diese als `mapping_definition.json`.

**Schritt 4.3: Mapping validieren**

Nutzen Sie das Skript `scripts/validate_mapping.py`, um Ihre JSON-Datei zu prüfen. Das Skript prüft nicht nur die Schema-Konformität, sondern auch logische Fehler und Best-Practice-Verletzungen.

```bash
# Beispiel für ein Daten-Mapping
python3.11 /home/ubuntu/skills/mapping-analysis-templates/scripts/validate_mapping.py data mapping_definition.json
```

Das Skript gibt einen Bericht mit Fehlern, Warnungen und Informationen aus. Beheben Sie alle gemeldeten Fehler, bevor Sie fortfahren.

### 5. Best Practices konsultieren

Lesen Sie während des gesamten Prozesses die Datei `references/best_practices.md`. Sie enthält wichtige Prinzipien für qualitativ hochwertige Mappings und Analysen, z.B. zu den Themen Idempotenz, Null-Handling, Interface Contracts und Observability.

### 6. Ergebnis liefern

Stellen Sie dem Benutzer das finale, validierte Mapping-Dokument (sowohl die Markdown-Vorlage als auch die validierte JSON-Datei) zur Verfügung. Fassen Sie die wichtigsten Erkenntnisse aus der Analyse und dem Validierungsbericht zusammen.

## Verwendung der Skripte

### `generate_schema.py`

Generiert ein JSON-Schema für einen bestimmten Mapping-Typ.

**Verwendung:**
```bash
python3.11 /home/ubuntu/skills/mapping-analysis-templates/scripts/generate_schema.py <schema_type> [output_file]
```

- **`schema_type`**: `data_mapping`, `process_mapping`, `system_mapping`, `analysis_output`
- **`output_file`**: (Optional) Datei, in die das Schema geschrieben wird. Ansonsten wird es auf der Konsole ausgegeben.

### `validate_mapping.py`

Validiert eine Mapping-Definitionsdatei (JSON) gegen ein Schema und Best Practices.

**Verwendung:**
```bash
python3.11 /home/ubuntu/skills/mapping-analysis-templates/scripts/validate_mapping.py <mapping_type> <mapping_file>
```

- **`mapping_type`**: `data`, `process`, `system`
- **`mapping_file`**: Pfad zur JSON-Datei mit der Mapping-Definition.
