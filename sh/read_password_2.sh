#!/bin/sh

getonechar() {
    stty cbreak -echo
    dd if=/dev/tty bs=1 count=1 2> /dev/null
    stty -cbreak echo
}

printf "Please input your passwd: "

while : ; do
    ret=`getonechar`
    if [ x$ret =  x ]; then
        echo
        break
    fi
    str="$str$ret"
    printf "*"
done

echo "Your password is: $str"