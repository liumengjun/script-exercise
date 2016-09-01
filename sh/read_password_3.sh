#!/bin/sh

getonechar() {
    stty cbreak -echo
    dd if=/dev/tty bs=1 count=1 2> /dev/null
    stty -cbreak echo
}

read_password() {
	local str=""
	while : ; do
		local ret=`getonechar`
		if [ "$ret" =  "" ]; then
			echo
			break
		fi
		str="$str$ret"
		printf "*"
	done
	eval "$1=\"$str\""
}

printf "Please input your passwd: "

read_password password

echo "Your password is: $password"