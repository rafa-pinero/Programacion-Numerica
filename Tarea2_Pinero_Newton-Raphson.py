import numpy as np
import matplotlib.pyplot as plt

x = 0.3
n = 5

f = lambda t: 8 * t * np.sin(t) * np.exp(-t) - 1
df = lambda t: (8 * np.exp(-t) - 8 * t * np.exp(-t)) * np.sin(t) + (8 * t * np.exp(-t)) * np.cos(t)
error = lambda x0 , x1: np.abs(x1-x0/x1)

for i in range(n):
    x = x - f(x)/df(x)
    print(f'i = {i+1} | x = {x} | error = {error(x,x-1)}')

x = np.linspace(-3,5,500)
y = f(x)
z = df(x)

plt.plot(x,y,label='f(x) = 8xsen(x)e^-x - 1', color='red', linestyle=':')
plt.plot(x,z,label="f'(x) = (8e^-x - 8xe^-x)sen(x) + (8xe^-x)cos(x)", color='blue', linestyle='-')
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title('Gráfica Newton-Raphson')
plt.legend()
plt.grid()
plt.show()
