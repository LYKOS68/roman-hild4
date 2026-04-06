# MASTER_PROTOCOL

## STATUS

| Feld | Wert |
|---|---|
| Modus | Kalibrierung |
| Zweck | Sanierung von Struktur, Regeln, Routing und Ausführung |
| Träger | Eine zentrale Markdown-Datei |
| Quelle | Bisheriger Projektverlauf und explizite Nutzervorgaben |
| Ziel | Reproduzierbares, adressierbares, kontrolliertes Arbeiten auf vorhandenen Dateiprojekten |

## PROBLEMRAHMEN

Das Kernproblem ist **nicht** nur ein chaotischer Ordnerbaum, sondern ein fehlendes **Steuerungsprotokoll**. Es gibt zu viele Ordner, zu viele Subordner, zu viele Dateien ohne Inhalt, zu viele Dateien ohne Format und zu viele Artefakte ohne eindeutige Adresse. Gleichzeitig existieren Regeln, Gesetze und Begriffe, ohne dass ihre Einhaltung technisch oder prozessual erzwungen wird. Dadurch entstehen unklare Anweisungen, falsche Zeitformen, Beschreibungen statt operativer Direktiven und fehlende Klarheit über Herkunft, Ziel, Zuständigkeit, Zweck und Randbedingungen.

Die Folge ist eine wiederkehrende Fehlform: Es wird generiert, bevor definiert ist, **woraus** generiert werden darf, **wie** verarbeitet werden muss, **welche Datei welchen Effekt auslöst** und **unter welchen Bedingungen ein Prozess stoppen muss**. Genau diese Blind-Generierung ist zu unterbinden.

## OBERSTES AXIOM

> Keine Generierung ohne gebundene Basis. Keine Analyse ohne adressierbare Quelle. Keine Umstrukturierung ohne Audit. Kein Push ohne Freigabe.

## DATEIBEZUGS-AXIOM

Ab sofort gilt, dass jede Analyse, Extraktion, Umordnung oder Ableitung **nur** auf **vorhandenen Dateiprojekten** erfolgen darf. Es werden keine generischen Beispiel-Templates erzeugt, keine theoretischen Platzhalter erfunden und keine frei formulierten Beschreibungen als Ersatz für echte Rohdaten akzeptiert. Jede Reproduktion muss direkt auf vorhandene Projektdateien bezogen sein.

| Regel | Wirkung |
|---|---|
| Nur vorhandene Dateiprojekte | echte Basis statt Raten |
| Keine generischen Beschreibungen | keine Pseudo-Antworten |
| Keine Beispiel-Templates | keine Schein-Struktur |
| Reproduktion nur aus Rohdaten | Muster müssen aus Dateien abgeleitet werden |

## ZIELMODELL

Das Projekt soll in ein System überführt werden, in dem jede relevante Einheit eindeutig an **Adresse**, **Zweck**, **Zustand**, **Besitzer**, **Zielsystem**, **Eingangsart** und **Ausgangswirkung** gebunden ist. Eine Datei ist erst dann gültig, wenn klar ist, woher sie kommt, wohin sie gehört, wem sie dient, in welchem Status sie sich befindet und welche operative Funktion sie erfüllt.

## ADRESSMODELL

| Feld | Bedeutung | Pflicht |
|---|---|---|
| Adresse | Zielort oder Zielsystem der Datei oder Anweisung | ja |
| Träger | Dateiformat oder Kanal der Übertragung | ja |
| Richtung | von wo nach wo | ja |
| Besitzer | verantwortliche Instanz | ja |
| Zweck | warum die Einheit existiert | ja |
| Zustand | Referenz, Arbeit, Archiv, Leer, Unklar | ja |
| Gate | Freigabebedingung vor Mutation | ja |

Wenn eine dieser Angaben fehlt, ist die Einheit als **unvollständig** zu markieren und darf nicht aktiv weiterverarbeitet werden.

## FEHLERKLASSEN

| Klasse | Beschreibung | Konsequenz |
|---|---|---|
| Leerdatei | Datei ohne verwertbaren Inhalt | markieren, nicht priorisieren |
| Formatlos | Datei ohne klare Endung oder Rolle | klassifizieren, nicht verschieben |
| Adresslos | kein Ziel, kein Besitzer, kein Zweck | sperren bis Klärung |
| Regelbruch | Anweisung widerspricht vorhandenen Gesetzen | stoppen |
| Beschreibung statt Anweisung | Text benennt nur Absichten, keine operative Direktive | umformulieren oder sperren |
| Routing-Fehler | unklar von wem an wen wohin | stoppen |
| Dublette | inhaltlich redundante Kopie | markieren, nicht sofort löschen |
| Unklar | nicht eindeutig bewertbar | in Review-Zone verschieben |

