#!/bin/bash
LC_ALL=C;
# cat /dev/urandom | strings | head
# cat /dev/urandom | sed 's/[^a-zA-Z0-9]//g' | head
#
n=32
if [ "$1" != "" ]; then
  expr $1 "+" 10 &> /dev/null
  if [ $? -eq 0 -a $1 -ge 1 -a $1 -le 256 ]; then
    n=$1
  else
    echo "$1 is a wrong number in [1,256]"
    exit -1
  fi
fi
# rand_line=`cat /dev/urandom | sed 's/[^a-zA-Z0-9]//g' | strings -n $n | head -1`
# echo ${rand_line:0:n}

cat /dev/urandom | sed 's/[^a-zA-Z0-9]//g' | strings -n $n | head | cut -b 1-$n

