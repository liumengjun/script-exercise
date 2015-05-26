#!/usr/bin/perl

use CGI qw(:all);
print header("text/plain");
foreach my $param ( param())
{
	print "$param: ". param($param) . "\n";
}

