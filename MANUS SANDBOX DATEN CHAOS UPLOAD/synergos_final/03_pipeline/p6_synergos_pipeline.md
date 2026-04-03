# P6 Synergos: Der 12-Stufen-Pipeline-Workflow (Die Signalkette)

**Status:** Aktiviert | **System:** Synergos | **Methode:** Curie (Extraktion) + Feynman (Einfachheit) + Allen (GTD-Flow)

Dieses Dokument ist der Master-Bauplan für Sektor 2. Es transformiert die 6 Design-Axiome aus P2 und den Kern-Prompt aus P5 in eine ausführbare 12-Stufen-Pipeline (Signalkette). Das Ziel: Eine rohe Alltagsanforderung – zum Beispiel "Ich muss meine Projekt-Emails sortieren und Aufgaben ableiten" – wird in einen fertigen, ausführbaren Master-Export verwandelt. Jede Stufe ist ein Plugin in der Kette. Fehlt eins oder ist es falsch konfiguriert, fällt die Murmel ins Loch und der Mix ist im Arsch.

> **Das Murmelbahnprinzip:** Signal geht rein oben (rohe Idee), läuft durch 12 Plugins (Stufen), kommt unten als fertiger Bounce (Master-Export) raus. Keine Lücken, kein Raten, kein Matsch.

---

## ABSCHNITT 1: PIPELINE-ÜBERSICHT (Das Patchbay)

Die 12 Stufen der Signalkette verteilen sich auf 4 Dimensionen (Frequenzbänder). Jede Dimension ist ein Abschnitt im Mixer. Die Erfassung nimmt das Rohsignal auf, die Strukturierung routet es in die richtigen Busse, die Verarbeitung wendet die Effektkette an, und die Validierung prüft den Mix vor dem Master-Export. Hier ist das komplette Routing-Setup:

| Stufe | Name (Plugin) | Dimension (Frequenzband) | Axiom-Bezug (Regler) | Genie-Methode (Vocal Preset) |
| :---: | :--- | :--- | :--- | :--- |
| 1 | Rohsignal-Aufnahme | Erfassung (Input) | – | Allen (Sammeln) |
| 2 | Nullpunkt-Scan | Erfassung (Input) | A1 (Nullpunkt-Kalibrierung) | Feynman (Identifizieren) |
| 3 | Frequenz-Trennung | Erfassung (Input) | – | Curie (Isolieren) |
| 4 | Format-Pressung | Strukturierung (Routing) | A4 (Format-Schablone) | Curie (Kategorisieren) |
| 5 | Signal-Routing | Strukturierung (Routing) | A2 (Zweckbindung) | Allen (Klären) |
| 6 | Architektur-Bauplan | Strukturierung (Routing) | A3 (Architektur-Zwang) | Feynman (Strukturieren) |
| 7 | Plugin-Kette laden | Verarbeitung (Mix) | A5 (Frequenz-Hierarchie) | Curie (Regelwerk) |
| 8 | Kaskaden-Verarbeitung | Verarbeitung (Mix) | R2 (Kaskaden-Bindung) | Allen (Organisieren) |
| 9 | Hierarchie-Resonanz | Verarbeitung (Mix) | R3 (Hierarchie-Resonanz) | Feynman (Vereinfachen) |
| 10 | A/B-Referenz-Check | Validierung (Mastering) | A6 (Feedback-Loop) | Curie (Messen) |
| 11 | UOP-Gate (3+1 Check) | Validierung (Mastering) | – | Feynman (Erklären) |
| 12 | Master-Export | Validierung (Mastering) | – | Allen (Engagieren) |

Der Signalfluss ist streng linear: Stufe 1 speist Stufe 2, Stufe 2 speist Stufe 3 – bis Stufe 12 den finalen Bounce ausspuckt. Kein Plugin darf übersprungen werden. Wenn Stufe 6 (Architektur-Bauplan) kein "Go" vom Nutzer bekommt, bleibt die Kette stehen. Das ist kein Bug, das ist das Design.

---

## ABSCHNITT 2: DIE 12 STUFEN IM DETAIL (Die Signalkette)

Hier wird jedes Plugin in der Signalkette aufgeschlüsselt. Für jede Stufe gibt es sieben Informationsblöcke: Name, Dimension, Axiom-Bezug, Handlungsanweisung, ein konkretes Input-Output-Beispiel aus der Praxis, Systemgrenzen mit drei Umgehungsstrategien, und eine Modularitätsbeschreibung. Der Signalfluss beginnt mit der rohen Idee und endet mit dem fertigen Master-Bounce.

