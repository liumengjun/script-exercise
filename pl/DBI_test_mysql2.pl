#! /usr/bin/perl

use strict;
#use warnings;
use DBI;

my $dsn = 'DBI:mysql:test:127.0.0.1';#"DBI:mysql:database=test;host=127.0.0.1"
my $username = 'root';
my $password = 'lmj';
my %conn_attrs = (RaiseError => 1, PrintError => 0, AutoCommit => 1);
my $dbh= DBI->connect($dsn, $username, $password, \%conn_attrs) 
    or die "unable to connect $DBI::errstr";

my $sth = $dbh->prepare("SELECT * FROM test WHERE 1");
my $rows = $sth->execute( );
#print $rows;
#print "\n";
my $numRows = $sth->rows;# $sth->rows();
my $numFields = $sth->{'NUM_OF_FIELDS'};
print "numRows $numRows, numFields $numFields\n";

foreach my $colno (0..$sth->{NUM_OF_FIELDS}-1) {
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

print "insert...\n";
#my $sth2 = $dbh->prepare("INSERT INTO test (`name`, `count`) VALUES('hello', RAND()*100)");
#my $ret = $sth2->execute();
#$sth2->finish;
#write like bellow in one row
my $ret = $dbh->do("INSERT INTO test (`name`, `count`) VALUES('hello', RAND()*100)");
print $ret;
print "\n";

print "select again:\t";
$sth = $dbh->prepare("SELECT * FROM test WHERE 1");
my $rows2 = $sth->execute( );
print "numRows $rows2, numFields $sth->{'NUM_OF_FIELDS'}\n";
while (my @row_ary = $sth->fetchrow_array) {
	printf "".("%-8s  " x @row_ary)."\n", @row_ary;
}
$sth->finish;

$dbh->disconnect( );