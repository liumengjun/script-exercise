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
echo �����\�е��@����̎���ļ�:
echo ��ȫ·��%%0: %0
echo ȥ����̖%%~0: %~0
echo ���ڷօ^%%~d0: %~d0
echo ��̎·��%%~p0: %~p0
echo ��̎·��%%~dp0: %~dp0
echo �ļ���%%~n0: %~n0
echo �Uչ��%%~x0: %~x0
echo �ļ�����%%~a0: %~a0
echo �޸ĕr�g%%~t0: %~t0
echo �ļ���С%%~z0: %~z0
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
	if not "%%a"=="<DIR>" if not "%%b"=="�ֽ�" if not "%%b"=="�����ֽ�" echo %%b
)
pause


set work_path=E:\temp
cd /d %work_path%
dir>filelist.temp.txt
for /f "skip=5 tokens=3* delims= " %%a in (filelist.temp.txt) do (
	if not "%%a"=="<DIR>" if not "%%b"=="�ֽ�" if not "%%b"=="�����ֽ�" echo %%b
)
del filelist.temp.txt
pause
