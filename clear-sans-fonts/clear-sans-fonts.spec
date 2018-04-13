%global fontname clear-sans
%global fontconf 61-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.0
Release: 1%{?dist}
Summary: Clear Sans is a versatile OpenType font for screen, print, and Web.

Group:   User Interface/X
License: ASL 2.0
URL:     https://www.fontsquirrel.com/fonts/coda
Source0: https://www.fontsquirrel.com/fonts/download/%{fontname}.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Clear Sans is a versatile OpenType font for screen, print, and Web. We
designed Clear Sans with on-screen legibility and glanceability in
mind. It strikes a balance between contemporary, professional, and
stylish expression and thoroughly functional purpose. It has a
sophisticated and elegant personality at all sizes, and its thoughtful
design becomes even more evident at the thin weight.

Clear Sans has minimized, unambiguous characters and slightly narrow
proportions, making it ideal for UI design. Its strong, recognizable
forms avoid distracting ambiguity, making Clear Sans comfortable for
reading short UI labels and long passages in both screen and print.

Clear Sans supports a wide range of languages using Latin, Cyrillic,
and Greek scripts. The font family includes Medium, Regular, Thin, and
Light weights with upright, italic, and bold styles.

%prep
%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f %{fontconf} *.ttf
%license "Apache License.txt"

%changelog
* Thu Apr 12 2018 Dawid Zych <dawid.zych@yandex.com> - 1.0-1
- Initial packaging.
