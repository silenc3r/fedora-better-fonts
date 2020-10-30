srpm:
	dnf -y install wget
	find -type f -executable -exec {} \;
	cp -r ./* /builddir/build/SOURCES/
	rpmbuild -bs *.spec
	cp -r /builddir/build/SRPMS/* \$(outdir)
