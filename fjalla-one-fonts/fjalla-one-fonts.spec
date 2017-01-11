%global fontname fjalla-one
%global fontconf 61-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.001
Release: 1%{?dist}
Summary: Fjalla One is a medium contrast display sans serif

Group:   User Interface/X
License: OFL
URL:     https://fonts.google.com/specimen/Fjalla+One
Source0: %{name}-%{version}.tar.xz
Source1: %{fontname}-fontconfig.conf
Source2: get-%{fontname}.sh

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Fjalla One is a medium contrast display sans serif. Fjalla One has been
carefully adjusted to the restrictions of the screen. Despite having
display characteristics Fjalla One can be used in a wide range of sizes.

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
* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 1.001-1
- Initial packaging.
