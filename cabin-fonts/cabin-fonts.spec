%global fontname cabin
%global fontconf 63-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 2.001
Release: 1%{?dist}
Summary: Humanist sans font with 4 weights and true italics

Group:   User Interface/X
License: OFL
URL:     https://fonts.google.com/specimen/Cabin
Source0: %{name}-%{version}.tar.xz
Source1: %{fontname}-fontconfig.conf
Source2: get-%{fontname}.sh

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
The Cabin font family is a humanist sans with 4 weights and true italics,
inspired by Edward Johnston's and Eric Gill's typefaces, with a touch of
modernism. Cabin incorporates modern proportions, optical adjustments, and
some elements of the geometric sans. It remains true to its roots, but has
its own personality. The weight distribution is almost monotone, although
top and bottom curves are slightly thin. Counters of the b, g, p and q are
rounded and optically adjusted. The curved stem endings have a 10 degree
angle. E and F have shorter center arms. M is splashed.

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
* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 2.001-1
- Initial packaging.
