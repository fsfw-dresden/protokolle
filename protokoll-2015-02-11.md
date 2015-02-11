prev:
[https://pad.zombofant.net/p/fsfw-dd-20150128](https://pad.zombofant.net/p/fsfw-dd-20150128)
next:
[https://pad.zombofant.net/p/fsfw-dd-20150225](https://pad.zombofant.net/p/fsfw-dd-20150225)


/etc/init.d/versammlung start
-----------------------------

-   Vorstellungsrunde; es gibt wieder einige Neue (17 Personen anwesend)


Infrastruktur
-------------

-   Vorfall-Kurzbericht: öffentliches Archiv der intern-Mailingliste
    (inkl. Passwort fürs Kontaktpad)
    -   Archiv wurde weggemacht; Passwort fürs Kontaktpad wurde geändert
    -   datenschutzrechtliche Relevanz des Vorfalls wird als gering
        eingeschätzt
    -   Vorschlag 1: allgemeines Keysigning, dann Credentials nur über
        GPG-verschlüsselte Mails verteilen
    -   Vorschlag 2: Credentials über Kanboard verteilen (via Aufgabe,
        die immer offen bleibt)
    -   siehe auch nächster TOP
-   Umgang mit internen Informationen
    -   Brauchen wir ein internes Wiki mit Nutzerverwaltung?
        -   Allgemeiner Konsens: Ja, Infrastrukturgruppe soll eine
            Wiki-Software wählen.
        -   Alternativ statt einem internen Wiki eine OwnCloud?
    -   Was wird intern, was öffentlich dokumentiert?
        -   Öffentlich nur Dokumentation (z.B. Protokolle) und
            offizielle Aussagen (Kampagnenmaterial, Flyer).
        -   Intern alles andere (insb. unfertige Materialien,
            Kontaktinfos).
-   Mailinglisten
    -   angelegt: intern, discuss, news, kontakt, group-latex, infra
        -   kontakt-Mailingliste ist auf kontakt@fsfw-dresden.de
            gealiast
        -   [https://lists.fsfw-dresden.de/mailman/listinfo/kontakt](https://lists.fsfw-dresden.de/mailman/listinfo/kontakt)
    -   group-latex-Liste ist noch nicht migriert, da Jonas keinen
        Zugriff auf die Userliste der alten Liste hat
    -   Frage: Wollen wir ein öffentliches Archiv? (interne Archive für
        Subscriber sowieso)
        -   Vorschlag: nur bei news
        -   Gegenvorschlag: auch bei discuss
        -   noch ein Vorschlag: öffentliches Archiv bei allen Listen,
            die frei subscribe-bar sind
        -   Gegenrede: Mailingliste ist kein sinnvolles
            Dokumentationsarchiv
    -   Subscription geht zurzeit nur mit Moderatorbestätigung.
        -   news@ bitte auf freie Subscription umstellen.
        -   discuss@ auch?
-   interne Organisation: Fluktuationsmanagement und (technische)
    Dokumentation
    -   Dokumentation ist wichtig! Damit Neue nachlesen können, was
        bisher wie besprochen wurde; wenn Leute ausscheiden, sollte
        nicht gleich alles zusammenbrechen.
    -   Mentoren für Neue
    -   praktische Umsetzung: Wir machen eine Wiki-Seite.
    -   Findet sich dafür ein dedizierter Ansprechpartner, der
        Neuankömmlinge mentoriert?
        -   Christoph meldet sich, ist ab sofort zum Mentor ernannt.
        -   Eventuell kann man auch mentor@fsfw-dresden.de einrichten.
-   Git(hub)-Organisation
    -   [https://github.com/fsfw-dresden](https://github.com/fsfw-dresden)
    -   einige neue Leute hinzugefügt
-   Redmine als Git/Projekt-Management-Plattform
    -   Vorteil: Redmine kann Kanboard via Plugin ersetzen, hat wohl ein
        sinnvolles Mail-Interface (im Gegensatz zu Kanboard)
    -   Konsens: Redmine ausprobieren, dann weitersehen
-   Exchange-Accounts für Studenten
    -   Neueingeschriebene TU-Studenten seit 2014 kriegen nur noch einen
        Exchange-Account, nicht mehr die alte Lösung (IMAP-Postfach mit
        Horde-Webmail).
    -   Verfahrensfrage: Wenn es jetzt inhaltlich wird, wollen wir das
        alles in einem öffentlichen Pad dokumentieren?
    -   Thema wird im Rahmen einer Gruppe weiterverfolgt
    -   nichtöffentliche Diskussion hierzu unter
        [https://pad.zombofant.net/p/dbXH80Fntt](https://pad.zombofant.net/p/dbXH80Fntt)
-   Finanzierung
    -   Kosten für Infrastruktur: Domain, evtl. Server (sofern wir da
        nichts gesponsert kriegen - solange wir da nichts  gesponsort
        kriegen!)
        -   Kann man von anderen Non-Profits (z.B. FSFE) Infrastruktur
            sponsoren lassen?
    -   Kosten für Veranstaltungen (Anfahrt etc. für externe Referenten,
        Material für Gewinnspiele)
    -   Antrag Finanzierung beim StuRa?
    -   Frage der Rechtsform, um eventuelle Haftungsansprüche der
        Einzelmitglieder auszuschließen; Vereinsgründung schwer, andere
        Formen reichen nicht aus
    -   Sind wir schon eine juristische Person, weil wir als
        Hochschulgruppe eingetragen sind?
    -   Impressum über Fachschaftsrat Informatik?  Schwierig, da
        formelle und politische Bindung an einzelne Fakultät. → Basti
        und Sebastian recherchieren
-   Server
    -   Frank: 1und1 für 1€ im Jahr für Studenten
        [http://hosting.1und1.de/campus-code?studentsclubtmsp=true](http://hosting.1und1.de/campus-code?studentsclubtmsp=true)
    -   Infrastrukturgruppe hilft beim Feldversuch (Jonas, …)
    -   [http://campus-code.de](http://campus-code.de)
-   Öffentlichkeitsarbeit
    -   Visitenkarten
    -   Farbschema der TU nutzen? → lieber nicht (markenrechtlich
        bedenklich)
    -   nicht so dringend
    -   auf die Website schreiben, dass man da mitmachen kann
    -   Vorschlag: Logowettbewerb (allgemein Design Identity:
        Hausschriftart und solche Dinge)
-   Mentoring
    -   aktuell beschäftigt sich die Gruppe mit sich selbst →
        Entlastung: an der Uni vorhandene Ressourcen nutzen (ähnlich wie
        Google Summer of Code)
    -   Idee: organisieren, dass sowas als AQua (ECTS-Punkte fürs
        Studium) anerkannt wird
    -   erstes Zieldatum: relevant ab kommendem Semester
    -   Frage: haben wir Leute, die in der Entwicklung freie Software so
        drinstecken, dass sie andere mentoren können?
    -   Idee: Call "in beide Richtungen", d.h. nach Studenten und
        Mentoren?  (Punkte gibts somit auch für letztere)
    -   <s>Haufen</s>Gruppengründung?
    -   Öffentliche Vorstellung von Projekten?
-   andere thematisch angrenzende Gruppen
    -   OK Lab der Open Knowledge Foundation wurde kurz vorgestellt (
        [http://offenesdresden.de/](http://offenesdresden.de/) )
    -   Können wir von sowas ne Liste zusammenstellen? Das wäre in
        kuratierter Form super Content für die Webseite.
        -   [https://fusionforge.zih.tu-dresden.de/plugins/mediawiki/wiki/fsfw/index.php/Andere\_Gruppen\_in\_der\_Umgebung\_mit\_%C3%A4hnlichem\_Ziel](https://fusionforge.zih.tu-dresden.de/plugins/mediawiki/wiki/fsfw/index.php/Andere_Gruppen_in_der_Umgebung_mit_%C3%A4hnlichem_Ziel)
    -   Zusammentragen von angrenzenden Informationen, SLUB-Projekte,
        Lehrstühle die Publikationen frei veröffentlichen, …
    -   Bestehende "freie" wissenschaftliche Szene in Dresden
        kartographieren und darstellen, als positiven Aspekt
    -   Content für die verschiedenen Hochschul-Journale
    -   Poster, das Freie Software vorstellt/ bewirbt
    -   Freie Software-DVD für Studis:
        [http://wiki.stura.htw-dresden.de/index.php/Erstie\_DVD](http://wiki.stura.htw-dresden.de/index.php/Erstie_DVD)
        -   that is sooo 2000! -\> optische Steinzeitmedien braucht
            keine Mensch mehr, internet is the shit! (das gibts auch als
            Usb-Stick;-)
        -   wie wäre es mit einem ansible playbook, das coole Software
            installiert (wäre natürlich etwas Distro spezifisch)
        -   Live Systeme ( hd usb oder DVD ) lässt sich vom Live-System
            aus auch fest installieren
        -   Meine Erfahrung mit Live-Systemen ist, dass niemand sie
            nutzt (weil es am Ende nur nervt, langsam ist, ...)
        -   eine Live-System kopie auf ssd ist super schnell (wer hat
            eine SSD rumliegen für sowas? anstatt einfach das System zu
            installieren)
        -   Auf nem USB 2.0 Stick ist so’n livesystem nicht mehr
            langsam, auf 3.0 schon garnicht.
        -   Jau am ehesten USB Stick, klar!
-   Idee: Party mit freier Musik -\> Problem:
    [http://www.kraftfuttermischwerk.de/blogg/die-gema-kassiert-bei-einer-veranstaltung-auf-der-einzig-cc-musik-lief/](http://www.kraftfuttermischwerk.de/blogg/die-gema-kassiert-bei-einer-veranstaltung-auf-der-einzig-cc-musik-lief/)
-   Workshop im März. link zum doodle:
    [https://dudle.inf.tu-dresden.de/FSFW\_Intern\_Workshop/](https://dudle.inf.tu-dresden.de/FSFW_Intern_Workshop/)
-   Filmabend im Kino-im-Kasten mit entsprechenden Filmen
    -   Citizenfour, Plug & Pray etc.
    -   Basti kümmert sich um Wiki
-   nächster Termin und Ort
    -   neuer Ort -\> auf nächtes mal verschoben
-   Makerspaceeröffnung
