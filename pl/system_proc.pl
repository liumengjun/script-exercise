#!/usr/bin/perl


system "date";

system 'ls –l $HOME';

my $now = `date`; #捕获 date 的输出
print "The time is now $now"; #已经有换行符

chomp(my $no_newline_now = `date`);
print "A moment ago, it was $no_newline_now, I think. \n";


#开始一个并发（并行） 子进程的语法是将命令作为“文件名 ” 传给 open， 并在其前面或后面加上竖线（ |）， 竖线是“ 管道（pipe）” 符。 基于这些原因， 这通常叫做管道打开（piped open）：
open DATE, "date|" or die "cannot pipe from date: $!";
my $now = <DATE>;
print $now;

