@echo off

for /f %%i in (a.txt) do echo %%i
pause

for %%i in (a.txt) do echo %%i 
pause

for /f "delims= " %%i in (a.txt) do echo %%i
pause

for /f "tokens=2,* delims= " %%i in (a.txt) do echo %%i %%j
pause


for /f "skip=2 tokens=*" %%i in (a.txt) do echo %%i
pause