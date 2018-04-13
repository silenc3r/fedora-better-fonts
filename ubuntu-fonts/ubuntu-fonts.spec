%global fontname ubuntu
%global fontconf 61-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 0.83
Release: 1%{?dist}
Summary: Ubuntu font family

License: Ubuntu Font Licence 1.0
URL:     http://font.ubuntu.com/
Source0: http://font.ubuntu.com/download/ubuntu-font-family-0.83.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
The new Ubuntu Font Family was started to enable the personality of Ubuntu
to be seen and felt in every menu, button and dialog. The typeface is
sans-serif, uses OpenType features and is manually hinted for clarity on
desktop and mobile computing screens.

%prep
%setup -q -n ubuntu-font-family-%{version}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg -f *-%{fontname}.conf *.ttf
%license LICENCE.txt LICENCE-FAQ.txt copyright.txt TRADEMARKS.txt
%doc CONTRIBUTING.txt FONTLOG.txt README.txt

%changelog
* Fri Jan 06 2017 Dawid Zych <dawid.zych@yandex.com> - 0.83-1
- Initial packaging.
