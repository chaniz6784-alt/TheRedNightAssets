@echo off
setlocal
set UEPATH="C:\Program Files\Epic Games\UE_5.6\Engine\Binaries\Win64\UnrealEditor.exe"
set UPROJECT="C:\Users\chani\Documents\Unreal Projects\TheRedNight\TheRedNight.uproject"
set SCRIPT="%~dp0install_full_demo.py"

echo --- The Red Night: One-Click Demo Installer ---
if not exist %UEPATH% echo [ERROR] Fix UEPATH in this .bat & pause & exit /b 1
if not exist %UPROJECT% echo [ERROR] Fix UPROJECT path in this .bat & pause & exit /b 1
if not exist %SCRIPT% echo [ERROR] Script missing at %SCRIPT% & pause & exit /b 1
start "" %UEPATH% %UPROJECT% -ExecutePythonScript=%SCRIPT%
echo If the Editor was already open, run in Python Console:
echo   exec(open(r"%SCRIPT%").read())
pause
endlocal
