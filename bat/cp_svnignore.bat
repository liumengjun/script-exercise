@echo off&setlocal EnableDelayedExpansion
ls>temp.txt

for /f "delims=" %%a in ('type temp.txt') do (
	set "filename=%%a"
	echo !filename!
	
	set dd=%%a
	if exist "!dd!\" (
		echo !dd! is a dir
		cp .svnignore !dd!
		cp cp_svnignore.bat !dd!
	) else (
		echo !dd! is a file
	)
)
del temp.txt
pause
