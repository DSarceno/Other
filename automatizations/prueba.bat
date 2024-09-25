@echo off

set CURRENT_DIR=%cd%

docker run --rm -v "%CURRENT_DIR%:/data" reporte

ren "%CURRENT_DIR%\main.pdf" "%CURRENT_DIR%\Google Cloud: Professional Data Engineer.pdf"


if %errorlevel% == 0 (

	echo Archivo Renombrado exitosamente.

) else (

	echo Error al renombrar archivo.

)


pause