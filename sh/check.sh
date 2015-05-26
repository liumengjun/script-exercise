# 变量名=值
# declare 变量名=值
# 
# export 变量=值
# declare -x 变量=值

otxadmindebugmode=true
# otxadmin_debug_option_str= 
if [ "$otxadmindebugport" = "" ]; then
	otxadmindebugport="9005"
fi
if [ "$otxadmindebugmode" = "true" ]; then
	otxadmin_debug_option_str="-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=$otxadmindebugport"
fi

echo $otxadmindebugport
echo $otxadmin_debug_option_str

unset otxadmindebugmode
unset otxadmin_debug_option_str
