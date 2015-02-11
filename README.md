Protokolle der
[Initiative für Freie Software und Freies Wissen Dresden](http://fsfw-dresden.de/)

Technisches
===========

Von den Pads zu bekommen mit

```
curl 'http://pad.zombofant.net/p/fsfw-dd-20150211/export/html' > protokoll-2015-02-11.html
pandoc -t markdown_strict protokoll-2015-02-11.html > protokoll-2015-02-11.md
… manuelles Nachbearbeiten …
gpg -b -a protokoll-2015-02-11.md
rm protokoll-2015-02-11.html
```
