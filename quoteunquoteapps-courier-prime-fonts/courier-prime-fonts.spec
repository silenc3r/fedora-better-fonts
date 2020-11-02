# SPDX-License-Identifier: MIT
%global forgeurl https://github.com/quoteunquoteapps/CourierPrime
%global commit   7fd585a2dd4c1612c79b3308e300923d1c13df93
%forgemeta

Version: 3.018
Release: 1%{?dist}
URL:     https://quoteunquoteapps.com/courierprime/

%global foundry       QuoteUnquoteApps
%global fontlicense   OFL
%global fontlicenses  OFL.txt
%global fontdocs      *txt *md
%global fontdocsex    %{fontlicenses} requirements.txt

%global fontfamily    Courier Prime
%global fontsummary   A free, improved, classical monospaced typeface
%global fonts         fonts/ttf/*ttf
%global fontconfs     %{SOURCE10}
%global fontpkgheader %{expand:
Obsoletes: courier-prime-fonts < %{version}-%{release}
}
%global fontdescription %{expand:
Courier Prime is a new take on IBM's Courier which was designed in 1956
by Howard Kettler.

It is a monospaced family, designed specifically for screenplays. Overall
the family is more refined than its predecessor. The serifs are crisper
and less rounded. The counters are subtly wider. The bold weight is a
bit darker and the italics are more cursive.}


Source0: %{forgesource}
Source10: 61-%{fontpkgname}.conf

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
* Mon Nov 02 2020 Dawid Zych <dawid.zych@yandex.com> - 3.018-1
- Initial packaging
