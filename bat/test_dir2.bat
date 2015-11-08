@echo off

echo %cd%
echo %DATE% 
echo %time%
echo %RANDOM% 
echo %ERRORLEVEL%
echo %CMDEXTVERSION%
echo %CMDCMDLINE%
echo %0
echo %1
echo %2
echo %temp%
echo %tmp%
echo %~dp0
echo %~nx0
echo >nul
echo 正在運行的這個比處理文件:
echo 完全路徑%%0: %0
echo 去掉引號%%~0: %~0
echo 所在分區%%~d0: %~d0
echo 所處路徑%%~p0: %~p0
echo 所處路徑%%~dp0: %~dp0
echo 文件名%%~n0: %~n0
echo 擴展名%%~x0: %~x0
echo 文件屬性%%~a0: %~a0
echo 修改時間%%~t0: %~t0
echo 文件大小%%~z0: %~z0
pause

set date_str=%date%
echo %date_str%
set datestr=%date_str:~0,4%-%date_str:~5,2%-%date_str:~8,2%
set tempfile=%~dp0%datestr%.%time%%RANDOM%.tmp
echo %tempfile%
pause

set work_path=E:\temp
cd /d %work_path%
for /f "skip=5 tokens=3* delims= " %%a in ('dir') do (
	if not "%%a"=="<DIR>" if not "%%b"=="字节" if not "%%b"=="可用字节" echo %%b
)
pause


set work_path=E:\temp
cd /d %work_path%
dir>filelist.temp.txt
for /f "skip=5 tokens=3* delims= " %%a in (filelist.temp.txt) do (
	if not "%%a"=="<DIR>" if not "%%b"=="字节" if not "%%b"=="可用字节" echo %%b
)
del filelist.temp.txt
pause
