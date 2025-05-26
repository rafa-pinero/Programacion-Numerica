import numpy as np
import matplotlib.pyplot as plt

a = -3
b = -2
n = 6
vr = -2.1913
f = lambda t: 2 * t * np.cos(2 * t) - (t + 1) ** 2

error_relativo= lambda xr, va: (np.abs(xr - va) / np.abs(va)) * 100

for i in range(5):
    xi = (a+b)/2
    fa=f(a)
    fxi=f(xi)
    if fa*fxi<0:
        b=xi
    else:
        a=xi
    print(f'i = {i+1} | a = {a} | b = {b} | xi = {xi} | error = {error_relativo(xi,vr)}% \n')

x = np.linspace(-3,-2,500)
y = f(x)

plt.plot(x,y,label='2xcos(2x)-(x+1)^2', color='red', linestyle=':')
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title('Gráfica Bisección')
plt.legend()
plt.grid()
plt.show()