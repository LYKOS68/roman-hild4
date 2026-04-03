# Analyse-Prompts für verschiedene Szenarien

## Datenanalyse-Prompts

### Explorative Datenanalyse (EDA)
```
Führe eine explorative Datenanalyse für [Datensatz] durch:

1. Datensatz-Übersicht:
   - Anzahl Zeilen und Spalten
   - Datentypen der Spalten
   - Speicherbedarf

2. Deskriptive Statistik:
   - Zentrale Tendenz (Mittelwert, Median, Modus)
   - Streuung (Standardabweichung, Varianz, Quartile)
   - Verteilung (Schiefe, Kurtosis)

3. Datenqualität:
   - Fehlende Werte (Anzahl, Prozentsatz pro Spalte)
   - Duplikate
   - Ausreißer (IQR-Methode, Z-Score)
   - Inkonsistenzen

4. Korrelationsanalyse:
   - Korrelationsmatrix für numerische Variablen
   - Identifizierung stark korrelierter Features
   - Multikollinearität prüfen

5. Visualisierungen:
   - Histogramme für numerische Variablen
   - Boxplots zur Ausreißererkennung
   - Heatmap der Korrelationen
   - Pairplot für Feature-Beziehungen

6. Erste Erkenntnisse und Hypothesen
```

### Zeitreihenanalyse
```
Analysiere die Zeitreihendaten [Datensatz] mit Fokus auf:

1. Zeitreihen-Eigenschaften:
   - Trend (aufsteigend/absteigend/stabil)
   - Saisonalität (Periode, Amplitude)
   - Zyklische Muster
   - Rauschen/Volatilität

2. Stationarität:
   - Augmented Dickey-Fuller Test
   - KPSS Test
   - Notwendige Transformationen (Differenzierung, Log)

3. Autokorrelation:
   - ACF (Autocorrelation Function)
   - PACF (Partial Autocorrelation Function)
   - Lag-Identifikation

4. Anomalie-Detektion:
   - Statistische Ausreißer
   - Strukturelle Brüche
   - Unerwartete Spikes/Drops

5. Dekomposition:
   - Trend-Komponente
   - Saisonale Komponente
   - Residuale Komponente

6. Prognose-Vorbereitung:
   - Train/Test Split
   - Geeignete Modellansätze (ARIMA, Prophet, LSTM)
```

### Segmentierungsanalyse
```
Führe eine Segmentierungsanalyse für [Datensatz] durch:

1. Feature-Engineering:
   - Relevante Features identifizieren
   - Feature-Skalierung/Normalisierung
   - Dimensionsreduktion (PCA, t-SNE)

2. Clustering-Ansätze:
   - K-Means (optimale K-Wert-Bestimmung via Elbow/Silhouette)
   - Hierarchisches Clustering (Dendrogram)
   - DBSCAN (Density-based)
   - Gaussian Mixture Models

3. Cluster-Evaluation:
   - Silhouette Score
   - Davies-Bouldin Index
   - Calinski-Harabasz Score
   - Within-Cluster Sum of Squares (WCSS)

4. Segment-Profile:
   - Größe jedes Segments
   - Charakteristische Merkmale pro Segment
   - Zentroide/Repräsentanten
   - Unterscheidungsmerkmale zwischen Segmenten

5. Business-Interpretation:
   - Segment-Beschreibungen in Business-Begriffen
   - Actionable Insights pro Segment
   - Empfohlene Strategien pro Segment

6. Visualisierung:
   - 2D/3D Scatter Plots der Cluster
   - Feature-Verteilungen pro Cluster
   - Radar Charts für Segment-Profile
```

## Prozessanalyse-Prompts

### Prozesseffizienz-Analyse
```
Analysiere den Prozess [Prozessname] hinsichtlich Effizienz:

1. Prozess-Metriken:
   - Durchlaufzeit (Lead Time)
   - Bearbeitungszeit (Processing Time)
   - Wartezeit (Waiting Time)
   - Zykluszeit (Cycle Time)

2. Engpass-Analyse:
   - Identifizierung von Bottlenecks
   - Kapazitätsauslastung pro Prozessschritt
   - Warteschlangen-Längen
   - Ressourcen-Constraints

3. Verschwendung (Waste):
   - Überproduktion
   - Wartezeiten
   - Unnötige Transporte
   - Überbearbeitung
   - Bestände
   - Bewegung
   - Fehler/Nacharbeit

4. Wertstrom-Analyse:
   - Wertschöpfende Aktivitäten (Value-Add)
   - Nicht-wertschöpfende aber notwendige Aktivitäten (Non-Value-Add)
   - Verschwendung (Waste)
   - Value-Add Ratio berechnen

5. Variabilität:
   - Standardabweichung der Durchlaufzeiten
   - Prozessstabilität
   - Sonderfälle und Ausnahmen

6. Verbesserungspotenziale:
   - Quick Wins (geringer Aufwand, hoher Impact)
   - Strategische Verbesserungen (hoher Aufwand, hoher Impact)
   - Priorisierung nach Impact/Aufwand-Matrix
```

