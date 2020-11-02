# SPDX-License-Identifier: MIT
%global forgeurl https://github.com/impallari/Libre-Baskerville
%global commit   2fba7c8e0a8f53f86efd3d81bc4c63674b0c613f
%forgemeta

Version: 1.000
Release: 1%{?dist}
Epoch:   1
URL:     %{forgeurl}

%global foundry       Impallari
%global fontlicense   OFL
%global fontlicenses  OFL.txt
%global fontdocs      *txt *md
%global fontdocsex    %{fontlicenses}

%global fontfamily    Libre Baskerville
%global fontsummary   Libre Baskerville is a webfont family optimized for body text
%global fonts         *ttf
%global fontconfs     %{SOURCE10}
%global fontpkgheader %{expand:
Provides:  libre-baskerville-fonts
Obsoletes: libre-baskerville-fonts < %{epoch}:%{version}-%{release}
}
%global fontdescription %{expand:
Libre Baskerville is a webfont family optimized for body text. It is
Based on 1941 ATF Baskerville Specimens but it has a taller x-height,
wider counters and less contrast that allow it to work on small sizes in
any screen.

Libre Baskerville characters set covers 103 Latin languages.}
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
* Mon Nov 02 2020 Dawid Zych <dawid.zych@yandex.com> - 1:1.000-1
- Initial packaging