## FORMAT-PROTOKOLL

Die Dateiformate dürfen nicht nur technisch verstanden werden, sondern müssen als **Wirkungsträger** definiert sein.

| Format | Primäre Funktion | Zulässige Wirkung | Verbotene Wirkung |
|---|---|---|---|
| `.md` | Referenz, Protokoll, Regelwerk, Auditbericht | dokumentieren, binden, erklären, freigeben | verdeckte Zustandsdaten ohne Kennzeichnung |
| `.yaml` / `.yml` | Routing, Konfiguration, strukturierte Regeln | Maschinenlogik, Mapping, Parameterbindung | freie Prosa ohne Schema |
| `.json` | kanonische Zustandsdaten, Inventar, Analyseobjekte | maschinenlesbare Fakten, Klassifikation, Status | unscharfe Mehrdeutigkeit |
| `.txt` | Rohtext, Extrakte, Übergangsablage | schnelle Rohaufnahme, unformatierte Quelle | finale Steuerlogik |
| ohne Endung | ungültig bis Klassifikation | keine | operative Nutzung |
| Skriptdateien | Transformation, Prüfung, Automatisierung | ausführen nur nach Freigabe | unkontrollierte Mutation |

## OUTPUT-VERTRAG

Eine gültige Antwort darf keine leere Bestätigung und keine ungebundene Zustimmung sein. Sie muss auf einer identifizierbaren Basis beruhen, einen klaren Zweck erfüllen und als kontrollierte Aktion oder als kontrolliertes Ergebnis adressierbar sein.

| Gültig | Ungültig |
|---|---|
| referenzbasiert | erfunden |
| dateibezogen | allgemein ausgedacht |
| adressierbar | ohne Ziel oder Besitzer |
| reproduzierbar | situationsabhängig und unprüfbar |
| kontrolliert | blind generiert |
| zustandsklar | vermischte Rollen |

## IF-THEN-STOP-LOGIK

| Bedingung | Reaktion |
|---|---|
| IF keine Basis definiert | STOP |
| IF kein System oder keine Adresse definiert | STOP |
| IF Träger oder Richtung fehlen | STOP |
| IF Quelle nicht als Datei oder Projekt referenzierbar ist | STOP |
| IF Regelkonflikt erkannt wird | STOP und Regel-Audit |
| IF Meta-Gate fehlschlägt | RESET → Analyse → Neuentscheidung |
| IF Datei leer oder formatlos ist | markieren statt mutieren |
| IF Nutzerfreigabe für kritische Mutation fehlt | kein Move, kein Delete, kein Push |

## SANIERUNGSLOGIK FÜR DEN ORDNERRAUM

Die Sanierung darf nicht als Großaktion beginnen. Der erste Fehler wäre, sofort umzuräumen oder zu löschen. Stattdessen muss der Ist-Zustand zuerst als auditierbare Realität sichtbar gemacht werden. Erst danach dürfen Regeln extrahiert, Klassifikationen gesetzt und Zielstrukturen vorgeschlagen werden.

| Phase | Inhalt | Änderungen erlaubt? |
|---|---|---|
| 1 | Root-Audit | nein |
| 2 | Regel-Audit | nein |
| 3 | Datei-Klassifikation | nein |
| 4 | Zielstruktur-Entwurf | nein |
| 5 | Migrationsregeln | nein |
| 6 | Batch-Moves | nur nach Freigabe |
| 7 | Push | nur nach Freigabe |

## 23-SESSION-MODELL

Die Idee einer längeren gemeinsamen Sanierung ist sinnvoll, wenn jede Sitzung genau einen kontrollierten Zustand besitzt und nicht mehrere Ebenen vermischt.

| Session-Typ | Zweck | Ergebnis |
|---|---|---|
| Audit-Session | Bestand sichtbar machen | Baum, Inventar, Anomalien |
| Regel-Session | Gesetze und Pflichten festschreiben | Regeldatei |
| Mapping-Session | alte Struktur auf neue Struktur abbilden | Migrationsmatrix |
| Review-Session | unklare Dateien entscheiden | Freigaben oder Sperren |
| Move-Session | freigegebene Umordnung | kontrollierte Mutation |
| Push-Session | bestätigten Zustand veröffentlichen | Commit und Push |

