
@echo off
setlocal

REM === Quick editable paths ===
set UEPATH="C:\Program Files\Epic Games\UE_5.6\Engine\Binaries\Win64\UnrealEditor.exe"
set UPROJECT="C:\Users\chani\Documents\Unreal Projects\TheRedNight\TheRedNight.uproject"
set SCRIPT="%~dp0install_all.py"

echo --- TheRedNight One‑Click HUD Installer ---
echo UE Path: %UEPATH%
echo Project: %UPROJECT%
echo Script : %SCRIPT%
echo.

if not exist %UEPATH% (
  echo [ERROR] UnrealEditor.exe not found at %UEPATH%
  echo Edit this .bat and point UEPATH to your actual UnrealEditor.exe.
  pause
  exit /b 1
)

if not exist %UPROJECT% (
  echo [ERROR] .uproject not found at: %UPROJECT%
  echo Edit this .bat and point UPROJECT to your actual .uproject file.
  pause
  exit /b 1
)

if not exist %SCRIPT% (
  echo [ERROR] Script not found: %SCRIPT%
  echo Make sure you extracted this folder into your project's Content\\Tools\\TheRedNight_Installer
  pause
  exit /b 1
)

echo Launching Unreal and executing installer script...
start "" %UEPATH% %UPROJECT% -ExecutePythonScript=%SCRIPT%
echo If Unreal already running, close it first or just run the script from Python Console:
echo   exec(open(r"%SCRIPT%").read())
echo.
echo When the Editor opens, watch the Output Log for "TheRedNight Installer: DONE".
echo Press any key to finish.
pause
endlocal
