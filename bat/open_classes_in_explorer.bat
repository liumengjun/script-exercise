@echo off
set classesdir=%1
set classfullname=%2

set classfullname=%classfullname:.=\%

explorer /select,%classesdir%\%classfullname%.class
