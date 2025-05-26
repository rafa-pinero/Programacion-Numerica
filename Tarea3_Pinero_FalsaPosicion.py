import numpy as np
import matplotlib.pyplot as plt

a = -3
b = -2

f = lambda t: 2 * t * np.cos(2 * t) - (t + 1) ** 2
error_relativo = lambda xi,xh: (np.abs(xi - xh))*100

xi_prev = None

for i in range(5):
    y = b - ((f(b)*(a-b))/(f(a)-f(b)))
    if f(y) < 0:
        a = y
    else:
        b = y
    if xi_prev is not None:
        error = error_relativo(y,xi_prev)
    else:
        error = None
    print(f'i = {i+1} | a = {a:.4f} | b = {b:.4f} | f(a) = {f(a):.4f} | f(b) = {f(b):.4f} | xi = {y} | f(xi) = {f(y):.4f} | error = {error}% \n')

    xi_prev = y

x = np.linspace(-3,-2,500)

y = f(x)

plt.plot(x,y,label='2xcos(2x)-(x+1)^2', color='red', linestyle=':')
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title('Gráfica Falsa Posicion')
plt.legend()
plt.grid()
plt.show()