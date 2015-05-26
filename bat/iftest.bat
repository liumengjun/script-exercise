@echo off
rem set otx_debug_mode=false
set flag_debug=0
if "%otx_debug_mode%"=="true" (
	rem @echo "debug"
	set flag_debug=1
)

if "%flag_debug%"=="1" goto finish 

set input= 
rem we'd better write set at the first of line, or it does not work well
set /p input="Run commond in dubeg mode Yes or Not:
rem @echo %input%

rem bat file does not support or ||
if "%input%"=="Y" goto setdebugflag 
if "%input%"=="y" goto setdebugflag 
if "%input%"=="Yes" goto setdebugflag 
if "%input%"=="YES" goto setdebugflag 
if "%input%"=="yes" goto setdebugflag 
goto finish

:setdebugflag
rem @echo "debug"
set flag_debug=1
set input= 

:finish
set debug_option_str=
if "%flag_debug%"=="1" (
	@echo "Now, run commond in dubeg mode"
	set debug_option_str=-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=9011
)

@echo %debug_option_str%

@echo on
