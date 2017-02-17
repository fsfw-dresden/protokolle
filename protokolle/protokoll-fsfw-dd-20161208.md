Übersicht über bisherige Pads:
[**https://wiki.fsfw-dresden.de/doku.php?id=orga:protokolle**](https://wiki.fsfw-dresden.de/doku.php?id=orga:protokolle)  
   
Sitzungsablauf:  

-   Festlegung der Sitzungsleitung
-   TOPs Sammeln und Strukturieren (inkl. Zeitplan)

   
   

Protokoll fsfw Dresden 2016-12-08
=================================

Formalia (Optional)
===================

Sitzungsleitung:
================

**Anwesende:  Carsten, Emanuel, Norman, Gerd; Johannes, Sebi, Jonas**  

Protokoll:
==========

Start-Ende: 18:30-21:00
=======================

Beschlossene Tagesordnung
=========================

...
---

Das tatsächliche Protokoll
--------------------------

Feedback, Anregungen, geknüpfte Kontakte auf den Veranstaltungen der
vorigen Woche (Norman+..., 15 Min+)

**Wissen kommt von Machen - SLUB Makerspace Meet up! "audiovisuell" am
1. Dezember:**
<http://blog.slub-dresden.de/beitrag/2016/11/25/wissen-kommt-von-machen-slub-makerspace-meet-up-audiovisuell-am-1-dezember/>

siehe auch Makerspace-Meetup-Pad:
<https://pad.fsfw-dresden.de/p/slub-makerspace> (für Infoaustausch)

es gibt jetzt ein Medien-Carrel in der SLUB (dort können verschieenste
Medienabspielgeräte genutzt werden etwa um alte Videoaufnahmen anzusehen
oder selbst auf modernere Medien zu überspielen um sie auch zukünftig
weiter/ wieder nutzen zu können)

Für welche Anwendungsfälle wäre Software (auf unserem Stick) hilfreich:

Audioschnitt und -bearbeitung/ DAW

Audacity

-   eher mathematischorientiert anmutende GUI, eine pragmatische wäre
    für Einsteiger aus nichttechnischen Studienrichtungen hilfreich;
    Gegenbsp.: "Garage-Band"/ "Logic"
-   <s>angeblich nur als 32 Bit (noch keine umstellung auf 64Bit-Rechner
    erfolgt)</s>
-   ist mehrspurfähig
-   hat gute und vor allem ASIO-fähige Treiberunterstützung
-   ist leider destruktiv arbeitend (Änderungen werden sofort angewendet
    und nicht als nachträglich änderbare Befehlsabfolge gespeichert, wie
    es mitlerweile üblich ist)
-   viele kompatible Plugins verfügbar (z.B. von SIR-Audio-Tools; oder
    einfach im netz nach "free plugins vst" suchen)
-   kann jedoch leider weder vst- (VST geht mit wine!) noch
    midi-Instrument-Plugins verwenden, die zumindest in der
    Musikindustrie häufig verwendet werden

Ardour \>=3  (im August 2016 kam Ardour 5 heraus) <http://ardour.org>

-   wäre ein DAW für Linux (mit gefälligerer GUI)
-   mehrspurfähig
-   nicht destruktiv arbeitend
-   Unterstützung für VST-Plugins und Midi
-   Gnome basiert

abcde ("A better CD encoder")

Videoschnitt und -bearbeitung:

-   Avidemux <https://de.wikipedia.org/wiki/Avidemux>
-   VirtualDub (letzte Version ist von 2013) 
-   Cinelerra ?
-   Shotcut <https://www.shotcut.org/>
-   OpenShot <http://openshot.org>
-   Kdenlive <https://kdenlive.org>
-   mkvtoolnix (Tools fürs Matroska-Mediencontainerformat)
-   blender ("wenn man auf Schmerzen steht")
-   ffmpeg
-   die MLT Video Rendering Engine scheint auch recht gut zu sein

Metadatenverwaltung

-   Zusatzinfos zu Mediendateien (Inhalt, Stichwörter etc.)
-   Referenzierbarkeit auf bestimmte Stellen/ Annotation bestimmter
    Stellen, auf die von extern verwiesen werden kann (etwa per Playlist
    oder dem AV-Portal der TIB Hannover)
-   hier sollte doch das Matroska-Mediencontainerformat auch helfen
    können?

bewährte Dateiformate/ Standards (auch wichtig für Langzeitarchivierung)

OAIS (Standard)

Container Matroshka (das ist cool, das will man haben, das kann alles)

FF v1.3

Wav/Flac/Wavpak

-   Wavpak braucht viel CPU-Zeit zum komprimieren (lohnt sich nur in
    Spezialfällen)

**Debian Bug-squashing-Event am 2.12. an der TU:**
<https://wiki.debian.org/BSP/2016/12/de/Dresden> (nun auch mit
Gruppenfoto ;-)

