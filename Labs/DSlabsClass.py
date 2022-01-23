#    2021-11-20
#    DSlabsClass.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    Gráfico de Incertezas.

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de compilación: requere un archivo con una sola columna con los datos
#    python3 DSlabsClass.py <inputfile.ext> <outputfile.ext>

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

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

class laboratories:
    def __init__(self, name):
        self.nameFile = name
        self.Data = None

    def readFile(self):
        file = open(self.nameFile, 'r')
        DataString = [line.split() for line in file]
        for i in range(len(DataString)):
            for j in range(len(DataString[i])):
                DataString[i][j] = eval(DataString[i][j])
        self.Data = DataString
        return self.Data

    def plotData(self):
        if self.Data[0] == 2:
            x = [self.Data[i][0] for i in range(len(self.Data))]
            y = [self.Data[i][1] for i in range(len(self.Data))]
            

lab = laboratories('prueba.tsv')
print(lab.readFile())
