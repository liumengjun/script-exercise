@echo off&setlocal ENABLEEXTENSIONS 

rem (1)
rem transfer value
:exp1
set str=Hello
call :demoA %str%
echo %str%
goto :exp2

:demoA
echo/%1
set %1=Hello world
goto :EOF 


rem (2)
rem transfer reference
:exp2
set str=Hello2
call :demoB str
echo %str%
goto :exp3

:demoB
echo/%%%1%%    rem wrong
call echo/%%%1%%    rem right
echo/%1   rem wrong
call echo/%1   rem wrong
echo %%1
set %1=Hello2 world
goto :EOF


rem (3)
rem with return value
:exp3
set x=2
set y=3
call :Area %x% %y% answer
echo/The area is: %answer%
goto :exp4

:Area %width% %height% result
setlocal
set /a res=%1*%2
endlocal & set "%3=%res%"
goto :EOF 


rem (4)
rem protect your parameters
:exp4
set a=one
set b=two
echo/Before call :swap a b [%a% %b%]
call :Swap a b
echo/After call 1 :swap a b [%a% %b%]
call :Swap b a
echo/After call 2 :swap b a [%a% %b%]
goto :finish

:Swap
setlocal
call set a=%%%1%%
call set b=%%%2%%
endlocal & set "%1=%b%" & set "%2=%a%" & goto :EOF 

:finish