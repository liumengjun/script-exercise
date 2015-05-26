#!/usr/bin/perl
$line=<STDIN>;
if($line eq "\n"){
	print "That was just a blank line!\n";
}else{
	print "That line of input was: $line";
}

$text="alineoftext\n";#也可以由<STDIN>输入
chomp($text);#去掉换行符(\n)。
print $text;

chomp($text=<STDIN>);#读入，但不含换行符
$text=<STDIN>;chomp($text);#同上，但用两步完成
print $text;

$madonna=<STDIN>;
if(defined($madonna)){
	print "The input was $madonna";
}else{
	print "No input available!\n";
}