---

### Stufe 1: Rohsignal-Aufnahme

**Dimension:** Erfassung | **Axiom-Bezug:** – (Grundvoraussetzung) | **Genie-Methode:** Allen (Sammeln)

**Handlungsanweisung:** Der Nutzer wirft sein unstrukturiertes Problem in den Mixer – ohne Filter, ohne Formatierung, ohne Vorarbeit. Das System nimmt alles auf, was reinkommt. Wie ein offenes Mikrofon im Studio: Erst mal aufnehmen, dann sortieren.

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** | "Ich habe 50 Mails im Projektordner und weiß nicht, was ich zuerst tun soll." |
| **Output** | Rohtext-Objekt mit Metadaten: `{menge: 50, kontext: "Projekt X", typ: "E-Mail", format: "unstrukturiert"}` |

**Systemgrenzen und Umgehungsstrategien:** Das Token-Limit von 8k bei `gpt-4.1-mini` ist die erste Wand. Wenn der Chaos-Ordner zu groß ist, bricht der Request ab, bevor das Signal überhaupt im Mixer ankommt. Drei Strategien, um das zu umgehen: Erstens, die Mails in 10er-Blöcke chunken – Stems bouncen, bevor der RAM überläuft. Zweitens, auf Gemini (1M Token Kontextfenster) umschalten, wenn die Rohdaten gigantisch sind. Drittens, nur die Header und Betreffzeilen extrahieren statt den vollen Body – das reduziert das Signalvolumen um 80-90%.

**Modularität:** Das Input-Modul ist komplett austauschbar. Statt Text kann hier ein Audio-Transkript (via `manus-speech-to-text`), ein PDF-Dump, ein Notion-Export oder ein Screenshot reinkommen. Die Stufe kümmert sich nicht um das Format – sie nimmt alles auf.

---

### Stufe 2: Nullpunkt-Scan

**Dimension:** Erfassung | **Axiom-Bezug:** A1 (Nullpunkt-Kalibrierung) | **Genie-Methode:** Feynman (Identifizieren)

**Handlungsanweisung:** Das System stoppt die Verarbeitung und fragt den aktuellen Ist-Zustand des Nutzers ab. Keine Durchschnittsannahmen, keine Vermutungen. Bevor ein Track produziert wird, muss das BPM klar sein. Wie viel Zeit ist da? Wie viel Energie? Welches Vorwissen existiert? Ohne diesen Scan arbeitet das System mit Phantomwerten – und der Mix klingt nach Durchschnitt.

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** (System fragt) | "Wie viel Zeit hast du heute für diese 50 Mails? Energielevel 1-10?" |
| **Output** (Nutzer antwortet) | "30 Minuten. Energielevel 4. Ich brauche nur die wichtigsten Aktionen." |

**Systemgrenzen und Umgehungsstrategien:** Das Hauptproblem ist der fehlende dauerhafte Kontexterhalt über Sessions hinweg. Das System vergisst den Nullpunkt beim nächsten Start komplett – als ob jemand den Mixer-State nicht gespeichert hat. Strategie 1: Den Nullpunkt in einer Notion-Datenbank speichern (via MCP), damit er beim nächsten Start geladen werden kann. Strategie 2: Einen zwingenden Pre-Flight-Check bei jedem neuen Task-Start einbauen – das System fragt immer, auch wenn es nervt. Strategie 3: Ein festes `user_context.md` File im `/home/ubuntu` Ordner pflegen, das als persistenter Nullpunkt-Speicher dient.

**Modularität:** Der Nullpunkt-Scan kann von "Zeit und Energie" (Allen-Logik für GTD-Produktivität) auf "Vorwissen und Lernstand" (Feynman-Logik für Didaktik) umgestellt werden. Bei einem Musik-Projekt fragt das System nach "Welches Genre? Welche DAW-Erfahrung?" statt nach "Wie viel Zeit?".

---

### Stufe 3: Frequenz-Trennung

**Dimension:** Erfassung | **Axiom-Bezug:** – (Vorbereitung für das Routing) | **Genie-Methode:** Curie (Isolieren)

