ifconfig en0 inet | tail -1 | cut -d ' ' -f2
ifconfig en4 inet | tail -1 | cut -d ' ' -f2
ifconfig vboxnet0 inet | tail -1 | cut -d ' ' -f2
# ifconfig vboxnet1 inet | tail -1 | cut -d ' ' -f2
