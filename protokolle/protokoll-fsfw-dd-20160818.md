Plenum FSFW-Dresden am 2016-08-18
=================================

  
Übersicht über bisherige Pads:
[**https://wiki.fsfw-dresden.de/doku.php?id=orga:protokolle**](https://wiki.fsfw-dresden.de/doku.php?id=orga:protokolle)  
  
**Beginn:**1830+0015  
**Ende:**  
**Anwesende:** Gerd, Daniel (bis 2000+0002), Carsten, Norman (ab 1957)  
  

### Feststellung der Tagesordnung

USB-Stick

-   Gestaltung Gutschein
-   Stand: Linux
-   Stand: Windows

Vorstellung der FSFW auf A5-Seite im Heft des FSR-Maschbau

Was ist die Meinung des Plenums zu den Konzepten Docker
\<[https://docs.docker.com/](https://docs.docker.com/)\> und Sandstorm
\<[https://sandstorm.io/](https://sandstorm.io/)\>

-   jeweils auf eigenen Servern..

Norman: Zusammenfassung des Edusharing-Hackathons (\#Hack4OER
\<[https://wiki.stura.htw-dresden.de/index.php/Hack4OER](https://wiki.stura.htw-dresden.de/index.php/Hack4OER)\>) 
(Norman 10 Min+)

Off-Topic (Carsten/Daniel)

-   Daniel könnte sich den ganzen Tag über git freuen
-   Das gleiche gilt für Emacs und org-mode
-   Daniel hat auch einen kleinen, bleibenden Schaden von seinem Besuch
    beim StuRa mitgenommen

  
"Ohne Gegenrede angenommen"  
  

### USB-Stick

Gerd stellt aktuellen Prototyp vor

Hintergrundbild GRUB

Testen GRUB/Kernel-Konfiguration

Debian-Live

-   3.16-Kernel in stable, nutzt aufs
-   Ab 4.xx overlayfs
-   "Tricky" mit stable zu bauen, bootet auch nicht (overlay-fs Fehler)
    - baut jetzt 2016-08-19
-   Konsens: erstmal bei stable und aufs bleiben
-   Carsten hat mit Ansgar auch schon einen Prototypen mal gebastelt
    (wrhs "nur" stable)
-   Info: Fork von debian-live im Dezember, Skripte wohl ähnlich
-   Erstmal nicht auf die neue Entwicklung setzen, aber mit "einem
    halben Auge weiterverfolgen"
-   Philosophie: die Gefahr, dass das Projekt aufgrund zu hoher
    Ansprüche versackt ist ziemlich groß; daher erstmal schnell eine
    lauffähige Version bekommen

Stand Repo "funzt", von Gerd vorgestellt

Daniel baut image mal selbst (als Laie) und testet das Resultat

-   Versuch auf Debian sid zu bauen, wenn das nicht klappt dann mit
    virtueller Maschine
-   Link:
    \<[https://fsfw-dresden.de/usb-stick](https://fsfw-dresden.de/usb-stick)\>,
    \<[https://github.com/fsfw-dresden/usb-live-linux](https://github.com/fsfw-dresden/usb-live-linux)\>

Dokumentation von freier Software in HTML im Homedir des USB-Nutzers

Einen separaten Namespace im Wiki anlegen und dann offline auf den Stick
packen

Ist das technisch möglich?  Vielleicht mit wget (wenn keine andere
Option "funzt"); vielleicht kann das Dokuwiki schon selbst?

Heißt: parallel kann \*jetzt\* schon Dokumentation im Wiki geschrieben
werden

Daniel beschwert sich, dass durch das Schreiben der Dokumentation im
Wiki im Browser eine Hürde besteht, die Leute™ davon abhält, selbige zu
schreiben

Idee: Dokumentation als Markdown im Stick-Repo behalten und via Hook in
das Wiki schieben

-   Frage an den Infrasturktur-Haufen: was ist eine sinnvolle und
    schnell zu realisierende technische Umsetzung für diese Idee?

**Antrag an das Plenum**: wir machen das so (sprich: Dokumentation als
Markdown im Stick-Repo)

Beschluss des Plenums: **ohne Gegenrede angenommen**

Arbeitsauftrage an den Infrakstruktur-Haufen: schnelle Umsetzung der
Synchronisation

-   Carsten schickt eine E-Mail an die ML und macht den dazugehörigen
    Issue auf

Der Name "Ersti(e)-Stick" ist nicht gut, da die Zielgruppe nicht nur die
Erstsemester sind

Vorschläge: UNI-Stick, Uni-Stick, FSFW-Uni-Stick, …

**Antrag an das Plenum**: wir nennen das ganze Projekt ab jetzt
vorläufig "FSFW-Uni-Stick"

Beschluss des Plenums:

-   Gegenrede von Carsten: das "FSFW-" ist umständlich
-   Gerd: wie es dann gegenüber den Studenten verkauft wird ist mit
    diesem Beschluss nicht fixiert, es geht nur um die Repo-Namen u.ä.
-   Daher: das "FSFW-" ist optional
-   **Beschluss angenommen**

**Antrag an das Plenum**: der Namesraum im Wiki ist "uni-stick"

-   **Ohne Gegenrede angenommen**
-   Arbeitsauftrag an Gerd: dummy-Seite anlegen (wird schon gemacht)

Anforderungen an die Dokumentation

es muss aus der Dokumentation ersichtlich sein, was auf dem Stick daruf
ist und was man mit dem Stick alles machen kann

muss nicht vollständig sein, aber die wichtigesten Sachen sollen schon
da sein

Brainstorming dazu?

Zuständigkeiten verteilen

Ansatz: so wenig wie möglich selber schreiben, existierende Sachen
zusammentragen

Der erste Anfang: Paketlisten nehmen, Aufteilung "vergröbern", und dann
von dort aus Zuständigkeiten erstellen und verteilen

-   Wichtig: am Ende soll man nicht von langen Listen erschlagen werden
-   Erste Zuständigkeit: dafür sorgen, dass der ganze Kram noch lesbar
    bleibt
-   Alles noch nicht fix jetzt, soll flexibel bleiben

Auch noch wichtig: der "Propaganda"-Teil muss auch noch rein

Arbeitsauftrag an Daniel: (Carsten muss nachdenken) alles, was mit LaTeX
zu tun hat, dokumentieren

-   Welche Vorlagen?
-   Mindestens eine coole Vorlage, z.B. eine Dummy-Masterarbeit mit
    Deckblatt, Inhaltsverzeichnis, …
-   Beamervorlagen für Folien im TUDCD (Daniel macht abfällige
    Kommentare zu diesem Design)
-   Idealerweise: im LaTeX-Dokumentations-HTML einen Link zur
    Dummy-Masterarbeit haben, der beim Anklicken TeXStudio mit dem
    Dokument öffnet

Arbeitsauftrag an Carsten (von sich selbst): Arbeitspaket Python und
Mathesoftware planen/sich-dafür-zuständig-fühlen

-   Erstatz für Matlab™®©
-   Eventuell Prof. Sander aus der Mathematik noch mit ins Boot holen?

zz\_ als Namensprefix für Paketlisten, wo noch optional ist ob die
reinkommen bzw. wo Diskussionsbedarf da ist

-   Kommentare in Paketlisten:
-   \# Das ist ein Kommentar
-   \#Das ist kein Kommentar, Leerzeichen fehlt

**Uni-Stick-Präsentation** (Veranstaltung, auf der die USB-Sticks
verteilt und erklärt werden)

-   Idee: SLUB-Vortragssaal anfragen -\> Carsten
-   Vorschlag für Termin: 20.10. (2. TU-Vorlesungswoche)
-   naja, wie wäre es mit einem "Probelauf" an der HTW zur dortigen ESE
    (Anfang Oktober)?

**Einbindung des FSR-Info der HTW**

Prinzipielle Meinung: Je mehr Personen in ein Projekt involviert sind,
desto höher der Koordinationsaufwand

Terminfindung, Mainungsäußerungen, Entscheidungsprozesse... dauert alles
länger und wird komplizierter

Dieser Koordinationsaufwand muss durch einen Mehrwehrt gerechtfertigt
sein

Ideen für konkrete Teilprojekte, die z.B. von HTW-Leuten umgesetzt
werden könnten

**1.**Den Stick für Inf-Studis nützlich machen:

Entwicklungsumgebungen für die (in der Lehre) wichtigsten bzw. coolsten
Programmiersprachen

z.B. C/C++ (inkl. make, cmake, ...), Assembler, Python, go, Java,
Java-Script-(Frameworks?), Android-Studio (gibt es das?)

-   Im Zweifeksfall eher weniger Quantität und dafür gut konfiguriert,
    getestet, dokumentiert

git mit guter config (Aliasen), vorbereitete bash-Integration

-   Detailnotiz: Doku muss darauf Hinweisen, dass \~/.gitconfig noch mit
    Namen und Mailadresse angepasst werden sollte
-   Es gibt schon etwas rudimentäres im Wiki:
    [https://wiki.fsfw-dresden.de/doku.php/doku/git](https://wiki.fsfw-dresden.de/doku.php/doku/git)

Dokus bzw. Links zu Dokus (Videos, Tutorials, Referenzen, möglichst
niedrigschwellig) zusammentragen und in die Stick-Doku einpflegen
(Markdown-Format, im repo)

**2.** freie Software für Windows zusammentragen und testen

  

### Vorstellung FSFW im Heft des FSR-Maschinenbau

Jemand muss ganz schnell die A5-Seite erstellen

Was soll da drauf?  Textlastig, Bildlastig, knackiges Zitat, …?

-   Daniel kann es nicht lassen, und schlágt vor: "Software is like Sex:
    it's better when it's free"
-   Daniel sucht mal nach weiteren (evtl. unverfänglicheren) Zitaten

Carsten erstellt Vorlage in Inkscape, Unterstützung willkommen

  

### Zusammenfassung (Hack4OER)

-   Norman war auf dem Edusharing-Hackathon (\#Hack4OER
    \<[https://wiki.stura.htw-dresden.de/index.php/Hack4OER](https://wiki.stura.htw-dresden.de/index.php/Hack4OER)\>)
-   Hat mehr oder weniger konstruktive Kritik an OPAL geübt
-   Ansonsten waren noch weitere Firmen da, die ganz coole Sachen machen
-   Es ging aber eher um spezielle Infrastrukturen und nicht um Inhalte

  

### Meinungen zu Docker und Sandstorm

-   vertagt

  
  
Links aus der Diskussion:  
    Auf alternativen Verweisen z.B. so:  
   
[http://alternativeto.net/software/gimp/?license=free&platform=linux](http://alternativeto.net/software/gimp/?license=free&platform=linux)  
  

