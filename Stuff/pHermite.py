# @Author: Diego Sarceno
# Date: 15.10.2020

import sympy as sym
import math as m
import sympy.plotting as splt
import numpy as np
import matplotlib.pyplot as plt


x = sym.symbols('x')

x_val = np.linspace(-10,10,100000)
p_val = np.zeros(len(x_val))

# funcion
def H(i):
    a = (-1)**i
    dif = sym.diff(sym.exp(-x**2 / 2),x,i)
    p_lam = sym.lambdify(x,a*dif*sym.exp(x**2 / 2), modules=['numpy'])
    for j in range(len(x_val)):
        p_val[j] = p_lam(x_val[j])
    return p_val

for i in range(4):
    lab = '$H_{num}$'.format(num = str(i))
    plt.plot(x_val,H(i),label = lab)

plt.title('Polinomios de Hermite')
plt.legend()
plt.xlim(-5,5)
plt.ylim(-10,10)
plt.xlabel('$x$')
plt.ylabel('$H_n$')
plt.savefig('polinomiosHermite.pdf')
plt.show()
