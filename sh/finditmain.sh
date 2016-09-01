#!/bin/sh 
# finditmain.sh
#
# findit: this is front end for the basic find command 
findit() { 
# findit 
if [ $# -lt 1 ]; then
 echo "usage : findit filename"
 echo "find the files named of filename in the current dir"
 return 1 
fi
find ./ -name $1 -print
}
