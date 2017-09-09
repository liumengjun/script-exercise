#!/bin/bash

#git show --name-only --oneline
lines=`git show --name-status --oneline`
num=0

#OLDIFS=$IFS;
IFS=$'\n';
for st_file in $lines
do
    num=`expr $num + 1`
    if [ $num -eq 1 ]; then
        continue;
    fi
    echo $st_file;
done
#IFS=$OLDIFS

