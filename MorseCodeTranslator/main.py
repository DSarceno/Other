#    2021-11-13
#    main.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    Gráfico de Incertezas.

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de compilación: requere el módulo 'alphabet.py' 
#    python3 main.py

#    Copyright (C) 2021
#    D. R. Sarceño Ramírez
#    dsarceno68@gmail.com
#
#
#    This program is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see
#    <http://www.gnu.org/licenses/>.
# PROGRAM analisis
import alphabet as ph

# menu inicial
print('Ingrese la frase a traducir.\n')
print('**Sin mayusculas o carácteres especiales**\n')


# lectura de la entrada
f = input('Ingrese frase: \n')

# frase traducida a Codigo Morse
mcf = ''

for letter in f:
	mcf += ph.alphabet[letter] + ' '
	
print('\n')
print(mcf)
