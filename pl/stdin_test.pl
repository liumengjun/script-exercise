#!/usr/bin/perl

# while(<STDIN>){
# 	print "I saw $_";
# }

while(<>){
	print "I saw $_";
}

my @items = qw( wilma dino pebbles );
my $format = "The items are:\n" . ("%10s\n" x @items);
## print "the format is >>$format<<\n"; #ÓÃÓÚµ÷ÊÔ
printf $format, @items;


if(!open PASSWD, "/etc/passwd"){
	die "How did you get logged in?($!)";
}
while(<PASSWD>){
	chomp;
	print $_."\n";
}