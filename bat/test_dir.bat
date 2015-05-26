
@echo off
set work_path=E:\temp
E:
cd %work_path%
for /R %%s in (.,*) do (
	echo %%s
)
pause
