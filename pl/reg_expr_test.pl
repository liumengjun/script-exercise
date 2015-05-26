#!/usr/bin/perl

$_ = " yabba dabba doo" ;
if(/abba/){
	print " It matched!\n" ;
}

if(m(abba)){
	print " It matched!\n" ;
}

print " Would you like to play a game? " ;
chomp($_ = <STDIN>);

if(/yes|y/i) {#大小写无关
print " In that case, I recommend that you go bowling.\n" ;
}

# Perl 中，注释可以被作为空白，因此使用/x，可以在模式中加上注释：
/
- ? #可选的负号
\d+ #小数点前一个或多个十进制数字
\. ? #可选的小数点
\d* #小数点后一些可选的十进制数字
/x; #模式结束

my $some_other = " I dream of betty rubble. " ;
if($some_other =~ /\brub/){
	print " Aye, there' s the rub.\n" ;
}

my $what = "larry" ;
print ":";
while(<>){
	if(/^($what)/){ #在字符串前面进行匹配
		print " We saw $what in beginning of $_" ;
	}
	print ":";
}
print "\n";

$_ = "Hello there, neighbor";
if(/\s(\w+),/){ #空格和逗号之间的词
	print " the word was $1\n" ; #the word was there
}
print "\n";

$_ = " Hello there, neighbor" ;
if(/(\S+) (\S+), (\S+)/){
	print " words were $1 $2 $3" ;
}
print "\n";


my $dino = "I fear that I'll be extinct after 1000 years.";
if ($dino =~ /(\d*) years/) {
	print "That said '$1' years. \n"; # 1000
}
print "\n";

my $dino = "I fear that I'll be extinct after a few millions years.";
if ($dino =~ /(\d*) years/) {
	print "That said '$1' years.\n"; # 空串
}
print "\n";


if("Hello there, neigbor"=~ / \S(\w+),/){
	print " That actually matched ' $&' . \n" ;
}

if ( " Hello there, neighbor" =~ /\S(\w+),/){
	print " That was ($`)($&)($') " ;
}