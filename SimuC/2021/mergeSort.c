//	mié 20 abr 2022 18:30:27 CST
//	mergeSort.c
//	Diego Sarceno (dsarceno68@gmail.com)

//	Funciones del algoritmo MERGE SORT

//	Codificado del texto: UTF8
//	Compiladores probados: GNU gcc (Ubuntu 20.04 Linux) 9.3.0
//	Instruciones de Compilacion: no requiere nada mas
//	gcc -Wall -pedantic -std=c11 -c -o mergeSort.o mergeSort.c
//	gcc -o mergeSort.x mergeSort.o

//	Librerias
#include <stdio.h>

void mergeSort(int main_array[], int start, int final);
void merge(int array[], int start, int half, int final);

int main(){
  int lista[20] = {8,9,3,4,5,2,7,2,6,3,4,6,8,2,3,7,1,9,3,8};
  int length = sizeof(lista)/sizeof(lista[0]);
  mergeSort(lista,0,length);

  for (int i = 0; i < length; i++){
    printf("%d \n",lista[i]);
  }
  return 0;
}

void mergeSort(int main_array[], int start, int final){
  int half;
  half = (start + final)/2;
  if (start < final){
    mergeSort(main_array, start, half);
    mergeSort(main_array, half + 1, final);
    merge(main_array, start, half, final);
  } // END IF
} // END MERGESORT

void merge(int array[], int start, int half, int final){
  int aux[final + 1],i,j,k,t;

  k = 0; // movimiento por la lista auxiliar
  i = start; // movimiento por la sublista izquierda
  j = half + 1; // movimiento por la sublista derecha

  // ciclo para empezar a unir los arrays
  while(i <= half && j <= final){
    k++;
    if (array[i] < array[j]){
      aux[k] = array[i];
      i++;
    } else {
      aux[k] = array[j];
      j++;
    } // END IF
  } // END WHILE

  // para los elementos sobrantes de alguna de las sublistas
  for (t = i; t <= half; t++){
    k++;
    aux[k] = array[t];
  } // END FOR

  for (t = j; t <= final; t++){
    k++;
    aux[k] = array[t];
  } // END FOR

  // regresar todo al vector original
  for (t = 1; t <= k; t++){
    array[start + t - 1] = aux[t];
  } // END FOR
} // END MERGE

















// asdfads
