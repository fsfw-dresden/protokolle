SHELL = /bin/bash
PROTOKOLLE = $(shell cat liste-der-protokolle | grep '^fsfw-dd' | sed -e 's/^\(.*\)$$/markdown\/protokoll-\1.md/')

protokoll-%.html:
	curl 'https://pad.fsfw-dresden.de/p/$*/export/html' > $@

%.md: %.html
	pandoc -t markdown_strict $< > $@

%.md.asc: %.md
	gpg --detach-sign --armor $<

update-all: $(PROTOKOLLE) $(foreach p,$(PROTOKOLLE), $(p).asc)

protokolle.html: protokolle.md
	pandoc -s -f markdown_strict -t html protokolle.md > protokolle.html

protokolle.md:
	./generate-protocol-overview.sh

