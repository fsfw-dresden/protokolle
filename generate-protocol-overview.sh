#!/bin/bash

# Alle Markdowndateien der Protokolle laden, durch einen Separator getrennt
# in eine große Markdowndatei zusammenfügen und Inhaltsverzeichnis erzeugen

protocols=$(cd markdown; ls -1 protokoll-fsfw-dd-*.md | sort -r)
content=$(tempfile)
toc=$(tempfile)
separator='<hr />'                # ugly

echo -e "## Inhaltsverzeichnis: \n" > $toc
echo "" > $content

for p in $protocols; do
    name=${p##protokoll-fsfw-dd-}
    link=$(printf '  1. [%s](#%s)' $name $name)
    anchor=$(printf '<a name="%s"></a>%s\n' $name $p)

    echo $link >> $toc
    echo $separator >> $content
    echo $anchor >> $content
    echo $separator >> $content
    cat markdown/$p >> $content
done

cat $toc $content > protokolle.md
rm -f $content $toc
