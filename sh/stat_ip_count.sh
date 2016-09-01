#!/bin/sh
# statistics the count of each ip in the file "apache access.log"

# set log file name
access_log=$1
if [ "$access_log" = "" ]; then
	echo -n "Enter the log file name:"
	read access_log
fi

## 先以-为分割符 分割文件获取第一列，然后排序，然后统计
cut -d- -f1 $access_log | sort | uniq -c

