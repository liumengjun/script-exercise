awk 'length($0) > 18' marks.txt
echo
awk 'NR < 3' marks.txt
echo
awk 'FNR < 3' marks.txt
echo
awk 'NF >=3' sample.txt
