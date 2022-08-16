#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Diego Sarceno
# Date: 20.10.2020
#
#
#

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# se crea el sistema de EDs a resolver
def system(t, y, q, E, B, m):
    # constantes (algo exageradas jeje)
    # q = 10
    # E0 = 20
    c = 1
    # B0 = 50
    # m = 60
    x1, y1, x2, y2 = y
    f = [y1,
        q*(E0*np.sin(((q*B0)/(m*c))*t) + y2*B0),
        y2,
        -(q*B0/m)*y1]
    return f

# condiciones iniciales
x1 = 0
y1 = 0
x2 = 0
y2 = 0

# Valor inicial de 'q'
valin = 1
q = valin

# Se crean los 'axes'
solAx = plt.axes([0.1, 0.2, 0.8, 0.65])
qAx = plt.axes([0.1, 0.05, 0.8, 0.05])
EAx = plt.axes([0.1, 0.05, 0.8, 0.05])
BAx = plt.axes([0.1, 0.05, 0.8, 0.05])
mAx = plt.axes([0.1, 0.05, 0.8, 0.05])

# Se crea el slider para 'q'
q_s = Slider(qAx,                       # Se coloca en el eje
                label = 'q',            # Nombre del slider
                valmin = 0.001,         # valor minimo
                valmax = 10,            # valor maximo
                valinit = valin         # valor inicial
                )

E_s = Slider(qAx,                       # Se coloca en el eje
                label = 'q',            # Nombre del slider
                valmin = 0.001,         # valor minimo
                valmax = 10,            # valor maximo
                valinit = valin         # valor inicial
                )


# Colocamos el plot en el eje asociado
plt.axes(solAx)

def q_update(val):
    q = q_s.val
    # Solucionamos el sistema de ecuaciones
    sol = solve_ivp(system,[0,10],[x1,y1,x2,y2],t_eval = np.linspace(0,10,10000), args = [q, E, B, m])
    # Ploteamos el sistema
    plt.plot(sol.y[0],sol.y[2],'-k',label='Trayectoria')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title('Trayectoria de la Partícula')
    plt.legend()
    plt.show()
    # Eliminamos el plot a cada cambio de 'q'
    plt.cla()

# Cambia el valor de 'q'
q_s.on_changed(q_update)



# se grafica y se añaden detalles chingones
# plt.savefig('problema4.pdf')
plt.show()
