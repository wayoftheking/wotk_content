"""Baut plan/HAEPPCHEN.md aus dem 3-Jahres-Plan und plan/haeppchen.csv.

Aufruf:  python plan/haeppchen_bauen.py   (Python 3, keine Zusatzpakete)
Liest die Reihenfolge aus read_plans/3y_plan_de.csv (im Repo) oder, falls die fehlt, aus
quellen/3-jahres-leseplan-de.csv (lokale Kopie).
Prüft dabei: jeder der 1.095 Schritte steht in genau einem Häppchen, keine Lücke, keine Überschneidung.
"""
import csv
import sys
from collections import OrderedDict
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
PLAN = next((p for p in (WURZEL / "read_plans" / "3y_plan_de.csv", WURZEL / "quellen" / "3-jahres-leseplan-de.csv")
             if p.exists()), WURZEL / "read_plans" / "3y_plan_de.csv")
HAEPPCHEN = WURZEL / "plan" / "haeppchen.csv"
ZIEL = WURZEL / "plan" / "HAEPPCHEN.md"

TEILE = [
    (1, 6, "Zum Einstieg"),
    (7, 56, "Am Anfang (1. Mose)"),
    (57, 194, "Befreiung und Wüste (2. bis 5. Mose)"),
    (195, 243, "Im versprochenen Land (Josua, Richter, Rut)"),
    (244, 285, "Hiob"),
    (286, 395, "Saul und David"),
    (396, 467, "Salomo und die Weisheit"),
    (468, 635, "Das geteilte Reich und seine Propheten"),
    (636, 766, "Untergang und Exil"),
    (767, 841, "Heimkehr und Wiederaufbau"),
    (842, 896, "Jesus und die ersten Christen"),
    (897, 994, "Paulus unterwegs"),
    (995, 1023, "Paulus in Haft, Briefe von Petrus und an die Hebräer"),
    (1024, 1095, "Lukas, Johannes und die Offenbarung"),
]

# Die deutsche Datei folgt der englischen Kapitelzählung. In der Lutherbibel hat Joel 4 Kapitel und
# Maleachi 3. Diese Schritte zeigen wir in Luther-Zählung.
LUTHER = {
    ("837", "Maleachi 3"): "Maleachi 3,1-18",
    ("838", "Maleachi 4"): "Maleachi 3,19-24",
    ("840", "Joel 2"): "Joel 2",
    ("841", "Joel 3"): "Joel 3 und 4",
}


