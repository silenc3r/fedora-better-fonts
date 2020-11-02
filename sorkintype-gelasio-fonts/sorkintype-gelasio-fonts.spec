# SPDX-License-Identifier: MIT
%global forgeurl https://github.com/SorkinType/Gelasio
%global commit   c709e349ff6ce37a3381f4eaecef0b5d91d72eae
%forgemeta

Version: 1.006
Release: 2%{?dist}
URL:     %{forgeurl}

%global foundry       SorkinType
%global fontlicense   OFL
%global fontlicenses  OFL.txt
%global fontdocs      *txt *md
%global fontdocsex    %{fontlicenses} requirements.txt

%global fontfamily    Gelasio
%global fontsummary   Gelasio is an original typeface which is metrics compatible with Georgia
%global fonts         fonts/ttf/*ttf fonts/variable/*ttf
%global fontconfs     %{SOURCE10}
%global fontpkgheader %{expand:
Provides:  gelasio-fonts
Obsoletes: gelasio-fonts < %{version}-%{release}
}
%global fontdescription %{expand:
Gelasio is an original typeface which is metrics compatible with Georgia
in its Regular, Bold, Italic and Bold Italic weights. It supports the
Google Fonts Latin Pro glyph set, enabling the typesetting of English,
Western, Eastern and Southern European languages as well as Vietnamese
and 130+ other languages.}

Source0: %{forgesource}
Source10: 60-%{fontpkgname}.conf

%fontpkg

%package doc
Summary: Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shippend with
%{name}.

%prep
%forgesetup
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt

%changelog
* Mon Nov 02 2020 Dawid Zych <dawid.zych@yandex.com> - 1.006-2
- Initial packaging
