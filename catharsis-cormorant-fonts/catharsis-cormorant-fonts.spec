# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/CatharsisFonts/Cormorant
%global commit      3f27825ce7aa990dc65761a7b323b92aecc84446
%forgemeta

Version: 3.604
Release: 2%{?dist}.better_fonts
URL:     https://www.behance.net/gallery/28579883/Cormorant-an-open-source-display-font-family

%global foundry           Catharsis Fonts
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global common_description %{expand:
Cormorant is an original design for an extravagant display serif font family
inspired by the Garamond heritage, hand-drawn and produced by Catharsis Fonts.
While traditional Garamond cuts make for exquisite reading at book sizes, they
appear clumpy and inelegant at larger sizes. The design goal of Cormorant was
to distill the aesthetic essence of Garamond, unfetter it from the limitations
of metal printing, and allow it to bloom into its natural refined form at high
definition.

Cormorant is characterized by scandalously small counters, razor-sharp serifs,
dangerously smooth curves, and flamboyantly tall accents. While many
implementations of Garamond at small optical sizes already exist (including the
open-sourced EB Garamond by Georg Duffner), Cormorant aims for the sparsely
populated niche of display-size counterparts that exploit the high resolution
of contemporary screens and print media to the fullest.

Cormorant is made for large sizes; the larger, the better. However, it works
well as a text face in high-resolution environments.

Cormorant is a native 21st-century typeface making ample use of OpenType
technology. Some OpenType features are applied automatically while you type,
subtly improving the flow of the text. This includes kerning, standard
ligatures, and contextual alternates. Other features are intended to be
activated manually by the user, such as discretionary ligatures, stylistic
alternates, small capitals, and alternate figure sets.}

%global fontfamily0       Cormorant
%global fontsummary0      Cormorant, a display serif font family inspired by the Garamond heritage
%global fonts0            2.*OpenType*Files/*otf
%global fontsex0          2.*OpenType*Files/CormorantSC*.otf %{fonts1} %{fonts2} %{fonts3} %{fonts4}
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}
}

%global fontfamily1       Cormorant Garamond
%global fontsummary1      Cormorant Garamond, a variant with more traditional shapes
%global fontpkgheader1    %{expand:
Suggests: font(cormorant)
}
%global fonts1            2.*OpenType*Files/CormorantGaramond*.otf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

While Cormorant’s quality is most evident in titling and poster usage at the
largest sizes, its Garamond genome renders it highly legible down to text sizes
on high-resolution devices and in print. This is particularly true about the
“Cormorant Garamond” cuts of the typeface.

Cormorant Garamond offers larger counters and subtly more traditional Garamond
shapes for a few key characters to achieve more reading comfort.}

%global fontfamily2       Cormorant Infant
%global fontsummary2      Cormorant Infant, a gentle schoolbook-style variant
%global fontpkgheader2    %{expand:
Suggests: font(cormorant)
}
%global fonts2            2.*OpenType*Files/CormorantInfant*.otf
%global fontconfngs2      %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

In Cormorant Infant, the letters “a g y” and their derivatives are replaced
by gentle schoolbook-style single-storey shapes.}

%global fontfamily3       Cormorant Upright
%global fontpkgname3      catharsis-cormorant-upright-fonts
%global fontsummary3      Cormorant Upright, an un-slanted cursive variant
%global fontpkgheader3    %{expand:
Suggests: font(cormorant)
}
%global fonts3            2.*OpenType*Files/CormorantUpright*.otf
%global fontconfngs3      %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

Cormorant Upright is an un-slanted cursive of the main Cormorant font family.}

%global fontfamily4       Cormorant Unicase
%global fontsummary4      Cormorant Unicase, a small-caps variant with some lowercase letter-forms
%global fontpkgheader4    %{expand:
Suggests: font(cormorant)
}
%global fonts4            2.*OpenType*Files/CormorantUnicase*.otf
%global fontconfngs4      %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}

Cormorant Unicase, is a small-caps variant with some lowercase letter-forms for
an eye-catching futuristic look.}

%fontmeta

%global source_files %{expand:
Source0:  %{forgesource}
Source10: 57-%{fontpkgname0}.xml
Source11: 57-%{fontpkgname1}.xml
Source12: 58-%{fontpkgname2}.xml
Source13: 60-%{fontpkgname3}.xml
Source14: 60-%{fontpkgname4}.xml
}

%fontpkg

%fontmetapkg

%new_package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

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
%doc 5.*Specimens*Test*Files/*pdf

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.604-1.20200422git3f27825
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.602-4.20200215git83d1fa9
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.602-3.20200215git83d1fa9
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.602-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 3.602-1.20191209git83d1fa9
✅ Initial packaging
