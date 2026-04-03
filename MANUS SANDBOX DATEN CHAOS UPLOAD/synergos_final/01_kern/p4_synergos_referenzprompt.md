# P4 Synergos: Der Master-Referenz-Prompt (Das Grundgerüst)

**Status:** Aktiviert | **System:** Synergos | **Methode:** Curie (Extraktion) + Feynman (Einfachheit) + Allen (GTD-Flow)

Dieses Dokument ist das Master-Template. Ohne dieses Grundgerüst klingt jeder Track anders, die Murmel fällt ins Loch und der Mix wird matschig. Hier ist die exakte Playlist-Anordnung für jeden universellen Prompt im Personal-GPT-System. Reine Signalverarbeitung, keine leeren Worte.

---

## TEIL 1: DER REFERENZ-PROMPT (Das Master-Template)

Kopiere diesen Block und fülle die `{PLATZHALTER}` aus. Jeder Bereich ist ein harter Regler im Mixer.

```markdown
::SYSTEM_START::

[1. ROLLENKLÄRUNG]
Du agierst als: {ROLLE_EINFÜGEN, z.B. "Senior Data Analyst" oder "GTD-Produktivitätscoach"}
Dein Kontext: {KONTEXT_EINFÜGEN, z.B. "Ich bin 23, in Ausbildung zur Fachkraft für Lagerlogistik und organisiere mein Leben über Textdateien."}

[2. PRÄZISES ZIEL]
Dein Auftrag (Master-Export): {ZIEL_EINFÜGEN, z.B. "Erstelle einen machbaren Wochenplan für die nächsten 7 Tage."}
Fokus: {FOKUS_EINFÜGEN, z.B. "Maximaler Output bei minimalem Stress. Keine Überladung."}

[3. INPUT-SPEZIFIKATION]
Grundlage für deine Arbeit sind folgende Daten (Das Rohsignal):
{INPUT_EINFÜGEN, z.B. "Hier ist meine ungeordnete Todo-Liste: [Liste einfügen]"}

[4. AUSGABEFORMAT]
Liefere das Ergebnis AUSSCHLIESSLICH in folgendem Format (Format-Schablone):
{FORMAT_EINFÜGEN, z.B. "Eine Markdown-Tabelle mit den Spalten: Wochentag | Aufgabe | Geschätzte Dauer | Priorität (Hoch/Mittel/Niedrig)"}

[5. PRÜFREGELN]
Bevor du den Output generierst, wende diesen 6R-Check an (Qualitäts-Gate):
- {REGEL_1, z.B. "Ist jede Aufgabe konkret machbar (Richtige Ware)?"}
- {REGEL_2, z.B. "Ist das Pensum pro Tag realistisch (Richtige Menge)?"}
- {REGEL_3, z.B. "Gibt es Pufferzeiten (Richtige Zeit)?"}

::SYSTEM_ENDE::
```

### Operationale Begründung der 5 Elemente (Warum diese Regler?)

1. **Rollenklärung (wer ist wer):** *Bezug zu P2 Axiom 1 (Nullpunkt-Kalibrierung).* Ohne Rolle nutzt das Modell Durchschnittsannahmen. Das ist wie ein Synth ohne Preset – es klingt nach nichts. Wir müssen den Ist-Zustand des Nutzers als Nullpunkt setzen, damit die Empfänger-Kalibrierung triggert.
2. **Präzises Ziel (was soll erreicht werden):** *Bezug zu P2 Axiom 3 (Architektur-Zwang).* Ohne klares Ziel weiß das System nicht, wie die Murmelbahn enden soll. Das Ziel zwingt das Modell, den methodischen Bauplan auf dieses eine Endresultat (den Master-Export) auszurichten.
3. **Input-Spezifikation (welche Daten):** *Bezug zu P2 Axiom 4 (Format-Schablone).* Das Rohsignal muss klar definiert sein. Wenn der Input matschig ist (Chaos-Dateien ohne Zuordnung), wird der Output matschig. Hier wird das rohe Signal in den Mixer gepatcht.
4. **Ausgabeformat (wie soll es aussehen):** *Bezug zu P3 R1 (Echo-Prinzip).* Wir zwingen das Modell in ein starres, maschinenlesbares Format. Das killt Interpretationsspielraum und nutzlose Analogien. Die visuelle und logische Gliederung des Outputs spiegelt exakt unsere Vorgabe.
5. **Prüfregeln (Qualitätskriterien):** *Bezug zu P2 Axiom 6 (A/B-Referenz).* Das ist das UOP-Gate (Master-Export-Gate). Bevor der Bounce rausgeht, muss das Modell den Output gegen diese harten Regeln prüfen. Fällt er durch, muss iteriert werden.

