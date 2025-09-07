REM Ejecutable que agrega y realiza el commit en el repositorio local, asi como juntar las ramas y subirlas al repositorio gitlab
REM https://gitlab.com/work_ine/cedulasupervision.git


git add .


REM Obtener la fecha y hora actual
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set year=%datetime:~0,4%
set month=%datetime:~4,2%
set day=%datetime:~6,2%
set hour=%datetime:~8,2%
set minute=%datetime:~10,2%
set seconds=%datetime:~12,2%
set datetime_formatted=%day%-%month%-%year% %hour%:%minute%:%seconds%

REM Realizar commit con un mensaje que incluya la fecha y hora
git commit -m "Actualizacion: %datetime_formatted%"

REM Subir las actualizaciones al repositorio gitlab
git push -u "https://gitlab.com/work_ine/cedulasupervision.git" main

REM COMPLETADO CORRECTAMENTE :3