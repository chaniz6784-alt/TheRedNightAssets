
@echo off
setlocal
set UEPATH="C:\Program Files\Epic Games\UE_5.6\Engine\Binaries\Win64\UnrealEditor.exe"
set UPROJECT="C:\Users\chani\Documents\Unreal Projects\TheRedNight\TheRedNight.uproject"
set SCRIPT="%~dp0install_demo.py"

echo --- TheRedNight RPG Demo Installer ---
echo UE Path: %UEPATH%
echo Project: %UPROJECT%
echo Script : %SCRIPT%
echo.

if not exist %UEPATH% (
  echo [ERROR] UnrealEditor.exe not found: %UEPATH%
  echo Edit this .bat and set UEPATH to your UnrealEditor.exe
  pause
  exit /b 1
)

if not exist %UPROJECT% (
  echo [ERROR] .uproject not found: %UPROJECT%
  echo Edit this .bat and set UPROJECT to your .uproject path
  pause
  exit /b 1
)

if not exist %SCRIPT% (
  echo [ERROR] Script missing: %SCRIPT%
  echo Make sure you extracted the ZIP into your project root so this exists:
  echo   Content\Tools\TheRedNight_RPG_Demo\install_demo.py
  pause
  exit /b 1
)

echo Launching Unreal and executing...
start "" %UEPATH% %UPROJECT% -ExecutePythonScript=%SCRIPT%
echo If Unreal is already running, paste this in the Python Console:
echo   exec(open(r"%SCRIPT%").read())
echo Watch Output Log for: "TRN Demo Installer: DONE"
pause
endlocal