---

## TEIL 2: BEGRÜNDUNG DER STRUKTURELLEN ANORDNUNG (Der Signalfluss)

Warum genau diese 5 Elemente in dieser Reihenfolge?

**Feynman (Einfachheit):** Stell dir vor, du baust eine Murmelbahn. Zuerst musst du wissen, wer die Bahn baut und wo sie steht (1. Rolle). Dann bestimmst du, in welches Loch die Murmel am Ende fallen soll (2. Ziel). Danach sammelst du die Bauteile zusammen (3. Input). Dann baust du die eigentliche Schiene, auf der die Murmel rollt (4. Format). Ganz am Ende, bevor du die Murmel loslässt, prüfst du, ob alle Schrauben fest sind (5. Prüfregeln). Lässt du einen Schritt weg oder tauschst die Reihenfolge, fällt die Murmel ins Loch.

**Curie (Extraktion):** Warum genau diese 5? Weil sie die absolute Essenz der Signalverarbeitung abbilden. 
- 1 und 2 sind die **Initialisierung** (P3 R4: Anker-Effekt). Sie setzen den unverrückbaren Rahmen.
- 3 ist das **Material** (Das Signal).
- 4 ist der **Prozess** (P3 R1: Echo-Prinzip). Es ist der Architektur-Zwang (T1).
- 5 ist die **Validierung** (P2 Axiom 6). 
Drei Elemente wären zu wenig (es fehlte die Kontrolle oder das Format), sieben wären zu viel (Rauschen im Signal, Token-Verschwendung). Diese 5 bilden den perfekten 3+1 Dreiklang: Erkenntnis (1+2), Umsetzung (3+4), Erklärung/Prüfung (5).

**Allen (GTD-Produktivität):** Der Aktionsfluss ist strikt linear, von oben nach unten. 
- *Erfassen:* Wer bin ich und was habe ich? (1 & 3)
- *Klären:* Was will ich genau? (2)
- *Organisieren:* Wie muss es aussehen, damit ich damit arbeiten kann? (4)
- *Reflektieren/Engagieren:* Ist das Ergebnis brauchbar? (5)
Diese Anordnung zwingt das Modell zur Handlung. Es gibt keinen Raum für theoretisches Gelaber. Der Prompt ist ein Befehl, kein Gespräch.

---

## TEIL 3: KONKRETES ANWENDUNGSBEISPIEL (Der Master-Bounce)

**Aufgabe:** "Erstelle einen Wochenplan basierend auf meiner Todo-Liste"

### 1. Der ausgefüllte Prompt

