!    2021-05-22
!    toroidRandom.f95
!    Diego Sarceño (dsarceno68@gmail.com)

!    Programa <program>

!    Codificación del texto: UTF8
!    Compiladores probados: GNU Fortran (Ubuntu 20.04 Linux) 9.3.0
!    Instrucciones de compilación: no requere nada mas
!    gfortran -Wall -pedantic -std=f95 -c -o toroidRandom.o toroidRandom.f95
!    gfortran -o toroidRandom.x toroidRandom.o

!    Copyright (C) 2021
!    D. R. Sarceño Ramírez
!    dsarceno68@gmail.com
!
!    This program is free software: you can redistribute it and/or
!    modify it under the terms of the GNU General Public License as
!    published by the Free Software Foundation, either version 3 of
!    the License, or (at your option) any later version.
!
!    This program is distributed in the hope that it will be useful,
!    but WITHOUT ANY WARRANTY; without even the implied warranty of
!    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
!    General Public License for more details.
!
!    You should have received a copy of the GNU General Public License
!    along with this program.  If not, see
!    <http://www.gnu.org/licenses/>.
!
PROGRAM toroidRandom
IMPLICIT NONE
  REAL(8) :: alpha, beta, Rg, Rp
  INTEGER(8) :: runs
  INTEGER(4) :: n, base
  INTEGER(4), ALLOCATABLE, DIMENSION(:) :: seed
  REAL(8), PARAMETER :: pi = 3.14159265359
  ! iterators
  INTEGER(4) :: i
  INTEGER(8) :: j
  INTEGER(4) :: err


  ! numero de iteraciones
  OPEN(21,FILE="runs.in",STATUS="OLD",IOSTAT=err)
  IF (err.EQ.0) THEN
     READ(21,*) runs
     CLOSE(21)
  ELSE
     runs = 100
  END IF

  ! GENERADOR DE NÚMEROS ALEATORIOS
  OPEN(21,FILE="seed.in",STATUS="OLD",IOSTAT=err)
  IF (err.EQ.0) THEN
     READ(21,*) base
     CLOSE(21)
  ELSE
     base=0
  END IF

  ! Tamaño optimo para la seed
  CALL RANDOM_SEED(SIZE = n)
  ! Resevar espacio de memoria para la seed
  ALLOCATE(seed(n),STAT=err)
  IF (err.NE.0) STOP 'Memoria no reservada'
  seed = base + 37*(/ (i - 1, i=1,n) /)

  ! Tomar la seed
  CALL RANDOM_SEED(PUT = seed)
  ! Liberar la memoria
  DEALLOCATE(seed)


  ! Generar las coordenadas de los puntos
  Rg = 10
  Rp = 5
  DO j = 1,runs
    CALL RANDOM_NUMBER(alpha)
    CALL RANDOM_NUMBER(beta)
    alpha = 2*pi*alpha
    beta = ACOS(2.*beta - 1)

    WRITE(99,*) COS(beta)*(Rg + Rp*COS(alpha)),SIN(beta)*(Rg + Rp*COS(alpha)),&
    Rp*SIN(alpha)
  END DO



END PROGRAM toroidRandom











! END
