# Better fonts for Fedora
This repository contains libraries that enable subpixel font rendering and
provide substitutions for popular Microsoft fonts on Fedora.

COPR repository: https://copr.fedorainfracloud.org/coprs/dawid/better_fonts/

## Screenshots
Before | After
-------|------
[Default fonts before](http://i.imgur.com/KOP6CDf.png) | [Default fonts after](http://i.imgur.com/RZXwkar.png)
[Facebook before](http://i.imgur.com/D5RJrvH.png) | [Facebook after](http://i.imgur.com/jmT0efu.png)
[Flask before](http://i.imgur.com/nEgNh81.png) | [Flask after](http://i.imgur.com/zKfIUEr.png)
[LWN.net before](http://i.imgur.com/eA9LMz1.png) | [LWN.net after](http://i.imgur.com/Yk6W1fa.png)
[NY Times before](http://i.imgur.com/jK0NqA8.png) | [NY Times after](http://i.imgur.com/kAuUv34.png)
[Reddit before](http://i.imgur.com/br7smlN.png) | [Reddit after](http://i.imgur.com/K23nauA.png)
[Wikipedia before](http://i.imgur.com/GnDv0np.png) | [Wikipedia after](http://i.imgur.com/QFdNfhd.png)

## Installation instructons

1. Enable COPR repository with packages from this repo:  
    `dnf copr enable dawid/better_fonts`  
2. Install packages:  
    `dnf install fontconfig-enhanced-defaults fontconfig-font-replacements`  
3. Log out and log in again or restart computer to see the effect  

## Building locally

Check [build_instructions](build_instructions.md)
