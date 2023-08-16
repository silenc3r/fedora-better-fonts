# Better fonts for Fedora
`fontconfig-font-replacements` provides free substitutions for popular
proprietary fonts from Microsoft and Apple operating systems.

It makes your web browsing more aesthetically pleasing - you won't be seeing
DejaVu Sans font on every damn webpage.

#### Subpixel (rgb) antialiasing
Default for Fedora are slight hinting and grayscale antialiasing.  
Some people find subpixel antialiasing to look better - others can't stand
color fringing caused by it. If you want to try it for yourself install
`fontconfig-enhanced-defaults` package. You can also enable it manually
in `Gnome Tweaks` or by running following command in terminal:

`dconf write /org/gnome/settings-daemon/plugins/xsettings/antialiasing "'rgba'"`

to change back to grayscale (default) antialiasing:

`dconf write /org/gnome/settings-daemon/plugins/xsettings/antialiasing "'grayscale'"`


COPR repository: https://copr.fedorainfracloud.org/coprs/hyperreal/better_fonts/

## Installation instructons

On `rpm-ostree` based distros, replace `dnf` with `rpm-ostree`.

1. Enable COPR repository:  
    `sudo dnf copr enable hyperreal/better_fonts -y`  
   Or on immutable variants (e.g. Silverblue):  
    ```
    . /etc/os-release
    wget https://copr.fedorainfracloud.org/coprs/hyperreal/better_fonts/repo/fedora-$VERSION_ID/hyperreal-better_fonts-fedora-$VERSION_ID.repo -O /tmp/copr_fonts.repo   
    sudo mv /tmp/copr_fonts.repo /etc/yum.repos.d/better_fonts_fedora.repo   
    ```
2. Install packages:  
    `sudo dnf install fontconfig-font-replacements -y`  
3. (Optional) Enable subpixel (rgb) antialiasing:  
    `sudo dnf install fontconfig-enhanced-defaults -y`  
4. Log out and log in again or restart computer to see the effect  

## Screenshots
(probably outdated)

Before | After
-------|------
[Default fonts before](http://i.imgur.com/KOP6CDf.png) | [Default fonts after](http://i.imgur.com/RZXwkar.png)
[Facebook before](http://i.imgur.com/D5RJrvH.png) | [Facebook after](http://i.imgur.com/jmT0efu.png)
[Flask before](http://i.imgur.com/nEgNh81.png) | [Flask after](http://i.imgur.com/zKfIUEr.png)
[LWN.net before](http://i.imgur.com/eA9LMz1.png) | [LWN.net after](http://i.imgur.com/Yk6W1fa.png)
[NY Times before](http://i.imgur.com/jK0NqA8.png) | [NY Times after](http://i.imgur.com/kAuUv34.png)
[Reddit before](http://i.imgur.com/br7smlN.png) | [Reddit after](http://i.imgur.com/K23nauA.png)
[Wikipedia before](http://i.imgur.com/GnDv0np.png) | [Wikipedia after](http://i.imgur.com/QFdNfhd.png)

## Building locally

Check [build_instructions](build_instructions.md)
