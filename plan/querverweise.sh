#!/usr/bin/env bash
# Listet jeden Verweis "(Woche N)" in den Wochendateien neben dem Kapitel, das GERUEST.md für Woche N nennt.
# Zum Durchsehen nach jedem neuen Bogen: links steht der Verweis, rechts nach "=>" das Kapitel laut Gerüst.
cd "$(dirname "$0")"
S=$(mktemp)
grep -E '^\| [0-9]+ \|' GERUEST.md | awk -F'|' 'NR>3{gsub(/ /,"",$2); k=$3; gsub(/^ +| +$/,"",k); print $2"\t"k}' > "$S"
for f in wochen/woche-*.md; do
 grep -oE "[A-Za-zäöüÄÖÜ0-9., ]{0,28}\(Woche [0-9]+[^)]*\)" "$f" | while read -r m; do
  for n in $(echo "$m" | grep -oE "Woche [0-9]+( und [0-9]+)?" | grep -oE "[0-9]+"); do
   echo "$(basename "$f" .md | sed 's/woche-//') | $m => $(awk -F'\t' -v n="$n" '$1==n{print $2}' "$S")"
  done
 done
done | sort -u
rm -f "$S"
