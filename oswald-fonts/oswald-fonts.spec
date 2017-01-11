%global fontname oswald
%global fontconf 64-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 4.0
Release: 2%{?dist}
Summary: Oswald is a reworking of the classic Gothic and Grotesque type styles

Group:   User Interface/X
License: OFL
URL:     https://fonts.google.com/specimen/Oswald
Source0: %{name}-%{version}.tar.xz
Source1: %{fontname}-fontconfig.conf
Source2: get-%{fontname}.sh

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Oswald is a reworking of the classic style historically represented
by the 'Alternate Gothic' sans serif typefaces. The characters
of Oswald have been re-drawn and reformed to better fit the pixel
grid of standard digital screens. Oswald is designed to be used
freely across the internet by web browsers on desktop computers,
laptops and mobile devices.

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

mv OFL.txt LICENSE
sed -i 's/\r$//' LICENSE

%_font_pkg -f %{fontconf} *.ttf
%license LICENSE

%changelog
* Wed Jan 11 2017 Dawid Zych <dawid.zych@yandex.com> - 4.0-2
- Update fontconfig and it's priority.

* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 4.0-1
- Initial packaging.
