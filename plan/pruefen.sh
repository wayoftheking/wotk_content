#!/usr/bin/env bash
# Prüft GERUEST.md: 156 Wochen, lückenlos nummeriert, kein Kapitel doppelt.
cd "$(dirname "$0")"
S=$(mktemp)
sed -n '/^## Jahr 1/,$p' GERUEST.md | grep -E '^\| [0-9]+ \|' \
 | awk -F'|' '{gsub(/^ +| +$/,"",$2);gsub(/^ +| +$/,"",$3);k=$3;sub(/^Mt /,"Matthäus ",k);sub(/^Ps /,"Psalm ",k);print $2"\t"k}' > "$S"
fehler=0
n=$(wc -l < "$S"); [ "$n" -eq 156 ] || { echo "FEHLER: $n Wochen statt 156"; fehler=1; }
awk -F'\t' '$1!=NR{print "FEHLER: Zeile "NR" trägt Woche "$1; exit 1}' "$S" || fehler=1
d=$(cut -f2 "$S" | sort | uniq -d); [ -z "$d" ] || { echo "FEHLER: doppelt: $d"; fehler=1; }
rm -f "$S"; [ $fehler -eq 0 ] && echo "OK: 156 Wochen, lückenlos, keine Doppel"; exit $fehler
