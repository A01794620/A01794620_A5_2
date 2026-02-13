@echo off
setlocal EnableDelayedExpansion

set "working_dir=C:\AlgoriML\docs\TecMon\cursos\TC4017\code\A01794620_A5_2\"
:: Exercises to be tested
set "len_exercises=0"
set "len_common_cls=8"

set "exes[0]=computeSales.py"

set "common_cls[0]=__init__.py"
set "common_cls[1]=FileMaster.py"
set "common_cls[2]=JsonManager.py"
set "common_cls[3]=ParseType.py"
set "common_cls[4]=PrinterHelper.py"
set "common_cls[5]=Product.py"
set "common_cls[6]=SaleItem.py"
set "common_cls[7]=Setting.py"
set "common_cls[8]=TimeManager.py"

:: Loop through the exercises.
echo.
echo ================================================================================
echo                       Testing Flake8 through the files.
echo ================================================================================

for /L %%i in (0,1,%len_exercises%-1) do (
    set /a path_id=%%i+1
    echo.
    echo ================================================================================
    echo Working folder set to := %working_dir%src\
    echo Testing this file := src/!exes[%%i]!
    flake8 src/!exes[%%i]!
)

echo Working folder set to := ../common

for /L %%j in (0,1,%len_common_cls%-1) do (
    echo.
    echo ================================================================================
    echo Testing this file := common\!common_cls[%%j]!
    flake8 common/!common_cls[%%j]!
)

echo.
echo ================================================================================
echo                            End of Test of Flake8
echo ================================================================================
