%global fontname    courier-prime
%global fontconf    61-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 1.203
Release: 2%{?dist}
Summary: A free, improved, classical monospaced typeface

Group:   User Interface/X
License: OFL
URL:     http://quoteunquoteapps.com/courierprime/
Source0: http://quoteunquoteapps.com/downloads/courier-prime.zip
Source1: %{fontname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

%description
Courier Prime is a TrueType monospaced font designed specifically
for screenplays. It was designed by Alan Dague-Greene for John August
and released by Quote-Unquote Apps under the SIL Open Font License (OFL).


%prep
%setup -q -c
cp -p 'Courier Prime'/*.ttf .
cp -p 'Courier Prime'/LICENSE/OFL.txt LICENSE
cp -p 'Courier Prime'/LICENSE/OFL-FAQ.txt LICENSE-FAQ
cp -p 'Courier Prime'/'Read me.txt' .


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

sed -i 's/\r$//' LICENSE-FAQ

%_font_pkg -f %{fontconf} *.ttf
%license LICENSE LICENSE-FAQ
%doc "Read me.txt"

%changelog
* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 1.203-2
- Update fontconfig and it's priority

* Thu Jan 05 2017 Dawid Zych <dawid.zych@yandex.com> - 1.203-1
- Initial packaging.
