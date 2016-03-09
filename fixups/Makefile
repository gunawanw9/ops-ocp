.PHONY: all install clean

all:

clean:

install:
	@echo Removing previous file
	rm $(DESTDIR)/../../openvswitch/install/usr/lib/libovsdb.la || true
	@echo Copying to $(DESTDIR)
	test -d  $(DESTDIR)/usr/lib || mkdir -p $(DESTDIR)/usr/lib
	cp libovsdb.la $(DESTDIR)/usr/lib/libovsdb.la
