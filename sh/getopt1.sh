#!/bin/sh
#getopt1

# set the vars
ALL=false
HELP=false
FILE=false
VERBOSE=false
COPIS=0   # the value for the -c options is set to zero

while getopts :ahfgvc: OPTION
do
	case $OPTION in
	a)ALL=true
		echo "ALL is $ALL"
		;;
	h)HELP=true
		echo "HELP is $HELP"
		;;
	f)FILE=true
		echo "FILE is $FILE"
		;;
	v)VERBOSE=true
		echo "VERBOSE is $VERBOSE"
		;;
	c)COPIES=$OPTARG
		echo "COPIES is $COPIES"
		;;
	\?)   #usage statement
		echo "`basename $0` -[a h f v] -[c value] file" >&2
		exit
		;;
    * ) echo "Unimplemented option chosen."
		exit
		;; # 默认情况的处理
	esac
done

