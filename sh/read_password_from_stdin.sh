#!/bin/sh
#getopt1

usage() {
	echo "Usage: `basename $0` -u user -p password -f filename"
	echo "Usage: -h for this help"
	exit 1
}
if [ $# = 0 ]; then
	usage
fi
# set the vars
USER=""
PASSWORD=""
FILE=""
# read vars from argv
while getopts :hu:p:f: OPTION
do
	case $OPTION in
	h) usage
		;;
	u) USER=$OPTARG
		;;
	p) PASSWORD=$OPTARG
		;;
	f) FILE=$OPTARG
		;;
    *) echo "Unimplemented option chosen."
		usage
		;; # 默认情况的处理
	esac
done

getOneChar() {
    stty cbreak -echo
    dd if=/dev/tty bs=1 count=1 2> /dev/null
    stty -cbreak echo
}

readPassword() {
	local str=""
	while : ; do
		local ret=`getOneChar`
		if [ "$ret" =  "" ]; then
			echo
			break
		fi
		str="$str$ret"
		printf "*"
	done
	eval "$1=\"$str\""
}
# check password
_retry_time=0
while [ "" = "$PASSWORD" ]; do
	echo "Please input password:"
	## stty -echo
	## read PASSWORD
	## stty echo
	readPassword PASSWORD
	_retry_time=$((_retry_time+1))
	if [ $_retry_time -ge 3 ]; then
		echo "error!"
		exit 255
	fi
done

# output the params
echo user is: $USER
echo password is: $PASSWORD
echo file is: $FILE

