%global fontname merriweather-sans
%global fontconf 62-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.006
Release: 3%{?dist}
Summary: Merriweather Sans-Serif font family by Eben Sorkin

License:  OFL
URL:      www.sorkintype.com
Source0: %{name}-%{version}.tar.xz
Source1: %{fontname}-fontconfig.conf
Source2: get-%{fontname}.sh

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem
Conflicts:     sorkintype-merriweather-sans-fonts

%description
Merriweather Sans is a low-contrast semi-condensed sans-serif text typeface
family designed to be pleasant to read at very small sizes. Merriweather Sans
is traditional in feeling despite the modern shapes it has adopted for
screens. Designed by Eben Sorkin, Merriweather Sans features a large x height,
slightly condensed letterforms, a mild diagonal stress and open forms.

%prep
%setup -q

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

cp -p OFL.txt LICENSE
sed -i 's/\r$//' LICENSE

%_font_pkg -f %{fontconf} *.ttf
%license LICENSE

%changelog
* Wed Jan 11 2017 Dawid Zych <dawid.zych@yandex.com> - 1.006-3
- Add conflicting package
- Last version for Fedora 31

* Wed Jan 11 2017 Dawid Zych <dawid.zych@yandex.com> - 1.006-2
- Update fontconfig and it's priority.

* Fri Jan 06 2017 Dawid Zych <dawid.zych@yandex.com> - 1.006-1
- Initial packaging.
