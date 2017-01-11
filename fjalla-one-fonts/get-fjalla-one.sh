#!/bin/bash
# Get upstream zip and make source tar.gz

ARCHIVE="fjalla-one-fonts-1.001"
TMPDIR=$(mktemp -d --tmpdir=/var/tmp getfjallaone-XXXXXXXXXX)
[ $? != 0 ] && exit 1
umask 022
pushd "$TMPDIR"

wget -N -O $ARCHIVE.zip https://fonts.google.com/download?family=Fjalla%20One
unzip $ARCHIVE.zip -d $ARCHIVE
tar -cvJf "$ARCHIVE.tar.xz" $ARCHIVE

popd
mv "$TMPDIR/$ARCHIVE.tar.xz" .
rm -fr "$TMPDIR"