def lies_plan():
    schritte = OrderedDict()
    with PLAN.open(encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            tag = r["Tag"]
            s = schritte.setdefault(int(tag), {"text": [], "videos": []})
            if r["Bibeltext / Video"] == "Video":
                for b, l in (("Beschreibung 1", "Link 1"), ("Beschreibung 2", "Link 2")):
                    if r[b]:
                        s["videos"].append((r[b], r[l]))
            else:
                t = r["Bibeltext / Video"]
                s["text"].append(LUTHER.get((tag, t), t))
    return schritte


def lies_haeppchen():
    with HAEPPCHEN.open(encoding="utf-8") as f:
        return [dict(r, von=int(r["von"]), bis=int(r["bis"])) for r in csv.DictReader(f, delimiter=";")]


def pruefe(schritte, haeppchen):
    fehler = []
    erwartet = 1
    for i, h in enumerate(haeppchen, 1):
        if h["von"] != erwartet:
            fehler.append(f"Häppchen {i} beginnt bei {h['von']}, erwartet {erwartet}")
        if h["bis"] < h["von"]:
            fehler.append(f"Häppchen {i}: bis vor von")
        if not h["titel"].strip() or not h["worum"].strip():
            fehler.append(f"Häppchen {i}: Titel oder Satz fehlt")
        erwartet = h["bis"] + 1
    if erwartet - 1 != max(schritte):
        fehler.append(f"letztes Häppchen endet bei {erwartet - 1}, Plan hat {max(schritte)} Schritte")
    for a, b in zip(TEILE, TEILE[1:]):
        if b[0] != a[1] + 1:
            fehler.append(f"Teile nicht lückenlos bei {a[2]}")
    for h in haeppchen:
        teile = {t[2] for t in TEILE if t[0] <= h["von"] <= t[1]} | {t[2] for t in TEILE if t[0] <= h["bis"] <= t[1]}
        if len(teile) != 1:
            fehler.append(f"Häppchen {h['titel']} liegt über einer Teilgrenze")
    for f in ("—", "–", "·"):
        for h in haeppchen:
            if f in h["titel"] + h["worum"]:
                fehler.append(f"Zeichen {f!r} in {h['titel']}")
    return fehler


def baue(schritte, haeppchen):
    groessen = [h["bis"] - h["von"] + 1 for h in haeppchen]
    z = [
        "# Der 3-Jahres-Plan in Häppchen",
        "",
        "<!-- Erzeugt mit `python plan/haeppchen_bauen.py` aus `read_plans/3y_plan_de.csv` "
        "(Reihenfolge) und `plan/haeppchen.csv` (Einteilung, Titel, ein Satz je Häppchen). Nicht von Hand "
        "ändern, sondern die beiden Quellen. Joel und Maleachi sind auf Luther-Zählung umgestellt. -->",
        "",
        f"Die Bibel ist eine Sammlung vieler Bücher. Dieser Plan führt in {max(schritte) // 1000}."
        f"{max(schritte) % 1000:03d} Schritten durch die 66 Bücher, die alle Kirchen gemeinsam haben. Ein Schritt ist ein Kapitel, manchmal zwei kurze oder ein paar Psalmen. Die Schritte "
        f"sind zu {len(haeppchen)} Häppchen von {min(groessen)} bis {max(groessen)} Schritten zusammengefasst. "
        "Jedes Häppchen hat einen Titel und einen Satz, worum es geht.",
        "",
        "**So liest du eine Angabe:** 1. Mose 3 heißt: Buch 1. Mose, Kapitel 3. Nehemia 9,5-37 heißt: "
        "Buch Nehemia, Kapitel 9, Verse 5 bis 37.",
        "",
        "**Wo du liest:** in der Lutherbibel 2017, als Buch, in einer Bibel-App oder online bei der Deutschen "
        "Bibelgesellschaft (die-bibel.de).",
        "",
        "**Was du in einem Schritt tust:** das Kapitel lesen und kurz darüber nachdenken. Wer mag, betet oder "
        "spricht mit anderen darüber.",
        "",
        "**Wo du anfängst:** bei Häppchen 1, einem Überblick über die ganze Geschichte. Wer lieber gleich mit "
        "der Erzählung beginnt, startet bei Häppchen 2. Wer zuerst Jesus kennenlernen will, liest zuerst die "
        "Häppchen 145 bis 147 (den Bericht des Markus über Jesus) und kommt danach zum Anfang zurück.",
        "",
        "**Die Reihenfolge** folgt ungefähr der Zeit, in der die Ereignisse geschahen, nicht dem "
        "Inhaltsverzeichnis der Bibel. Darum stehen Psalmen und Propheten mitten in den Geschichtsbüchern.",
        "",
        "**Videos:** Manche Häppchen nennen kurze Erklärfilme von BibleProject zu einem Buch. Sie sind freiwillig.",
        "",
        "**Dein Tempo:** Wer jeden Tag einen Schritt geht, ist nach rund 3 Jahren durch. Andere brauchen "
        "1 Jahr oder 5. Pausen sind normal, du machst dort weiter, wo du warst.",
        "",
        "## Wörter kurz erklärt",
        "",
        "- **Bund:** eine feierliche Zusage, die Gott und Menschen verbindet.",
        "- **Prophet:** jemand, der im Auftrag Gottes spricht.",
        "- **Gesetz:** Gottes Weisungen, vor allem in den fünf Büchern Mose.",
        "- **heilig:** ganz zu Gott gehörig. Gott selbst ist heilig: ganz rein und anders als alles, was er geschaffen hat.",
        "- **Herrlichkeit Gottes:** seine Größe und seine sichtbare Gegenwart.",
        "- **Sünde:** was den Menschen von Gott trennt, Schuld gegen Gott und gegen andere.",
        "- **Gnade:** Gottes Geschenk, das man sich nicht verdienen kann.",
        "- **Gericht:** Gott urteilt über das Unrecht.",
        "- **verheißen:** fest versprechen.",
        "- **Opfer:** eine Gabe an Gott, in den älteren Büchern der Bibel oft ein Tier.",
        "- **Altes und Neues Testament:** die beiden Teile der Bibel. Das Alte erzählt die Zeit vor Jesus, das Neue von Jesus und den ersten Christen.",
        "- **Evangelium:** \"gute Nachricht\", auch der Name der vier Berichte über Leben, Tod und Auferstehung Jesu.",
        "- **Priester:** dient im Heiligtum und tritt zwischen Gott und das Volk.",
        "- **Psalm:** ein Lied oder Gebet aus dem Buch der Psalmen.",
        "- **Christus:** griechisch für \"der Gesalbte\", der von Gott versprochene Retter. Gemeint ist Jesus.",
        "- **Jünger, Apostel:** die Schüler Jesu und die, die er als Boten ausgesandt hat.",
        "- **Gleichnis:** eine Bildgeschichte, mit der Jesus etwas über Gott erklärt.",
        "- **Heiliger Geist:** Gott selbst. Er wirkt in der Welt, wohnt in allen, die an Jesus glauben, und führt sie in die Wahrheit.",
        "- **Gemeinde:** die Gemeinschaft der Christen an einem Ort.",
        "",
        "## Übersicht",
        "",
        "| Teil | Schritte | Häppchen |",
        "|---|---|---|",
    ]
    nr_von = {}
    n = 0
    for h in haeppchen:
        n += 1
        h["nr"] = n
    for von, bis, name in TEILE:
        hs = [h for h in haeppchen if von <= h["von"] <= bis]
        nr_von[name] = hs
        nrs = str(hs[0]["nr"]) if len(hs) == 1 else f"{hs[0]['nr']} bis {hs[-1]['nr']}"
        z.append(f"| {name} | {von} bis {bis} | {nrs} |")
    for von, bis, name in TEILE:
        z += ["", f"## {name}", ""]
        for h in nr_von[name]:
            anz = h["bis"] - h["von"] + 1
            bereich = f"Schritt {h['von']}" if anz == 1 else f"Schritte {h['von']} bis {h['bis']}"
            z += [f"### {h['nr']}. {h['titel']}", "", f"{bereich}. {h['worum']}", ""]
            for s in range(h["von"], h["bis"] + 1):
                eintrag = schritte[s]
                z.append(f"- {s}: {'; '.join(eintrag['text'])}")
            videos = [v for s in range(h["von"], h["bis"] + 1) for v in schritte[s]["videos"]]
            if videos:
                z.append("")
                z.append("Video: " + ", ".join(f"[{b}]({l})" if l else b for b, l in videos))
            z.append("")
    return "\n".join(z).rstrip() + "\n"


def main():
    schritte = lies_plan()
    haeppchen = lies_haeppchen()
    fehler = pruefe(schritte, haeppchen)
    if fehler:
        print("FEHLER:")
        for f in fehler:
            print(" ", f)
        sys.exit(1)
    ZIEL.write_text(baue(schritte, haeppchen), encoding="utf-8")
    g = [h["bis"] - h["von"] + 1 for h in haeppchen]
    print(f"ok: {len(haeppchen)} Häppchen, Schritte je Häppchen {min(g)} bis {max(g)}, geschrieben nach {ZIEL}")


if __name__ == "__main__":
    main()
