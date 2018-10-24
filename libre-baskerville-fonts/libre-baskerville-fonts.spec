%global fontname libre-baskerville
%global fontconf 63-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.0
Release: 2%{?dist}
Summary: Libre Baskerville font designed by Pablo Impallari
Group:   User Interface/X
License: OFL
URL:     https://fonts.google.com/specimen/Libre+Baskerville
Source0: %{name}-%{version}.tar.xz
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Libre Baskerville is a web font optimized for body text (typically 16px.)
It is based on the American Type Founder's Baskerville from 1941, but it
has a taller x-height, wider counters and a little less contrast, that
allow it to work well for reading on-screen.


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
* Wed Jan 11 2017 Dawid Zych <dawid.zych@yandex.com> 1.0-2
- Update fontconfig and it's priority.

* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> 1.0-1
- Initial packaging.
