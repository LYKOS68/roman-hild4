# Daten-Mapping Template

## Mapping-Übersicht
**Quelle:** [Quellsystem/Datenbank/API]
**Ziel:** [Zielsystem/Datenbank/API]
**Mapping-Typ:** [1:1 / 1:N / N:M / Transformation]
**Datum:** [YYYY-MM-DD]

## Feldmapping

| Quellfeld | Typ | Zielfeld | Typ | Transformation | Validierung | Anmerkungen |
|-----------|-----|----------|-----|----------------|-------------|-------------|
| source_id | INT | target_id | VARCHAR | CAST(id AS VARCHAR) | NOT NULL | Primärschlüssel |
| name | VARCHAR(100) | full_name | VARCHAR(255) | CONCAT(first_name, ' ', last_name) | LENGTH > 0 | - |
| created_at | TIMESTAMP | creation_date | DATE | DATE(created_at) | - | Zeitzone beachten |

## Transformationslogik

### Regel 1: [Regelname]
```
WENN [Bedingung]
DANN [Aktion]
SONST [Alternative]
```

### Regel 2: [Regelname]
```
INPUT: [Eingabeformat]
PROCESS: [Verarbeitungsschritte]
OUTPUT: [Ausgabeformat]
```

## Datenqualität

### Validierungsregeln
- **Pflichtfelder:** [Liste der Pflichtfelder]
- **Wertebereich:** [Min/Max-Werte, erlaubte Werte]
- **Format:** [Regex-Pattern, Datumsformat, etc.]
- **Referenzielle Integrität:** [Fremdschlüssel-Beziehungen]

### Fehlerbehandlung
| Fehlertyp | Aktion | Logging | Benachrichtigung |
|-----------|--------|---------|------------------|
| NULL-Wert in Pflichtfeld | Zeile überspringen | ERROR | Ja |
| Ungültiges Format | Standardwert verwenden | WARNING | Nein |
| Duplikat | Merge/Update | INFO | Nein |

## Abhängigkeiten

### Voraussetzungen
- [System/Tabelle/API muss existieren]
- [Berechtigungen erforderlich]
- [Datenbereinigung notwendig]

### Nachgelagerte Prozesse
- [Prozess 1: Beschreibung]
- [Prozess 2: Beschreibung]

## Performance

- **Erwartete Datenmenge:** [Anzahl Datensätze]
- **Batch-Größe:** [Anzahl pro Batch]
- **Geschätzte Laufzeit:** [Zeitangabe]
- **Ressourcenbedarf:** [CPU/RAM/Storage]

## Testfälle

### Testfall 1: Standard-Mapping
**Input:**
```json
{
  "source_id": 123,
  "name": "Max Mustermann",
  "created_at": "2024-01-15T10:30:00Z"
}
```

**Expected Output:**
```json
{
  "target_id": "123",
  "full_name": "Max Mustermann",
  "creation_date": "2024-01-15"
}
```

### Testfall 2: Edge Case
[Beschreibung des Sonderfalls]

## Versionierung

| Version | Datum | Änderung | Autor |
|---------|-------|----------|-------|
| 1.0 | YYYY-MM-DD | Initiale Version | [Name] |
