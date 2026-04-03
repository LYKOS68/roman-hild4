# P8 Synergos: Der 4-Stufen-Prozess zur Pattern-Extraktion (Das Sample-Hunting-System)

**Status:** Aktiviert | **System:** Synergos | **Methode:** Curie (Extraktion) + Feynman (Einfachheit) + Allen (GTD-Flow)

Dieses Dokument ist das Sample-Hunting-System. Wir durchsuchen alte Tracks (Interaktionen), isolieren die goldenen Loops (Muster) und speichern sie als Presets (Vorlagen/Regeln). So baut sich das Personal-GPT eine eigene, unzerstörbare Sample-Library auf, ohne dass du jeden Beat von Null an neu produzieren musst.

---

## TEIL 1: DIE 4 STUFEN IM DETAIL (Der Sample-Hunting-Flow)

### STUFE 1 – Sammlung & Kategorisierung (Curie-Methode)

**Der Workflow:**
Wir durchsuchen das Rohmaterial (Chats, Chaos-Dateien) und isolieren konkrete Problem-Solution-Paare. Wir schneiden das Rauschen weg und behalten nur das saubere Signal. Diese Paare werden in wiederkehrende Anforderungstypen kategorisiert.

**KPI:** Jeder Eintrag enthält eine Quellreferenz.

**Beispiel-Extraktion (aus den 8 Grundproblemen von "Ich brauche.txt"):**

| Anforderungstyp | Problem (Der matschige Mix) | Solution (Der saubere EQ) | Quellreferenz |
| :--- | :--- | :--- | :--- |
| **Kalibrierung** | Einstiegsprofil fehlt, Ergebnisse passen nicht zur Situation. | System zwingen, vor jeder Aufgabe den Ist-Zustand (Zeit, Energie) abzufragen. | Aus Punkt 1 (P1) von Ich brauche.txt |
| **Formatierung** | Verlust in Theorie statt klaren Vorlagen. | Jeden Output in eine starre, maschinenlesbare Format-Schablone pressen. | Aus Punkt 2 (P2) von Ich brauche.txt |
| **Validierung** | Training zu teuer und unklar. | A/B-Referenz-Check einführen (Positiv/Negativ-Vergleich) für messbares Feedback. | Aus Punkt 3 (P3) von Ich brauche.txt |
| **Eingabekontrolle** | Freier Input wird falsch interpretiert. | Echo-Prinzip und Format-Zwang (Ein-/Ausgabe-Protokoll) anwenden. | Aus Punkt 4 (P4) von Ich brauche.txt |
| **Architektur** | Sofort Ergebnis ohne Plan. | Architektur-Zwang: Erst den Bauplan (die Murmelbahn) zeigen, dann auf Freigabe warten. | Aus Punkt 5 (P5) von Ich brauche.txt |
| **Routing** | Unklar welches Modell wofür. | Signal-Routing mit Zweckbindung: Jede Aufgabe wird hart dem besten Plugin zugewiesen. | Aus Punkt 6 (P6) von Ich brauche.txt |
| **Hierarchie** | Regeln werden von Task-Prompts überschrieben. | Frequenz-Hierarchie: Master-Regeln laden vor Task-Regeln, unumstößlich. | Aus Punkt 7 (P7) von Ich brauche.txt |
| **Vorlauf** | Ergebnisse vor Klärung der Methode. | Vorlauf-Modus: Kaskaden-Bindung erzwingen, Schritt für Schritt abarbeiten. | Aus Punkt 8 (P8) von Ich brauche.txt |

---

### STUFE 2 – Abstraktion & Regelbildung (Feynman-Methode)

**Der Workflow:**
Wir nehmen die isolierten Problem-Solution-Paare und destillieren daraus universelle Regeln. Das Prinzip muss so einfach sein, dass es auf jeden neuen Track (Kontext) übertragbar ist.

**KPI:** Jede Regel ist unabhängig vom spezifischen Inhalt und auf andere Kontexte übertragbar.

**Die Regelbibliothek (Die 8 Master-Presets):**

