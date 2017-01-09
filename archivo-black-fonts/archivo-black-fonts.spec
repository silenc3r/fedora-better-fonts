%global fontname    archivo-black
%global fontconf    45-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.0004
Release: 1%{?dist}
Summary: Grotesque sans-serif typeface family derived from Chivo

Group:   User Interface/X
License: OFL
URL:     http://omnibus-type.com/
Source0: http://omnibus-type.com/download/ArchivoBlack-for-Print.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Archivo from Omnibus-Type is a grotesque sans-serif typeface family
derived from Chivo. Black style.


%prep
%setup -q -n ArchivoBlack-for-Print

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
* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> 1.0004-1
- Initial packaging.
