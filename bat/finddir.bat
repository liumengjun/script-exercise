@echo off&setlocal EnableDelayedExpansion

set work_path=E:\temp
cd /d %work_path%
rem for /R %%s in (*) do (
for /R /D %%s in (*) do (
	rem echo %%s
	set dd=%%s
	if exist "!dd!\" (
		echo !dd!
	)
)
pause