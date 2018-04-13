%global fontname komika-text
%global fontconf 61-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 2.0
Release: 1%{?dist}
Summary: Casual typeface similar to Comic Sans MS.
Group:   User Interface/X
License: custom
URL:     https://www.fontsquirrel.com/fonts/Komika-Text
Source0: https://www.fontsquirrel.com/fonts/download/Komika-Text.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Casual typeface similar to Comic Sans MS.

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
%license "Apostrophic Labs License.txt"

%changelog
* Fri Apr 13 2018 Dawid Zych <dawid.zych@yandex.com> - 2.0-1
- Initial packaging.
