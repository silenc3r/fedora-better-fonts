%global fontname eb-garamond
%global fontconf 45-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 0.016
Release: 1%{?dist}
Summary: Free version of Garamond font
Group:   User Interface/X
License: OFL
URL:     http://www.georgduffner.at/ebgaramond/
Source0: https://bitbucket.org/georgd/eb-garamond/downloads/EBGaramond-0.016.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
EB Garamond is a free version of the Garamond types, based on the Designs of
the Berner specimen from 1592. Fonts cover extended latin, greek and cyrillic
scripts in different styles and design sizes. There are also fonts containing
initials based on those found in a 16th century french bible print. The fonts
make heavy use of opentype features for specialities like small caps or
different number styles as well as for imitating renaissance typography.


%prep
%setup -q -n EBGaramond-0.016

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p ttf/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

sed -i 's/\r$//' COPYING

%_font_pkg -f %{fontconf} *.ttf
%license COPYING
%doc Changes README.markdown

%changelog
* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> 0.016-1
- Initial packaging.
