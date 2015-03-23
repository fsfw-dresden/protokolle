# -*- coding: utf-8 -*-

"""
Python Skript um folgendes Vorgehen zu automatisieren:

curl 'http://pad.zombofant.net/p/fsfw-dd-20150211/export/html' > protokoll-2015-02-11.html
pandoc -t markdown_strict protokoll-2015-02-11.html > protokoll-2015-02-11.md
… manuelles Nachbearbeiten …
gpg -b -a protokoll-2015-02-11.md
rm protokoll-2015-02-11.html


"""
import os

cmd1 = "curl 'http://pad.zombofant.net/p/###/export/html' > protokoll-###.html"
#cmd2 = "pandoc -t markdown_strict protokoll-###.html > protokoll-###.md"
cmd2 = "pandoc -t markdown --strict protokoll-###.html > protokoll-###.md"
cmd3 = "gpg -b -a protokoll-###.md"
cmd4 = "rm protokoll-###.html"

repl = "###"

commands = [cmd1, cmd2, cmd3, cmd4]

identifiers = ['fsfw-dd-20150311',
              'fsfw-dd-20150306-plenum',
              'fsfw-dd-20150306-infrastruktur',
              'fsfw-dd-20150306-Mitgliedergewinnung',
              'fsfw-dd-20150306-corporatedesign',
              'fsfw-dd-20150306-textverarbeitung',
              'fsfw-dd-20150306-CryptoChallange']



for idf in identifiers:
    print('\n'+idf+':\n')
    for cmd_template in commands:
        cmd = cmd_template.replace(repl, idf)
        print cmd
        os.system(cmd)
        #break




