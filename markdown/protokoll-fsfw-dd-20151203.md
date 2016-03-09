Protokoll fsfw Dresden 2015-12-03
=================================

Übersicht über bisherige Pads:
[**https://wiki.fsfw-dresden.de/doku.php?id=orga:protokolle**](https://wiki.fsfw-dresden.de/doku.php?id=orga:protokolle)  

TOP-Vorschläge
--------------

  

Linux-Install-Party-Werbung (Carsten, 15min)

[https://fsfw-dresden.de/installparty](https://fsfw-dresden.de/installparty)

Nochmal Ankündigung auf der Startseite unserer Homepage (Wie für
LaTex-Kurs?)

Facebook&Co (Aber schon jetzt oder später?)

Werbung an der HTW:

-   FSR-Info/Mathe (will Plakat machen)
-   StuRa (
    [http://www.stura.htw-dresden.de/stura/ref/hopo/dk/termine/linux-installparty](http://www.stura.htw-dresden.de/stura/ref/hopo/dk/termine/linux-installparty)
    )

Zielgruppe?

[https://wiki.fsfw-dresden.de/doku.php?id=orga:oeffentlichkeitsarbeit](https://wiki.fsfw-dresden.de/doku.php?id=orga:oeffentlichkeitsarbeit)

ScienceSlam 9.12. 19:30 HSZ

Status: Telefonliste? (Carsten, 5min,
<[https://tracker.fsfw-dresden.de/issue52](https://tracker.fsfw-dresden.de/issue52)\>)

Protokolle gesammelt durchsuchbar machen (Carsten, 5min,
<[https://tracker.fsfw-dresden.de/issue51](https://tracker.fsfw-dresden.de/issue51)\>)

Tracker-Usability-Wünsche (Carsten, 3min):

-   Listen-Fenster Geometrie
-   Priorität: normal als Standardwert

(automatische) Übersicht über FSFW-Kurzlinks? (Carsten, 2min)

Bilder für die Startseite (Christoph)

Upgrade Rosetta, Finanzierung

  

Das tatsächliche Protokoll
--------------------------

  

nac ist da (C3D2, internet4refugees)

Möchte für eigene Workshops und How-Tos unser Wiki zu Rate ziehen und
mitbenutzen

-   Trennung von FSFW-Orgakram beibehalten
-   nac und weitere kriegen Invites
-   Alles weitere ergibt sich über zukünftige Kommunikation

Hat Orte für Workshops (Problem teilweise: Nutzer haben keine Computer)

Kulturtreff Johannstadt und Evangelische Hochschule

sucht noch andere Räume falls o.g. ausgebucht sind

-   Hinweis: beim iFSR würde man diesbezüglich offene Türen einrennen

Themen: PGP (zu hoch) also allgemein E-Mail-Verarbeitung (Mailinglisten,
Filter, ...)

Technikausleihe?

-   StuRa der TU hat Technik und engagiert sich in der Richtung –
    Kontakte zur entsprechenden StuRa AG herstellen
-   muc xmpp:refugees@chat.c3d2.de

Telefonliste:

-   Niemand hat gerade Zeit das ldap-dingens auszubauen – daher
    verschoben
-   Jetzt bekommt Carsten erstmal eine Hardware-Liste

Carsten wünscht sich ein durchsuchbares Protokollarchiv

wie kriegen wir pads in text-form --\> siehe übernächste Zeile

Aktuelles Pad exportieren als .txt ?

-   -\> geht per Pad-URL + /export/txt (also z.B.:
    [https://pad.fsfw-dresden.de/p/fsfw-dd-20151203/export/txt](https://pad.fsfw-dresden.de/p/fsfw-dd-20151203/export/txt)
    ); Pad-Übersicht auf Wikiseite

Sebis Vorschlag: Ein Ritual aus dem Pad exportieren machen

-   wolf: einer klickt, die andreen müssen rituell tanzen und die
    beschwörung säuseln ;)

Vorgehensvorschlag: Export der Protokolle in einzelne Commits. Sebi
bastelt CGI-Skript, das alle Protokolle zusammencuttet

-   Protokolle werden in Zukunft auf git.fsfw-dresden.de gepushed
-   Sebi bastelt ein Skript, dass bei Aufruf einer URL sich ein Pad
    holt, dieses als neue Datei ins Repo commited, aus allen vorhandenen
    Protokollen eine statische Seite bastelt und diese zur Verfügung
    stellt
-   git.fsfw-dresden.de könnte man mit Webfrontend ausstatten,
    möglicherweise dann hinter HTTP-Auth
-   wie wäre es die ..txt im wiki unter
    ../orga/protokolle/fsfw-dd-2015...txt abzulegen -- damit wären sie
    im wiki durchsuchbar.
-     

Übersicht der Kurzlinks

-   Es gibt momentan /installparty und /sprechstunde
-   Bei der Apache-Migration ist /gewinnspiel weggefallen, sollte auf
    [https://wiki.fsfw-dresden.de/doku.php?id=doku:verschluesselungsgewinnspiel](https://wiki.fsfw-dresden.de/doku.php?id=doku:verschluesselungsgewinnspiel)
    zeigen

Christoph fordert mehr Bilder auf der Startseite (z.B. ein Foto mit
Wolken)

-   Gruppenfoto steht zur Diskussion. Meinung geteilt (man sieht, mit
    wem man es zu tun hat)
-   Norman merkt an, dass die Gliederung auch verbesserungswürdig ist
-   wolf: eher bilder wie bei themen einbinden; gruppenbild ermangelt
    noch content zur (abgebildeten) "gruppe"

LIP

Werbung bisher schmal. Ist über den Studierenden-Newsletter gegangen

gibt es schon einen Eintrag im Diaspora?

Werbung an der HTW:

FSR-Info/Mathe (will Plakat machen) (Norman berichtete)

Norman kann einige Linux-affine Info-Profs kurz drauf aufmerksam machen

-   -\> erledigt: 2 der 3 angeschriebenen Informatik-Profs an der HTW
    Dresden, haben bisher geantwortet, das sie den Veranstaltungshinweis
    gerne weiter geben

StuRa (
[http://www.stura.htw-dresden.de/stura/ref/hopo/dk/termine/linux-installparty](http://www.stura.htw-dresden.de/stura/ref/hopo/dk/termine/linux-installparty)
)

wolf versucht die monitore zu ownen (legal wise)

Carsten will für ausgewählte Kreise Hörsaalansprachen machen

Es braucht noch Plakate. Wenn Plakate vorhanden, wohin damit?

was ist mit Mensawerbung (Displays)

Upgrade Rosetta

-   Rosetta ist ein altes Hetzner-Produkt. Es gibt mittlerweile
    billigere Produkte, die die gleiche Performance ausweisen
-   Jonas bezahlt bisher immer noch privat, beläuft sich mittlerweile
    auf ca. 60€
-   Migration ist momentan zeittechnisch schwierig, aber dank Ansible
    kleiner Aufwand
-   Domain ist btw jetzt auch bei Gandi(+1 der freude)

