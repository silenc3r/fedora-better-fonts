# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/itfoundry/kalam
%global commit      03a4d8a33849b1ad9afdee95006bc66d2d4aed94
%forgemeta

Version: 2.001
Release: 1%{?dist}
URL:     %{forgeurl}

%global foundry         ITF
%global fontlicense     OFL
%global fontdocs        *md

%global fontfamily      Kalam
%global fontsummary     Kalam is a handwriting-style typeface supporting the Devanagari and Latin scripts
%global fonts           build/*otf
%global fontconfs       %{SOURCE10}
%global fontdescription %{expand:
Kalam is a handwriting font family that supports the Devanagari and
Latin writing systems. Even though Kalam's letterforms derive from
handwriting, the fonts have each been optimized for text usage on
screen. All in all, the typeface is a design that feels very personal.
Like many informal handwriting-style fonts, it appears rather fresh and
new when seen on screen or printed on the page.

Kalam's letterforms feature a very steep slant from the top right to the
bottom left. They are similar to letters used in everyday handwriting,
and look like they might have been written with either a thin felt-tip
pen, or a ball-point pen. In the Devanagari letterforms, the
knotted-terminals are open, but some other counter forms are closed.
Features like these strengthen the feeling that text set in this
typeface has been written very quickly, in a rapid manner.}

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

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)

%changelog
* Mon Nov 02 2020 Dawid Zych <dawid.zych@yandex.com> - 2.001-1
- Initial packaging
