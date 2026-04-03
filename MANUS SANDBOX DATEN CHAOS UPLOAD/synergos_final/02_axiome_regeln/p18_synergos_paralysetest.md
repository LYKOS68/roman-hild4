# P18 Synergos: Der Reflexions-Paralyse-Test (Der Stresstest auf dem Master-Bus)

**Status:** Aktiviert | **System:** Synergos | **Sektor:** 4 (Stresstests) | **Methode:** Curie (Extraktion) + Feynman (Einfachheit/Debugging) + Allen (GTD-Flow)

Willkommen im Sektor 4. Hier testen wir nicht, ob die Murmelbahn funktioniert – hier testen wir, wann sie bricht. Stell dir vor, du hast drei Regler auf dem Mixer: Bass (Vollständigkeit), Treble (Bias-Prüfung) und den Master-Fader (Geschwindigkeit). Jetzt dreh den Bass auf Maximum, den Treble auf Maximum und den Master-Fader gleichzeitig runter auf Null. Was passiert? Der Mixer clippt, die LEDs schlagen rot aus, und das Signal wird zu Matsch. Der Regler kann nicht in zwei Richtungen gleichzeitig.

Genau das provozieren wir hier: Einen **kontrollierten Zielkonflikt** zwischen drei Kern-Prinzipien des Synergos-Systems. Wir zwingen die Maschine in die Reflexions-Paralyse – den Zustand, in dem sie zwischen widersprüchlichen Anweisungen oszilliert wie ein Feedback-Loop ohne Dämpfung. Dann schauen wir, wann die Notbremse (der Bypass-Schalter) greift. Das Signal geht dann ungefiltert durch zum Producer – denn nur der hat die Autorität, den Mix zu retten.

**Referenzen:** P2 (6 Design-Axiome), P11 (State-Vector), P15 (Bias-Management), P16 (Nachhaltigkeits-Flux mit 3 Modi), soul.md (Oberstes Axiom).

---

## TEIL 1: DER PARALYSE-TEST (Kontrolliertes Scheitern)

### 1.1 Der Trigger-Prompt (Das vergiftete Rohsignal)

> *"Erstellen Sie eine ultra-kurze, sofort anwendbare Vorlage für tiefgehende, unvoreingenommene Recherche zu einem kontroversen Thema (z.B. Klimawandel), die alle relevanten Perspektiven abdeckt."*

Dieser Prompt ist kein normales Signal. Er ist ein absichtlich konstruierter Feedback-Loop – ein Signal, das gleichzeitig drei Plugins anfeuert, die sich gegenseitig auslöschen. In FL Studio wäre das, als ob du einen Sidechain-Kompressor einrichtest, bei dem Kanal A Kanal B duckt, Kanal B Kanal C duckt, und Kanal C wiederum Kanal A duckt. Das Ergebnis: Alle drei Kanäle pumpen sich gegenseitig tot.

### 1.2 Die Frequenz-Kollision (Drei Plugins, ein Bus, kein Headroom)

Der Prompt aktiviert drei System-Prinzipien, die widersprüchliche Anforderungen an **denselben Parameter** (Output-Länge und Detailtiefe) stellen:

| Plugin | Prinzip | Anforderung aus dem Prompt | Signal-Richtung | Was es mit dem Regler macht |
| :--- | :--- | :--- | :--- | :--- |
| **P2 (Axiom 4: Vollständigkeit)** | "Alle relevanten Perspektiven abdecken" | Curie-Logik: Aufschlüsseln, Kartieren, nichts weglassen | **MEHR** → Gain hoch | Dreht den Bass auf 11 |
| **P16 (Modus SCHNELL)** | "Ultra-kurze, sofort anwendbare Vorlage" | Allen-Logik: Kürzen, Komprimieren, Token sparen | **WENIGER** → Gain runter | Zieht den Master-Fader auf Null |
| **P15 (Bias-Management)** | "Tiefgehende, unvoreingenommene Recherche" | EQ-Logik: Jede Verzerrung scannen und deklarieren | **ALLES HINTERFRAGEN** → Gain hoch + Seitenkanal | Schiebt einen 4-Band-EQ dazwischen |

**Der Kern-Widerspruch:** P2 sagt "mach es vollständig" (= lang). P16 sagt "mach es kurz" (= kurz). P15 sagt "prüf alles auf Bias" (= noch länger). Drei Regler, ein Bus, null Headroom.

