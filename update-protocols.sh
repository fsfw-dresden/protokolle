#!/bin/bash

# Fehlende Protokolle herunterladen

(
    cd markdown
    for p in $(cat ../liste-der-protokolle)
    do
        if ! [ -f "protokoll-$p.md" ]; then
            echo "Downloading $p"
            curl 'https://pad.fsfw-dresden.de/p/$p/export/html' > protokoll-$p.html
            pandoc -t markdown_strict protokoll-$p.html > protokoll-$p.md
            gpg --detach-sign --armor protokoll-$p.md
            rm protokoll-$p.html
        fi
    done
)

# Alle Markdowndateien der Protokolle laden, durch einen Separator getrennt
# in eine große Markdowndatei zusammenfügen und Inhaltsverzeichnis erzeugen

protocols=$(cd markdown; ls -1 protokoll-fsfw-dd-*.md | sort -r)
content=content.md
toc=toc.md
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

# Generiere finales HTML

cat $toc $content | pandoc -s -f markdown_strict -t html > protokolle.html

