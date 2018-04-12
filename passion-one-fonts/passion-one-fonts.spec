%global fontname passion-one
%global fontconf 61-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.001
Release: 1%{?dist}
Summary: Passion One is a set of 3 display fonts aimed to composing titles in big sizes.

Group:   User Interface/X
License: OFL
URL:     https://fonts.google.com/specimen/Passion+One
Source0: https://www.fontsquirrel.com/fonts/download/passion-one.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Passion One is a set of 3 display fonts aimed to composing titles in
big sizes. Its counterforms decrease as the passion increases! Please
use them only for your most passionate thoughts and ideas.

%prep
%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

mv "SIL Open Font License.txt" LICENSE

%_font_pkg -f %{fontconf} *.otf
%license LICENSE

%changelog
* Thu Apr 12 2018 Dawid Zych <dawid.zych@yandex.com> - 1.001-1
- Initial packaging.