### Root-Cause-Analyse
```
Führe eine Root-Cause-Analyse für [Problem/Fehler] durch:

1. Problem-Definition:
   - Präzise Beschreibung des Problems
   - Häufigkeit und Muster
   - Impact (Kosten, Zeit, Qualität)
   - Betroffene Stakeholder

2. 5-Why-Analyse:
   - Warum tritt das Problem auf? [Antwort 1]
   - Warum [Antwort 1]? [Antwort 2]
   - Warum [Antwort 2]? [Antwort 3]
   - Warum [Antwort 3]? [Antwort 4]
   - Warum [Antwort 4]? [Root Cause]

3. Fishbone-Analyse (Ishikawa):
   Kategorien: Menschen, Methoden, Maschinen, Material, Messung, Umwelt
   - Potenzielle Ursachen pro Kategorie
   - Haupt- und Nebenursachen
   - Zusammenhänge zwischen Ursachen

4. Datensammlung:
   - Relevante Daten und Logs
   - Zeitpunkt des Auftretens
   - Umgebungsbedingungen
   - Beteiligte Systeme/Personen

5. Hypothesen-Validierung:
   - Hypothese 1: [Beschreibung] → Test: [Methode] → Ergebnis: [Bestätigt/Widerlegt]
   - Hypothese 2: [Beschreibung] → Test: [Methode] → Ergebnis: [Bestätigt/Widerlegt]

6. Lösungsempfehlungen:
   - Kurzfristige Maßnahmen (Symptombekämpfung)
   - Langfristige Maßnahmen (Root-Cause-Beseitigung)
   - Präventionsmaßnahmen
```

### Compliance-Analyse
```
Analysiere [Prozess/System] auf Compliance mit [Standard/Regulation]:

1. Anforderungs-Mapping:
   - Liste aller relevanten Anforderungen aus [Standard]
   - Mapping zu aktuellen Prozessschritten/Kontrollen
   - Gap-Identifikation

2. Kontroll-Bewertung:
   | Anforderung | Kontrollmaßnahme | Implementiert | Effektivität | Evidenz | Gap |
   |-------------|------------------|---------------|--------------|---------|-----|
   | [ID] | [Beschreibung] | [Ja/Teilweise/Nein] | [Hoch/Mittel/Niedrig] | [Link/Dokument] | [Beschreibung] |

3. Risiko-Assessment:
   - Identifizierte Compliance-Risiken
   - Wahrscheinlichkeit und Impact
   - Risiko-Score und Priorisierung

4. Dokumentations-Review:
   - Vorhandene Dokumentation
   - Vollständigkeit und Aktualität
   - Fehlende Dokumentation

5. Audit-Trail:
   - Nachvollziehbarkeit von Änderungen
   - Logging und Monitoring
   - Aufbewahrungsfristen

6. Remediation-Plan:
   - Maßnahmen zur Schließung der Gaps
   - Verantwortlichkeiten
   - Timeline
   - Kosten-Nutzen-Analyse
```

## System-Analyse-Prompts

### Architektur-Review
```
Führe ein Architektur-Review für [System] durch:

1. Architektur-Prinzipien:
   - Einhaltung von Best Practices (SOLID, 12-Factor-App, etc.)
   - Separation of Concerns
   - Loose Coupling, High Cohesion
   - Skalierbarkeit und Erweiterbarkeit

2. Technologie-Stack:
   - Aktualität der verwendeten Technologien
   - End-of-Life und Support-Status
   - Technologie-Fit für Use Case
   - Alternativen und Modernisierungsoptionen

3. Skalierbarkeit:
   - Horizontale vs. Vertikale Skalierung
   - Stateless vs. Stateful Components
   - Caching-Strategien
   - Load Balancing

4. Resilienz:
   - Single Points of Failure
   - Fehlertoleranz-Mechanismen (Retry, Circuit Breaker, Bulkhead)
   - Graceful Degradation
   - Disaster Recovery

5. Sicherheit:
   - Authentication und Authorization
   - Verschlüsselung (in Transit, at Rest)
   - Input Validation und Sanitization
   - Secrets Management
   - Security Vulnerabilities (OWASP Top 10)

6. Performance:
   - Response Time Analyse
   - Throughput und Latenz
   - Resource Utilization
   - Performance Bottlenecks
   - Optimization Opportunities

7. Wartbarkeit:
   - Code Quality (Complexity, Duplication, Test Coverage)
   - Dokumentation
   - Deployment-Prozess
   - Monitoring und Observability

8. Empfehlungen:
   - Kritische Probleme (sofortige Maßnahmen erforderlich)
   - Mittelfristige Verbesserungen
   - Langfristige strategische Änderungen
```

