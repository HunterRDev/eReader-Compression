@ECHO OFF
cd %~dp0
for %%A IN (%~dp0\cards\bin\*.bin) DO nedcenc.exe -e -i "%%A" -o "%~dp0\cards\raw\%%~nA-customs.raw"