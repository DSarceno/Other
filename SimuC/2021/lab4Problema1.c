//   2022-01-23
//   lab4Problema1.c
//   Diego Sarceño (dsarceno68@gmail.com)

//   Programa destinado a encontrar el factorial de un entero positivo,
//   ingresado por el usuario, por medio de una función recursiva.

//   Codificación del texto: UTF8
//   Compiladores probados: GNU gcc (Ubuntu 20.04 Linux) 9.3.0
//   Instrucciones de compilación: no requiere nada mas
//   gcc -Wall -pedantic -std=c11 -c -o lab4Problema1.o lab4Problema1.c
//   gcc -o lab4Problema1.x lab4Problema1.o -lm

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
//PROGRAM lab4Problema1
#include <stdio.h>
#include <math.h>

char choise;
int i; // Iterator
int list[10] = {18,16,2,4,10,6,14,20,8,12}; // Even messy numbers


int main(){
  int stay == 1; // Stay on loop variable
  while (stay == 1){
    printf("Ingrese 'a' para orden ascendente y \n 'b' para orden descendente. \n");
    scanf("%c", &choise);
    if  (choise == "a"){
      // Upward sort code
      stay = 0;
    } else if (choise == "b"){
      // Falling sort code
      stay = 0;
    } else {
      printf("Caracter no valido, ingrese un valor nuevamente. \n");
    } // end nested if
  } // end while
  return 0;
}
// END lab4Problema1