**Handlungsanweisung:** Das System zerlegt das Rohsignal in atomare, voneinander unabhängige Bestandteile. Frequenzen trennen – wie beim EQ: Bässe, Mitten und Höhen auf separate Busse legen, damit sie einzeln bearbeitet werden können. Kein Matsch, kein Übersprechen.

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** | Rohtext-Objekt (50 Mails, 30 Min Zeit, Energielevel 4) |
| **Output** | Drei getrennte Arrays: `[Informations-Mails: 20]`, `[Aktions-Mails: 15]`, `[Spam/Irrelevant: 15]` |

**Systemgrenzen und Umgehungsstrategien:** Die CPU-Leistung der Sandbox (3 Kerne, Intel Xeon) limitiert extrem komplexe NLP-Zerlegungen in Echtzeit. Strategie 1: Die Kategorisierung an den LLM-Proxy (`gpt-4.1-mini`) auslagern – der macht das in Sekunden, was ein lokales Script Minuten braucht. Strategie 2: Regex-Muster für einfache Trennungen nutzen (z.B. Absender-Domains für Spam-Erkennung) – schneller und billiger als ein LLM-Call. Strategie 3: Bei Hunderten von Dateien auf parallele Verarbeitung (Map-Reduce-Logik) setzen.

**Modularität:** Die Trennungslogik ist der austauschbare Kern dieser Stufe. Bei E-Mails trennt sie nach "Info/Aktion/Spam". Bei Songtexten trennt sie nach "Strophe/Refrain/Bridge". Bei philosophischen Notizen nach "These/Argument/Frage". Das Plugin bleibt gleich, nur die Trennkriterien ändern sich.

---

### Stufe 4: Format-Pressung

**Dimension:** Strukturierung | **Axiom-Bezug:** A4 (Format-Schablone) | **Genie-Methode:** Curie (Kategorisieren)

**Handlungsanweisung:** Jeder getrennte Bestandteil wird in ein starres, maschinenlesbares Format gepresst. Kein theoretisches Gelaber, keine Prosa, keine "Zusammenfassung in eigenen Worten". Das Signal wird in eine Schablone gezwungen – wie ein Kompressor, der das Dynamikspektrum auf einen definierten Bereich presst.

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** | Array `[Aktions-Mails: 15]` |
| **Output** | Markdown-Tabelle: `| ID | Absender | Betreff | Aktion | Prio | Deadline |` mit 15 Zeilen |

**Systemgrenzen und Umgehungsstrategien:** LLMs tendieren zu "Chattiness" – sie fügen unaufgefordert Erklärungen, Einleitungen und Schlussworte hinzu, die niemand braucht. Strategie 1: Harter System-Prompt mit der Anweisung "Antworte AUSSCHLIESSLICH mit der Tabelle. Kein Text davor oder danach." Strategie 2: JSON-Mode erzwingen, wenn der Call über die API läuft – dann ist das Ausgabeformat technisch fixiert. Strategie 3: Ein Post-Processing Script in der Sandbox, das alles außerhalb der `|...|` Syntax automatisch löscht.

**Modularität:** Die Schablone selbst ist beliebig austauschbar. Markdown-Tabelle, JSON, YAML, CSV – das Format richtet sich nach dem Ziel-Plugin in Stufe 5. Wenn Linear JSON braucht, liefert Stufe 4 JSON. Wenn der Nutzer eine Tabelle lesen will, liefert sie Markdown.

---

### Stufe 5: Signal-Routing

**Dimension:** Strukturierung | **Axiom-Bezug:** A2 (Zweckbindung) | **Genie-Methode:** Allen (Klären)

**Handlungsanweisung:** Das formatierte Signal wird zwingend dem richtigen Tool oder MCP-Server zugewiesen – basierend auf dessen nachgewiesener Stärke, nicht auf Vermutung. Kein Raten, welches Plugin den Job macht. Das ist der Mixer-Bus: Jede Spur geht in den richtigen Kanal.

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** | Formatierte Tabelle mit 10 "To-Do"-Mails (Prio 1-3) |
| **Output** | Routing-Entscheidung: Prio 1 → `linear` (Issue-Tracking), Prio 2 → `notion` (Projektnotiz), Prio 3 → `gmail` (Antwort-Draft) |

**Systemgrenzen und Umgehungsstrategien:** Fehlende oder kaputte MCP-Verbindungen sind das Hauptrisiko – wie der 400er Fehler beim xAI Key aus P1. Strategie 1: Automatischer Fallback auf ein lokales Textfile (`todo.md`), wenn der Ziel-MCP-Server nicht erreichbar ist. Strategie 2: Try-Catch-Blöcke in der Routing-Logik, die Fehler abfangen und den Nutzer informieren statt abzustürzen. Strategie 3: Ping-Test des MCP-Servers vor dem finalen Routing – wenn der Server nicht antwortet, wird sofort auf den Fallback umgeschaltet.