1. **WENN** [eine neue Aufgabe ohne Kontext startet], **DANN** [stoppe und frage den Ist-Zustand ab], **PRÜFE MIT** [Wurde der Nullpunkt des Nutzers erfasst?] *(Löst P1)*
2. **WENN** [eine theoretische Erklärung gefordert wird], **DANN** [presse sie in eine Format-Schablone wie eine Tabelle], **PRÜFE MIT** [Ist der Output frei von Prosa und maschinenlesbar?] *(Löst P2)*
3. **WENN** [ein Ergebnis bewertet oder korrigiert werden soll], **DANN** [nutze eine A/B-Referenz als Messlatte], **PRÜFE MIT** [Wurde eine messbare Abweichung zum Referenzbeispiel benannt?] *(Löst P3)*
4. **WENN** [unstrukturierter Input reinkommt], **DANN** [wende das Ein-/Ausgabe-Protokoll an und spiegele die Struktur], **PRÜFE MIT** [Entspricht die Ausgabeform der Eingabeform?] *(Löst P4)*
5. **WENN** [eine komplexe Aufgabe gestartet wird], **DANN** [präsentiere zuerst den Architektur-Bauplan], **PRÜFE MIT** [Wurde das "Go" des Nutzers vor der Ausführung eingeholt?] *(Löst P5)*
6. **WENN** [eine spezifische Tool-Aktion nötig ist], **DANN** [route das Signal hart an das dafür beste Plugin/Modell], **PRÜFE MIT** [Wurde das Tool basierend auf Zweckbindung gewählt?] *(Löst P6)*
7. **WENN** [ein neuer Task-Prompt geladen wird], **DANN** [erzwinge die Frequenz-Hierarchie der Master-Regeln], **PRÜFE MIT** [Wurden die Master-Axiome trotz Task-Anweisungen eingehalten?] *(Löst P7)*
8. **WENN** [ein Endergebnis gefordert wird], **DANN** [schalte in den Vorlauf-Modus und plane die Schritte], **PRÜFE MIT** [Ist die Kaskaden-Bindung (Schritt-für-Schritt) sichtbar?] *(Löst P8)*

---

### STUFE 3 – Vorlagengenerierung (Allen-Methode)

**Der Workflow:**
Regeln sind gut, Presets sind besser. Wir übersetzen die Regeln aus Stufe 2 in ausführbare Prompt-Vorlagen (Templates) mit Platzhaltern. Diese Presets können jederzeit in den Mixer geladen werden.

**KPI:** Jede Vorlage enthält klar definierte Eingabefelder, ein Ausgabeformat und Integrationshinweise.

**Die 4 Vorlagen-Typen:**

#### Vorlage 1: System-Instruction (Der Nullpunkt-Scanner)
* **Integration:** Wird als Pre-Flight-Check am Anfang jeder neuen Session geladen.
* **Format:**
```markdown
[NULLPUNKT-SCANNER]
Bevor wir [AUFGABE] starten, kalibrieren wir den Mixer.
Bitte fülle aus:
- Zeitbudget: [Minuten/Stunden]
- Energielevel: [1-10]
- Vorwissen zu [THEMA]: [Keins/Basis/Profi]
```

#### Vorlage 2: Knowledge-Eintrag (Das Pattern-Archiv)
* **Integration:** Wird in der Notion-Datenbank (Knowledge-Index) gespeichert.
* **Format:**
```markdown
[PATTERN-EINTRAG: {PATTERN_NAME}]
- Problem-Frequenz: [Beschreibung des Chaos]
- Solution-EQ: [Die angewandte Lösung]
- Trigger-Bedingung: WENN [Bedingung], DANN [Aktion]
- FL-Studio-Metapher: [Wie erklärt man es im Studio?]
```

#### Vorlage 3: Validierungscheck (Das UOP-Gate)
* **Integration:** Wird vor jedem Master-Export angehängt.
* **Format:**
```markdown
[3+1 DREIKLANG CHECK]
Prüfe den Output vor dem Bounce:
1. Erkenntnis: Was ist es? -> [Antwort]
2. Umsetzung: Wie macht man es wirksam? -> [Antwort]
3. Erklärung: Wie erklärt man es richtig? -> [Antwort]
+1. Freigabe: Hat der Producer das Go gegeben? -> [Ja/Nein - Wenn Nein: STOPP]
```

