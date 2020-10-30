#!/bin/bash
# Get upstream zip and make source tar.gz

ARCHIVE="gelasio-fonts-1.006"
TMPDIR=$(mktemp -d --tmpdir=/var/tmp getgelasio-XXXXXXXXXX)
[ $? != 0 ] && exit 1
umask 022
pushd "$TMPDIR"

wget -N -O $ARCHIVE.zip https://fonts.google.com/download?family=Gelasio
unzip $ARCHIVE.zip -d $ARCHIVE
tar -cvJf "$ARCHIVE.tar.xz" $ARCHIVE

popd
mv "$TMPDIR/$ARCHIVE.tar.xz" .
rm -fr "$TMPDIR"