### Dependency-Analyse
```
Analysiere die Abhängigkeiten von [System]:

1. Dependency-Mapping:
   - Direkte Abhängigkeiten (1st level)
   - Transitive Abhängigkeiten (2nd+ level)
   - Visualisierung als Dependency Graph

2. Dependency-Bewertung:
   | Dependency | Version | Latest Version | License | Vulnerabilities | Maintainance Status | Kritikalität |
   |------------|---------|----------------|---------|-----------------|---------------------|--------------|
   | [Name] | [X.Y.Z] | [A.B.C] | [MIT/Apache/etc.] | [CVE-IDs] | [Active/Deprecated] | [Hoch/Mittel/Niedrig] |

3. Risiko-Analyse:
   - Veraltete Dependencies (Major Versions hinter Latest)
   - Bekannte Sicherheitslücken (CVE-Analyse)
   - Deprecated/Unmaintained Libraries
   - License-Compliance-Risiken

4. Zirkuläre Abhängigkeiten:
   - Identifikation von Circular Dependencies
   - Impact auf Build-Zeit und Wartbarkeit
   - Refactoring-Empfehlungen

5. Dependency-Konflikte:
   - Version-Konflikte
   - Transitive Dependency-Probleme
   - Resolution-Strategien

6. Update-Strategie:
   - Priorisierung von Updates (Security > Major > Minor > Patch)
   - Breaking Changes Assessment
   - Test-Strategie für Updates
   - Rollback-Plan
```

### Integration-Analyse
```
Analysiere die Integrationen von [System]:

1. Integration-Inventar:
   | Integration | Typ | Protokoll | Datenformat | Frequenz | Kritikalität | Owner |
   |-------------|-----|-----------|-------------|----------|--------------|-------|
   | [System] | [Inbound/Outbound] | [REST/SOAP/etc.] | [JSON/XML] | [Real-time/Batch] | [Hoch/Mittel/Niedrig] | [Team] |

2. Integration-Patterns:
   - Request-Response
   - Event-Driven (Pub/Sub)
   - Batch Processing
   - Stream Processing
   - Pattern-Fit für Use Case

3. Fehlerbehandlung:
   - Retry-Mechanismen
   - Dead Letter Queues
   - Circuit Breaker Implementation
   - Timeout-Konfiguration
   - Fehler-Logging und Alerting

4. Datenqualität:
   - Schema-Validierung
   - Data Transformation und Mapping
   - Inkonsistenzen zwischen Systemen
   - Data Loss Prevention

5. Performance:
   - Latenz pro Integration
   - Throughput und Datenvolumen
   - Rate Limiting
   - Caching-Strategien

6. Monitoring:
   - Health Checks
   - SLA-Monitoring
   - Error Rates
   - Dashboards und Alerting

7. Verbesserungsempfehlungen:
   - Konsolidierung redundanter Integrationen
   - Modernisierung veralteter Protokolle
   - Einführung von API Gateway/Service Mesh
   - Standardisierung von Integration-Patterns
```

## Geschäftsanalyse-Prompts

### Stakeholder-Analyse
```
Führe eine Stakeholder-Analyse für [Projekt/Initiative] durch:

1. Stakeholder-Identifikation:
   | Stakeholder | Rolle | Organisation | Einfluss | Interesse | Haltung |
   |-------------|-------|--------------|----------|-----------|---------|
   | [Name] | [Position] | [Abteilung] | [Hoch/Mittel/Niedrig] | [Hoch/Mittel/Niedrig] | [Unterstützer/Neutral/Gegner] |

2. Power-Interest-Matrix:
   - Hoher Einfluss, Hohes Interesse: [Stakeholder] → Strategie: Eng einbinden
   - Hoher Einfluss, Niedriges Interesse: [Stakeholder] → Strategie: Zufriedenstellen
   - Niedriger Einfluss, Hohes Interesse: [Stakeholder] → Strategie: Informieren
   - Niedriger Einfluss, Niedriges Interesse: [Stakeholder] → Strategie: Beobachten

3. Stakeholder-Bedürfnisse:
   - [Stakeholder]: [Bedürfnisse, Erwartungen, Bedenken]

4. Kommunikationsplan:
   | Stakeholder | Informationsbedarf | Frequenz | Kanal | Verantwortlich |
   |-------------|-------------------|----------|-------|----------------|
   | [Name] | [Was wird kommuniziert] | [täglich/wöchentlich/etc.] | [Email/Meeting/etc.] | [Person] |

5. Risiken:
   - Widerstand von [Stakeholder]: [Mitigation-Strategie]
   - Mangelnde Unterstützung von [Stakeholder]: [Mitigation-Strategie]

6. Engagement-Strategie:
   - Maßnahmen zur Gewinnung von Unterstützern
   - Umgang mit Gegnern und Bedenken
   - Change Management Ansatz
```

