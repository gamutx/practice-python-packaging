@echo off
REM Studio Tools Pipeline Runner - Windows
REM This script demonstrates entry point scripts for the package
REM Entry points can also be configured in setup.py/pyproject.toml

setlocal enabledelayedexpansion

REM Colors for output (limited in Windows CMD)
echo.
echo ========================================
echo === Studio Tools Pipeline Runner ===
echo ========================================
echo Platform: Windows
echo.

REM Check if studio_tools is installed
python -c "import studio_tools" >nul 2>&1
if errorlevel 1 (
    echo Installing studio_tools...
    cd /d "%~dp0.."
    pip install -e .
)

REM Run the pipeline
echo Starting pipeline tasks...
echo.

REM Import and use the studio_tools package
python << 'EOF'
from studio_tools.shots.shot_creator import ShotCreator
from studio_tools.publishing.publisher import AssetPublisher
from studio_tools.validation.asset_checker import AssetChecker
import os
import tempfile

print("\nInitializing pipeline components...")

# Get temp directory for demo
temp_dir = tempfile.gettempdir()

# Create a shot
shot = ShotCreator("SQ001_SH010", os.path.join(temp_dir, "studio_project"))
print(f"✓ Shot created: {shot.shot_name}")
print(f"  Path: {shot.shot_path}")

# Initialize publisher
publisher = AssetPublisher(os.path.join(temp_dir, "studio_archive"))
print(f"✓ Publisher initialized")

# Initialize checker
checker = AssetChecker()
print(f"✓ Asset checker ready")

print("\n" + "="*50)
print("Pipeline components ready for use!")
print("="*50)
EOF

if errorlevel 1 (
    echo.
    echo ERROR: Pipeline runner failed
    exit /b 1
)

echo.
echo ✓ Pipeline runner completed successfully
pause