**Modularität:** Das Ziel-Plugin kann jederzeit getauscht werden. Von Linear zu Monday.com, von Notion zu Airtable, von Gmail zu einem lokalen Markdown-File. Die Routing-Logik bleibt identisch – nur die Zieladresse ändert sich. Das ist der Kern der Zweckbindung: Das Tool wird dem Task zugewiesen, nicht umgekehrt.

---

### Stufe 6: Architektur-Bauplan

**Dimension:** Strukturierung | **Axiom-Bezug:** A3 (Architektur-Zwang) | **Genie-Methode:** Feynman (Strukturieren)

**Handlungsanweisung:** Bevor das Routing ausgeführt wird, präsentiert das System den methodischen Plan (die Murmelbahn) und wartet auf die explizite Freigabe des Nutzers. Kein Bounce ohne Go. Das System zeigt das Arrangement, der Producer entscheidet, ob es passt.

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** | Routing-Entscheidung aus Stufe 5 |
| **Output** | "Plan: 5 Issues in Linear anlegen (Prio 1), 3 Notizen in Notion (Prio 2), 2 Antwort-Drafts in Gmail (Prio 3). Hier ist die Liste. Go?" |

**Systemgrenzen und Umgehungsstrategien:** Das asynchrone Telegram-Polling ist das Nadelöhr. Der Nutzer antwortet vielleicht erst Stunden später – und die Sandbox geht in der Zwischenzeit schlafen. Strategie 1: Den kompletten State (Plan, Routing-Entscheidung, Fortschritt) in `/home/ubuntu/state.json` speichern, bevor die Sandbox hiberniert. Strategie 2: Bei Wiedererwachen liest das System den State-File und macht exakt dort weiter, wo es aufgehört hat. Strategie 3: Klare Timeout-Regeln definieren – nach 24 Stunden ohne Antwort wird der Plan verworfen und der Nutzer bekommt eine Zusammenfassung.

**Modularität:** Der Detailgrad des Bauplans ist anpassbar. Für Routineaufgaben reicht ein Einzeiler ("10 Tickets anlegen, Go?"). Für komplexe Projekte wird ein vollständiger JSON-Payload mit allen Feldern angezeigt. Der Nutzer entscheidet über die Granularität.

---

### Stufe 7: Plugin-Kette laden

**Dimension:** Verarbeitung | **Axiom-Bezug:** A5 (Frequenz-Hierarchie) | **Genie-Methode:** Curie (Regelwerk)

**Handlungsanweisung:** Nach dem "Go" des Nutzers lädt das System die übergeordneten Master-Regeln aus dem P5 Kern-Prompt und stellt sicher, dass sie nicht von der aktuellen Aufgabe überschrieben werden. Die Lade-Reihenfolge ist unumstößlich: Erst die Master-Regeln (Axiome), dann die Task-Regeln. Wie beim Laden eines Templates in FL Studio – erst das Grundgerüst, dann die individuellen Plugins.

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** | Nutzer-Go plus Zusatz: "Mach das schnell und unkompliziert, ohne die ganzen Metaphern." |
| **Output** | System lädt Master-Regeln (A5: "FL-Studio-Metaphern sind Pflicht") und ignoriert den Wunsch "ohne Metaphern", weil er der Frequenz-Hierarchie widerspricht. |

**Systemgrenzen und Umgehungsstrategien:** Context Window Overlap ist das kritische Problem. Zu viele System-Prompts fressen den 8k Token RAM auf, bevor die eigentliche Aufgabe überhaupt beginnt. Strategie 1: Strikte Kompression der Master-Regeln – genau wie in P5 geschehen, wo 8 Probleme auf 6 Axiome verdichtet wurden. Strategie 2: Dynamisches Laden nur der relevanten Axiome für den spezifischen Task – bei einer E-Mail-Sortierung braucht man A4 (Format) und A2 (Routing), aber nicht zwingend A6 (A/B-Referenz). Strategie 3: Nutzung von Kürzeln und Tags (`[A1]`, `[A4]`) statt voll ausgeschriebener Regeln.

