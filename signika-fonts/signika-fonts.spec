%global fontname    signika
%global fontconf    45-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.0001
Release: 1%{?dist}
Summary: Sans-serif font with a gentle character

Group:   User Interface/X
License: OFL
URL:     http://fontfabric.com/signika-font/
Source0: http://www.fontfabric.com/downfont/signika.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Signika is a sans-serif with a gentle character, developed
for wayfinding, signage, and other media where clarity of
information is required. It has a low contrast and tall x-height
to improve readability of texts in small sizes as well as in
large distances from the reader. Being a typical signage
typeface it is inspired by typefaces such as Ronnia, Meta
and Tahoma.


%prep
%setup -q -c
cp -p Signika/*.ttf .
# cp -p Signika_Negative/*.ttf .
cp -p Signika/OFL.txt LICENSE

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

sed -i 's/\r$//' LICENSE

%_font_pkg -f %{fontconf} *.ttf
%license LICENSE

%changelog
* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> 1.0001-1
- Initial packaging.
