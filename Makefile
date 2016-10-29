PROTOKOLLE = $(shell cat liste-der-protokolle | grep '^fsfw-dd' | sed -e 's/^\(.*\)$$/protokolle\/protokoll-\1.md/')
SIGNATUREN = $(foreach p,$(PROTOKOLLE),$(p).asc)

protokoll-%.html:
	w3m -dump_source 'https://pad.fsfw-dresden.de/p/$(*F)/export/html' | gunzip > $@

%.md: %.html
	pandoc -t markdown_strict $< > $@

%.md.asc: %.md
	gpg --detach-sign --armor $<

update-all: $(PROTOKOLLE) $(SIGNATUREN)

protokolle.html: protokolle.md
	pandoc -s -f markdown_strict -t html protokolle.md > protokolle.html

protokolle.md: $(PROTOKOLLE)
	./generate-protocol-overview.sh

test: $(PROTOKOLLE) $(SIGNATUREN)
	for file in protokolle/protokoll-*.md; do \
	  gpg --quiet --verify $${file}.asc $${file}; \
	done
