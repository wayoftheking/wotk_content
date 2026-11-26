# Plan: 3 Jahre in Teilen

Die Reihenfolge ist der 3-Jahres-Plan in `read_plans/3y_plan_de.csv`: 1.095 Schritte, ein Kapitel je Schritt,
die ganze Bibel, ungefähr in der Zeit der Ereignisse. Hier ist er in 189 Teile zu je 1 bis 8 Schritten
eingeteilt, ohne Datum, jeder mit einem Titel und einem Satz, worum es geht. "3 Jahre" ist nur ein Richtwert: jeder geht in
seinem Tempo, der eine in 1 Jahr, der andere in 3, der nächste in 5.

| Datei | Inhalt |
|---|---|
| `TEILE.md` | Die Übersicht zum Lesen: Einleitung für Neulinge, Wörter kurz erklärt, 14 Abschnitte, 189 Teile mit Stellen und Videos |
| `teile.csv` | Die Einteilung: erster und letzter Schritt, Titel, ein Satz je Teil |
| `teile_bauen.py` | Baut `TEILE.md` aus `read_plans/3y_plan_de.csv` und `teile.csv` und prüft, dass jeder Schritt in genau einem Teil steht |

Ändern: `teile.csv` bearbeiten, dann `python plan/teile_bauen.py` (Python 3, keine Zusatzpakete).
`TEILE.md` nicht von Hand ändern.

## Bibeltext

Gelesen wird in der Lutherbibel 2017, jeder in seiner eigenen Bibel oder App. Die Teile enthalten nur
Stellenangaben und eigene Zusammenfassungen, keine Bibelzitate. Kapitel in Luther-Zählung: in der Lutherbibel
hat Joel 4 Kapitel und Maleachi 3, darum stehen die Schritte 837, 838 und 841 hier anders als in
`3y_plan_de.csv`.

## Geprüft

Jede Fassung prüfen zwei Leser mit Vetorecht: einer auf Bibeltreue (stimmt jede Aussage mit den genannten
Kapiteln, nichts hinzugedichtet, keine Zitate), einer mit dem Blick eines Suchenden ohne Vorwissen (verständlich,
ohne Kirchensprache, kein Druck). Diese Fassung haben beide freigegeben.
