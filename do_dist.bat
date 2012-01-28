cd /d D:\10\dev\impactuX
del /s /q /f dist
del /s /q /f build

python "setup.py" py2exe

copy "libogg-0.dll" ".\dist"
copy "sdl_ttf.dll" ".\dist"

copy /y ".\pic" ".\dist\pic"
copy /y ".\fonts" ".\dist\fonts"
copy /y ".\sounds" ".\dist\sounds"
copy /y ".\saves" ".\dist\saves"


pause
REM del "%0"

REM pause

