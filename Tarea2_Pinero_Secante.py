import numpy as np
import matplotlib.pyplot as plt

x0 = -0.3
x_1 = 0.5

f = lambda t: 8 * t * np.sin(t) * np.exp(-t) - 1
error = lambda a, b: np.abs(b-a/b)

for i in range(5):
    x1 = x0 - ((f(x0) * (x_1 - x0)) / (f(x_1) - f(x0)))

    print(f'i = {i+1} | x0 = {x0} | x1 = {x1} | error = {error(x_1,x0)}')

    x_1, x0 = x0, x1

x = np.linspace(-3,5,500)
y = f(x)

plt.plot(x,y,label='f(x) = 8xsen(x)e^-x - 1', color='red', linestyle=':')
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title('Gráfica Secante')
plt.legend()
plt.grid()
plt.show()