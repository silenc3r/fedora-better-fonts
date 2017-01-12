# Better fonts for Fedora
This repository provides libraries that enable subpixel font rendering and
provide substitutions for popular Microsoft fonts on Fedora

COPR repository: https://copr.fedorainfracloud.org/coprs/dawid/better_fonts/

# Installation instructons:

- enable RPM Fusion repository:  
    `su -c 'dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm'`  

- enable COPR repository with packages from this repo:  
    `dnf copr dawid enable dawid/better_fonts`  

- install packages:  
    dnf install fontconfig-enhanced-defaults fontconfig-font-replacements  

- log out and log in again or restart computer to see the effect  
