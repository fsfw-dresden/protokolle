Protokolle der
[Initiative für Freie Software und Freies Wissen Dresden](http://fsfw-dresden.de/)

Einzelprotokolle
================

Um die aktuellen Protokolle zu bekommen:
```
make update-all
```
Die Protokolle werden dann im Verzeichnis `protokolle` abgelegt (als HTML und
Markdown).  Zusätzlich wird eine Signatur im gleichen Verzeichnis abgelegt.  Es
werden nur die Protokolle heruntergeladen, die in der Datei
`liste-der-protokolle` enthalten sind. Um die Datums-Strings in dieser Datei
nicht manuell eintragen zu müssen gibt es das Python-Skript `dates.py`
(Warnhinweis bezüglich der Zeilenenden beachten).

Erstellung einer Übersicht aller Protokolle
===========================================

Mit dem Aufruf
```
make protokolle.html
```
wird eine Datei `protokolle.html` erzeugt, die sich aus einem einfachen
Inhaltsverzeichnis und allen Protokollen aus dem Verzeichnis `protokolle`, die
mit `fsfw-dd-` beginnen, zusammensetzt.

Überprüfung der Signatur
========================

Das geht mit `make test`.

Wer es schafft, die Ausgabe etwas zu reduzieren, möge dies bitte tun: weder
`--quiet` noch `--no-tty` noch `--batch` haben `gpg` dazu gebracht, die Ausgabe
während der Verifikation zu unterdrücken.  Ein radikales `2>/dev/null` hingegen
würde eventuell wichtige Fehlermeldungen mit unterdrücken, und ist deswegen
keine gute Lösung.
