#!/usr/bin/perl

open CONFIG, "dino";
open CONFIG, "<dino";
open BEDROCK, ">fred";
open LOG, ">>logfile";

$done=10;
$total=100;

print LOG "Captain’s log, stardate 3.14159\n"; #输出到 LOG 中
printf STDERR "%D percent complete. \n", $done/$total * 100;

printf (STDERR "%d percent complete.\n", $done/$total * 100);
printf STDERR ("%d percent complete.\n", $done/$total * 100);

select BEDROCK;
print "I hope Mr. Slate doesn’t find out about this.\n";
print "Wilma! \n";