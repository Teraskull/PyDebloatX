@echo off
Color 07
cls

set steps=6


:createenv
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [1/%steps%] Creating virtual environment...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install -U virtualenv
virtualenv env
call env\Scripts\activate
goto pip


:pip
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [2/%steps%] Updating Pip...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install -U pip
goto reqs


:reqs
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [3/%steps%] Installing packages from requirements.txt...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install -r requirements.txt
goto update


:update
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [4/%steps%] Installing/Updating PyInstaller...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install -U pyinstaller
if ERRORLEVEL 1 goto errorupdate
goto build


:build
echo.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [5/%steps%] Creating executable...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip show PySide6 | findstr "Location:" > "%temp%\set_var.tmp"
set /P Location=<"%temp%\set_var.tmp"
set dll_path=%Location:~10,-13%site-packages\PySide6\
ren %dll_path%opengl32sw.dll opengl32sw_bak.dll

pyinstaller --noconfirm --onefile --name "PyDebloatX_portable" --windowed --icon "pydebloatx/icon.ico" --add-data "pydebloatx/icon.ico;." --add-data "pydebloatx/style.css;." --add-data "pydebloatx/Language/*.qm;Language" "pydebloatx/app.py"
if ERRORLEVEL 1 goto errorbuild
goto clean


:clean
echo.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [6/%steps%] Removing build files...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rmdir /s /q "./build/"
del PyDebloatX_portable.spec

del "%temp%\set_var.tmp"
ren %dll_path%opengl32sw_bak.dll opengl32sw.dll
call deactivate

echo.
echo Done.
goto buildsuccess


:buildsuccess
color a
echo.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [+] Executable built successfully and is
echo     located in dist/PyDebloatX_portable.exe
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo.
pause
cd ../../
Color 07
exit /B 0


:errorupdate
color c
echo.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [!] There was an error while installing/updating PyInstaller.
echo [!] Attempting to build executable anyway.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
goto build


:errorbuild
color c
del PyDebloatX_portable.spec
rmdir /s /q "./build/"
rmdir /s /q "./dist/"
del "%temp%\set_var.tmp"
ren %dll_path%opengl32sw_bak.dll opengl32sw.dll
call deactivate
echo.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [!] There was an error while building the executable.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo.
pause
Color 07
exit /B 1


