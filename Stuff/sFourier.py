import matplotlib.pyplot as plt
import numpy as np


def f(x,n):
    sum = 0
    for i in range(1,n + 1):
        sum += ((-1)**(i+1)/(i))*np.sin(i*x)
    return 2*sum

x = np.linspace(-np.pi,np.pi,1000)
y = np.zeros(len(x))

for n in range(1,101,10):
    for j in range(len(x)):
        y[j] = f(x[j],n)
    lab = '$n={num}$'.format(num = str(n - 1))
    plt.plot(x,y,label=lab)

plt.title('Serie de Fourier para $f(x) = x$')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()
plt.show()
