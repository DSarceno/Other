//   2022-01-23
//   mergeSort.c
//   Diego Sarceño (dsarceno68@gmail.com)

//   Módulo que contiene las funciones "MergeSort" y "Merge", con el fin de
//   utilizar dicho método de ordenamiento en listas de vectores enteros.

//   Codificación del texto: UTF8
//   Compiladores probados: GNU gcc (Ubuntu 20.04 Linux) 9.3.0
//   Instrucciones de compilación: no requiere nada mas
//   gcc -Wall -pedantic -std=c11 -c -o mergeSort.o mergeSort.c
//   gcc -o mergeSort.x mergeSort.o -lm

//   Copyright (C) 2022
//   D. R. Sarceño Ramírez
//   dsarceno68@gmail.com

//   This program is free software: you can redistribute it and/or
//   modify it under the terms of the GNU General Public License as
//   published by the Free Software Foundation, either version 3 of
//   the License, or (at your option) any later version.

//   This program is distributed in the hope that it will be useful,
//   but WITHOUT ANY WARRANTY; without even the implied warranty of
//   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
//   General Public License for more details.


//   You should have received a copy of the GNU General Public License
//   along with this program.  If not, see
//   <http://www.gnu.org/licenses/>.
//PROGRAM mergeSort
#include <stdio.h>
#include <math.h>

// VARIABLES
int i = 0; // Left index
int j = 0; // Right index
int k = 0; // new array index
int n; // mergeSort left index
int m; // mergeSort right index
int extra = 0;
int length_left; // left array length
int length_right; // right array length
int length_main; // start
int left_array; // left array in mergeSort function
int right_array; // right array in mergeSort function

// MERGE FUNCTION
int merge(int la, int ra){ // Left and right array as entries
  int length_left = sizeof(la)/sizeof(la[0]);
  int length_right = sizeof(ra)/sizeof(ra[0]);
  int new[length_left + length_right];

  while ((i < length_left) && (j < length_right)){
    if (la[i] < ra[j]){
      new[k] = la[i];
      i += 1;
    } else{
      new[k] = ra[j];
      j += 1;
    } // end if
    k += 1;
  } // end while

  while (i < length_left){
    new[k] = la[i];
    i += 1;
    k += 1;
  } // end while

  while (j < length_right){
    new[k] = ra[j];
    j += 1;
    k += 1;
  } // end while
  return new;
} // END MERGE FUNCTION

// MERGESORT FUNCTION
int mergeSort(int main_array){
  length_main = sizeof(main_array)/sizeof(main_array[0]);
  // 1-element list
  if (length_main == 1){
    return main_array;
  } // end if

  // more than 1 element in the list
  left_array[ceil(length_main/2)] = {0};
  right_array[length_main - ceil(length_main/2)] = {0};
  for (n = 0; n < ceil(length_main/2); n++){
    left_array[n] = main_array[n];
  } // end for
  for (m = ceil(length_main/2); m < length_main; m++){
    left_array[extra] = main_array[m];
    extra += 1;
  } // end for

  // recursive part
  left_array = mergeSort(left_array);
  right_array = mergeSort(right_array);

  return merge(left_array, right_array);

} // END MERGESORT FUNCTION

// END mergeSort























//