**Modularität:** Die Master-Regeln selbst sind das austauschbare Modul. Der P5 Kern-Prompt (mit FL-Studio-Metaphern und dem 3+1 Dreiklang) kann durch ein komplett anderes "Vocal Preset" ersetzt werden – zum Beispiel ein formelles Business-Preset ohne Metaphern oder ein technisches Preset für Code-Reviews.

---

### Stufe 8: Kaskaden-Verarbeitung

**Dimension:** Verarbeitung | **Axiom-Bezug:** R2 (Kaskaden-Bindung) aus P5 | **Genie-Methode:** Allen (Organisieren)

**Handlungsanweisung:** Das System arbeitet die Aufgabe streng sequenziell in If-Then-Schritten ab. Kein Schritt wird übersprungen, kein Schritt wird parallel ausgeführt (es sei denn, die Modularität erlaubt es). Wie eine Kaskade im Mixer: Das Signal fließt von Effekt zu Effekt, und jeder Effekt baut auf dem Ergebnis des vorherigen auf.

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** | Auftrag: 5 Issues in Linear anlegen |
| **Output** | "Schritt 1/5: Issue 'Budget-Review' angelegt. Schritt 2/5: Issue 'Kundenfeedback' angelegt. [...] Schritt 5/5: Abgeschlossen." |

**Systemgrenzen und Umgehungsstrategien:** Sandbox-Timeouts bei langlaufenden Schleifen sind das Risiko. Wenn 50 API-Calls nacheinander laufen, kann die Session ablaufen. Strategie 1: Batch-Processing – alle Tickets in einem einzigen API-Call anlegen, falls der MCP-Server das unterstützt. Strategie 2: Checkpointing nach jedem Schritt – der Fortschritt wird in `/home/ubuntu/progress.json` gespeichert, damit bei einem Timeout nicht von vorne begonnen werden muss. Strategie 3: Asynchrone Ausführung mit Status-Updates an den Nutzer via Telegram.

**Modularität:** Die Schleifenlogik kann von sequenziell (maximale Sicherheit, jeder Fehler wird sofort erkannt) auf parallel (maximale Geschwindigkeit, aber Fehler werden erst am Ende sichtbar) umgestellt werden. Für kritische Operationen (Datenbank-Writes) bleibt es sequenziell. Für unkritische (Lese-Operationen) kann parallelisiert werden.

---

### Stufe 9: Hierarchie-Resonanz

**Dimension:** Verarbeitung | **Axiom-Bezug:** R3 (Hierarchie-Resonanz) aus P5 | **Genie-Methode:** Feynman (Vereinfachen)

**Handlungsanweisung:** Das System passt die Detailtiefe der Verarbeitung proportional an die Gliederung des Inputs an. Ein langer, strukturierter Input bekommt einen langen, strukturierten Output. Ein Einzeiler bekommt einen Einzeiler zurück. Das Echo-Prinzip (R1) und die Hierarchie-Resonanz (R3) arbeiten hier zusammen – die Form des Inputs bestimmt die Form des Outputs.

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** | Mail A: 5 Absätze mit Projektdetails. Mail B: "Passt, danke." |
| **Output** | Ticket A: Titel, Beschreibung, 3 Subtasks, Tags, Deadline. Ticket B: Einzeiler-Ticket "Bestätigung erhalten". |

**Systemgrenzen und Umgehungsstrategien:** Das LLM verliert bei extrem langen Inputs die Gewichtung – der Attention Mechanism priorisiert den Anfang und das Ende, die Mitte geht unter. Strategie 1: Explizite Gewichtungs-Marker im Prompt setzen (`::WICHTIG::`, `::KERN::`), um die Attention auf die relevanten Stellen zu lenken. Strategie 2: Lange Inputs vorab zusammenfassen, bevor sie in die Kaskade gehen – ein Pre-Processing-Schritt, der den Kern extrahiert. Strategie 3: Markdown-Header (`#`, `##`, `###`) als strukturelle Steuerung nutzen, weil LLMs auf Header-Hierarchien besser reagieren als auf Fließtext.

**Modularität:** Die Resonanz-Tiefe ist stufenlos skalierbar. Von der 1:1-Kopie (jedes Detail wird übernommen) bis zur extremen Verdichtung (nur der Kern bleibt). Der Nutzer kann über den Nullpunkt-Scan (Stufe 2) steuern, welche Tiefe er braucht: "Ich will nur die Überschriften" vs. "Ich will alles im Detail".

---

### Stufe 10: A/B-Referenz-Check

