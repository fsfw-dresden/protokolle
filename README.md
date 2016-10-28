Protokolle der
[Initiative für Freie Software und Freies Wissen Dresden](http://fsfw-dresden.de/)

Technisches
===========

Um die aktuellen Protokolle zu bekommen:
```
make update-all
```
Die Protokolle werden dann im Verzeichnis `protokolle` abgelegt (als HTML und
Markdown).  Zusätzlich wird eine Signatur im gleichen Verzeichnis abgelegt.  Es
werden nur die Protokolle heruntergeladen, die in der Datei
`liste-der-protokolle` enthalten sind.

Zur Erstellung einer Übersicht aller Protokolle:
```
make protokolle.html
```
