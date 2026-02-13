@echo off
setlocal EnableDelayedExpansion
set "working_dir=C:\AlgoriML\docs\TecMon\cursos\TC4017\code\A01794620_A5_2\"
:: Exercises to be Tested
set "len_exercises=0"

set "exes[0]=computeSales.py"
set "cases[0]=2"

:: Loop through the exercises.
echo.
echo ================================================================================
echo                        Loop through the exercises.
echo ================================================================================

for /L %%i in (0,1,%len_exercises%-1) do (
    set cases_count=!cases[%%i]!
    set /a path_id=%%i+1
    echo.
    echo Testing this Exercise := !path_id!
    echo Working folder set to := %working_dir%
    cd %working_dir%

    for /L %%j in (0,1,!cases_count!-1) do (
        set /a file_id=%%j+1
        echo ................................................................................
        echo Test using this file := tests/TC!file_id!.Sales.json
        python .\src\!exes[%%i]! ProductList.json TC!file_id!.Sales.json
    )
)

echo.
echo ================================================================================
echo                 Test of exercises successfully completed.
echo ================================================================================

::