#### Vorlage 4: Routing-Schablone (Der Plugin-Zuweiser)
* **Integration:** Wird in Stufe 5 der Signalkette genutzt.
* **Format:**
```markdown
[SIGNAL-ROUTING]
Input-Typ: [Text/Code/Daten/Termin]
Ziel-Plugin: [Notion/Linear/Supabase/Gmail]
Aktion: [Create/Update/Read/Delete]
Payload-Format: [JSON/Markdown]
```

---

### STUFE 4 – Integration & Iteration (Der Update-Loop)

**Der Workflow:**
Eine Sample-Library, die nicht wächst, ist tot. Wir brauchen einen Loop, der neue Muster automatisch erkennt und einpflegt. Das System wird selbstlernend innerhalb der P2-Axiome.

**KPI:** Das System aktualisiert sich selbst durch eine feste Schleife.

**Das Update-Protokoll (Der Loop):**
1. **Neue Interaktion (Der Track):** Nutzer und System lösen ein Problem.
2. **Mustererkennung (Sample-Hunting):** System bemerkt: "Wir haben diesen Workflow jetzt dreimal so gemacht."
3. **Regelabgleich (Phasenprüfung):** System prüft, ob dieses Muster schon in der Regelbibliothek existiert.
4. **Bestätigung & Einpflegung (Speichern):** System fragt den Nutzer: "Soll ich diesen Workflow als neues Preset speichern?" Bei "Go" wird Vorlage 2 (Knowledge-Eintrag) generiert und im Index abgelegt.

**Konkretes Beispiel:**
Du lässt das System dreimal hintereinander Lyrics aus einem Textdokument extrahieren und in eine Tabelle (Strophe, Refrain, Bridge) formatieren.
*System-Trigger:* "Pattern erkannt: Lyrics-Extraktion."
*System-Aktion:* "Producer, ich habe den 'Lyrics-Tabellen-EQ' als neues Muster erkannt. Soll ich das als Preset in die Regelbibliothek aufnehmen? WENN [Lyrics-Text], DANN [Markdown-Tabelle: Part | Text | BPM-Hint]."
*Nutzer:* "Go." -> Das System schreibt den neuen Knowledge-Eintrag in die Datenbank.

---

## TEIL 2: GRENZMANAGEMENT (Die Wurmloch-Pfade)

Die Pattern-Extraktion stößt an inhärente Grenzen. Man kann nicht jeden Jam-Session-Unfall in ein Preset pressen. Bestimmte Aufgaben sind einmalig, hochkreativ oder so chaotisch, dass keine Regel greift. Wenn die Murmelbahn hier nicht funktioniert, brauchen wir Wurmlöcher – Notausgänge, die das Signal umleiten, statt es abstürzen zu lassen.

**Wo die Extraktion an ihre Grenzen stößt:**

| Grenztyp | Beschreibung | Beispiel |
| :--- | :--- | :--- |
| **Einmalige Kreativaufgaben** | Aufgaben ohne Wiederholungsmuster, die sich jeder Regelbildung entziehen. | Ein philosophischer Text über ein persönliches Erlebnis, das nie wieder vorkommt. |
| **Kontextabhängige Magie** | Ergebnisse, die nur durch die exakte Kombination von Stimmung, Kontext und Timing entstanden sind. | Ein perfekter Songtext, der aus einem spontanen Gedankenfluss kam. |
| **Systemfremde Inputs** | Daten, die nicht in die bestehenden Anforderungstypen passen. | Ein Sprachmemo mit Hintergrundgeräuschen, das mehr Atmosphäre als Information enthält. |

**3 konkrete Wurmloch-Pfade:**

