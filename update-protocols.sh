#!/bin/bash

read -r -d '' protocol_list <<'LIST'
fsfw-dd-20160303
fsfw-dd-20160218
fsfw-dd-20160204
fsfw-dd-20160121
fsfw-dd-20160107
fsfw-dd-20151217
fsfw-dd-20151203
fsfw-dd-20151119
fsfw-dd-20151105
fsfw-dd-20151022
fsfw-dd-20151008
fsfw-dd-20150924
fsfw-dd-20150910
fsfw-dd-20150827
fsfw-dd-20150813
fsfw-dd-20150729
fsfw-dd-20150715
fsfw-dd-20150701
fsfw-dd-20150617
fsfw-dd-20150603
fsfw-dd-20150520
plenum-20150506
fsfw-dd-20150422
fsfw-dd-20150408
fsfw-dd-20150401
fsfw-dd-20150325
fsfw-dd-20150306-plenum
fsfw-dd-20150306-corporatedesign
fsfw-dd-20150306-infrastruktur
fsfw-dd-20150306-textverarbeitung
fsfw-dd-20150306-Mitgliedergewinnung
fsfw-dd-20150306-CryptoChallange
fsfw-dd-20150311
fsfw-dd-20150225
fsfw-dd-20150211
fsfw-dd-20150128
fsfw-dd-20150114
gc2rfrunRB
LIST

# Fehlende Protokolle herunterladen

(
    cd markdown
    for p in $protocol_list
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

