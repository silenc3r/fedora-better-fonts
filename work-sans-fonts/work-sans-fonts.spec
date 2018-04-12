%global fontname work-sans
%global fontconf 62-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.6
Release: 1%{?dist}
Summary: Work Sans

Group:   User Interface/X
License: OFL
URL:     https://fonts.google.com/specimen/Work+Sans
Source0: https://github.com/weiweihuanghuang/Work-Sans/archive/v1.6.tar.gz
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Work Sans is a 9 weight typeface family based loosely on early Grotesques
— i.e. Stephenson Blake, Miller & Richard and Bauerschen Giesserei. The
core of the fonts are optimised for on-screen medium-sized text usage
(14px-48px) – but still can be used in print well. The fonts at the extreme
weights are designed more for display use. Overall, features are simplified
and optimised for screen resolutions – for example, diacritic marks are
larger than how they would be in print.

%prep
%setup -q -n Work-Sans-%{version}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/desktop/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

mv LICENSE.txt LICENSE
sed -i 's/\r$//' LICENSE

%_font_pkg -f %{fontconf} *.otf
%attr(0644,root,root) %license LICENSE

%changelog
* Fri Jan 19 2018 Dawid Zych <dawid.zych@yandex.com> - 1.60-1
- Initial packaging.
