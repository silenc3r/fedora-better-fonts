%global fontname quintessential
%global fontconf 45-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.001
Release: 1%{?dist}
Summary: Calligraphic lettering typeface based on the Italic Hand

Group:   User Interface/X
License: OFL
URL:     https://fonts.google.com/specimen/Quintessential
Source0: %{name}-%{version}.tar.xz
Source1: %{fontname}-fontconfig.conf
Source2: getquintessential.sh

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
The Quintessential typeface is a calligraphic lettering style based
on the Italic Hand. As speed became more essential in writing hands,
styles became less formal and more relaxed. Classic, clean, and casual,
Quintessential fits a lot of design uses - hence its name.

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
* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 1.001-1
- Initial packaging.
