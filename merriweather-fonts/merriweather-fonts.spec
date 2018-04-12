%global fontname merriweather
%global fontconf 62-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 2.002
Release: 1%{?dist}
Summary: Merriweather Serif font family by Eben Sorkin

License: OFL
URL:     www.sorkintype.com
Source0: %{name}-%{version}.tar.xz
Source1: %{fontname}-fontconfig.conf
Source2: get-%{fontname}.sh

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Merriweather was designed to be a text face that is pleasant to read on
screens. Designed by Eben Sorkin, Merriweather features a very large x
height, slightly condensed letterforms, a mild diagonal stress, sturdy
serifs and open forms.

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
* Thu Apr 11 2018 Dawid Zych <dawid.zych@yandex.com> - 2.002-1
- Update to new version

* Wed Jan 11 2017 Dawid Zych <dawid.zych@yandex.com> - 1.584-2
- Update fontconfig and it's priority.

* Fri Jan 06 2017 Dawid Zych <dawid.zych@yandex.com> - 1.584-1
- Initial packaging.
