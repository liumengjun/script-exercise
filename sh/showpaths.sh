#!/bin/sh
# showpath.sh: show env path one dir per line
echo $PATH | sed -e 's/:/\
/g'