**Dimension:** Validierung | **Axiom-Bezug:** A6 (Feedback-Loop) | **Genie-Methode:** Curie (Messen)

**Handlungsanweisung:** Bevor das Ergebnis finalisiert wird, vergleicht das System es mit einem positiven (Referenz A: so soll es aussehen) und/oder negativen (Referenz B: so soll es NICHT aussehen) Beispiel. Die Abweichung wird messbar gemacht. Kein "sieht gut aus" – sondern "Abweichung in Feld X: Tags fehlen. Korrektur durchgeführt."

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** | Generiertes Linear-Ticket (ohne Tags, ohne Deadline) |
| **Output** | "Vergleich mit Referenz-Ticket A: Abweichung 1: Tags fehlen → 'Prio1' hinzugefügt. Abweichung 2: Deadline fehlt → '2026-03-29' gesetzt." |

**Systemgrenzen und Umgehungsstrategien:** In einer frischen Sandbox existieren keine historischen Referenzdaten. Strategie 1: Hardcodierte Referenz-Beispiele direkt in den System-Prompts hinterlegen – ein "Gold Standard" Ticket, das immer verfügbar ist. Strategie 2: Historische "gute" Tickets aus Linear oder Notion via MCP abrufen, bevor die Generierung startet. Strategie 3: Das Nutzer-Feedback aus dem aktuellen Lauf als sofortige Referenz für den nächsten Lauf speichern – ein selbstlernender Feedback-Loop.

**Modularität:** Die Referenzquelle ist austauschbar. Sie kann intern (hardcodiert im Prompt), extern (Datenbank-Abfrage via MCP) oder dynamisch (letztes Nutzer-Feedback) sein. Das Vergleichsverfahren bleibt immer gleich: Ist-Zustand vs. Soll-Zustand, Abweichungen benennen, Korrekturen durchführen.

---

### Stufe 11: UOP-Gate (3+1 Check)

**Dimension:** Validierung | **Axiom-Bezug:** – (Qualitätskontrolle, soul.md) | **Genie-Methode:** Feynman (Erklären)

**Handlungsanweisung:** Das Ergebnis muss zwingend den 3+1 Dreiklang bestehen, bevor es den Mixer verlässt. Drei Fragen, keine Ausnahme: Was ist es (Erkenntnis/Frequenzscan)? Wie setzt man es um (Umsetzung/Routing)? Wie erklärt man es richtig (Erklärung/Preset speichern)? Plus die +1 Frage: Hat der Producer (Nutzer) die Freigabe erteilt?

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** | Korrigiertes Linear-Ticket nach A/B-Check |
| **Output** | "Erkenntnis: Action-Item mit Deadline. Umsetzung: Liegt als Issue #142 in Linear. Erklärung: Die Spur ist im richtigen Bus geroutet, der Regler steht auf Prio 1." |

**Systemgrenzen und Umgehungsstrategien:** Die Gefahr liegt in repetitiven, nutzlosen Meta-Erklärungen, die Token verschwenden und den Nutzer nerven. Strategie 1: Der 3+1 Check läuft intern als System-Validierung – der Nutzer sieht ihn nur, wenn ein Fehler auftritt. Strategie 2: Strikte Längenbegrenzung von maximal einem Satz pro Ebene. Strategie 3: Bei Routineaufgaben wird das Gate auf "Fast-Pass" gestellt – nur die +1 Freigabe wird eingeholt, die drei Ebenen laufen automatisch im Hintergrund.

**Modularität:** Die Erklärungsebene (FL-Studio-Metaphern) kann durch jede andere Metaphernwelt ersetzt werden. Für einen Business-Kontext wird aus "Die Spur ist im Bus geroutet" ein "Das Ticket ist dem Sprint zugewiesen". Das Gate selbst – die drei Fragen plus Freigabe – bleibt immer identisch.

---

### Stufe 12: Master-Export

**Dimension:** Validierung | **Axiom-Bezug:** – (Das Finale) | **Genie-Methode:** Allen (Engagieren)

**Handlungsanweisung:** Das System holt das finale "Go" des Nutzers ein und führt die tatsächliche Integration in die Zielarchitektur durch. Der Bounce wird exportiert. Die MCP-Calls werden abgefeuert. Die Dateien werden geschrieben. Das ist der Moment, in dem der Master-Regler auf Export geht.

**Praxis-Beispiel:**

