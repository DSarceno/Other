!    2021-05-31
!    SphereRandomWalk.f95
!    Diego Sarceño (dsarceno68@gmail.com)

!    Programa <program>

!    Codificación del texto: UTF8
!    Compiladores probados: GNU Fortran (Ubuntu 20.04 Linux) 9.3.0
!    Instrucciones de compilación: no requere nada mas
!    gfortran -Wall -pedantic -std=f95 -c -o SphereRandomWalk.o SphereRandomWalk.f95
!    gfortran -o SphereRandomWalk.x SphereRandomWalk.o

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
PROGRAM hexagonRandomWalk
IMPLICIT NONE
  !CONSTANTES
  REAL(8), DIMENSION(2) :: r
  INTEGER(8) :: i
  INTEGER(4) :: j
  INTEGER(4), ALLOCATABLE, DIMENSION(:) :: seed
  INTEGER(8) :: runs
  INTEGER(4) :: n, base
  INTEGER(4) :: err
  REAL(8), PARAMETER :: pi = 3.14159265359
  REAL(8) :: ra
  INTEGER(8) :: c


  ! READING FILES AND RANDOM NUMBERS GENERATOR
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
  seed = base + 37*(/ (j - 1, j=1,n) /)

  ! Tomar la seed
  CALL RANDOM_SEED(PUT = seed)
  ! Liberar la memoria
  DEALLOCATE(seed)


  ! iterador para generar la caminata
  ! caminata step-by-step
  r = 0
  DO i = 1, runs
    CALL RANDOM_NUMBER(ra)
    c = FLOOR(ra*6) + 1
    SELECT CASE (c)
    CASE (1)
      r(1) = r(1) + COS(pi/3)
      r(2) = r(2) + SIN(pi/3)
      WRITE(99,*) r(1), r(2)
    CASE (2)
      r(1) = r(1) + COS(2*pi/3)
      r(2) = r(2) + SIN(2*pi/3)
      WRITE(99,*) r(1), r(2)
    CASE (3)
      r(1) = r(1) + COS(3*pi/3)
      r(2) = r(2) + SIN(3*pi/3)
      WRITE(99,*) r(1), r(2)
    CASE (4)
      r(1) = r(1) + COS(4*pi/3)
      r(2) = r(2) + SIN(4*pi/3)
      WRITE(99,*) r(1), r(2)
    CASE (5)
      r(1) = r(1) + COS(5*pi/3)
      r(2) = r(2) + SIN(5*pi/3)
      WRITE(99,*) r(1), r(2)
    CASE (6)
      r(1) = r(1) + COS(6*pi/3)
      r(2) = r(2) + SIN(6*pi/3)
      WRITE(99,*) r(1), r(2)
    END SELECT
  END DO
  CLOSE(99)
END PROGRAM hexagonRandomWalk