## ANALYSEPROTOKOLL FÜR ROHDATEN

Der Analysehebel liegt in den Dateien selbst. Daher muss der Analyseschritt die Rohdaten durchlaufen und wiederkehrende Strukturen extrahieren. Das gilt für Begriffe, Cluster, Satzmuster, semantische Anker, Kommandoformen, Regelverweise und wiederkehrende Übergänge zwischen Zuständen.

| Analyseschritt | Ziel |
|---|---|
| Häufige Begriffe identifizieren | semantische Schwerpunkte sichtbar machen |
| Cluster bilden | thematische Gruppen aus Projektdaten extrahieren |
| Wiederkehrende Satzstrukturen extrahieren | operative Sprachmuster erkennen |
| Semantische Anker benennen | stabile Referenzpunkte des Systems definieren |
| Adress- und Routingmuster prüfen | von wem an wen wohin wozu sichtbar machen |

Das Ergebnis dieser Analyse ist ein **persönliches Semantic-Lexikon**, das kontrolliert, reproduzierbar und adressierbar ist.

## ROUTING-REGELN

Jede Eingabe muss an ein bestehendes System oder an eine definierte Basis gebunden sein. Ohne diese Bindung ist sie ein ungebundenes Paket. Vor jeder Ausführung muss klar sein, welche Quelle in welches System gelangt, welcher Träger genutzt wird, welche Richtung gilt und welche Nebenbedingungen aktiv sind.

| Feld | Leitfrage |
|---|---|
| Woher? | Welche Datei oder welches Projekt ist die Quelle? |
| Wohin? | Welcher Zielordner, welches Zielsystem, welches Artefakt? |
| Von wem? | Welche Instanz ist verantwortlich? |
| An wen? | Welche Instanz oder welcher Nutzer empfängt das Ergebnis? |
| Weshalb? | Welcher Zweck rechtfertigt die Operation? |
| Was beachten? | Welche Regeln, Sperren und Gates gelten? |

## PUSH-PROTOKOLL

Pushes dürfen nicht implizit geschehen. Sie sind eine veröffentlichende Mutation und benötigen daher ein explizites Freigabegate.

| Stufe | Bedingung |
|---|---|
| Datei erstellt | lokal möglich |
| Datei geändert | lokal möglich |
| Datei verschoben | nur nach Freigabe |
| Datei gelöscht | nur nach expliziter Sonderfreigabe |
| Commit | nur nach Review |
| Push | nur nach Nutzerfreigabe |

## ARBEITSREGEL FÜR DIE WEITEREN SCHRITTE

Ab jetzt soll nicht mehr gefragt werden, welche Theorie man noch bauen könnte, sondern welche **vorhandenen Dateien** als Basis nutzbar sind, warum sie relevant sind und welche konkrete Wirkung ein Ergebnis haben soll. Der Fokus liegt nicht auf „Was könnte man generieren?“, sondern auf „Wie wird aus vorhandenen Projektdateien kontrolliert verarbeitet, klassifiziert, gebunden und nur dann mutiert, wenn die Gates erfüllt sind?“.

## NÄCHSTER MINIMALSCHRITT

Der nächste sinnvolle Schritt ist **kein globales Umsortieren** und **kein blindes Löschen**, sondern ein reines **Root-Audit** auf dem tatsächlichen Projektbestand. Danach folgen Regel-Audit, Klassifikation und erst dann Migrationsentscheidungen in kleinen freigegebenen Batches.

| Minimale Eingaben | Zweck |
|---|---|
| ROOT | Zielbasis für das Audit |
| SCOPE | welcher Teil analysiert wird |
| DATEITYPEN | welche Formate priorisiert werden |
| AUSSCHLUSS | was ignoriert werden soll |
| PUSH | ob nur vorbereitet oder tatsächlich veröffentlicht wird |

## SCHLUSSSATZ

Dieses Protokoll dient als zentrale Bindung zwischen Projektstruktur, Regelwerk, Analyse, Routing und Ausführung. Es ersetzt Blind-Generierung durch kontrollierte, dateibezogene, reproduzierbare Verarbeitung.
