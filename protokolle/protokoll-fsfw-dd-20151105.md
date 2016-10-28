Sitzungsablauf:  

-   Festlegung der Sitzungsleitung
-   TOPs Sammeln und Strukturieren (inkl. Zeitplanung)

  
  
  

Protokoll fsfw Dresden 2015-11-05
=================================

Übersicht über bisherige Pads:
[**https://wiki.fsfw-dresden.de/doku.php?id=orga:protokolle**](https://wiki.fsfw-dresden.de/doku.php?id=orga:protokolle)  

**TOP-Vorschläge**  

fährt jemand zur diesjährigen KIF (
[https://kif.fsinf.de/wiki/Hauptseite](https://kif.fsinf.de/wiki/Hauptseite),
11.11.-15.11.2015 in Bonn ) Norman, 10 Minuten

-   Dies ist die *Konferenz der Informatikfachschaften* (ich (Norman)
    war voriges Jahr, in diesem fehlt mir leider die Zeit)
-   geplante Arbeitskreise:
    [https://kif.fsinf.de/wiki/KIF435:Arbeitskreise](https://kif.fsinf.de/wiki/KIF435:Arbeitskreise)
-   bisherige Resolutionen:
    [https://kif.fsinf.de/wiki/Portal:Resolutionen](https://kif.fsinf.de/wiki/Portal:Resolutionen)

TOPs von Daniel (per E-Mail, da er heute nicht kommen kann):

Die Integration des Twitter-Accounts in den Diaspora\*-Accounts hat noch
nicht statt gefunden, da ich Daniel keine Zugangsdaten für ersteren
bekommen habe. Für die Verbindung Facebook-Diaspora\* weiß Christoph
mehr zu berichten.

Gibt es aktuell Pläne, den Tracker so zu erweitern, dass Erinnerungen
versendet werden, wenn die Deadline für einen zugewiesenen Issue sich
nährt? (vertagt, sowas weiß Jonas)

-   Siehe meine (Jonas‘) E-Mail-Antwort (da hängt auch Sourcecode dran …
    ;-) )

Infrastruktur-Report (zum Verlesen durch die Sitzungsleitung, 5min):

Wir benutzen nun überall (außer auf
[http://fsfw-dresden.de](http://fsfw-dresden.de) ) Let’s Encrypt
(<[https://letsencrypt.org](https://letsencrypt.org)\>) Zertifikate (wir
sind in der Closed Beta)

Diese werden automatisch erneuert und von Browsern vertraut

Deshalb werden jetzt alle Requests auch automatisch auf HTTPS umgeleitet

Webseite ist noch nicht fertig von Johannes’ Server auf Rosetta (unseren
Server) umgezogen, daher hat die noch kein Let’s Encrypt-Zertifikat. Das
wird aber am Wochenende, sind nur noch Kleinigkeiten zu fixen.

Fragen und Probleme bitte direkt an
<[mailto:infra@lists.fsfw-dresden.de](mailto:infra@lists.fsfw-dresden.de)\>
oder im discuss- bzw. Infrastruktur-Chat anbringen.

Further Reading:

-   Webseite: [https://letsencrypt.org/](https://letsencrypt.org/)
-   Sourcecode der Tools von Let’s Encrypt für Interessierte:
    Clientseite
    <[https://github.com/letsencrypt/letsencrypt/](https://github.com/letsencrypt/letsencrypt/)\>
    (also zum Holen von Zertifikaten für einen Server), Serverseite(!,
    also das Tool das auf deren Server läuft)
    <[https://github.com/letsencrypt/boulder](https://github.com/letsencrypt/boulder)\>
-   Dokumentation:
    [https://letsencrypt.readthedocs.org/en/latest/using.html](https://letsencrypt.readthedocs.org/en/latest/using.html)

[https://tosdr.org/](https://tosdr.org/) - mehr Erkennbarkeit für
Vertrauen

Diskussion zu (a)SocialMedia passt zu... 32C3: Gated Communities
(27.-30.12. Hamburg) s.a. [http://events.ccc.de/](http://events.ccc.de/)

  

### Das tatsächliche Protokoll

  

Sebastian informiert über den fortgeschrittenen Stand der HP-Migration.

-   Abschluss bis Ende der Woche
-   Dann sollte auch das https-Zertifikat funktionieren
-   Eventuell implementiert Sebi am WE auch schon die Testing-Branches

KIF

-   wie bringen wir unser Programm dort unter? (Kann es jemand von den
    Info-FSRs mitnehmen?) -\> Sebi fragt Jonas (TU) und vv0l1 fragt Jana
    (HTW)

Integration Twitter-Account in Diaspora

Twitter geht

facebook ist kritischer

Plan A: Fake-Account

-   Problem: Nachrichten kommen eventuell auf der Account-Seite statt
    der Gruppenseite an

Plan B: (braucht Handynummer)

genauer Ablauf unklar (wie generieren wir das)

[https://wiki.diasporafoundation.org/Integrating\_other\_social\_networks](https://wiki.diasporafoundation.org/Integrating_other_social_networks)

oder RSS-Feed (geht das?)

Plenumsbeschluss: Symbole auf der Startseite sollen in SVGs geändert und
Diaspora ergänzt werden

Logo für Diaspora auf HP, done:
[https://github.com/fsfw-dresden/medien/blob/master/corporate-design/diaspora-logo.svg](https://github.com/fsfw-dresden/medien/blob/master/corporate-design/diaspora-logo.svg)

done: WebFonts sind problematisch + FontAwesome entschnleunigt
Weiterentwicklung zugunsten eines kommerziellen Projektes:
[https://fonticons.com/start](https://fonticons.com/start) -\> convert
webfonts2svg ; rm font-awesome; add new-icons (e.g. diaspora) -\> neuer
"feature-" branch f. hp

  
  
Argumente für Linux: statt Windows - falls man mal wieder gefragt wird
(christoph wurde gefragt und war zu schnell ratlos)  

-   Sicherheit
-   Transparenz
-   keine Malware
-   Mehr Kontrolle über das System
-   Festplatte verschlüsseln besser und leichter
-   besser an eigene Bedürfnisse anpassbar
-   Windows achtet keine Nutzerrechte
-   Verstehen wie das System funktioniert
-   Wenn du auch Linux nutzte
-   Einfache Neuinstallation, Backup/Restore
-   keine Antifeatures (wie: du darfst nur x mal dies oder jenes)
-   sinnvolle Editoren
-   sinnvolle Terminalemulatoren

  

