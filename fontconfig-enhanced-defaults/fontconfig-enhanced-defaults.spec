Name:    fontconfig-enhanced-defaults
Version: 1.0
Release: 1%{?dist}
Summary: Dummy package. It does nothing.

Group:   System Environment/Libraries
License: Public Domain
URL:     https://github.com/silenc3r/fedora-better-fonts

BuildArch:     noarch

%description
This package does nothing. There's no reason to install it.
It's there just for compatability reasons.

%changelog
* Fri Oct 30 2020 Dawid Zych <dawid.zych@yandex.com> - 1.0-1
- Make it a dummy package

* Wed Aug 28 2019 Dawid Zych <dawid.zych@yandex.com> - 0.4.3
- Drop support for Fedora < 29

* Tue Nov 06 2018 Dawid Zych <dawid.zych@yandex.com> - 0.4.2
- Use stock Freetype on Fedora 29 and newer

* Fri Apr 06 2018 Dawid Zych <dawid.zych@yandex.com> - 0.4-1
- Add enhanced-defaults.conf again just in case

* Thu Jan 18 2018 Dawid Zych <dawid.zych@yandex.com> - 0.3-1
- Replace config file with symlinks to fontconfig configuration files

* Tue Jan 17 2017 Dawid Zych <dawid.zych@yandex.com> - 0.2-1
- Fix font rendering in Java apps.

* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 0.1-1
- Initial packaging.
