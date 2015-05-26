#!/bin/sh
# opt
usage()
{
echo "usage:`basename $0` start|stop process name"
}
OPT=$1
PROCESSID=$2
if [ $# -ne 2 ]
then
  usage
  exit 1
fi
case $OPT in
start|Start) echo "Starting... $PROCESSID"
	# some process to go here
	;;
stop|Stop) echo "Stopping... $PROCESSID"
  # some process to go here
  ;;
*) usage
  ;;
esac

