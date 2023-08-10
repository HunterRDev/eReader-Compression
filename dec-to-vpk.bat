@ECHO OFF
cd %~dp0
for %%A IN (%~dp0\cards\dec\*) DO nevpk.exe -i "%%A" -o "%~dp0\cards\vpk\%%~nA.vpk" -v -c