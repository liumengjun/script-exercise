#!/bin/sh
echo -n "Enter you name:"
read name
if [ "$name" = "" ]; then
	echo "You did not input any thing"
else
	echo "Hello! $name!"
fi

