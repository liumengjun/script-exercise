awk 'BEGIN {print "Conversion Format =", CONVFMT }'
awk 'BEGIN {print ENVIRON["USER"] }'
awk 'END {print FILENAME}' marks.txt
awk 'BEGIN {print "OFMT =", OFMT }'
awk 'BEGIN {print "OFS =", OFS }' | cat -etv
awk 'BEGIN {print "ORS =", ORS }' | cat -etv
awk 'BEGIN {print "RS =", RS }' | cat -etv
awk 'BEGIN { if (match("one two three", "re")) {print RLENGTH} }'
awk 'BEGIN { if (match("one two three", ".*re")) {print RLENGTH} }'
awk 'BEGIN { if (match("one two three", "re")) {print RSTART} }'
