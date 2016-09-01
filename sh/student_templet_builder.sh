#!/bin/sh

# ***请您按顺序输入学员的用户名、密码、邮箱（选填）、昵称（选填）、电话（选填）***
# ***用户名限定3-20个字符，可由英文、数字及“_”、“-”组成，不能以“_”、“-”开头，不能包含空格***
# ***真实姓名限定1-20个字符，可由英文、数字及“_”、“-”组成，不能以“_”、“-”开头，不能包含空格***
# ***密码限定6-20位字符，必须使用字母、数字或符号的组合***
# ***-----------------------------------------------------------------------------------------***
# ***以下是我们为您提供的两个例子，选填项不填请输入“-”，不同信息请用空格分开，不同学员请换行***
# ***您若自建模板或删除注释信息，必须空出第一行，从文本第二行开始输入创建信息***
# ***您还可以直接从Excel表格中粘贴对应信息到此文本中***
# ***其中***表示注释信息，不列入创建信息***
# 
# ***zhangsan 1234aa zhangsan@ablesky.com 张三 13988888888
# ***lisi 1234aa - - -
# 
# tmp_test_l001 1234aa - - -
# tmp_test_l002 1234aa - - -
# tmp_test_l003 1234aa - - -

prefix="tmp_test_"
start_num=1000
count=10
pawd="1234aa"
if [ "$1" != "" ] ; then
	prefix=$1
fi
echo "*** prefix is: $prefix ***"
if [ "$2" != "" ] ; then
	start_num=$2
fi
echo "*** start num: $start_num ***"
if [ "$3" != "" ] ; then
	count=$3
fi
echo "*** count: $count ***"
if [ "$4" != "" ] ; then
	pawd=$4
fi
echo "*** password is: $pawd ***"

i=0
while [ $i -lt $count ]
do
	#echo $i
	stu_name=$prefix`expr $i + $start_num`
	#echo $stu_name
	echo $stu_name" $pawd $stu_name@a.cn - -"
	i=`expr $i + 1`
done
