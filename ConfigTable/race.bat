call basePath.bat
@echo off
set pydatas=%ktpydatas%/d_race.py
set excel1=%ktexcels%/xlsxs/race.xlsx
echo on
python ../Tools/xlsx2py/xlsx2py/xlsx2py.py %pydatas% %excel1%
if not defined ktall (ping -n 30 127.1>nul)

