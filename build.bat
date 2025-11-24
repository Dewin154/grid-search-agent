@echo off
TITLE Python App Builder

echo ==========================================
echo Step 1: activate .venv
echo ==========================================

if not exist .venv (
    echo FEHLER: .venv not found!
    pause
    exit
)

call .venv\Scripts\activate

echo.
echo ==========================================
echo Step 2: find version
echo ==========================================

for /f "delims=" %%i in ('python -c "import _version; print(_version.__version__)"') do set VERSION=%%i

echo Found version: %VERSION%
echo.

echo ==========================================
echo Step 3: buld .exe
echo ==========================================

pyinstaller --onefile --clean --name "GridAgent_v%VERSION%" main.py

echo.
echo ==========================================
echo Done!
echo File saved in dist folder as: GridAgent_v%VERSION%.exe
echo ==========================================
pause