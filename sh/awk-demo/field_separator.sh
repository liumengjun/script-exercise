awk 'BEGIN {print "FS = " FS}' | cat -vte
awk -F , 'BEGIN {print "FS = " FS}' | cat -vte
