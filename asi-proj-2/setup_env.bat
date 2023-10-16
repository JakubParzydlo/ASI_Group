@echo off

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

REM Create a virtual environment
python -m venv venv

REM Activate virtual environment and install dependencies
call venv\Scripts\activate
pip install -r requirements.txt

REM Provide feedback to the user
echo Setup complete. Activate the virtual environment using "venv\Scripts\activate".
pause