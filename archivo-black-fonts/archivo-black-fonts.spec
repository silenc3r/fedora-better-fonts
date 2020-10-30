%global fontname archivo-black
%global fontconf 64-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.001
Release: 1%{?dist}
Summary: Grotesque sans-serif typeface derived from Chivo. Black style

Group:   User Interface/X
License: OFL
URL:     https://omnibus-type.com/
Source0: https://www.omnibus-type.com/wp-content/uploads/Archivo-Black.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Archivo from Omnibus-Type is a grotesque sans-serif typeface family
derived from Chivo. Black style.


%prep
%setup -q -n Archivo-Black

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p otf/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

cp -p OFL.txt LICENSE
sed -i 's/\r$//' LICENSE

%_font_pkg -f %{fontconf} *.otf
%license LICENSE

%changelog
* Fri Oct 30 2020 Dawid Zych <dawid.zych@yandex.com> 1.001-1
- Use otf version of the font
- Bump version

* Wed Jan 11 2017 Dawid Zych <dawid.zych@yandex.com> 1.0004-2
- Update fontconfig and it's priority.

* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> 1.0004-1
- Initial packaging.
