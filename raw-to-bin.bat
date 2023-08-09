@ECHO OFF
cd %~dp0
for %%A IN (%~dp0\cards\raw\*.raw) DO nedcenc.exe -d -i "%%A" -o "%~dp0\cards\bin\%%~nA.bin"