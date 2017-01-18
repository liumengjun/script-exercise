#!/bin/sh
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
jot -r -c $n 33 126 | rs -g 0 $n
