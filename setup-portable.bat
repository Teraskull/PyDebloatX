@echo off
cls

:pip
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [1] Updating Pip...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install -U pip
goto :reqs

:reqs
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [2] Installing packages from requirements.txt...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install -r requirements.txt
goto :update

:update
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [3] Installing/Updating PyInstaller...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install -U pyinstaller
if ERRORLEVEL 1 goto errorupdate
goto build


:build
color 7
echo.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [4] Creating executable...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip show pyqt5 | findstr "Location:" > "%temp%\set_var.tmp"
set /P Location=<"%temp%\set_var.tmp"
set dll_path=%Location:~10,-13%site-packages\PyQt5\Qt\bin\
ren %dll_path%opengl32sw.dll opengl32sw_bak.dll

pyinstaller --noconfirm --onefile --name "PyDebloatX" --windowed --icon "pydebloatx/icon.ico" --add-data "pydebloatx/icon.ico;." --add-data "pydebloatx/style.css;." --add-data "pydebloatx/Language/*;Language" "pydebloatx/app.py"
if ERRORLEVEL 1 goto errorbuild

echo.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [5] Removing build files...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rmdir /s /q "./build/"
del PyDebloatX.spec

del "%temp%\set_var.tmp"
ren %dll_path%opengl32sw_bak.dll opengl32sw.dll

echo.
echo Done.

color a
echo.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [+] Executable built successfully and is located in dist/PyDebloatX.exe
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo.
pause
exit

:errorupdate
color c
echo.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [!] There was an error while updating PyInstaller.
echo [!] Attempting to build executable anyway.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
goto build

:errorbuild
color c
del PyDebloatX.spec
rmdir /s /q "./build/"
rmdir /s /q "./dist/"

del "%temp%\set_var.tmp"
ren %dll_path%opengl32sw_bak.dll opengl32sw.dll
echo.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [!] There was an error while building the executable.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo.
pause
exit