| Richtung | Inhalt |
| :--- | :--- |
| **Input** | "Gate bestanden. Darf ich die 5 Issues in Linear und 3 Notizen in Notion scharfschalten?" → Nutzer: "Go." |
| **Output** | Ausführung aller MCP-Calls. Bestätigung: "Master-Export abgeschlossen. 5 Spuren in Linear, 3 in Notion. Keine Fehler." |

**Systemgrenzen und Umgehungsstrategien:** Netzwerkausfälle während des finalen Exports können den gesamten Bounce zerstören. Strategie 1: Transaktions-Logik implementieren – entweder werden alle Calls erfolgreich ausgeführt, oder keiner (Alles oder Nichts). Strategie 2: Lokales Backup der finalen Payloads in `/home/ubuntu/export_backup.json`, damit bei einem Abbruch manuell nachgearbeitet werden kann. Strategie 3: Retry-Mechanismus mit maximal 3 Versuchen bei API-Timeouts, bevor der Nutzer informiert wird.

**Modularität:** Das Export-Ziel ist völlig frei wählbar. API-Call an einen MCP-Server, Datei-Download in die Sandbox, Telegram-Nachricht an den Nutzer, PDF-Export via `manus-md-to-pdf`, oder ein Push an ein Git-Repository. Die Stufe kümmert sich nur um die Ausführung – wohin das Signal geht, entscheidet Stufe 5 (Routing).

---

## ABSCHNITT 3: META-REFLEXION (Das Master-Template)

Diese Pipeline ist kein Zufall und kein theoretisches Konstrukt. Sie ist die direkte, 1:1-Antwort auf die 8 Grundprobleme aus Sektor 1. Jeder Fehler im Mix hat jetzt seinen eigenen Regler. Und die Signalkette ist so gebaut, dass sie als universelles Template für jedes Projekt funktioniert – man tauscht nur die Plugins, nicht den Mixer.

### 1. Die 8 Grundprobleme im Signalfluss

Die folgende Tabelle zeigt, wie jedes der 8 Probleme aus "Ich brauche.txt" in eine konkrete Pipeline-Stufe gegossen wurde. Kein Problem bleibt unbehandelt, kein Regler steht auf Null.

| Problem | Beschreibung | Pipeline-Stufe | Begründung (FL-Studio-Sprache) |
| :--- | :--- | :---: | :--- |
| **P1** | Einstiegsprofil fehlt | **Stufe 2** (Nullpunkt-Scan) | Kein Track startet ohne BPM-Check. Das System fragt den Ist-Zustand ab, bevor es einen einzigen Regler anfasst. |
| **P2** | Regel-Set gegen Analogien | **Stufe 4** (Format-Pressung) | Das Signal wird in eine Tabelle gezwungen. Keine schwammigen Synth-Flächen, keine "ungefähr so"-Antworten. |
| **P3** | Lernpfad mit Rückkopplung | **Stufe 10** (A/B-Referenz-Check) | Wir messen die Abweichung vom perfekten Mix, bevor wir bouncen. Positiv vs. Negativ, messbar, nicht gefühlt. |
| **P4** | Ein-/Ausgabe-Protokoll | **Stufe 4 + 11** (Format-Pressung + UOP-Gate) | Doppelte Absicherung: Erst wird das Format erzwungen, dann prüft das Gate, ob der Output die drei Fragen besteht. |
| **P5** | Rollen-Module & Zwei-Stufen-Ausgabe | **Stufe 6** (Architektur-Bauplan) | Erst das Arrangement zeigen, dann produzieren. Kein Bounce ohne Freigabe. |
| **P6** | Modell-Landkarte | **Stufe 5** (Signal-Routing) | Das richtige Plugin für die richtige Spur. Linear für Issues, Notion für Notizen, Gmail für Mails. |
| **P7** | Feste Konfiguration & Lade-Reihenfolge | **Stufe 7** (Plugin-Kette laden) | Die Master-Regeln aus P5 überschreiben jeden Task-Prompt. Die Frequenz-Hierarchie ist unantastbar. |
| **P8** | Vorlauf-Modus "Plan vor Ergebnis" | **Stufe 6** (Architektur-Bauplan) | Deckungsgleich mit P5. Kein Ergebnis ohne vorherigen Plan. Der Producer hat immer das letzte Wort. |

### 2. Die Universalität der Signalkette

