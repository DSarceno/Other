//   2021-05-21
//   lab4Problema6.c
//   Diego Sarceño (dsarceno68@gmail.com)

//   Programa <program>

//   Codificación del texto: UTF8
//   Compiladores probados: GNU gcc (Ubuntu 20.04 Linux) 9.3.0
//   Instrucciones de compilación: no requiere nada mas
//   gcc -Wall -pedantic -std=c11 -c -o lab4Problema6.o lab4Problema6.c
//   gcc -o lab4Problema6.x lab4Problema6.o -lm

//   Copyright (C) 2021
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
//PROGRAM lab4Problema6
#include <stdio.h>
#include <math.h>

int i; // iterator
int n; // limite
float sum1 = 0;
float sum2 = 0;
float sum3 = 0;
float sum4 = 0;

void ask(){
  printf("Ingrese un número: ");
  scanf("%d", &n);
} // END MAIN


float a(int n){
  for (i = 1; i <= n; i++){
    sum1 += pow(i,2)*(i - 3);
  }
  return sum1;
} //END a

float b(int n){
  for (i = 2; i <= n; i++){
    sum2 += 3/(i - 1);
  }
  return sum2;
} // END b

float c(int n){
  for (i = 1; i <= n; i++){
    sum3 += (1/sqrt(5))*pow(((1 + sqrt(5))/2),i) - (1/sqrt(5))*pow(((1 - sqrt(5))/2),i);
  }
  return sum3;
} // END c

float d(int n){
  for (i = 2; i <= n; i++){
    sum4 += 0.1*(3*pow(2,i - 2) + 4);
  }
  return sum4;
} // END d

int main(){
  ask();
  printf("Inciso a) %.2f \n", a(n));
  printf("Inciso b) %.2f \n", b(n));
  printf("Inciso c) %.2f \n", c(n));
  printf("Inciso d) %.2f \n", d(n));
}






//END PROGRAM lab4Problema6
