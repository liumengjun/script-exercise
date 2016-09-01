#!/usr/bin
# product
# LOGIN_SERVER=http://passport.ablesky.com
# MAIN_SERVER=http://web1mb1.bp1.ablesky.com
# USERNAMEADM=adm_qa_liuhj
# password0=135qet

# web1.beta
LOGIN_SERVER=http://passport.beta.ablesky.com
MAIN_SERVER=http://web1.bt1.ablesky.com:8080
USERNAMEADM=adm_web_ztan
password0=1234

timestamp=$(date '+%Y-%m-%d_%H.%M.%S')
echo $timestamp
prifix=temp
LOGFILE=$prifix$timestamp.log
# echo $LOGFILE
PASSWORDADM=`echo -n $password0 | md5sum | cut -d ' ' -f1`
# echo $PASSWORDADM
wget $LOGIN_SERVER/login.do --post-data "ajax=true&jsonp=ablesky_1418717839329&isPopUp=false&j_username=$USERNAMEADM&j_password=$PASSWORDADM&_acegi_save_account=on&_acegi_security_remember_me=off&_=$RANDOM" --load-cookies cookies.txt --save-cookies cookies.txt --keep-session-cookies --referer "$MAIN_SERVER" -q -O $LOGFILE
cat $LOGFILE
# rm $LOGFILE
mkdir $timestamp
mv $LOGFILE $timestamp/

# USERNAME=mliu_test002
# wget $MAIN_SERVER/upgrade.do  --post-data "action=loadStudyCenterByUserName&userName=$USERNAME&_dc=$RANDOM" --load-cookies cookies.txt --save-cookies cookies.txt --keep-session-cookies --referer "http://www.ablesky.com/" -q -O loadStudyCenter_$USERNAME.txt

##!/bin/bash
FILENAME="$1"
batch_count="$2"
start="$3"
limit="$4"

if [ "" = "$FILENAME" ]; then
	echo "please give one file name!"
	exit
fi
if [ "" = "$batch_count" ]; then
	batch_count=50
fi
if [ "" = "$start" ]; then
	start=0
fi
if [ "" = "$limit" ]; then
	limit=0
fi

echo "read $FILENAME begin:"

sentinel=0
time=1
line_num=0
total_count=0
usernames=""
let end=start+limit-1
while read LINE
do
	let line_num=line_num+1
	if [ $line_num -lt $start ]; then
		continue
	fi
	usernames=$usernames,$LINE
	let sentinel=sentinel+1
	let total_count=total_count+1
	if [ $sentinel -ge $batch_count ]; then
		# echo $usernames
		echo 第$time次: count=$sentinel No:$((line_num-sentinel+1))~$line_num usernames=$usernames > $prifix$timestamp"_"$time.req.txt
		output_file=$prifix$timestamp"_"$time.res.txt
		echo $output_file
		# echo "action=loadStudyCenterForUsers&all=true&usernames=$usernames&_dc=$RANDOM"
		wget $MAIN_SERVER/upgrade.do  --post-data "action=loadStudyCenterForUsers&all=true&usernames=$usernames&_dc=$RANDOM" --load-cookies cookies.txt --save-cookies cookies.txt --keep-session-cookies --referer "http://www.ablesky.com/" -q -O $output_file
		cat $output_file
		let sentinel=0
		let time=time+1
		usernames=""
		 sleep 1
	fi
	if [ $limit -gt 0 -a $line_num -ge $end ]; then
		break
	fi
done < $FILENAME

# the last request
if [ $sentinel -gt 0 ]; then
	# echo $usernames
	echo 第$time次: count=$sentinel No:$((line_num-sentinel+1))~$line_num usernames=$usernames > $prifix$timestamp"_"$time.req.txt
	output_file=$prifix$timestamp"_"$time.res.txt
	echo $output_file
	# echo "action=loadStudyCenterForUsers&all=true&usernames=$usernames&_dc=$RANDOM"
	wget $MAIN_SERVER/upgrade.do  --post-data "action=loadStudyCenterForUsers&all=true&usernames=$usernames&_dc=$RANDOM" --load-cookies cookies.txt --save-cookies cookies.txt --keep-session-cookies --referer "http://www.ablesky.com/" -q -O $output_file
	cat $output_file
	let sentinel=0
	let time=time+1
	usernames=""
	 sleep 1
fi

for _tmp in `ls $prifix$timestamp*`
do 
	mv $_tmp $timestamp/
done

echo $((time-1))次提交，总数$total_count
echo "$FILENAME end"