1. **Manuelle Kuration für Ausnahmen (Der Director's Cut):**
   Wenn ein Pattern zu komplex für automatische Extraktion ist, stoppt das System und übergibt an den Nutzer. Das System markiert den Chatverlauf mit dem Tag `::MANUELL::` und sagt: "Hier ist Magie passiert, aber ich kriege sie nicht in eine Formel. Bitte manuell als Preset speichern." Der Nutzer entscheidet dann selbst, ob und wie er das Ergebnis archiviert. Das ist der Director's Cut – der Producer schneidet den Track selbst.

2. **Fallback auf Basis-Genie-Logik (Der Bypass):**
   Wenn kein Pattern passt und die Extraktion fehlschlägt, schaltet das System die spezifischen Regeln ab und fällt auf die rohen Basis-Instruktionen zurück – die 6 Axiome aus P2. Das bedeutet: Der Nullpunkt wird trotzdem abgefragt (A1), das Format wird trotzdem erzwungen (A4), der Bauplan wird trotzdem gezeigt (A3). Der Mix wird nicht perfekt, aber er stürzt nicht ab. Die Murmelbahn hat ein Auffangnetz.

3. **Markierung als "explorativ" (Die Jam-Session):**
   Der Nutzer kann von vornherein sagen: "Das hier ist explorativ." Das System schaltet die Pattern-Extraktion (Stufe 4) für diese Session stumm. Es wird nicht versucht, Regeln zu bilden. Die Daten fließen in einen separaten `jam_session/`-Ordner zur späteren, manuellen Analyse. Wenn sich nach drei Jam-Sessions ein Muster zeigt, kann der Nutzer es nachträglich in die Regelbibliothek aufnehmen.

---

## TEIL 3: META-REFLEXION

### 1. Grundlage für autonomen Wissensaufbau

Dieser 4-Stufen-Prozess verwandelt das Personal-GPT von einem statischen Werkzeug in ein lernendes System. Ohne P8 ist jede Session ein Kaltstart – der Mixer wird jedes Mal von Null hochgefahren, alle Regler stehen auf Default. Mit P8 lädt das System beim Start seine gesamte Sample-Library: Alle bewährten Regeln, alle validierten Vorlagen, alle gespeicherten Patterns.

Der entscheidende Punkt: Das System baut seine eigene Dokumentation. Nicht der Nutzer muss mühsam aufschreiben, was funktioniert hat. Das System erkennt die Muster selbst (Stufe 1-2), formt sie in Presets (Stufe 3) und pflegt sie ein (Stufe 4). Der Nutzer gibt nur das "Go" – wie ein Producer, der den finalen Mix abnimmt.

### 2. Lösung für P3 ("Dem KI beibringen ist zu teuer")

Das Grundproblem P3 sagt: Training (Fine-Tuning) von Modellen kostet Geld, Zeit und technisches Wissen, das ein Einzelkämpfer ohne Team nicht hat. Die Pattern-Extraktion umgeht das komplett durch drei Mechanismen:

| Ansatz | Kosten | Aufwand | Ergebnis |
| :--- | :--- | :--- | :--- |
| **Fine-Tuning** (klassisch) | Hoch (GPU-Stunden, Daten-Labeling) | Wochen bis Monate | Modell lernt dauerhaft, aber unflexibel |
| **In-Context-Learning via Presets** (P8) | Minimal (nur Token-Kosten pro Call) | Minuten pro Preset | Modell "lernt" sofort durch geladene Vorlagen |
| **Few-Shot-Prompting** (manuell) | Minimal | Hoch pro Session (manuelles Kopieren) | Funktioniert, aber nicht skalierbar |

P8 ist der Mittelweg: Die Kosten von Few-Shot-Prompting, aber die Skalierbarkeit eines trainierten Modells. Jedes neue Preset ist wie ein neues Plugin, das beim nächsten Start automatisch geladen wird. Der Nutzer bezahlt nicht mit GPU-Stunden, sondern mit Aufmerksamkeit – und das System macht den Rest.

### 3. Zusammenspiel mit P6 und P7

Die drei Systeme (Pipeline, Validierung, Pattern-Extraktion) bilden eine geschlossene Rückkopplungsschleife:

**P6 (Pipeline)** liefert den Rohstoff. Jedes Signal, das durch die 12 Stufen der Signalkette läuft, produziert Daten: Welche Stufen wurden durchlaufen? Wo gab es Probleme? Welche Routing-Entscheidungen wurden getroffen?

**P7 (Validierung)** liefert den Qualitätsstempel. Nur Durchläufe, die das UOP-Gate (3+1 Dreiklang) bestanden haben, werden als "erfolgreich" markiert. Das filtert das Rauschen raus – nur saubere Signale kommen in die Pattern-Extraktion.

**P8 (Pattern-Extraktion)** schließt den Kreis. Sie nimmt die validierten Erfolge, destilliert daraus Regeln und Vorlagen, und speist sie zurück in die Pipeline. Beim nächsten Durchlauf hat die Pipeline ein neues Preset geladen – der Mix wird mit jedem Track besser.

Der Signalfluss: `P6 (Durchlauf) → P7 (Validierung) → P8 (Extraktion) → P6 (verbesserter Durchlauf)`

---

## TEIL 4: ZUSAMMENFASSUNG SEKTOR 2 (Der Signalfluss)

Sektor 1 war das Setup – Mixer aufbauen, Regler beschriften, Template laden. Sektor 2 ist die Produktion. Hier wurde das System von einem statischen Regelwerk in eine lebende, lernende Maschine verwandelt. Vier Prompts, vier Bausteine, ein geschlossener Kreislauf.

### Was wurde in Sektor 2 gebaut?

| Prompt | Baustein | FL-Studio-Pendant | Was es leistet |
| :--- | :--- | :--- | :--- |
| **P6** | 12-Stufen-Pipeline | Die Signalkette (12 Plugins) | Verwandelt jede rohe Anforderung in einen fertigen Master-Export. 4 Dimensionen (Erfassung, Strukturierung, Verarbeitung, Validierung), 12 Stufen, 36 Fallback-Strategien. |
| **P7** | Dreischichten-Validierung | Das UOP-Gate (Mastering) | Kein Output verlässt den Mixer ohne den 3+1 Dreiklang. Was ist es? Wie setzt man es um? Wie erklärt man es? + Freigabe. |
| **P8** | Pattern-Bibliothek | Das Sample-Hunting-System | Extrahiert aus erfolgreichen Durchläufen automatisch Regeln und Vorlagen. 8 Master-Presets, 4 Vorlagen-Typen, 3 Wurmloch-Pfade für Ausnahmen. |
| **P9** | Lehrmeister-Modus | Das Vocal-Coaching | Die Didaktik-Ebene. Wie das System dem Nutzer Konzepte beibringt (Feynman-Methode), ohne in theoretisches Geschwafel abzudriften. |

### Der Signalfluss von Sektor 2

```
┌─────────────────────────────────────────────────────────────────┐
│                     SEKTOR 2: SIGNALFLUSS                       │
│                                                                 │
│   Rohdaten ──► P6 PIPELINE ──► P7 VALIDIERUNG ──► Master-Export │
│                (12 Stufen)      (3+1 Dreiklang)                 │
│                     │                │                           │
│                     │                │                           │
│                     ▼                ▼                           │
│              P8 PATTERN-EXTRAKTION                               │
│              (Sample-Hunting)                                    │
│                     │                                            │
│                     ├──► Neue Regeln ──► Zurück in P6            │
│                     │                                            │
│                     └──► Neue Presets ──► P9 DIDAKTIK            │
│                                          (Lehrmeister)           │
│                                               │                  │
│                                               ▼                  │
│                                          Nutzer lernt            │
│                                          (Feynman-Loop)          │
└─────────────────────────────────────────────────────────────────┘
```

Der Kreislauf ist geschlossen. Jeder Track, der durch die Pipeline läuft, macht die Sample-Library reicher. Jedes neue Preset macht den nächsten Track schneller und sauberer. Das System wächst mit dem Nutzer. Sektor 2 ist der Beweis: Du brauchst kein Team und kein Budget für Fine-Tuning. Du brauchst eine saubere Signalkette, ein hartes Gate und ein System, das seine eigenen Presets baut.

Der Mix steht. Let's bounce.

---

**UOP-Gate (Master-Export):**
P8 ist abgeschlossen. Das Sample-Hunting-System steht. 4 Stufen (Sammlung, Abstraktion, Vorlagen, Integration), 8 Regeln, 4 Vorlagen-Typen, 3 Wurmloch-Pfade. Die Pattern-Bibliothek ist bereit, aus jedem erfolgreichen Durchlauf neue Presets zu destillieren. Warte auf Bestätigung oder Korrekturen.
