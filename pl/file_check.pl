#!/usr/bin/perl

$filename="file_check.pl";

#die "Oops! A file called ‘ $filename’ already exists.\n"
print "Oops! A file called ‘ $filename’ already exists.\n"
if !-e $filename;


warn "Config file is looking pretty old! \n"
if !-M CONFIG > 28;

my ($dev, $ino, $mode, $nlink, $uid, $gid, $rdev, $size, $atime, $mtime, $ctime, $blksize, $blockes)
= stat($filename);

print $dev." ".$ino." ".$mode." ".$nlink." ".$uid." ".$gid." ".$rdev." ".$size." ".$atime." ".$mtime." ".$ctime." ".$blksize." ".$blockes."\n";


my $timestamp = 1180630098;
my $date = localtime $timestamp;
print $date;
print "\n";

my($sec, $min, $hour, $day, $mon, $year, $wday, $yday, $isdst)
= localtime $timestamp;

print $sec." ".$min." ".$hour." ".$day." ".$mon." ".$year." ".$wday." ".$yday." ".$isdst."\n";

print time."\n";
my $now = gmtime; #得到当前的时间
print $now;
print "\n";

