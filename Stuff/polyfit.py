import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,100,10)
y = np.zeros(len(x))

f = lambda x: x**3 + x**2 + 4*x - 3

for i in range(len(x)):
    y[i] = f(x[i])

p = np.polyfit(x,y,3)
print(p)

sol = lambda x: p[0]*x**3 + p[1]*x**2 + p[2]*x + p[3]
ysol = np.zeros(len(x))
for i in range(len(x)):
    ysol[i] = sol(x[i])

plt.plot(x,y,'.k')
plt.plot(x,ysol,'-r')
plt.show()
