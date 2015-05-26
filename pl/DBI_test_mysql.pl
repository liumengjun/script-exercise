#! /usr/bin/perl

use DBI;

my $dbh= DBI->connect('DBI:mysql:database=test;host=127.0.0.1', 'root', 'lmj') 
    or die "unable to connect $DBI::errstr";

$sth = $dbh->prepare("SELECT * FROM test WHERE 1");
$rows = $sth->execute( );
$numRows = $sth->rows;
$numFields = $sth->{'NUM_OF_FIELDS'};
print "numRows $numRows, numFields $numFields\n";

foreach $colno (0..$sth->{NUM_OF_FIELDS}-1) {
	print $sth->{NAME}->[$colno]."\t  ";
}
print "\n";

#@row_ary = $sth->fetchrow_array;
while (my @row_ary = $sth->fetchrow_array) {
	printf "".("%-8s  " x @row_ary)."\n", @row_ary;
}

# while (my $row_as_map = $sth->fetchrow_hashref()) {
# 	while (($key, $value) = each $row_as_map){
# 		print "$key => $value, ";
# 	}
# 	print "\n";
# }

$sth->finish;

$dbh->disconnect( );