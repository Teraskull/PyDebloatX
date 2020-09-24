@echo off
cls

echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [1] Updating PyInstaller...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install -U pyinstaller
if ERRORLEVEL 1 goto errorupdate

echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [2] Creating executable...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pyinstaller --noconfirm --onedir --windowed --icon "pydebloatx/icon.ico" --add-data "pydebloatx/icon.ico;." --add-data "pydebloatx/style.css;."  "pydebloatx/app.py"
if ERRORLEVEL 1 goto errorbuild

echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo [3] Removing unused files...
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
rmdir /s /q "./build/"
del app.spec

cd dist/app

del _asyncio.pyd
del _bz2.pyd
del _ctypes.pyd
del _decimal.pyd
del _elementtree.pyd
del _hashlib.pyd
del _lzma.pyd
del _multiprocessing.pyd
del _overlapped.pyd
del _queue.pyd
del _ssl.pyd
del _testcapi.pyd
del _tkinter.pyd
del pyexpat.pyd
del unicodedata.pyd

del d3dcompiler_47.dll
del libcrypto-1_1.dll
del libEGL.dll
del libffi-7.dll
del libGLESv2.dll
del libssl-1_1.dll
del MSVCP140.dll
del opengl32sw.dll
del Qt5DBus.dll
del Qt5Network.dll
del Qt5Qml.dll
del Qt5QmlModels.dll
del Qt5Quick.dll
del Qt5Svg.dll
del Qt5WebSockets.dll
del tcl86t.dll
del tk86t.dll
del VCRUNTIME140.dll
del VCRUNTIME140_1.dll

rmdir /s /q "./lib2to3/"
rmdir /s /q "./tcl/tzdata/"
rmdir /s /q "./tcl\encoding/"
rmdir /s /q "./PyQt5/Qt/translations/"

color a
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo Executable built successfully and is located in dist/app.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pause
exit

:errorupdate
color c
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo There was an error while updating PyInstaller.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pause
exit

:errorbuild
color c
del app.spec
rmdir /s /q "./build/"
rmdir /s /q "./dist/"
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo There was an error while building the executable.
echo.
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pause
exit
