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

if(/yes|y/i) {#��Сд�޹�
print " In that case, I recommend that you go bowling.\n" ;
}

# Perl �У�ע�Ϳ��Ա���Ϊ�հף����ʹ��/x��������ģʽ�м���ע�ͣ�
/
- ? #��ѡ�ĸ���
\d+ #С����ǰһ������ʮ��������
\. ? #��ѡ��С����
\d* #С�����һЩ��ѡ��ʮ��������
/x; #ģʽ����

my $some_other = " I dream of betty rubble. " ;
if($some_other =~ /\brub/){
	print " Aye, there' s the rub.\n" ;
}

my $what = "larry" ;
print ":";
while(<>){
	if(/^($what)/){ #���ַ���ǰ�����ƥ��
		print " We saw $what in beginning of $_" ;
	}
	print ":";
}
print "\n";

$_ = "Hello there, neighbor";
if(/\s(\w+),/){ #�ո�Ͷ���֮��Ĵ�
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
	print "That said '$1' years.\n"; # �մ�
}
print "\n";


if("Hello there, neigbor"=~ / \S(\w+),/){
	print " That actually matched ' $&' . \n" ;
}

if ( " Hello there, neighbor" =~ /\S(\w+),/){
	print " That was ($`)($&)($') " ;
}