### Gap-Analyse
```
Führe eine Gap-Analyse für [Bereich/Prozess/System] durch:

1. Ist-Zustand (Current State):
   - Detaillierte Beschreibung des aktuellen Zustands
   - Stärken
   - Schwächen
   - Metriken und KPIs

2. Soll-Zustand (Future State):
   - Vision und Ziele
   - Erwartete Verbesserungen
   - Ziel-Metriken und KPIs

3. Gap-Identifikation:
   | Dimension | Ist-Zustand | Soll-Zustand | Gap | Priorität | Impact |
   |-----------|-------------|--------------|-----|-----------|--------|
   | [Aspekt] | [Beschreibung] | [Beschreibung] | [Differenz] | [Hoch/Mittel/Niedrig] | [Beschreibung] |

4. Root-Cause der Gaps:
   - Warum existiert dieser Gap?
   - Welche Faktoren tragen dazu bei?
   - Strukturelle vs. temporäre Ursachen

5. Lösungsoptionen:
   | Gap | Option 1 | Option 2 | Option 3 | Empfehlung |
   |-----|----------|----------|----------|------------|
   | [Gap-ID] | [Beschreibung, Aufwand, Nutzen] | [Beschreibung, Aufwand, Nutzen] | [Beschreibung, Aufwand, Nutzen] | [Begründung] |

6. Roadmap:
   - Phase 1 (Quick Wins): [Maßnahmen, Timeline]
   - Phase 2 (Foundation): [Maßnahmen, Timeline]
   - Phase 3 (Transformation): [Maßnahmen, Timeline]

7. Erfolgskriterien:
   - Wie wird Erfolg gemessen?
   - Meilensteine und Checkpoints
   - KPIs zur Fortschrittsmessung
```

### Kosten-Nutzen-Analyse
```
Führe eine Kosten-Nutzen-Analyse für [Projekt/Initiative] durch:

1. Kostenaufstellung:
   
   **Einmalige Kosten:**
   | Kostenart | Beschreibung | Betrag | Annahmen |
   |-----------|--------------|--------|----------|
   | Entwicklung | [Details] | € X | [Annahmen] |
   | Lizenzen | [Details] | € X | [Annahmen] |
   | Hardware | [Details] | € X | [Annahmen] |
   | Training | [Details] | € X | [Annahmen] |
   | **Summe Einmalig** | | **€ X** | |
   
   **Laufende Kosten (pro Jahr):**
   | Kostenart | Beschreibung | Betrag | Annahmen |
   |-----------|--------------|--------|----------|
   | Wartung | [Details] | € X | [Annahmen] |
   | Support | [Details] | € X | [Annahmen] |
   | Betrieb | [Details] | € X | [Annahmen] |
   | **Summe Laufend** | | **€ X/Jahr** | |

2. Nutzenaufstellung:
   
   **Quantifizierbare Nutzen (pro Jahr):**
   | Nutzenart | Beschreibung | Betrag | Annahmen |
   |-----------|--------------|--------|----------|
   | Zeitersparnis | [X Stunden * Y €/Stunde] | € X | [Annahmen] |
   | Fehlerreduktion | [X Fehler * Y € Kosten/Fehler] | € X | [Annahmen] |
   | Umsatzsteigerung | [Details] | € X | [Annahmen] |
   | **Summe Quantifizierbar** | | **€ X/Jahr** | |
   
   **Qualitative Nutzen:**
   - [Nutzen 1]: [Beschreibung und erwarteter Impact]
   - [Nutzen 2]: [Beschreibung und erwarteter Impact]

3. ROI-Berechnung:
   ```
   Gesamtkosten (3 Jahre) = Einmalige Kosten + (Laufende Kosten * 3)
   Gesamtnutzen (3 Jahre) = Quantifizierbare Nutzen * 3
   
   ROI = (Gesamtnutzen - Gesamtkosten) / Gesamtkosten * 100%
   
   Break-Even-Point = Einmalige Kosten / (Jährlicher Nutzen - Jährliche Kosten)
   ```

4. Sensitivitätsanalyse:
   - Best Case: [ROI bei optimistischen Annahmen]
   - Base Case: [ROI bei realistischen Annahmen]
   - Worst Case: [ROI bei pessimistischen Annahmen]

5. Nicht-finanzielle Faktoren:
   - Strategische Bedeutung
   - Risiko-Reduktion
   - Compliance-Anforderungen
   - Wettbewerbsvorteil

6. Empfehlung:
   - Investition empfohlen: [Ja/Nein/Bedingt]
   - Begründung
   - Voraussetzungen für Erfolg
   - Risiken und Mitigation
```
