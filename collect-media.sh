#!/bin/bash

#Based on https://gist.github.com/sfan5/6351560

###### Options ######
MEDIADIR=m

die () {
	echo "$1" >&2
	exit 1
}

collect_from () {
	find -L "$1" -type f -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.ogg" -o -name "*.x" -o -name "*.b3d" -o -name "*.obj" | while read f; do
		basename "$f"
		hash=`openssl dgst -sha1 <"$f" | cut -d " " -f 2`
		mv "$f" $MEDIADIR/$hash
	done
}

which openssl &>/dev/null || die "OpenSSL not installed."

mkdir -p $MEDIADIR

while read "p"; do
	echo "Loading and Extracting: $p"
	mkdir -p tmp
  curl -L --retry 2 --retry-delay 60 "$p" > download.zip
	unzip -qn download.zip -d tmp
	# For special cases saving perms in zip files:
	chmod -R +rwx tmp
	collect_from tmp
	rm download.zip
	rm -rf tmp
done < sources.txt

echo "done"