Diese 12 Stufen sind das Grundgerüst (Template) der DAW. Wenn ein neues Projekt gestartet wird, lädt man nicht jedes Mal einen neuen Mixer – man tauscht nur die Plugins (die inhaltsbezogenen Module) auf den Spuren aus. Die Architektur bleibt immer gleich. Um das zu beweisen, hier zwei komplett verschiedene Anwendungsfälle, durchgespielt durch dieselbe Signalkette.

**Beispiel 1: Social-Media-Planung (Der Pop-Track)**

| Stufe | Standard-Pipeline (E-Mail) | Social-Media-Variante | Status |
| :---: | :--- | :--- | :---: |
| 1 | "50 Mails im Ordner" | "Ich brauche 5 Posts für nächste Woche" | Getauscht |
| 2 | "Wie viel Zeit?" | "Welche Plattform? Welche Zielgruppe?" | Getauscht |
| 3 | Info/Aktion/Spam trennen | Themen/Formate/Plattformen trennen | Getauscht |
| 4 | Markdown-Tabelle | Content-Kalender (JSON oder Tabelle) | Getauscht |
| 5 | → Linear, Notion, Gmail | → Notion (Entwürfe), Airtable (Kalender) | Getauscht |
| 6 | "5 Issues anlegen, Go?" | "5 Posts geplant, Go?" | **Gleich** |
| 7 | Master-Regeln laden | Master-Regeln laden | **Gleich** |
| 8 | Tickets sequenziell anlegen | Posts sequenziell entwerfen | **Gleich** |
| 9 | Detailtiefe nach Mail-Länge | Detailtiefe nach Plattform-Anforderung | Getauscht |
| 10 | Vergleich mit Referenz-Ticket | Vergleich mit erfolgreichem Post | Getauscht |
| 11 | 3+1 Dreiklang | 3+1 Dreiklang | **Gleich** |
| 12 | Export nach Linear | Export nach Notion/Airtable | Getauscht |

**Beispiel 2: Business-Analyse (Der Orchester-Score)**

| Stufe | Standard-Pipeline (E-Mail) | Business-Analyse-Variante | Status |
| :---: | :--- | :--- | :---: |
| 1 | "50 Mails im Ordner" | "PDF-Dump der Quartalszahlen" | Getauscht |
| 2 | "Wie viel Zeit?" | "Welcher Zeitraum? Welche KPIs?" | Getauscht |
| 3 | Info/Aktion/Spam trennen | Umsatz/Kosten/Risiken isolieren | Getauscht |
| 4 | Markdown-Tabelle | Pivot-Tabelle oder JSON-Dataset | Getauscht |
| 5 | → Linear, Notion, Gmail | → Supabase (Daten), Notion (Report) | Getauscht |
| 6 | "5 Issues anlegen, Go?" | "Analyse-Struktur: 3 KPIs, Go?" | **Gleich** |
| 7 | Master-Regeln laden | Master-Regeln laden (+ "Bleib sachlich") | **Gleich** |
| 8 | Tickets sequenziell anlegen | KPIs sequenziell berechnen | **Gleich** |
| 9 | Detailtiefe nach Mail-Länge | Detailtiefe nach Datenkomplexität | Getauscht |
| 10 | Vergleich mit Referenz-Ticket | Vergleich mit Vorjahres-Report | Getauscht |
| 11 | 3+1 Dreiklang | 3+1 Dreiklang | **Gleich** |
| 12 | Export nach Linear | Export als PDF-Report | Getauscht |

Das Muster ist klar: Die Stufen 6, 7, 8 und 11 bleiben in jedem Projekt identisch. Sie sind die tragenden Wände des Studios. Die Stufen 1-5, 9, 10 und 12 sind die austauschbaren Plugins – sie bestimmen den Sound, aber nicht die Architektur.

> **Fazit:** Die Signalkette ist unzerstörbar, solange die Murmelbahn keine Lücken hat. Wenn ein Plugin ausfällt, greifen die Systemgrenzen-Strategien (3 pro Stufe = 36 Fallbacks insgesamt). Sektor 2 hat jetzt seinen Master-Bauplan. Die Chaos-Ordner können kommen. Let's bounce.

---

**UOP-Gate (Master-Export):**
P6 ist abgeschlossen. Die 12-Stufen-Signalkette steht. Alle 6 Axiome sind verdrahtet, alle 8 Grundprobleme haben ihren Regler, und die Universalität ist mit zwei Praxisbeispielen bewiesen. Warte auf Bestätigung für P7 oder Korrekturen an der Pipeline.
