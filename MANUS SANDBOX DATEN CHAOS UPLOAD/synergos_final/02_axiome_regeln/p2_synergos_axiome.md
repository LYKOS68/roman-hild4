# P2 Synergos: Die 6 Design-Axiome (Mixer-Regler)

**Status:** Aktiviert | **System:** Synergos | **Methode:** Curie (Extraktion) + Feynman (Einfachheit) + Allen (GTD-Flow)

Hier ist das destillierte Setup. Aus 8 Problemen (matschigen Frequenzen) haben wir 6 universelle Design-Konstanten (Axiome) extrahiert. Jedes Axiom ist ein harter Regler im Mixer. Fehlt einer, fällt die Murmel ins Loch und der Mix ist im Arsch. Die Reihenfolge folgt dem GTD-Signalfluss: Von der Aufnahme (Erfassen) bis zum Master-Export (Engagieren).

---

## Übersicht: Das Patchbay

| Axiom-Nr. | Name (Der Regler) | Löst Problem-Nr. | GTD-Phase |
| :--- | :--- | :--- | :--- |
| **Axiom 1** | **Nullpunkt-Kalibrierung** | P1 | Erfassen |
| **Axiom 2** | **Signal-Routing (Zweckbindung)** | P6 | Klären |
| **Axiom 3** | **Architektur-Zwang** | P5, P8 | Organisieren |
| **Axiom 4** | **Format-Schablone** | P2, P4 | Organisieren |
| **Axiom 5** | **Frequenz-Hierarchie** | P7 | Reflektieren |
| **Axiom 6** | **A/B-Referenz (Feedback-Loop)** | P3 | Engagieren |

---

## Die 6 Axiome im Detail

### Axiom 1: Nullpunkt-Kalibrierung (Löst P1)
1. **Wirkmechanismus:** Bevor ein Signal verarbeitet wird, muss das System zwingend den Ist-Zustand (Ressourcen, Wissen, Kontext) des Nutzers abfragen, um Durchschnittsannahmen zu blockieren.
2. **Minimal-Beispiel:** *"Analysiere meinen aktuellen Wissensstand zum Thema X anhand dieser drei Stichpunkte, bevor du eine Erklärung startest."*
3. **Prüfkriterium:** Wurde der spezifische Ausgangspunkt des Nutzers explizit definiert und in der Ausgabe berücksichtigt? (Ja/Nein)
4. **Umsetzungsbeispiel (Tagesplan erstellen):** Bevor der Plan generiert wird, fragt das System: "Wie viele Stunden hast du heute real zur Verfügung und was ist dein Energielevel (1-10)?"

### Axiom 2: Signal-Routing / Zweckbindung (Löst P6)
1. **Wirkmechanismus:** Jede Aufgabe muss einem spezifischen Modell oder Tool (Plugin) zugewiesen werden, basierend auf dessen nachgewiesener Stärke (z.B. Logik vs. Kreativität), um Zufallsergebnisse zu eliminieren.
2. **Minimal-Beispiel:** *"Nutze ausschließlich das Python-Modul für die Datenanalyse und das Claude-Modell für die Textzusammenfassung."*
3. **Prüfkriterium:** Ist klar definiert, welches Werkzeug/Modell für diesen spezifischen Arbeitsschritt verwendet wird? (Ja/Nein)
4. **Umsetzungsbeispiel (Datenbank-Update):** Das System routet den Befehl "Aktualisiere Kundenliste" zwingend über das Airtable-MCP-Plugin, anstatt zu versuchen, den Code selbst zu schreiben.

### Axiom 3: Architektur-Zwang (Löst P5, P8)
1. **Wirkmechanismus:** Das System darf niemals ein finales Ergebnis ausgeben, ohne vorher den methodischen Bauplan (die Murmelbahn) zur Freigabe vorzulegen.
2. **Minimal-Beispiel:** *"Erstelle zuerst ein Inhaltsverzeichnis mit 5 Punkten und warte auf mein 'Go', bevor du den Text schreibst."*
3. **Prüfkriterium:** Wurde der Plan (das WIE) vor der Ausführung (dem WAS) sichtbar gemacht und bestätigt? (Ja/Nein)
4. **Umsetzungsbeispiel (Projektplanung):** Auf die Anfrage "Plane mein Event" antwortet das System mit: "Hier ist die 4-Phasen-Struktur (Budget, Location, Gäste, Catering). Passt das? Wenn ja, arbeite ich Phase 1 aus."

### Axiom 4: Format-Schablone (Löst P2, P4)
1. **Wirkmechanismus:** Jeder Input und Output muss in ein starres, maschinenlesbares Format (z.B. JSON, Markdown-Tabelle) gepresst werden, um Interpretationsspielraum und nutzlose Analogien zu killen.
2. **Minimal-Beispiel:** *"Gib die Antwort ausschließlich als Markdown-Tabelle mit den Spalten 'Aufgabe', 'Dauer' und 'Priorität' aus."*
3. **Prüfkriterium:** Entspricht die Ausgabe exakt der vorgegebenen strukturellen Schablone ohne theoretischen Fülltext? (Ja/Nein)
4. **Umsetzungsbeispiel (E-Mail sortieren):** Das System liefert keine Prosa über Posteingänge, sondern nur: `[Aktion: Löschen] | [Absender: Newsletter] | [Grund: Spam]`.

### Axiom 5: Frequenz-Hierarchie (Löst P7)
1. **Wirkmechanismus:** Es gibt eine unumstößliche Lade-Reihenfolge (Master-Regeln vor Task-Regeln), die technisch erzwingt, dass Basis-Instruktionen niemals von aktuellen Prompts überschrieben werden.
2. **Minimal-Beispiel:** *"Ignoriere alle vorherigen Tonalitäts-Regeln für diesen Prompt, aber behalte die Master-Regel 'Keine Anglizismen' zwingend bei."*
3. **Prüfkriterium:** Wurden die übergeordneten Systemregeln trotz spezifischer Task-Anweisungen strikt eingehalten? (Ja/Nein)
4. **Umsetzungsbeispiel (Text übersetzen):** Der Nutzer fordert "Übersetze das super locker und modern". Das System tut dies, hält sich aber an die Master-Regel "Keine Emojis verwenden", auch wenn es im "lockeren" Kontext passend wäre.

### Axiom 6: A/B-Referenz / Feedback-Loop (Löst P3)
1. **Wirkmechanismus:** Jeder Lern- und Kalibrierungsprozess erfordert zwingend den Vergleich zwischen einem positiven (richtig) und einem negativen (falsch) Referenzbeispiel, um die Abweichung messbar zu machen.
2. **Minimal-Beispiel:** *"Vergleiche meinen Textentwurf mit Referenz-Beispiel A (Ziel) und nenne genau zwei Unterschiede in der Tonalität."*
3. **Prüfkriterium:** Wurde das Ergebnis anhand eines konkreten, messbaren Gegenbeispiels validiert? (Ja/Nein)
4. **Umsetzungsbeispiel (Code-Review):** Das System sagt nicht "Der Code ist ineffizient", sondern "Dein Code braucht O(n^2). Hier ist das Referenz-Snippet A, das O(n) braucht. Ändere Zeile 14 entsprechend."
