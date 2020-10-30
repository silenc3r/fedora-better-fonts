# Better fonts for Fedora
`fontconfig-font-replacements` provides free substitutions for popular
proprietary fonts from Microsoft and Apple operating systems.

It makes your web browsing more aesthetically pleasing - you won't be seeing
DejaVu Sans font on every damn webpage.

Packages from this repository don't change your hinting or antialiasing settings.  
Default for Fedora are slight hinting and grayscale antialiasing.  
Some people find subpixel antialiasing to look better - others can't stand
color fringing caused by it.  If you want to try it for yourself change font
settings in `Gnome Tweaks` or run this command in your terminal:

`dconf write /org/gnome/settings-daemon/plugins/xsettings/antialiasing "'rgba'"`

to change back to grayscale (default) antialiasing:

`dconf write /org/gnome/settings-daemon/plugins/xsettings/antialiasing "'grayscale'"`


COPR repository: https://copr.fedorainfracloud.org/coprs/dawid/better_fonts/

## Installation instructons

1. Enable COPR repository:  
    `sudo dnf copr enable dawid/better_fonts -y`  
2. Install packages:  
    `sudo dnf install fontconfig-font-replacements -y`  
3. Log out and log in again or restart computer to see the effect  

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
