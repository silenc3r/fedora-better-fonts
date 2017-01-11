Name:    fontconfig-font-replacements
Version: 0.001
Release: 1%{?dist}
Summary: Font replacement rules for popular MS fonts

Group:   System Environment/Libraries
License: MIT
URL:     https://github.com/silenc3r/fedora-better-fonts
Source0: 36-repl-liberation-fonts.conf
Source1: 37-repl-global-free.conf
Source2: 52-latin-free.conf
Source3: 66-aliases-wine-free.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem
Requires:      archivo-black-fonts
Requires:      cabin-fonts
Requires:      courier-prime-fonts
Requires:      eb-garamond-fonts
Requires:      fjalla-one-fonts
Requires:      gelasio-fonts
Requires:      google-croscore-arimo-fonts
Requires:      google-croscore-cousine-fonts
Requires:      google-croscore-symbolneu-fonts
Requires:      google-croscore-tinos-fonts
Requires:      google-crosextra-caladea-fonts
Requires:      google-crosextra-carlito-fonts
Requires:      google-noto-sans-fonts
Requires:      google-noto-serif-fonts
Requires:      google-roboto-fonts
Requires:      liberation-narrow-fonts
Requires:      libre-baskerville-fonts
Requires:      linux-libertine-biolinum-fonts
Requires:      merriweather-fonts
Requires:      merriweather-sans-fonts
Requires:      mozilla-fira-sans-fonts
Requires:      signika-fonts

%description
Font replacement rules for popular MS fonts. Based on Bohoomil's fontconfig
ultimate. This package will install all required fonts as dependencies.


%install
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p *.conf \
        %{buildroot}%{_fontconfig_templatedir}
for fconf in *.conf; do
    ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

%files
%{_fontconfig_confdir}/*
%{_fontconfig_templatedir}/*

%changelog
* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 0.001-1
- Initial packaging.
