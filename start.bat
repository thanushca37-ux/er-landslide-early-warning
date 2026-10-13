@echo off
title NER-LandslideWatch Platform
echo ======================================================================
echo    Starting NER-LandslideWatch Early Warning Platform...
echo    URL: http://127.0.0.1:8000
echo ======================================================================
cd /d "%~dp0"
python run.py
if errorlevel 1 (
    echo.
    echo Failed with standard python command. Trying direct Python 3.11 path...
    "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" run.py
)
pause
