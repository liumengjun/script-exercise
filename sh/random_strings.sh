#!/bin/bash
LC_ALL=C;
# cat /dev/urandom | strings | head
# cat /dev/urandom | sed 's/[^a-zA-Z0-9]//g' | head
#
n=32
# rand_line=`cat /dev/urandom | sed 's/[^a-zA-Z0-9]//g' | strings -n $n | head -1`
# echo ${rand_line:0:n}

cat /dev/urandom | sed 's/[^a-zA-Z0-9]//g' | strings -n $n | head | cut -b 1-$n

