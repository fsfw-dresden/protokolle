Übersicht über bisherige Pads:
<https://wiki.fsfw-dresden.de/doku.php?id=orga:protokolle>  
  
<https://dudle.inf.tu-dresden.de/fsfw-plenum/>  
   
Sitzungsablauf:  
  
    Festlegung der Sitzungsleitung  
  
    TOPs Sammeln und Strukturieren (inkl. Zeitplan)  
  
   
Protokoll fsfw Dresden 2017-02-02  
   
Formalia (Optional)  
Sitzungsleitung:   
Anwesende:   
Protokoll: hauptsächlich Carsten  
Start-Ende: 18:51-21:00  
  
  
   
TOP-Vorschläge  
  

TU-Mailserver (exchange-only-Pläne) (Carsten 15min)

Terminfindung für Uni-Stick-Workshop (Carsten 10min)

-   Ziel sollte sein bis zum Linux-Tag das Projekt auf einen
    vorzeigbaren Stand zu bringen

Der Emailentwurf für Anja Winkler würde sich über Fertigstellung freuen!
<https://pad.fsfw-dresden.de/p/Emailentwurf_an_Behindertenbeautragte>

-   siehe ihre Antwortmail vom 22.1.

Kreta an der EHS (siehe Frage von Florian Antelmann bei einem der
vorigen Plenen) - wie ist hier der Stand

-   Hat jemand Interesse sich mit CMS auszutauschen?

Wie weitermachen bei der Organisation unserer Beteiligung zur
Ringveranstaltung „Zertifikatskurs Medienpädagogik"? (Anfrage von
Daniel, der leider nicht da sein kann …)

  
    Unterpunkt  
  
       
  
    Sonstiges  
  
  
Beschlossene Tagesordnung  
...  
   
   

Das tatsächliche Protokoll
==========================

  
  

### Exchange-Problem:

    Das (ziemlich realistische) Gerücht der Abschaltung des
Unix-Mailserves ist wieder aufgetaucht  
    Infos vom ZIH zu Exchange:
<https://tu-dresden.de/zih/dienste/service-katalog/arbeitsumgebung/e_mail?set_language=de#section-2>  
    Argumente:  

Es gab mal das Gerücht, dass IMAP nicht unterstützt würde, bzw. dass man
mit anderen Clienten als Outlook keine Chance hätte TU-Mail-Dienste zu
nutzen.

-   Da es aber eine Thunderbird-Anleitung mit IMAP vom ZIH gibt scheint
    das nicht zu stimmen

Barrierefreiheit der Web-Anwedung?

-   -\> Rückfragen bei Frank.

Offizielle Exhange-App sendet Zugangsdaten an Drittanbieter und ist
daher mit ZIH-Benutzerrichtlinien

-   <https://www.heise.de/mac-and-i/meldung/Microsofts-Outlook-App-schleust-E-Mails-ueber-Fremd-Server-2533240.html>

Abhängigkeit von einer Firma (Microsoft) 

(Lizenz-)Kosten

iCal, CalDav Nutzung ?

-   wird vermutlich nicht unterstützt, sonst bräucht man keine extra
    Software

Verschlüsselung bei Nutzung eines Webclients möglich ?

-   Zu überprüfen ist:, ob Horde mailenvelope unterstütz
-     

Datensicherheit (Hat MS Zugriff auf die Maildaten?, Siehe UJ-Artikel:
"Windows 10 für Dienstgebrauch nicht zulässig")

ZIH blockert Outlook App (auf Anweisung der Stabsstelle für
Informationssicherheit)

-   <https://tu-dresden.de/zih/die-einrichtung/zih-info/zih_info_91#1>

  
Weiteres   

Argumente an Argumentations-Kontaktgruppe senden

Ist das geplante Abschalten von Unixmail schon offiziell? Worauf kann
man sich ggf. beziehen, wenn man mehr Öffentlichkeit herstellen will?
Man könnte z.B. eine Umfrage unter den Mitarbeiter\*innen durchführen.

-   Die Mittelstandsinitiative hat gff. die Mailadressen

  

### Stick-Treffen

Mo. 6.02. 18:00, SLUB -2.115

Vorzeigbaren Stand für die CLT 

Zielgruppe: potentielle Helfer -\> Repo sollte sie nicht vergraulen

darum Repo muss gut sein

build-process

braucht dooferweise root

-   ggf. hilft fakeroot

zu viel shell

krude Vermischung von shell und python

kein sinnvolles branching model

-   -\> nur ein Feature pro branch!

gemischtsprachige commit-messages

Tippfehler / Grammatik in Commitmessages und Readme-Dateien

Repo neu aufsetzen,

empfehlenswertes Vorgehen: 

-   kein direkter commit auf master!
-   Nur PR wenn ein positiver review darf gemergt werden
-   muss hinreichend granular sein

vielleicht Umstellung des Uni-Stick-Repos auf Projekt-Repo (gibts seit
einiger Zeit neu bei Github)?

Umstieg auf Debian Stretch für WS 17/18

  
Ergänzungen für die Agenda des Stick-Treffens:  

Anleitung bzw. Checkliste, was konkret zu testen ist

Verzeichnis-Struktur des Repos ggf. überarbeiten oder zumindest
Dokumentieren

Wichtige Dateien dokumentieren:

-   Skripte
-   Paketquellen
-   hooks

Richtlinien wo englisch und wo deutsch verwendet wird erarbeiten und
umsetzen

-   Betrifft: Dateinamen, Code, Doku, Commit-Messages

Versionnierung / Dateinamen des Images

  
Restliche Themen vertagt.  
  
Neben-Erkenntnisse:  
    FF-Plugin Umatrix führt noscript-tags von HTML nicht aus. Deswegen
bleiben manche Seiten leer  
    mutmaßliche MS-Strategie: Embrace, Extend, Extinguish:
<https://de.wikipedia.org/wiki/Embrace,_Extend_and_Extinguish>  
  
  
  
  
  
  
  

