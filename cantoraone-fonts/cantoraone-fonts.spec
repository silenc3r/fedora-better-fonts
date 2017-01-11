%global fontname cantoraone
%global fontconf 63-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.1
Release: 2%{?dist}
Summary: Cantora is a friendly semi formal, semi condensed, semi sans serif

License: OFL
URL:     http://www.impallari.com
Source0: http://www.impallari.com/media/uploads/prosources/update-67-source.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Cantora ('Singer' in Spanish) is a friendly semi formal, semi condensed, semi
sans serif. It has reminiscences of hand lettering, mixing straight and bowed
stems, and natural curves.

%prep
%setup -q -c
cp CantoraOne-v%{version}/{*.ttf,*.txt} .

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

cp OFL.txt LICENSE
for _file in FONTLOG.txt LICENSE; do
    chmod 0644 $_file
    sed -i 's/\r$//' $_file
done

%_font_pkg -f %{fontconf} *.ttf
%license LICENSE
%doc FONTLOG.txt

%changelog
* Wed Jan 11 2017 Dawid Zych <dawid.zych@yandex.com> - 1.1-2
- Update fontconfig and it's priority.

* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 1.1-1
- Initial packaging.
