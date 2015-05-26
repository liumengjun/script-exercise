#############################################
#!/bin/ksh
#该段脚本实现输入密码并且用*号显示输入字符，
#输入回车键终止输入密码。该代码在SCO 5.05上
#KSH下已经调试通过。
#河南 平顶山 王向宇    2005.05.11
#############################################

#该函数实现无缓冲输入一个字符，并传给位置参数$1
getchar()
{
        #设置无缓冲输入模式
        stty raw
        #设置输入不回显
        stty -echo
        #将该字符传送给位置参数$1
        eval $1=`dd if=/dev/tty bs=1 count=1 2> /dev/null`
        #恢复回显
        stty echo
        #恢复原终端输入模式,也可用命令:stty sane实现同样功能
        stty cooked
}
clear
#将光标定位到15行10列
#tput cup 15 10
echo -n "请输入密码:\c"
#初始化光标位置
CURPOS=20
while true
do
        #光标向前移动一列
        CURPOS=`expr ${CURPOS} + 1`
        getchar char
        #tput cup 15 ${CURPOS}
        echo "*"
        if [ "${char}"  = "^M" ]
        then
                break
        else
                PWDSTR=${PWDSTR}${char}
        fi
done
echo "你输入的密码是: ${PWDSTR}"