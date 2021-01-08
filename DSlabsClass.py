#!/usr/bin/env python
#
#
# @Author: Diego Sarceno
# Date: 13.12.2020
#
#
#
# This Class contains methods to use in basic data analisis for Laboratories
#

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
