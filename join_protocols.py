# -*- coding: utf-8 -*-

"""
Python Skript um folgendes Vorgehen zu automatisieren

# Alle Markdowndateien der Protokolle laden
# durch einen Separator getrennt zusammenfügen
# eine große Markdowndatei schreiben
# diese in HTML umwandeln

"""
import os
import codecs


path = os.getcwdu()
fnames = os.listdir( path )

fnames.sort(reverse=True)



#1/0

fname_result = "result.md"

separator =\
"""
*******************************************************************************

"""


def fname_to_link_anchor(fname):
    name = fname.replace('protokoll-fsfw-dd-', '')[:-3]
    
    # html
    #anchor = '<a name="%s">%s</a>' %(name, name)
    #link = '<li><a href="#%s">%s</a></li>' %(name, name)
    
    # markdown links to anchors
    # http://stackoverflow.com/questions/6695439/how-do-you-create-link-to-a-named-anchor-in-multimarkdown
    anchor = '<a name="%s"></a>%s\n' %(name, fname)
    link = '  1. [%s](#%s)' %(name, name)

    return link, anchor
    

contents = []
toc_links = []

for fname in fnames:
    if not fname.startswith('protokoll-'):
        continue
    #with open(fname) as txtfile:
    with codecs.open(fname, encoding='utf-8') as txtfile:
        link, anchor = fname_to_link_anchor(fname)
        toc_links.append(link)
        contents.append(separator)
        contents.append(anchor)
        contents.append(separator)
        contents.append(txtfile.read())
        contents.append(separator)

# Table of contents
#toc= "## Inhaltsverzeichnis: <ol>\n%s\n</ol>" % "\n".join(toc_links)
toc= "## Inhaltsverzeichnis: \n%s\n" % "\n".join(toc_links)

print toc
from IPython import embed as IPS
IPS()
all_txt = u"".join([toc, separator] + contents)

#with open(fname_result, "w") as txtfile:
with codecs.open(fname_result, mode='wb', encoding='utf-8') as txtfile:
    txtfile.write(all_txt)

    
# now use: pandoc -s -t html result.md > protokolle.html

