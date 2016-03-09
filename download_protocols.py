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



cmd1 = "curl 'https://pad.fsfw-dresden.de/p/###/export/html' > protokoll-###.html"
#cmd2 = "pandoc -t markdown_strict protokoll-###.html > protokoll-###.md"
cmd2 = "pandoc -t markdown --strict protokoll-###.html > protokoll-###.md"
cmd3 = "gpg -b -a protokoll-###.md"
cmd4 = "rm protokoll-###.html"

repl = "###"

commands = [cmd1, cmd2, cmd3, cmd4]

identifiers = """
fsfw-dd-20160303
fsfw-dd-20160218
fsfw-dd-20160204
fsfw-dd-20160121
fsfw-dd-20160107
fsfw-dd-20151217
fsfw-dd-20151203
fsfw-dd-20151119
fsfw-dd-20151105
fsfw-dd-20151022
fsfw-dd-20151008
fsfw-dd-20150924
fsfw-dd-20150910
fsfw-dd-20150827
fsfw-dd-20150813
fsfw-dd-20150729
fsfw-dd-20150715
fsfw-dd-20150701
fsfw-dd-20150617
fsfw-dd-20150603
fsfw-dd-20150520
plenum-20150506
fsfw-dd-20150422
fsfw-dd-20150408
fsfw-dd-20150401
fsfw-dd-20150325
fsfw-dd-20150306-plenum
fsfw-dd-20150306-corporatedesign
fsfw-dd-20150306-infrastruktur
fsfw-dd-20150306-textverarbeitung
fsfw-dd-20150306-Mitgliedergewinnung
fsfw-dd-20150306-CryptoChallange
fsfw-dd-20150311
fsfw-dd-20150225
fsfw-dd-20150211
fsfw-dd-20150128
fsfw-dd-20150114
gc2rfrunRB
""".strip().split("\n")



for idf in identifiers:
    print('\n'+idf+':\n')
    for cmd_template in commands:
        cmd = cmd_template.replace(repl, idf)
        print(cmd)
        os.system(cmd)
        #break




