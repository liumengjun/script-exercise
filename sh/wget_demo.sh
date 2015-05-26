#!/usr/bin

# set env and param
LOGIN_SERVER=http://passport.ablesky-a.com:8080/as-passport
MAIN_SERVER=http://www.ablesky-a.com:8080
USERNAMEADM=admin
PASSWORD0=1234
PASSWORDADM=`echo -n $PASSWORD0 | md5sum | cut -d ' ' -f1`

LOGINFILE=login$USERNAMEADM.out
wget $LOGIN_SERVER/login.do --post-data "ajax=true&jsonp=ablesky_1418717839329&isPopUp=false&j_username=$USERNAMEADM&j_password=$PASSWORDADM&_acegi_save_account=on&_acegi_security_remember_me=off&_=$RANDOM" --load-cookies cookies.txt --save-cookies cookies.txt --keep-session-cookies --referer "$MAIN_SERVER" -q -O $LOGINFILE
#rm $LOGINFILE


USERNAME=mliu_test002
REQ_OUT_FILE=loadStudyCenter_$USERNAME.txt
wget $MAIN_SERVER/upgrade.do  --post-data "action=loadStudyCenterByUserName&userName=$USERNAME&_dc=$RANDOM" --load-cookies cookies.txt --save-cookies cookies.txt --keep-session-cookies --referer "http://www.ablesky-a.com:8080/" -q -O $REQ_OUT_FILE
