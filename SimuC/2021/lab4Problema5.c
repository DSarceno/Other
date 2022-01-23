//   2022-01-23
//   lab4Problema5.c
//   Diego Sarceño (dsarceno68@gmail.com)

//   Programa destinado a encontrar el factorial de un entero positivo,
//   ingresado por el usuario, por medio de una función recursiva.

//   Codificación del texto: UTF8
//   Compiladores probados: GNU gcc (Ubuntu 20.04 Linux) 9.3.0
//   Instrucciones de compilación: no requiere nada mas
//   gcc -Wall -pedantic -std=c11 -c -o lab4Problema5.o lab4Problema5.c
//   gcc -o lab4Problema5.x lab4Problema5.o -lm

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
//PROGRAM lab4Problema5
#include <stdio.h>
#include <math.h>

int fact(int); // Function declaration

int main(){
  int n, f; // Number and storage variable

  printf("Ingrese un número entero: ");
  scanf("%d",&n);

  // Storage variable
  f = fact(n);

  // print
  printf("El factorial de %d es %d\n", n, f);

  return 0;
} // END MAIN FUNCTION

int fact(int n){
  if (n == 0){
    return(1);
  } else {
    return(n*fact(n - 1));
  } // end if
} // END FACT FUNCTION

//END lab4Problema5
