#!/usr/bin/perl
sub sum_of_fred_and_barney{
	#print "Hey,you called the sum_of_fred_and_barney subroutine!\n";
	$fred+$barney;#返回值
}
$fred=3;$barney=4;
$wilma=&sum_of_fred_and_barney;
#$wilma得到7
print "\$wilma is $wilma.\n";
$betty=3*&sum_of_fred_and_barney;#$betty得到21
print "\n$bettyis$betty.\n";


sub max{
	#和&larger_of_fred_or_barney比较
	if($_[0]>$_[1]){
		$_[0];
	}else{
		$_[1];
	}
}

print &max(12,23)."\n";
print &max(12,5,23)."\n";
