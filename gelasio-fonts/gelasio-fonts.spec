%global fontname gelasio
%global fontconf 45-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.0
Release: 1%{?dist}
Summary: Gelasio serif family by Eben Sorkin

Group:   User Interface/X
License: OFL
URL:     www.sorkintype.com
Source0: https://fontlibrary.org/assets/downloads/gelasio/4d610887ff4d445cbc639aae7828d139/gelasio.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Gelasio is designed to be metrics compatible with Georgia. Gelasio is
a "Reale" or Transitional design with many style cues coming from the
period immediately after the Romain du Roi type was introduced. Despite
sharing common letter widths the texture and feeling of the two typefaces
are different. Georgia is warmer and friendlier while Gelasio is cooler
and more formal.

%prep
%setup -q -c

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

%_font_pkg -f %{fontconf} *.ttf

%changelog
* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 1.0-1
- Initial packaging.
