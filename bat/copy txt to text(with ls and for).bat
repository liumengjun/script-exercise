@echo off&setlocal EnableDelayedExpansion
set work_path=E:\temp\shell
cd /d %work_path%
rem for /f "skip=0 tokens=* delims= " %%a in ('ls') do (
rem Linux's command: ls
ls>temp.txt

rem the follow [for loop] is bad one
rem for /f "delims=" %%a in (temp.txt) do (
rem 	set filename=%%a
rem 	echo %filename%
rem )

rem the follow [for loop] is right
for /f "delims=" %%a in ('type temp.txt') do (
	set "filename=%%a"
	echo !filename!
)
pause

rem use Linux's command: cat
for /f "delims=" %%a in ('cat temp.txt') do (
	set filename=%%a
	rem set "filename=!filename:bat=sh!"
	set textname=!filename:.txt=.text!
	rem echo !textname!
	if not "!textname!"=="!filename!" (
		rem Linux's command: cp
		cp !filename! !textname!
	)
	echo !textname!
)
pause