# !/bin/sh
# scan_port.sh: scan port, host:start~end
if [ "$1" = "" ]; then echo "no host"; exit; fi
if [ "$2" = "" ]; then echo "no start port"; exit; fi
if [ "$3" = "" ]; then echo "no end port"; exit; fi
host="$1"
start="$2"
end="$3"
if [ $start -lt 1 ]; then start=1; fi
if [ $end -lt 1 ]; then end=1; fi
seq $start $end > /dev/null 2>&1
if [ $? != 0 ]; then echo "params error"; exit; fi
for port in `seq $start $end`; do
    # echo $port;
    nc -v -G 2 -w 2 $host $port > /dev/null 2>&1;
    if [ $? = 0 ]; then
        echo "$port is open";
    fi;
done
