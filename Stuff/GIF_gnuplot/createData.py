# CURVAS DE LISSAJOUS
import math as m
import numpy as np
import subprocess

omega_x = int(input('Frecuencia en x: '))
omega_y = int(input('Frecuencia en y: '))
delta = m.pi/4


y = lambda t: m.sin(omega_y*t + delta)
x = lambda t: m.sin(omega_x*t)

file = open('data.dat','w')
t = np.linspace(0,20)

for i in range(len(t)):
    file.write(str(x(t[i])) + '\t' + str(y(t[i])) + '\n')

file.close()

subprocess.call(['gnuplot', 'plottedData.gp'])
