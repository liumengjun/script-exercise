#!/usr/bin/perl

sub max {
	my($m,$n); #新的， 私有变量
	#if(@_!=2){
	#	print "WARNING! &max should get exactly two arguments! \n";
	#}
	($m,$n) = @_; #赋值
	if($m > $n) {$m} else{$n}
}

print &max(12,23,sdf)."\n";


sub max2 {
	my($max_so_far) = shift @_;
	foreach (@_){
		if($_>$max_so_far){
			$max_so_far=$_;
		}
	}
	$max_so_far;
}

print &max2(12,23,3,234,3234,234,234,978)."\n";