Sebastin Humenda auf Accessibility (Screenreader, Braillezeile,
Speechtotext, texttospeech) angesprochen

-   KDE sei da aktuell nicht so gut; Gnome wäre zumindest hierbei (dank
    gnome-orca) besser; villeicht mal den MATE-Desktop probieren
-   er hat interesse uns bei der Verbesserung der Accessibitilty zu
    Unterstützen allerdings fehlt ihm aktuell die Zeit dafür

Johannes Kleine \<johannes@cj-k.de\> vom Maschbau-FSR der TU ist
interessiert am Uni-Stick und würde sogar versuchen uns Rechenzeit auf
einem FSR-Server - etwa zum automatisierten Bauen der Images für den
Stick - einzuräumen (wir bekämen eine VM)

-   Automautisierte Tests zu aufwendig
-   von ihm stammt auch der Hinweis auf eine Vorlesung
    "Studienkompetenz", wo man Werbung für freie Software fürs Studium
    machen könnte

**WikiLibrary-Barcamp am 3.12. in der SLUB**
<https://de.wikipedia.org/wiki/Wikipedia:WikiLibrary_Barcamp_2016> (im
SLUB-Blog:
<http://blog.slub-dresden.de/beitrag/2016/12/04/bibliotheken-im-netz-rueckschau-auf-das-wikilibrary-barcamp/)>

siehe auch meine gestrige Email an discuss@ (Bibliotheken, Makerspaces,
Wikipedia&Co. und Coworking finden zueinander; vom Gatekeeper zum
Knowledge-Coach)

-   demnach sollen also Nutzergruppen gezielt angesprochen und
    eingebunden werden; ggf. Kooperation mit CMS zwecks
    Medienkompetenzkursen?
-   in dem Zusammenhang wurde auch das Ergebnis der Umfrage zum
    wissenschaftlichen Schreiben/ Arbeiten 
    <http://innoscholcomm.silk.co/> erwähnt und angemerkt das sich
    Bibliotheken i.d.R bisher nur in einigen wenigen Bereichen aktiv
    waren und dies doch bestimmt ausgebaut werden könne

Norman hat den Uni-Stick und die FSFW im Allgemeinen in einer Session
vorgestellt (Dank an Daniel, dessen gute Kurz-Präsentation ich hierfür
nutzte)

Im Pad gibt es auch einen Bereich für Softwarewünsche bzw.
Anwendungsfälle, für die freie Software gesucht wird:
<https://etherpad.wikimedia.org/p/BINDANormann>

es gab Interesse von einigen Leuten

-   Fr. Kaiser von der SLUB, stellte in meiner Session viele Rückfragen
-   Herr Lambert Heller von der Technischen Informationsbibliothek (TIB)
    Hannover interessierte sich für Freie Software als Basis für eine
    jedermann zugängliche dezentrale Basisinfrastruktur (was sich auch
    gut mit einem anderen Projekt von mir rund ums "Mundaneum" des Paul
    Otlet und H.G. Wells "World Brain" ergänzen ließe)
-   Fr. Elena Stöhr Referentin für Kommunikation und digitale Medien
    beim Deutschen Bibliotheksverband (dbv) tippte als Toastmasterin
    fleißig im Pad mit
-   Herr Tim Moritz Hector, Präsidiumsvorsitzender von Wikimedia
    Deutschland, erhielt ein Positionspapier von mir

Sonstiges

Sonstiges:

-   Sebi schlägt vor, ein günstiges Braile-Display zu entwickeln

Carsten berichtet von der Konferenz n

Jonas weist auf folgendes hin

-   <https://digitalcharta.eu/>
-   kann man kommentieren und sich einbringen

  
<http://codefor.de/dresden/>  
  
  
  

