Name:    fontconfig-font-replacements
Version: 0.5
Release: 2%{?dist}
Summary: Font replacement rules for popular proprietary fonts.

Group:   System Environment/Libraries
License: MIT
URL:     https://github.com/silenc3r/fedora-better-fonts
Source0: 36-repl-liberation-fonts.conf
Source1: 37-repl-global-free.conf
Source2: 52-latin-free.conf
Source3: 66-aliases-wine-free.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      adobe-source-code-pro-fonts
Requires:      archivo-black-fonts
Requires:      courier-prime-fonts
Requires:      eb-garamond-fonts
Requires:      fontpackages-filesystem
Requires:      gelasio-fonts
Requires:      google-croscore-arimo-fonts
Requires:      google-croscore-cousine-fonts
Requires:      google-croscore-tinos-fonts
Requires:      google-crosextra-caladea-fonts
Requires:      google-crosextra-carlito-fonts
Requires:      google-noto-sans-fonts
Requires:      google-noto-serif-fonts
Requires:      google-roboto-fonts
Requires:      komika-text-fonts
Requires:      lato-fonts
Requires:      libre-baskerville-fonts
Requires:      libreoffice-opensymbol-fonts
Requires:      linux-libertine-biolinum-fonts
Requires:      merriweather-fonts
Requires:      merriweather-sans-fonts
Requires:      mozilla-fira-sans-fonts
Requires:      mozilla-fira-mono-fonts
Requires:      passion-one-fonts
# Requires:      signika-fonts

%if 0%{?fedora} <= 29
Requires: liberation-narrow-fonts
%endif

%description
Font replacement rules for popular proprietary fonts. This includes
Microsoft TrueType Core Fonts, Microsoft ClearType Font Collection and
some others.
Based on Bohoomil's fontconfig ultimate.

%prep

%build

%install
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE0} \
        %{buildroot}%{_fontconfig_templatedir}/36-repl-liberation-fonts.conf
ln -s %{_fontconfig_templatedir}/36-repl-liberation-fonts.conf \
      %{buildroot}%{_fontconfig_confdir}/36-repl-liberation-fonts.conf
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/37-repl-global-free.conf
ln -s %{_fontconfig_templatedir}/37-repl-global-free.conf \
      %{buildroot}%{_fontconfig_confdir}/37-repl-global-free.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/52-latin-free.conf
ln -s %{_fontconfig_templatedir}/52-latin-free.conf \
      %{buildroot}%{_fontconfig_confdir}/52-latin-free.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/66-aliases-wine-free.conf
ln -s %{_fontconfig_templatedir}/66-aliases-wine-free.conf \
      %{buildroot}%{_fontconfig_confdir}/66-aliases-wine-free.conf

%files
%{_fontconfig_confdir}/*
%{_fontconfig_templatedir}/*

%changelog
* Wed Aug 28 2019 Dawid Zych <dawid.zych@yandex.com> - 0.5-2
- Remove liberation-narrow-fonts from Fedora 30+

* Fri Apr 13 2018 Dawid Zych <dawid.zych@yandex.com> - 0.5-1
- Remove some less common Lucida variants substitutions
- Substitute Lucida Console with Fira Mono
- Substitute Lucida Sans fonts with Source Code Pro
- Substitute Consolas with Fira Mono
- Substitute Helvetica Neue with Source Code Pro
- Substitute Menlo with Cousine
- Substitute Wingdings with Open Symbol
- Substitute Comic Sans MS with Komika Text

* Thu Apr 12 2018 Dawid Zych <dawid.zych@yandex.com> - 0.4-2
- Update version

* Thu Apr 12 2018 Dawid Zych <dawid.zych@yandex.com> - 0.4-1
- Replace SymbolNeu with Open Symbol
- Fix package versioning

* Fri Apr 05 2018 Dawid Zych <dawid.zych@yandex.com> - 0.1-1
- Replace cabin with lato

* Wed Jan 11 2017 Dawid Zych <dawid.zych@yandex.com> - 0.003-1
- Update font replacement rules

* Wed Jan 11 2017 Dawid Zych <dawid.zych@yandex.com> - 0.002-1
- Set monospace font to Source Code Pro
- Add fantasy and cursive default fonts

* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 0.001-1
- Initial packaging.
