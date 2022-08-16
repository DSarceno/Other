#   2022-01-23
#   mergeSort.py
#   Diego Sarceño (dsarceno68@gmail.com)

#   Módulo que contiene las funciones "MergeSort" y "Merge", con el fin de
#   utilizar dicho método de ordenamiento en listas de vectores enteros.

#   Codificación del texto: UTF8
#   Compiladores probados: Python3 (Ubuntu 20.04 Linux)
#   Instrucciones de compilación: no requiere nada mas
#   python3 mergeSort.py

#   Copyright (C) 2022
#   D. R. Sarceño Ramírez
#   dsarceno68@gmail.com

#   This program is free software: you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as
#   published by the Free Software Foundation, either version 3 of
#   the License, or (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   General Public License for more details.


#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see
#   <http://www.gnu.org/licenses/>.
# PROGRAM mergeSort

# Librerías
import sys

# VARIABLES


# MERGE FUNCTION
def merge(left_array, right_array):
    new = []
    # merge part
    while (0 < len(left_array)) and (0 < len(right_array)):
        if left_array[0] < right_array[0]:
            new.append(left_array[0])
            left_array = left_array[1:]
        else:
            new.append(right_array[0])
            right_array = right_array[1:]

    if 0 < len(left_array): # Last element, if len(main_array) was odd
        new += left_array

    if 0 < len(right_array): # Last element, if len(main_array) was odd
        new += right_array
    return(new)

# DIVIDE RECURSIVE FUNCTION
def mergeSort(main_array):
    # 1 element in list
    if len(main_array) == 1:
        return main_array
    # more than 1 element in the list
    left_array = main_array[:len(main_array)//2]
    right_array = main_array[len(main_array)//2:]

    # recursive part
    left_array = mergeSort(left_array)
    right_array = mergeSort(right_array)

    return(merge(left_array, right_array))

#################

numbers = [6,9,7,8,4,9,6,6,6,6,5,7,5,5,1,6,4,9,7,1]
print(mergeSort(numbers))




































###########################
