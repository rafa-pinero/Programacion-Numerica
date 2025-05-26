import numpy as np
import matplotlib.pyplot as plt

def division_sintetica(coef, xi):
    n = len(coef)
    b = [coef[0]]
    for i in range(1, n):
        b.append(b[i - 1] * xi + coef[i])

    c = [b[0]]
    for i in range(1, n - 1):
        c.append(c[i - 1] * xi + b[i])

    return b, c

coeficientes = [1, -5, 5, -1]
x0 = 0.8

error = lambda a, b: np.abs(b-a/b)

for j in range(5):
    y = x0
    valor_b, valor_c = division_sintetica(coeficientes, y)
    x1 = x0 - (valor_b[3] / valor_c[2])
    x0 = x1
    error_relativo = error(x1, x0)
    print(f'i = {j+1} | x0 = {x0} | xi = {x1} | error = {error_relativo}% \n')

f = lambda t: (t ** 3) - (5 * (t ** 2)) + (5 * t) -1

x = np.linspace(-20,20,500)

y = f(x)

plt.plot(x,y,label='t^3 - 5t^2 + 5t - 1', color='red', linestyle=':')
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title('Gráfica Birge-Vieta')
plt.legend()
plt.grid()
plt.show()





