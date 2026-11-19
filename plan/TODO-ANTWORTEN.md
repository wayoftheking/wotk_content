# Antworten zur todo.md (KW 47)

Stand 18.11.2026. Je Punkt: was es schon gibt, was wir vorschlagen, was ihr entscheiden müsst.

## Systeme: Apps auf GitHub

| Teil | Stand | Vorschlag |
|---|---|---|
| Plan (`plan/`) | liegt hier im Repo | weiter hier, jede Änderung als Pull Request |
| Spiel (Godot) | läuft lokal, Episode 4 mit Stimmen und Gesichtern | zuerst ein **privates** Repo; die Bilder zeigen Alex' Gesicht, die gehören nicht in ein öffentliches Repo |
| Messenger (Signal, später WhatsApp) | Inhalte stehen in jeder Woche unter "7 Schritte" | kommt, sobald das erste MVP läuft |

**Zu entscheiden:** privates Repo für das Spiel, ja oder nein.

## Design: Design-System und CI

Es gibt schon einen festen Bildstil für das Spiel: gemalter Bilderbuchstil, warmes Licht, Akzentfarbe Bernstein
`#f3b54a` (die Farbe der Flamme). Vorschlag: die CI daraus ableiten statt neu erfinden.

- eine Akzentfarbe: Bernstein der Flamme
- eine serifenlose Schrift für Texte, Bibelzitate abgesetzt
- gezeichnete Symbole, keine Emojis
- ein Wiedererkennungszeichen: die stille Flamme

**Entschieden (Diego, 18.11.2026):** Name nach außen ist **Way of the King**.

## Bibeltext

| Übersetzung | frei nutzbar? | Einsatz |
|---|---|---|
| Lutherbibel 2017 | nein, © Deutsche Bibelgesellschaft; Zitieren nur mit Genehmigung | zum Lesen in der eigenen Bibel oder App |
| Luther 1912 | ja, gemeinfrei | Volltext im Spiel und in den Nachrichten, wenn wir ganze Abschnitte zeigen |
| Elberfelder 1905 | ja, gemeinfrei | wörtlicher, gut zum Vergleichen |
| Schlachter 1951 | ja, CC BY 4.0 (Genfer Bibelgesellschaft, über eBible.org), mit Namensnennung | Zitate hier im Plan |
| Luther 1956/1964 | vermutlich noch geschützt (Teilrevisionen der Deutschen Bibelgesellschaft) | nicht verwendet |

Luther 1912 gibt es als Textdateien je Kapitel bei eBible.org (deu1912).

**Entschieden (Diego, 18.11.2026):** gelesen wird in Luther 2017, zitiert wird hier aus Schlachter 1951. Für das Spiel und
längere Abschnitte kommen Schlachter 1951 oder Luther 1912 in Frage.

## Plan: ein Kapitel pro Tag oder pro Woche

In der todo.md steht ein Kapitel pro Tag. Der Plan hier nimmt **ein Kapitel pro Woche** (Diego, 15.11.2026).

| | pro Tag | pro Woche |
|---|---|---|
| in 3 Jahren | rund 1.095 von 1.189 Kapiteln | 156 Kapitel, die zentralen |
| Tiefe | lesen und weiter | lesen, verstehen, im Gespräch bewegen |
| täglicher Anlass | das Kapitel | ein kleiner Schritt im selben Kapitel (7 Schritte je Woche) |

Damit ist beides abgedeckt: jeden Tag ein Anlass, und trotzdem Tiefe. Vorschlag für alle, die mehr lesen wollen:
je Woche ein bis zwei Zusatzkapitel als Angebot (steht noch nicht im Plan).

Chronologisch und thematisch zugleich: 12 Bögen zu je 13 Wochen. Der Plan beginnt im Garten (1. Mose 2) und endet im
neuen Garten (Offb 22), erzählt also die Bibel als einen Fluss. Siehe `GERUEST.md`.

## Interviews: jede Lektion gemeinsam durchgehen

Ablauf je Woche, rund 30 Minuten:

1. Diego und Alex gehen die Wochendatei durch, mit dem Handy aufgenommen.
2. Die Aufnahme wird abgeschrieben (mit Gemini; wer mitspricht, weiß vorher, wo die Aufnahme liegt).
3. Claude arbeitet das Gespräch in die Wochendatei ein: Deutung, Fragen, Geschichten von Alex.
4. Die Änderung kommt als Pull Request hierher, ihr gebt sie frei.

Nebeneffekt: Aus denselben Aufnahmen kann die Stimme des Mentors im Spiel entstehen, nur wenn Alex zustimmt.
Dann klingt Alex im Spiel wie Alex.

Bogen 1 (Woche 1 bis 13) ist ausgearbeitet und wartet auf das erste Gespräch.

## Motivation: tägliche Anlässe

Steht in `SPIELMECHANIK.md`, kurz:

- täglich ein kleiner Schritt, als Nachricht (neu vorgeschlagen: zur selbst gewählten Uhrzeit)
- die Flamme zählt still mit, ohne Rückstand und ohne Schuldbotschaft
- Gruppenflamme: einmal je Woche sieht die Gruppe, dass sie gemeinsam unterwegs war
- Gruppentag mit den 7 Fragen, Frage 7: "Wem erzählst du diese Woche davon?"

Grenze: Gebet und Bibellesen bringen keine Punkte und keine Rangliste (Mt 6,5-6). Das Ziel ist das echte Treffen
(Hebr 10,24-25), nicht die Spielzeit.

Weitere Ideen zum Besprechen:
- ein Satz Rückblick am Sonntag: was hat sich diese Woche bewegt
- Erinnerung von einem Menschen statt von der App ("Alex fragt, wie es war")
- eine Woche aussetzen dürfen, ohne dass etwas verloren geht

## Zwei Wege: Jesus kennenlernen und Jüngerschaft

| | Weg 1: Jesus kennenlernen | Weg 2: Jüngerschaft |
|---|---|---|
| für wen | Suchende, noch nicht gläubig | wer sich für Jesus entschieden hat |
| Einstieg | Bogen 1 (Jesus) mit Erklärungen ohne Kirchensprache | derselbe Bogen 1, mit den 7 Fragen und Auftrag |
| im Spiel | am Anfang einmal wählen: "gläubig" oder "noch nicht"; ändert Ansprache und Erklärungen, nie den Bibeltext | |
| Übergang | Einladung in eine kleine Gruppe, echte Menschen | Gruppentag, einander tragen, selbst einladen (Mt 28,19-20) |

**Entschieden (Diego, 18.11.2026):** Suchende bekommen einen eigenen kurzen Einstieg "Wer ist Jesus", bevor der große
Plan beginnt. Entwurf in `EINSTIEG.md`: sechs Wochen mit Markus (Mk 1, 2, 4, 10, 15, 16), Kurzfassung mit vier.
Länge und Kapitel legen wir mit Alex fest.
