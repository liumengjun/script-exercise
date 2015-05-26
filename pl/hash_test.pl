#!/usr/bin/perl

$family_name{ "fred" } = "flintstone" ;
$family_name{ "barney" } = "rubble" ;

print $family_name{ "fred" };
foreach $person (qw<barney fred>){
	print "I ’ ve heard of $person $family_name{$person}.\n" ;
}

%some_hash = ("foo", 35, "bar", 12.4, 2.5, "hello", "wilma", 1.72e30, "betty", "bye \n");
print %some_hash;
print "\n";

@array_array = %some_hash;
print @array_array;
print "\n";

my %last_name = (
"fred" => "flintstone",
"dino" => undef,
"barney"=> "rubble",
"betty"=> "rubble",
);
# foreach %last_name {
# 	print $_."\n";
# }
my @k = keys %last_name;
# foreach $me (@k) {
# 	print "my name is $me, my last is $last_name{$me}.\n";
# }
foreach (@k) {
	print "my name is $_, my last is $last_name{$_}.\n";
}

my %hash = ("a" =>1, "b"=>2, "c"=>3);
my @k = keys %hash;
my @v = values %hash;
print @k;
print "\n";
print @v;
print "\n";

while (($key, $value) = each %hash){
	print " $key => $value\n" ;
}

foreach $key (sort keys %hash){
	$value =$hash{$key};
	print " $key => $value\n" ;
	#也可以不使用额外的临时变量$value
	#print " $key => $hash{key} \n" ;
}


