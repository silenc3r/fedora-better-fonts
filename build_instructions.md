# Build instructions

Download source packages:

    spectool -g *.spec

... or if `get-font-name.sh` script exists:

    ./get-font-name.sh

Build package locally:

    fedpkg mockbuild --release f29

Build in copr:

    copr build repo_name package_name.src.rpm


# Useful commands

Check installed fonts:

    rpm -q --whatrequires fontpackages-filesystem

Check what font is matched with given name:

    fc-match font-name

Get font information:

    otfinfo --info fontname.ttf

Some fonts may not work because of FsType bit

    ttembed -n fontname.ttf  # to check
    ttembed fontname.ttf  # to reset
