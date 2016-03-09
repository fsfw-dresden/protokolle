Protokoll fsfw Dresden 2015-03-11
=================================

  
back:
[https://pad.fsfw-dresden.de/p/fsfw-dd-20150225](https://pad.fsfw-dresden.de/p/fsfw-dd-20150225)  
next:
[https://pad.fsfw-dresden.de/p/fsfw-dd-20150325](https://pad.fsfw-dresden.de/p/fsfw-dd-20150325)  
  

### Technisch

  

"Reflektiert. Engagiert" (Carsten; von vorletzter Woche)

-   muss wohl nur noch ein Link dazu
-   vertagt auf in zwei Wochen, da der Link leider noch fehlt D:

Corporate Design (Stefan)

-   Vorstellung der Ergebnisse vom Workshop
-   es gab noch einen zweiten Logoentwurf -\> **Kampfabstimmung \\o/**
-   Kampfabstimmung ist vertagt, da zu wenig Teilnehmer und damit zu
    wenig basisdemokratische Legitimierung
-   Meinungen zur Eule: sieht von der Haltung her ziemlich nach nem
    Reichsadler aus, "cannot unsee"
-   Meinungen zum Flyer: prinzipiell positiv, Layout bräuchte auch mal
    ne Kampfabstimmung

Bericht Infrastruktur-Gruppe

im Nachgang des Workshops wurden ganz viele Kanboard-Aufgaben angelegt

Jonas arbeitet am portieren des Mailsetups auf rosetta ($bald (eher so
gegen ende märz, das ist $bald!))

Container fürs DokuWiki ist da

anscheinend ist die empfohlene Methode, DokuWiki zu installieren, das
release.tar.gz zu entpacken

kann man das stattdessen vielleicht aus einem git machen?

kann man Plugins anders als aus der UI installieren, updaten?

-   -\> ja, früher hat man die Dinger händisch runtergeladen und im
    entspr. Verz. entpackt (diese konnten nach Aktivierung in der Konfig
    genutzt werden; ich bin aber mitlerweile froh, das es sogar einen
    Klicki-Bunti-Updater gibt ;-)
-   Ich habe da schon etwas zu Plugins vorbereitet (leider funktionieren
    auf der Instanz auf dem Hochschulserver nicht alle:
    [http://www2.htw-dresden.de/\~s70341/cgi-bin/dokuwiki/doku.php](http://www2.htw-dresden.de/~s70341/cgi-bin/dokuwiki/doku.php)
    ; speziell Bereich Playground dürfte interessant sein)

User über LDAP? Muss man das gleich entscheiden (Ja, besser ist das )
oder ist ne spätere Umstellung möglich? - mehr arbeit

Gegenfrage: Gibt es einen Grund gegen LDAP, unter dem Gesichtspunkt,
dass wir mehrere Dienste haben (werden), welche die gleichen
Benutzerdaten verwenden sollen? Sonst machen wir das einfach.

-   ging nur darum, dass das Aufsetzen dann länger dauert (weil dann das
    LDAP auch gleich hochgezogen werden muss)

  

### Organisatorisch

  

Raum fürs nächste Mal buchen

-   ist erledigt; bitte diesen Punkt beim nächsten Mal wieder ins Pad
    aufnehmen, da SLUB Raumbuchungen nur 2 Wochen im Voraus
    funktionieren

heute nur sechs Teilnehmer :( (plus einige wenige Online)

-   Anscheinend ist es wohl doch besser, das Treffen mi-t 1-2 Tagen
    Vorlauf auf der Mailingliste anzukündigen.
-   Stefan macht sich eine Erinnerung in seinen Kalender, das Treffen
    immer am Montag vorher auf der Mailingliste zu posten. -\> Hmm, ein
    Onlinekalender wäre schon praktisch (aber CalDav/ iCal/ vCal und
    nicht Go...gle) ← Da gibts Software, solange man kein Webinterface
    will ;) OwnCloud hätte sogar beides ;-)
-   -\> der OwnCloud-Kalender (CalDav) und das Adressbuch (CardDav)
    funktionieren (sogar mit Android)

  

### Inhaltlich

  

Doku-Filmabend (Verantwortlicher unklar; Basti?; von vorletzter Woche)

-   dafür wär nen Wiki cool, um z.B. ne Filmliste anzulegen -\> gibts
    bereits:
    [https://fusionforge.zih.tu-dresden.de/plugins/mediawiki/wiki/fsfw/index.php/Filmabende](https://fusionforge.zih.tu-dresden.de/plugins/mediawiki/wiki/fsfw/index.php/Filmabende)

Erstie-Quiz (stand letzte Woche auf der Tagesordnung; Verantwortlicher
unklar; Norman?)

-   vertagt -\> Ja, ich mach da gerne mit (allerdings nicht allein;
    siehe auch
    [http://wiki.stura.htw-dresden.de/index.php/Erstie-Quiz)](http://wiki.stura.htw-dresden.de/index.php/Erstie-Quiz))

Bestehende Open-Source-Aktivitäten an der TU/anderer HS sammeln und
sichtbar machen

-   s.a. (Freie) Software beim StuRa der HTW:
    [http://wiki.stura.htw-dresden.de/index.php/Software](http://wiki.stura.htw-dresden.de/index.php/Software)
    (sowie prism-break.org)
-   [http://wiki.stura.htw-dresden.de/index.php/Freie\_Software\_an\_der\_Hochschule](http://wiki.stura.htw-dresden.de/index.php/Freie_Software_an_der_Hochschule)

Übersicht freier Programme erstellen (s.a. vorigen Punkt)

[http://wiki.stura.htw-dresden.de/index.php/Diskussion:Freie\_Software\_an\_der\_Hochschule](http://wiki.stura.htw-dresden.de/index.php/Diskussion:Freie_Software_an_der_Hochschule)

Textverwaltung/ DTP:

LibreOffice

DTP-Tool:Scribus (war für die Erstellung eigener Flyer im Gespräch) -\>
wie hat sichs bewährt? fand ich nen bisschen mühsam im Vergleich zu
Inkscape, ist aber wohl Gewöhnungssache

ich (Norman) kann gerne etwas zu LiteraturVerwaltung ( DocEar, Zotero)
machen

LaTeX / LyX (Norman / FSR-Info) -\> Anfrage an Daniel ausstehend

Markup-Syntax + Converter (etwa Wikisyntax) -\> Wikikurs ist bereits im
(alten) Wiki verlinkt und kann gerne überarbeitet werden

-   in Wikis gibts i.d.R. verschiedene Im-/ Exportfunktionen (etwa für
    PDF, ODT und LaTeX)
-   Markdown/ Pandoc geht auch, berücksichtigt aber meist keine Plugins
    (wie auch)

Anregungen fürs Positionspapier:
[https://fsfe.org/news/2015/news-20150210-01.de.html](https://fsfe.org/news/2015/news-20150210-01.de.html)

  
Da, beim letzen mal, im Zusammenhang mit dem geplanten Info-Abend, die
Frage aufkam, ob man nicht auch die anderen Dresdner Hochschulen mit ins
Boot holen könne, hier nun ein Link zu den
[http://www.stura.htw-dresden.de/weitere/kss/dresdner-sturae](http://www.stura.htw-dresden.de/weitere/kss/dresdner-sturae)
(bzw.: [http://stura-dresden.de/)](http://stura-dresden.de/)).  
  
  
  

