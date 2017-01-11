Name:    fontconfig-enhanced-defaults
Version: 0.1
Release: 1%{?dist}
Summary: Enhanced default settings for Fontconfig and FreeType

Group:   System Environment/Libraries
License: Public Domain
URL:     https://github.com/silenc3r/fedora-better-fonts
Source0: 10_fontconfig-enhanced-defaults.gschema.override
Source1: fontconfig-enhanced-defaults.sh
Source2: 10-enhanced-defaults.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem
Requires:      freetype-freeworld

%description
Font configuration files that enable subpixel rendering.

%install
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}
ln -s %{_fontconfig_templatedir}/10-enhanced-defaults.conf \
      %{buildroot}%{_fontconfig_confdir}/10-enhanced-defaults.conf

install -m 0755 -d %{buildroot}%{_datadir}/glib-2.0/schemas
install -m 0644 -p %{SOURCE0} \
        %{buildroot}%{_datadir}/glib-2.0/schemas/10_org.fontconfig-enhanced-defaults.gschema.override

install -m 0755 -d %{buildroot}%{_sysconfdir}/profile.d/
install -m 0755 -p %{SOURCE1} \
        %{buildroot}%{_sysconfdir}/profile.d/fontconfig-enhanced-defaults.sh

%files
%{_fontconfig_confdir}/*
%{_fontconfig_templatedir}/*
%{_datadir}/glib-2.0/schemas/*
%config %{_sysconfdir}/profile.d/*

%changelog
* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 0.1-1
- Initial packaging.
