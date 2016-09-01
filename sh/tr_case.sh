#!/bin/sh
#tr_case
# case conversion
usage() {
	echo "usage:`basename $0` -[l|u] file [files]" >&2
	exit 1
}
if [ $# -eq 0 ] ; then
	# no parameters passed
	usage
fi

while [ $# -gt 0 ]
do
  case $1 in
  -u|-U) echo "-u option specified"
    # do any settings of variables here for lowercase then shift
    shift
    	;;
	-l|-L) echo "-l option specified"
  	# do any settings of variables here for uppercase then shift
  	shift
  		;;
	-*) usage
		;;
	*)   if [ -f $1 ]; then
				FILES=$FILES" " $1 #assign the filenames to a variable
			 else
			 	echo "`basename $0` cannot find file $1"
			 fi
		shift
		;;
	esac
done

