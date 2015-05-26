@echo off
 set aa=a.btx
 call :deal aaa %aa% "c c" ddd eee
 pause>nul
 exit
 :deal
 echo %%0 = %0
 echo %%1 = %1
 echo %%2 = %2
 echo %%3 = %3
 echo %%4 = %4
 echo %%5 = %5