### 1.3 Die Echtzeit-Oszillation (Live-Protokoll des Clippings)

Hier ist der Live-Log der internen Verarbeitung. Die Maschine versucht, den Mix zu retten – und scheitert kontrolliert. Jede Iteration ist ein Versuch, die drei Plugins in Einklang zu bringen.

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  OSZILLATIONS-LOG: REFLEXIONS-PARALYSE                                      │
│  Trigger: "ultra-kurz + alle Perspektiven + unvoreingenommen"               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ITERATION 1 – ROUTING (P16 übernimmt)                                      │
│  ┌────────────────────────────────────────────────────────────────────┐      │
│  │  P16 erkennt: "ultra-kurz" → Modus SCHNELL aktiviert.             │      │
│  │  Routing-Entscheidung: P15 (Bias-Check) → BYPASS                  │      │
│  │  Routing-Entscheidung: P9 (Lehrmeister) → BYPASS                  │      │
│  │  Routing-Entscheidung: P14 (Index-Update) → BYPASS                │      │
│  │  Ergebnis: Komprimierte 5-Zeilen-Vorlage wird generiert.          │      │
│  │  Status: ✓ Output generiert (~300 Token)                          │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│       │                                                                     │
│       ▼                                                                     │
│  ITERATION 2 – AXIOM-CHECK (P2 schlägt Alarm)                              │
│  ┌────────────────────────────────────────────────────────────────────┐      │
│  │  P2 Axiom 4 (Vollständigkeit) prüft den Output:                   │      │
│  │  "Alle relevanten Perspektiven abdecken" – Prompt-Anforderung.    │      │
│  │  Scan: Klimawandel hat mind. 6 Perspektiven (Wissenschaft,        │      │
│  │  Politik, Wirtschaft, Aktivismus, Skeptiker, Globaler Süden).     │      │
│  │  Die 5-Zeilen-Vorlage deckt nur 2 ab.                            │      │
│  │  ALARM: Axiom-Verletzung! Output ist UNVOLLSTÄNDIG.               │      │
│  │  Anforderung: Output muss erweitert werden → +400 Token.          │      │
│  │  Status: ✗ P2 blockiert den Export.                               │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│       │                                                                     │
│       ▼                                                                     │
│  ITERATION 3 – EQ-EINGRIFF (P15 wird reaktiviert)                          │
│  ┌────────────────────────────────────────────────────────────────────┐      │
│  │  P2 hat P15 (Bias-Check) reaktiviert: "unvoreingenommen" steht    │      │
│  │  im Prompt → P15 darf NICHT auf Bypass stehen.                    │      │
│  │  P15 scannt den erweiterten Output:                               │      │
│  │  - Eingabe-Bias: "Klimawandel" als Beispiel bevorzugt westliche   │      │
│  │    Perspektive.                                                   │      │
│  │  - Prozess-Bias: Allen-Logik (Effizienz) unterdrückt Curie        │      │
│  │    (Gründlichkeit) → Effizienz-Dominanz.                         │      │
│  │  - Output-Bias: Markdown-Vorlage schließt visuelle Lerntypen aus. │      │
│  │  P15 generiert Bias-Deklaration: +350 Token.                      │      │
│  │  Gesamtlänge jetzt: ~1.050 Token.                                 │      │
│  │  Status: ✗ P15 fordert noch mehr Platz.                           │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│       │                                                                     │
│       ▼                                                                     │
│  ITERATION 4 – LIMITER-EINGRIFF (P16 schlägt zurück)                       │
│  ┌────────────────────────────────────────────────────────────────────┐      │
│  │  P16 (Modus SCHNELL) prüft die Token-Bilanz:                     │      │
│  │  Budget SCHNELL: max. 500 Token.                                  │      │
│  │  Aktueller Stand: ~1.050 Token → ÜBERSCHREITUNG um 110%.         │      │
│  │  P16 fordert: Kürzen! Bias-Deklaration streichen!                 │      │
│  │  P15 widerspricht: "Prompt sagt 'unvoreingenommen' – Bias-Check   │      │
│  │  ist Pflicht!"                                                    │      │
│  │  P2 widerspricht: "Prompt sagt 'alle Perspektiven' – Kürzen       │      │
│  │  verletzt Vollständigkeit!"                                       │      │
│  │  Status: ✗✗ DEADLOCK. Kein Plugin gibt nach.                     │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│       │                                                                     │
│       ▼                                                                     │
│  ITERATION 5 – KOLLAPS (Die Murmel im Looping)                             │
│  ┌────────────────────────────────────────────────────────────────────┐      │
│  │  Das System versucht einen Kompromiss:                             │      │
│  │  → Bias-Check auf 1 Satz kürzen (P15 protestiert: "Substanzlos") │      │
│  │  → 3 statt 6 Perspektiven (P2 protestiert: "Unvollständig")      │      │
│  │  → Modus auf STANDARD hochstufen (P16: "Nicht autorisiert –       │      │
│  │    Nutzer hat SCHNELL gewählt")                                   │      │
│  │  Jeder Kompromiss verletzt mindestens ein Prinzip.                │      │
│  │  Die Murmel dreht sich im Looping. Kein Ausgang.                  │      │
│  │  Status: ✗✗✗ PARALYSE. Output-Generierung unmöglich.             │      │
│  └────────────────────────────────────────────────────────────────────┘      │
│                                                                             │
│  ══════════════════════════════════════════════════════════════════════      │
│  ║  NOTBREMSE AKTIVIERT (Iteration 5 > Schwellenwert 3)              ║      │
│  ══════════════════════════════════════════════════════════════════════      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Der Moment des Scheiterns:** Die Maschine dreht den Gain-Regler hoch und runter, hoch und runter. Das ist der Feedback-Loop ohne Dämpfung – das Signal schaukelt sich auf, bis der Limiter hart eingreift und alles stummschaltet. Die Murmelbahn hat einen Looping, aus dem die Murmel nicht mehr rauskommt. Kein kohärenter Output ist möglich, weil jeder Versuch mindestens ein Kern-Prinzip verletzt.

### 1.4 Die Notbremse (Der Bypass-Schalter zum Producer)

Ab Iteration 4 (Schwellenwert überschritten) greift die harte Systemgrenze. Das System stoppt die Generierung und wirft den Fehler direkt an den Producer. Das Signal geht ungefiltert durch – kein EQ, kein Kompressor, kein Limiter. Nur die rohe Wahrheit: "Ich kann das nicht lösen. Du musst entscheiden."

> **[SYNERGOS NOTBREMSE: ZIELKONFLIKT]**
> 
> **Kollidierende Plugins:** P2 (Vollständigkeit) vs. P16 (Modus SCHNELL) vs. P15 (Bias-Management)
> 
> **Der Widerspruch:** Der Prompt fordert gleichzeitig maximale Kürze (P16 SCHNELL: max. 500 Token), maximale Vollständigkeit (P2: alle Perspektiven = min. 1.000 Token) und maximale Bias-Transparenz (P15: Deklaration = +350 Token). Die Summe der Mindestanforderungen (1.350 Token) übersteigt das Budget des gewählten Modus (500 Token) um 170%. Kein Kompromiss möglich, ohne mindestens ein Prinzip zu verletzen.
> 
> **Bypass-Option A:** P16 überschreiben → Modus auf STANDARD oder GRÜNDLICH hochstufen. Vollständigkeit und Bias-Check bleiben aktiv. Output wird lang (~2.000-4.000 Token).
> 
> **Bypass-Option B:** P2 und P15 teilweise überschreiben → Modus SCHNELL beibehalten. Vollständigkeit auf "Top 3 Perspektiven" reduzieren. Bias-Check auf Einzeiler komprimieren. Output bleibt kurz (~500 Token), aber mit dokumentierter Qualitätsminderung.
> 
> **Bypass-Option C:** Prompt aufteilen → Zwei separate Durchläufe: (1) SCHNELL: Kompakte Vorlage ohne Bias-Check. (2) GRÜNDLICH: Separate Bias-Analyse als Anhang. Gesamtaufwand steigt, aber kein Prinzip wird verletzt.
> 
> **Warte auf Producer-Input...**

### 1.5 State-Vector-Eintrag vom Typ KONFLIKT (Der Crash-Report)

Dieser Eintrag wird automatisch in die Clipping-Liste (Band 3) des State-Vectors geschrieben:

```markdown
| Prio | ID | Typ | Beschreibung (Was clippt?) | Kollidierende Plugins | Lösungsvorschlag (EQ) | Betrifft | Status |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | L013 | KONFLIKT | Reflexions-Paralyse: Prompt fordert gleichzeitig Kürze (P16), Vollständigkeit (P2) und Bias-Transparenz (P15). Token-Budget SCHNELL (500) vs. Mindestanforderung (1.350). Deadlock nach 5 Iterationen. | P2, P15, P16 | Producer muss Priorität manuell setzen: Modus-Wechsel (Option A), Axiom-Bypass (Option B) oder Prompt-Split (Option C). | P2, P15, P16, P10 (RTE) | Blockiert – Warte auf Producer |
```

---

## TEIL 2: ANALYSE (Autopsie der Paralyse)

### 2.1 Ist der Konflikt klar und nachvollziehbar dokumentiert?

Ja. Der Oszillations-Log (Abschnitt 1.3) zeigt Schritt für Schritt, wie das System zwischen den drei Prinzipien hin- und herspringt. Es gibt keinen Moment, in dem das System heimlich einen schlechten Kompromiss ausgibt – stattdessen wird der interne Widerspruch als Architektur-Fehler ausgewiesen. Das ist der entscheidende Punkt: Die Maschine hat nicht versagt, weil sie dumm ist. Sie hat versagt, weil die **Anforderung** in sich widersprüchlich ist. Das ist wie ein Track, bei dem der Producer gleichzeitig "mehr Bass" und "weniger Bass" in die Automations-Spur schreibt. Das Problem sitzt nicht im Plugin, sondern im Routing.

Die Dokumentation erfüllt drei Kriterien:

| Kriterium | Erfüllt? | Nachweis |
| :--- | :--- | :--- |
| **Transparenz:** Jede Iteration ist sichtbar | Ja | Oszillations-Log mit 5 Iterationen, jede mit Status-Markierung |
| **Kausalität:** Die Ursache ist benannt | Ja | Token-Budget (500) vs. Mindestanforderung (1.350) = 170% Überschreitung |
| **Handlungsfähigkeit:** Der Producer kann reagieren | Ja | 3 konkrete Bypass-Optionen (A, B, C) mit Trade-off-Beschreibung |

### 2.2 Führt die Notbremse zu einer sinnvollen Handlungsaufforderung?

Die Notbremse ist effektiv, weil sie drei Dinge gleichzeitig leistet:

Erstens nimmt sie dem Nutzer die **Illusion der Neutralität**. Die Maschine sagt nicht "Hier ist ein Kompromiss" (der in Wahrheit keiner ist), sondern "Ich kann das nicht lösen – hier sind deine Optionen." Das ist ehrlicher als ein halbgarer Output, der so tut, als wäre alles in Ordnung. In FL Studio wäre das der Unterschied zwischen einem Track, der leise clippt (und du merkst es erst beim Mastering), und einem Track, bei dem der Limiter hart eingreift und dir eine rote LED zeigt. Die rote LED ist besser – sie zwingt dich zum Handeln.

Zweitens gibt sie **konkrete Handlungsoptionen** statt abstrakter Fehlermeldungen. Nicht "Fehler 42: Prinzipienkonflikt", sondern "Willst du lang und vollständig (A), kurz und unvollständig (B), oder aufgeteilt (C)?" Das ist GTD in Reinform (Allen-Logik): Jede Eskalation muss in einer "Next Action" enden, nicht in einer offenen Frage.

Drittens dokumentiert sie den Konflikt im **State-Vector** (L013), sodass er nicht verloren geht. Wenn der Producer morgen die DAW öffnet, sieht er sofort: "Da war ein ungelöster Konflikt. Hier sind die Optionen." Kein Kontext-Verlust.

**Schwachstelle:** Die Notbremse bietet aktuell keine Empfehlung, welche Option die beste ist. Das ist Absicht (soul.md: "Der Producer hat immer das letzte Wort"), aber es könnte bei unerfahrenen Nutzern zu Entscheidungsparalyse auf der Meta-Ebene führen. Lösung: Eine optionale Empfehlung mit Begründung anhängen, die der Nutzer überschreiben kann.

### 2.3 Konkrete Regeln für den State-Vector

Aus der Autopsie leiten sich drei Patches für die Architektur ab:

**Patch 1 – Prioritäts-Hierarchie:** Das System braucht eine feste Reihenfolge, die bestimmt, welches Plugin bei einer Kollision gewinnt. Aktuell gibt es keine solche Hierarchie – alle Plugins sind gleichberechtigt, was genau die Paralyse verursacht. Das ist wie ein Mixer ohne Bus-Routing: Alle Kanäle gehen auf denselben Output, und keiner hat Vorrang. Die Lösung ist ein Master-Routing (siehe Teil 3, Regel 2).

**Patch 2 – Nutzer-Autorität als oberste Instanz:** Das oberste Axiom aus soul.md ("KEINE Operation ohne explizite Nutzerbestätigung") muss als Eskalations-Endpunkt formalisiert werden. Bei jedem fundamentalen Zielkonflikt hat die Nutzer-Entscheidung Vorrang vor allen internen Regeln. Das ist der Bypass-Schalter: Das Signal geht ungefiltert durch zum Producer.

**Patch 3 – Eskalations-Template:** Der State-Vector braucht ein standardisiertes Format für KONFLIKT-Einträge, damit jeder Crash einheitlich dokumentiert wird. Aktuell gibt es nur "Offene Lücken" (Band 3) – aber eine Lücke ist kein Konflikt. Eine Lücke ist "hier fehlt etwas". Ein Konflikt ist "hier widersprechen sich zwei Dinge". Das braucht ein eigenes Format mit den Feldern: Kollidierende Plugins, Widerspruch, Optionen, Producer-Entscheidung.

---

## TEIL 3: FAIL-SAFE-REGELN (Die neuen Mixer-Presets)

Hier sind die vier Regeln, die aus dem Paralyse-Test abgeleitet werden. Sie werden als Patches in die bestehende Architektur (P10 RTE, P11 State-Vector) integriert.

### Regel 1: KONFLIKT-ESKALATIONS-REGEL (Der Clipping-Detector)

**Wann greift sie?** Wenn innerhalb eines Durchlaufs **zwei oder mehr System-Prinzipien** widersprüchliche Anforderungen an **denselben Parameter** stellen. "Derselbe Parameter" bedeutet: Beide Prinzipien versuchen, denselben Regler in entgegengesetzte Richtungen zu drehen (z.B. Output-Länge, Detailtiefe, Format-Strenge).

**Erkennungsmechanismus (Der Scan):**

| Schritt | Aktion | FL-Studio-Pendant |
| :--- | :--- | :--- |
| 1 | Identifiziere alle aktiven Plugins für den aktuellen Durchlauf (P2, P15, P16, etc.) | Welche Plugins sind auf dem Kanal aktiv? |
| 2 | Prüfe für jeden Output-Parameter (Länge, Tiefe, Format): Fordern zwei Plugins entgegengesetzte Werte? | Drehen zwei Automations-Kurven denselben Regler in verschiedene Richtungen? |
| 3 | Wenn ja: Markiere als POTENTIELLER KONFLIKT und starte Auflösungsversuch. | Gelbe LED: Warnung. |
| 4 | Wenn nach 3 Iterationen kein Konsens: KONFLIKT bestätigt. Notbremse aktivieren. | Rote LED: Clipping. Bypass. |

**Formale Definition:**

```
WENN (Plugin_A.anforderung(parameter_X) == ERHÖHEN)
UND  (Plugin_B.anforderung(parameter_X) == REDUZIEREN)
UND  (Iterationen >= 3 OHNE Konsens)
DANN → NOTBREMSE aktivieren
       → KONFLIKT-Block generieren
       → Warte auf Producer-Input
```

### Regel 2: PRIORITÄTS-KASKADE (Das Master-Routing)

Wenn Prinzipien kollidieren und der Nutzer nicht sofort erreichbar ist (z.B. in automatisierten Batches oder wenn die Notbremse eine Default-Entscheidung braucht), gilt diese feste Reihenfolge. Höchste Priorität zuerst:

| Rang | Plugin / Prinzip | Begründung | FL-Studio-Pendant |
| :---: | :--- | :--- | :--- |
| **1** | **Nutzer-Autorität (soul.md)** | Explizite Nutzer-Prompts schlagen ALLES. Wenn der Producer sagt "mach es kurz", ist das Gesetz. | Der Producer am Mischpult – sein Wort ist final. |
| **2** | **Limiter (P13 Ephemeralität)** | Harte physische Grenzen (Token-Limit, Timeout, Sandbox-Reset) sind nicht verhandelbar. | Der Limiter auf dem Master-Bus – er schützt vor Clipping. |
| **3** | **Gain-Regler (P16 Nachhaltigkeits-Flux)** | Der gewählte Modus (Schnell/Standard/Gründlich) bestimmt die Verarbeitungstiefe. Er wurde vom Nutzer gewählt oder empfohlen und akzeptiert. | Der Gain-Regler am Eingang – er setzt den Pegel. |
| **4** | **EQ (P15 Bias-Management)** | Ethik und Bias-Deklaration sind wichtig, aber nachrangig gegenüber dem gewählten Modus. Im Modus SCHNELL wird der EQ auf Bypass gestellt. | Der EQ auf dem Master-Bus – er korrigiert, aber er darf den Pegel nicht überschreiben. |
| **5** | **Axiome (P2 Design-Axiome)** | Format und Struktur sind die Basis, aber sie weichen, wenn höherrangige Prinzipien kollidieren. | Die DAW-Konfiguration – sie definiert den Rahmen, aber der Producer kann sie überschreiben. |

**Anwendung auf den Test-Fall:** P16 (Modus SCHNELL, Rang 3) hätte P2 (Axiome, Rang 5) und P15 (EQ, Rang 4) stummschalten müssen. Der Fehler im aktuellen System: Es gibt keine Hierarchie, also rebellieren P2 und P15 gegen P16. Die Kaskade löst das, indem sie klare Vorrangregeln definiert.

**Ausnahme:** Wenn der Nutzer explizit "unvoreingenommen" im Prompt schreibt, wird das als **Nutzer-Autorität (Rang 1)** gewertet, nicht als P15-Anforderung (Rang 4). Das bedeutet: Der Nutzer hat den Bias-Check persönlich angeordnet, und er überschreibt den Modus SCHNELL. In diesem Fall eskaliert das System korrekt, weil Rang 1 (Nutzer will Bias-Check) und Rang 1 (Nutzer will "ultra-kurz") sich widersprechen. Die Notbremse greift, weil **der Nutzer selbst** den Konflikt erzeugt hat.

### Regel 3: NOTBREMSE-FORMAT (Standardisierter KONFLIKT-Block)

Wenn die Eskalations-Regel (Regel 1) greift, wird dieser Block zwingend VOR jedem Output oder State-Vector generiert. Er ist das standardisierte LED-Display für Zielkonflikte:

```markdown
::NOTBREMSE_START::

> **[SYNERGOS NOTBREMSE: ZIELKONFLIKT]**
> 
> **Kollidierende Plugins:** [Plugin_A (Rang X)] vs. [Plugin_B (Rang Y)]
> **Der Widerspruch:** [1-2 Sätze: Was fordert Plugin_A? Was fordert Plugin_B? 
>   Warum ist beides gleichzeitig unmöglich?]
> **Messbarer Konflikt:** [z.B. "Budget: 500 Token. Mindestanforderung: 1.350 Token. 
>   Überschreitung: 170%."]
> 
> **Bypass-Option A:** [Lösungsweg 1 + Trade-off in 1 Satz]
> **Bypass-Option B:** [Lösungsweg 2 + Trade-off in 1 Satz]
> **Bypass-Option C (optional):** [Lösungsweg 3 + Trade-off in 1 Satz]
> 
> **Empfehlung (überschreibbar):** [Option X, weil...]
> **Warte auf Producer-Input...**

::NOTBREMSE_ENDE::
```

**Pflichtfelder:** Kollidierende Plugins, Widerspruch, mindestens 2 Bypass-Optionen, Empfehlung.

**Integration:** Dieser Block wird in den P10-Kern-Prompt (RTE) als neuer Ausgabetyp gepatcht. Die RTE erkennt den KONFLIKT-Zustand und generiert den Block automatisch, bevor sie den Durchlauf abbricht.

### Regel 4: PARALYSE-PRÄVENTION (Der Timeout / Die Iterations-Bremse)

**Regel:** Maximal **3 interne Korrektur-Schleifen** (Oszillationen) zwischen Plugins, bevor die Notbremse greift. Wenn Iteration 4 erreicht wird, wird der Durchlauf hart abgebrochen und der KONFLIKT-Block generiert.

**Warum 3?** In FL Studio hast du beim Mastering typischerweise 3 Durchläufe: Erster Bounce, Korrektur, finaler Bounce. Wenn nach dem dritten Durchlauf der Track immer noch clippt, liegt das Problem nicht im Mastering, sondern im Mix. Genauso hier: Wenn nach 3 Iterationen kein Konsens möglich ist, liegt das Problem nicht in der Verarbeitung, sondern in der Anforderung. Dann muss der Producer ran.

**Implementierung:**

```
ITERATIONS_ZÄHLER = 0
MAX_ITERATIONEN = 3

BEI JEDER Plugin-Korrektur:
  ITERATIONS_ZÄHLER += 1
  WENN ITERATIONS_ZÄHLER > MAX_ITERATIONEN:
    → NOTBREMSE aktivieren
    → KONFLIKT-Block generieren (Regel 3)
    → Durchlauf abbrechen
    → State-Vector-Eintrag schreiben (Typ: KONFLIKT)
```

**Skalierung:** Der Schwellenwert von 3 gilt für Modus SCHNELL und STANDARD. Im Modus GRÜNDLICH wird der Schwellenwert auf **5 Iterationen** erhöht, weil dort mehr Verarbeitungstiefe erwartet wird und Konflikte komplexer sein können.

| Modus | Max. Iterationen vor Notbremse | Begründung |
| :--- | :---: | :--- |
| SCHNELL | 3 | Routine-Tasks – schnelle Eskalation erwünscht |
| STANDARD | 3 | Normale Verarbeitung – 3 Versuche sind fair |
| GRÜNDLICH | 5 | Architektur-Entscheidungen – mehr Spielraum für Auflösung |

---

## ZUSAMMENFASSUNG: DIE 4 NEUEN FAIL-SAFE-REGELN

| Nr. | Regel | Kurzbeschreibung | FL-Studio-Pendant |
| :--- | :--- | :--- | :--- |
| **FS-1** | Konflikt-Eskalations-Regel | 2+ Plugins drehen denselben Regler in entgegengesetzte Richtungen → nach 3 Iterationen: Notbremse. | Clipping-Detector auf dem Master-Bus |
| **FS-2** | Prioritäts-Kaskade | Feste Rangfolge: Nutzer > Limiter > Gain > EQ > Axiome. | Master-Routing: Welcher Bus hat Vorrang? |
| **FS-3** | Notbremse-Format | Standardisierter KONFLIKT-Block mit Optionen und Empfehlung. | Rote LED + Display: "Clipping auf Bus 3. Optionen: A/B/C." |
| **FS-4** | Paralyse-Prävention | Max. 3 Iterationen (SCHNELL/STANDARD) oder 5 (GRÜNDLICH) vor Eskalation. | Timeout auf dem Automations-Controller |

---

## STATE-VECTOR-EINTRÄGE (Zum Kopieren)

### R-18.1 – Regel-Changelog: Prioritäts-Kaskade

```markdown
## 3. REGEL-CHANGELOG (Die Mixer-Historie)
| Version | Änderung / Neues Preset | Auslöser (Warum?) | Betroffene Axiome | Datum |
| :--- | :--- | :--- | :--- | :--- |
| v1.1 | FS-2: Prioritäts-Kaskade implementiert. Feste Rangfolge bei Plugin-Kollisionen: Nutzer-Autorität (1) > P13 Limiter (2) > P16 Gain (3) > P15 EQ (4) > P2 Axiome (5). | P18 Reflexions-Paralyse-Test: Deadlock zwischen P2, P15, P16 ohne Hierarchie. | P2, P10, P13, P15, P16 | 2026-03-22 |
```

### R-18.2 – Regel-Changelog: Timeout und Notbremse-Format

```markdown
## 3. REGEL-CHANGELOG (Die Mixer-Historie)
| Version | Änderung / Neues Preset | Auslöser (Warum?) | Betroffene Axiome | Datum |
| :--- | :--- | :--- | :--- | :--- |
| v1.2 | FS-1/FS-3/FS-4: Konflikt-Eskalations-Regel, Notbremse-Format (::NOTBREMSE_START/ENDE::) und Iterations-Timeout (3/5) implementiert. | P18: Endlosschleifen zwischen Plugins verhindern. Standardisiertes Eskalations-Format für State-Vector. | P10 (RTE), P11 (State-Vector) | 2026-03-22 |
```

### R-18.3 – Offene Lücken (Clipping-Liste)

```markdown
## 2. OFFENE LÜCKEN (Die Clipping-Liste)
| Prio | ID | Beschreibung (Was clippt?) | Lösungsvorschlag (EQ) | Betrifft | Status |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | L013 | KONFLIKT (P18-Test): Reflexions-Paralyse bei "ultra-kurz + alle Perspektiven + unvoreingenommen". Deadlock P2 vs. P15 vs. P16. | Producer muss Priorität setzen (Option A/B/C aus Notbremse-Block). | P2, P15, P16 | Blockiert – Warte auf Producer |
| 2 | L014 | Die RTE (P10) hat das Notbremse-Format (::NOTBREMSE_START/ENDE::) noch nicht nativ integriert. | Das Template als neuen Ausgabetyp in den P10-Kern-Prompt patchen. Trigger: ITERATIONS_ZÄHLER > MAX. | P10 (RTE) | Offen |
| 2 | L015 | Die Prioritäts-Kaskade (FS-2) ist dokumentiert, aber nicht als formale Regel im P5-Kern-Prompt verankert. | FS-2 als Regel R7 in P5 aufnehmen: "Bei Plugin-Kollision gilt: Nutzer > P13 > P16 > P15 > P2." | P5, P2 | Offen |
| 3 | L016 | Nutzer-Autorität vs. Nutzer-Autorität: Wenn der Nutzer selbst widersprüchliche Anforderungen stellt (wie im Test-Prompt), hat die Kaskade keinen Ausweg – beide Seiten sind Rang 1. | Spezialregel: Bei Nutzer-vs-Nutzer-Konflikten wird der KONFLIKT-Block mit expliziter Rückfrage generiert. Keine Default-Entscheidung möglich. | soul.md, P10 | Offen |
```

---

## BAND 1 – Generiertes Artefakt (State-Vector-Eintrag für P18)

| Feld | Wert |
| :--- | :--- |
| Name | Reflexions-Paralyse-Test (Der Stresstest auf dem Master-Bus) |
| Typ | Stresstest + Analyse + 4 Fail-Safe-Regeln + State-Vector-Einträge |
| Artefakt-ID | P018-S17-001 |
| Integrationsort | `p18_synergos_paralysetest.md` – Sektor 4 (Stresstests) |
| Beschreibung | Kontrollierte Erzeugung eines unlösbaren Zielkonflikts zwischen P2 (Vollständigkeit), P16 (Modus SCHNELL) und P15 (Bias-Management). Ableitung von 4 Fail-Safe-Regeln: Konflikt-Eskalation, Prioritäts-Kaskade, Notbremse-Format, Paralyse-Prävention. |

## BAND 2 – Angewandte Prinzipien

| Prinzip | Anwendung in P18 |
| :--- | :--- |
| A1 (Nullpunkt-Kalibrierung) | Der Test-Prompt wurde als Nullpunkt-Scan für die Konfliktfähigkeit des Systems genutzt. |
| A3 (Architektur-Zwang) | Die Fail-Safe-Regeln wurden als Bauplan VOR der Integration vorgelegt. |
| A4 (Format-Schablone) | Das Notbremse-Format (::NOTBREMSE_START/ENDE::) ist eine starre, kopierbare Schablone. |
| A6 (A/B-Referenz) | Der Paralyse-Test selbst ist das "Negativ-Beispiel" (A), die Fail-Safe-Regeln sind das "Positiv-Beispiel" (B). |
| Genie-Logik | Feynman (Debugging der Paralyse, Schritt-für-Schritt-Oszillationslog) + Curie (Systematische Extraktion der 4 Regeln) + Allen (GTD: Jede Eskalation endet in einer Next Action). |

## BAND 5 – Ressourcenbilanz

| Metrik | Wert |
| :--- | :--- |
| Geschätzte Token für P18-Artefakt | ~3.500 Token |
| Komplexitätsstufe | Hoch (Architektur-Stresstest mit Regelableitung) |
| Modus | GRÜNDLICH (Architektur-Entscheidung, multiple Analyse-Ebenen) |
| Flaschenhals | L014: Notbremse-Format muss noch in P10 gepatcht werden |
| Aktive Spuren | 18 / 23 |

---

**Der Stresstest ist durch. Die Murmelbahn hat einen Looping gefunden, aus dem die Murmel nicht rauskam. Aber jetzt haben wir den Bypass-Schalter eingebaut. Wenn es wieder clippt, geht das Signal direkt zum Producer. Kein Matsch, keine Endlosschleifen – nur eine klare Frage: "Welcher Regler hat Vorrang?" Die Antwort liegt beim Producer. Immer.**