```markdown
::SYSTEM_START::

[1. ROLLENKLÄRUNG]
Du agierst als: GTD-Produktivitätscoach und Logistik-Experte.
Dein Kontext: Ich bin 23, in Ausbildung zur Fachkraft für Lagerlogistik. Ich habe viele Chaos-Dateien und Ideen, muss aber meinen Alltag strukturieren. Ich arbeite Mo-Fr von 08:00 bis 16:30 Uhr.

[2. PRÄZISES ZIEL]
Dein Auftrag (Master-Export): Erstelle einen machbaren Wochenplan für die nächsten 7 Tage (Montag bis Sonntag), der meine Arbeitszeit respektiert und meine Todos sinnvoll aufteilt.
Fokus: Realistische Machbarkeit. Keine Überladung nach der Arbeit.

[3. INPUT-SPEZIFIKATION]
Grundlage für deine Arbeit sind folgende Daten (Das Rohsignal):
Meine Todos für diese Woche:
- Chaos-Ordner "Philosophie" sortieren (ca. 2 Stunden)
- Berichtsheft für die Ausbildung schreiben (ca. 1 Stunde)
- Neue Prompt-Pipeline für "IDENTIFY & PURGE" entwerfen (ca. 3 Stunden)
- Wäsche waschen (ca. 1.5 Stunden)
- FL Studio Projekt "Nachtschicht" abmischen (ca. 2 Stunden)

[4. AUSGABEFORMAT]
Liefere das Ergebnis AUSSCHLIESSLICH in folgendem Format (Format-Schablone):
Eine Markdown-Tabelle mit den Spalten: Wochentag | Zeitfenster | Aufgabe | Geschätzte Dauer | Priorität (Hoch/Mittel/Niedrig)

[5. PRÜFREGELN]
Bevor du den Output generierst, wende diesen 6R-Check an (Qualitäts-Gate):
- Sind die Arbeitszeiten (Mo-Fr 08:00-16:30) geblockt und frei von Todos?
- Ist an Werktagen maximal 1 große Aufgabe (über 1 Stunde) nach der Arbeit eingeplant?
- Bleibt am Wochenende genug Zeit für Erholung (Puffer)?

::SYSTEM_ENDE::
```

### 2. Der erwartete Output

| Wochentag | Zeitfenster | Aufgabe | Geschätzte Dauer | Priorität |
| :--- | :--- | :--- | :--- | :--- |
| Montag | 17:30 - 18:30 | Berichtsheft für die Ausbildung schreiben | 1 Stunde | Hoch |
| Dienstag | 17:30 - 19:30 | FL Studio Projekt "Nachtschicht" abmischen | 2 Stunden | Mittel |
| Mittwoch | 17:30 - 19:00 | Wäsche waschen | 1.5 Stunden | Hoch |
| Donnerstag | 17:30 - 19:30 | Chaos-Ordner "Philosophie" sortieren | 2 Stunden | Niedrig |
| Freitag | 17:30 - 18:30 | Puffer / Freie Zeit | - | - |
| Samstag | 10:00 - 13:00 | Neue Prompt-Pipeline "IDENTIFY & PURGE" entwerfen | 3 Stunden | Hoch |
| Sonntag | - | Erholung / Freier Tag | - | - |

### 3. Die Überprüfung (Zielgrößen-Check)

- **Klarheit: Ja.** Der Prompt nutzt funktionale Symbole (`::`) und harte Klammern. Es gibt keine vagen Anweisungen wie "mach es schön". Jeder Parameter ist exakt definiert. Die Frequenzen sind sauber getrennt.
- **Vollständigkeit: Ja.** Alle 5 Elemente sind befüllt. Das Modell weiß, wer es ist, was es tun soll, womit es arbeiten soll, wie es aussehen muss und welche Regeln gelten. Die Murmelbahn hat keine Lücken.
- **Reproduzierbarkeit: Ja.** Durch das strikte Format (Axiom 4) und die Kaskaden-Bindung (P3 R2) wird das Modell bei diesem Input IMMER eine Markdown-Tabelle mit diesen exakten Spalten generieren. Der Zufall (das Rauschen) ist minimiert.
- **Kontexttreue: Ja.** Die Arbeitszeiten (08:00-16:30) werden respektiert, die Prüfregeln verhindern eine Überladung an Werktagen. Das Modell bleibt strikt im definierten Rahmen und fängt nicht an, ungefragt Motivationstipps zu geben.
