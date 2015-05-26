#!/usr/bin/perl


chdir "/etc2" or print "cannot chdir to /etc2: $!";
print"\n";

foreach $args (@ARGV){
	print "one arg is $args\n";
}

my @all_files = glob "*";
my @perl_files = glob "*.pl";


# 下面printf语句的前导字符串"".不能省略
printf "".("%s, " x @all_files)."\n",  @all_files;
print"\n";
# printf "".("%s, " x @perl_files)."\n",  @perl_files;
# print"\n";

# Perl 自身有六个文件句柄： STDIN， STDOUT， STDERR， DATA， ARGV， ARGVOUT◆。 虽然可以任意给文件句柄命名，但不能选择上面六个， 除非你想利用它们的某些特殊性质◆。

my @all_files = <*>; ##基本上同@all_files = glob "*"一样；
printf "".("%s, " x @all_files)."\n",  @all_files;
print"\n";

my $dir = "/etc";
my @dir_files = <$dir/* $dir/.*>;
printf "".("%s, " x @dir_files)."\n",  @dir_files;
print"\n";

my @files = <FRED/*>; ##glob
my @lines = <FRED>; ##文件句柄读入
my $name = "FRED";
my @files = <$name/*>; ##glob
my @lines = <$name>; ##间接的文件句柄读入操作
my $name = "FRED";
my @lines = readline FRED; #从 FRED 读入
my @lines = readline $name; #从 FRED 读入


my $dir_to_process = "/etc";
opendir DH, $dir_to_process or die "Cannot open $dir_to_process: $!";
foreach $file(readdir DH) {
	print " file in $dir_to_process is $file\n";
}
closedir DH;










