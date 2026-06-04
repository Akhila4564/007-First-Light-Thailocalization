@echo off
title Build 007 First Light Thai Localization Installer

echo Installing PyInstaller...
pip install pyinstaller

echo Building EXE...
pyinstaller --onefile --windowed --name 007FirstLightThaiLocalizationSetup src/installer.py

echo.
echo Done.
echo EXE created in dist folder.
pause
