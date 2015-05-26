#!/usr/bin/perl

$_ = " He’ s out bowling with Barney tonight." ;
s/Barney/Fred/; #Barney 被 Fred 替换掉
print " $_\n";

$_ = " green scaly dinosaur";
s/( \w+) (\w+)/$2, $1/; #现在为 " scaly, green dinosaur" ;
print $_."\n";
s/^/huge, /; #现在为 " huge, scaly, green dinosaur"
print $_."\n";
s/,.*een//; # 空替换, 现在为 " huge dinosaur"
print $_."\n";
s/green/red/ ; # 匹配失败, 仍然为 " huge dinosaur"
print $_."\n";
s/ \w+$/($`!)$& /; #现在为 " huge (huge !)dinosaur"
print $_."\n";
s/ \s+(!\W+)/$1 /; #现在为 " huge (huge!) dinosaur "
print $_."\n";
s/huge/gigantic/; # 现在为 " gigantic (huge!) dinosaur"
print $_."\n";

$_ = " fred flintstone " ;
if(s/fred/wilma/){
	print " Successfully replaced fred with w ilma ! \n" ;
}

$_ = "home, sweet home!";
s/home/cave/;
print " $_\n" ; # " cave, sweet cave! " ;

$_ = "home, sweet home!";
s/home/cave/g;
print " $_\n" ; # " cave, sweet cave! " ;

$_ = "      Input   data   \t   may  hav  e   extra   whitespace.   " ;
#s/\s+/ /g; #现在是 " Input data may have extra whitespace."
s%\s+% %g; #现在是 " Input data may have extra whitespace."
print $_."\n";

s/^\s+|\s+$//g; #将开头，结尾的空白去掉
print $_."\n";

# 大小写转换
$_ = " I saw Barney with Fred." ;
s/(fred|barney)/\U$1/gi; #$_ 现在是 " I saw BARNEY with FRED."
print $_."\n";

#$_ = " I saw Barney with Fred." ;
s/(fred|barney)/\L$1/gi; #$_现在是 " I saw barney with fred."
print $_."\n";

#$_ = " I saw Barney with Fred." ;
#s/( \w+) with (\w+)/\U$2 with $1/i; #$1 现在是 " I saw FRED WITH BARNEY."
#\E结束转换
s/( \w+) with (\w+)/\U$2\E with $1/i; #$1 现在是 " I saw FRED with barney."
print $_."\n";

#$_ = " I saw Barney with Fred." ;
s/ (fred|barney)/\u$1/ig; #$_现在是 " I saw FRED with Barney."
print $_."\n";

#$_ = " I saw Barney with Fred." ;
s/(fred|barney)/\u\L$1/ig; #$_现在为 " I saw Fred with Barney. "
print $_."\n";

#$_ = " I saw Barney with Fred." ;
$name="barney";
print " Hello, \L\u$name\E, would you like to play a game?\n";
print $_."\n";


@fields = split /:/, " abc:def:g:h" ; #返回( " abc" , " def" , " g" , " h"
@fields = split /:/, " abc:def::g:h" ; #得到( " abc" , " def" , "" , " g" , " h"
print @fields."\n"; # 数组会强行转换为标量,== scalar @fields
printf ": ".(" %s," x @fields), @fields;
print "\n";


my $x = join " :" , 4, 6, 8, 10, 12; #$x 为 " 4:6:8:10:12"
print $x."\n";

my $y = join " foo" , " bar" ; #得到 " bar"
my @empty; #空数组
my $empty = join " baz " , @empty; #没有元素，因此为空串

my @values = split /:/, $x; #@values 为(4, 6, 8, 10, 12)
my $z =join " - " , @values; #$z 为 " 4- 6- 8- 10- 12"
print $z."\n";

# 9．4 列表上下文中的 m//
$_ = " Hello there, neighbor!" ;
my($first, $second, $third ) =/(\S+) (\S+), (\S+)/;
print " $second is my $third \n ";


$_="I thought you said Fred and <BOLD>Velma</BOLD>, not <BOLD>Wilma</BOLD>";
s#<BOLD>(.*)</BOLD>#$1#g; # 星号是贪婪的，即最大限度匹配
print $_."\n";

$_="I thought you said Fred and <BOLD>Velma</BOLD>, not <BOLD>Wilma</BOLD>";
s#<BOLD>(.*?)</BOLD>#$1#g; #非贪婪的类型是*?
print $_."\n";

