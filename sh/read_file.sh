#!/bin/bash
FILENAME="$1"

if [ "" = "$FILENAME" ]; then
	echo "please give one file name!"
	exit
fi

echo "read $FILENAME begin:"

i=0
while read LINE
do
	echo $LINE
	let i=i+1
	if [ $i -ge 10 ]; then
		break
	fi
done < $FILENAME

echo "$FILENAME end"