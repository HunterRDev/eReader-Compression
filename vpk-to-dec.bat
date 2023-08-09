@ECHO OFF
cd %~dp0
for %%A IN (%~dp0\cards\vpk\*.vpk) DO nevpk.exe -i "%%A" -o "%~dp0\cards\dec\%%~nA" -v -d