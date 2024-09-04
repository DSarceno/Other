@echo off

set CURRENT_DIR=%cd%

docker run --rm -v "%CURRENT_DIR%:/data" reporte