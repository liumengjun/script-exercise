#! /usr/bin/perl

use DBI;

my $data_source = "dbi:Pg:dbname=name_of_database";
$dbh = DBI->connect($data_source, $username, $password);

$sth = $dbh->prepare("SELECT * FROM foo WHERE bla");
$sth->execute( );
@row_ary = $sth->fetchrow_array;
$sth->finish;

$dbh->disconnect( );