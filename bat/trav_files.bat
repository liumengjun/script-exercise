@echo off

set /p input=please input one directory path:
@echo The dir is:"%input%"


cd /d "%input%"

set cur_dir=%cd%

for /R %%d in (*.java) do (
	echo %%d
)

pause
