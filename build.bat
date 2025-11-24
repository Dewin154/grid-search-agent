@echo off
TITLE Python App Builder

echo ==========================================
echo STEP 1: Activating Virtual Environment
echo ==========================================

:: Check if the .venv folder actually exists
if not exist .venv (
    echo ERROR: The folder .venv was not found!
    echo Please make sure you are in the correct project directory.
    pause
    exit
)

:: IMPORTANT: 'call' is required here.
:: Without 'call', the script would stop immediately after activation.
call .venv\Scripts\activate

echo Environment activated successfully!
echo.

echo ==========================================
echo STEP 2: Running PyInstaller
echo ==========================================

:: --onefile: Packs everything into a single .exe file
:: --clean: Clears PyInstaller cache to avoid errors
:: --name: The name of your final .exe (e.g., "GridAgent")
:: REPLACE 'main.py' with your actual python filename if it is different!

pyinstaller --noconsole --onefile --clean --name "GridAgent_1.0.1" main.py

echo.
echo ==========================================
echo DONE!
echo Your executable is ready in the 'dist' folder.
echo ==========================================
pause