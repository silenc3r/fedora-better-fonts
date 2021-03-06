Name:    fontconfig-enhanced-defaults
Version: 2.0
Release: 1%{?dist}
Summary: Enables slight hinting and subpixel (rgb) antialiasing

Group:   System Environment/Libraries
License: Public Domain
URL:     https://github.com/silenc3r/fedora-better-fonts
Source0: 10_fontconfig-enhanced-defaults.gschema.override
Source1: 19-enhanced-defaults.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem
Requires:      freetype

%description
Font configuration files that enable subpixel rendering.

%install
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/19-enhanced-defaults.conf
ln -s %{_fontconfig_templatedir}/19-enhanced-defaults.conf \
      %{buildroot}%{_fontconfig_confdir}/19-enhanced-defaults.conf

ln -s %{_fontconfig_templatedir}/70-no-bitmaps.conf \
      %{buildroot}%{_fontconfig_confdir}/70-no-bitmaps.conf
ln -s %{_fontconfig_templatedir}/10-sub-pixel-rgb.conf \
      %{buildroot}%{_fontconfig_confdir}/10-sub-pixel-rgb.conf
ln -s %{_fontconfig_templatedir}/11-lcdfilter-default.conf \
      %{buildroot}%{_fontconfig_confdir}/11-lcdfilter-default.conf

install -m 0755 -d %{buildroot}%{_datadir}/glib-2.0/schemas
install -m 0644 -p %{SOURCE0} \
        %{buildroot}%{_datadir}/glib-2.0/schemas/10_org.fontconfig-enhanced-defaults.gschema.override

%files
%{_fontconfig_templatedir}/*
%{_fontconfig_confdir}/*
%{_datadir}/glib-2.0/schemas/*

%changelog
* Mon Nov 02 2020 Dawid Zych <dawid.zych@yandex.com> - 2.0-1
- Enable the package again

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
