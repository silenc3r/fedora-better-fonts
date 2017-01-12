# Better fonts for Fedora
This repository provides libraries that enable subpixel font rendering and
provide substitutions for popular Microsoft fonts on Fedora.

COPR repository: https://copr.fedorainfracloud.org/coprs/dawid/better_fonts/

## Installation instructons

1. Enable RPM Fusion repository:  
    `su -c 'dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm'`  
2. Enable COPR repository with packages from this repo:  
    `dnf copr enable dawid/better_fonts`  
3. Install packages:  
    `dnf install fontconfig-enhanced-defaults fontconfig-font-replacements`  
4. Log out and log in again or restart computer to see the effect  
