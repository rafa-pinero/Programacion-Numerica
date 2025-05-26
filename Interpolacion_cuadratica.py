import matplotlib.pyplot as plt
import numpy as np

x0, f_x0 = 2, 6
x1, f_x1 = 3, 19
x2, f_x2 = 5, 99
x = 4  

A = np.array([
    [x0**2, x0, 1],
    [x1**2, x1, 1],
    [x2**2, x2, 1]
])
B = np.array([f_x0, f_x1, f_x2])

a, b, c = np.linalg.solve(A, B)

f_x = a * x**2 + b * x + c
print(f"Estimated value of f(4) using quadratic interpolation with Cramer's rule: {f_x}")

x_valor = np.array([x0, x1, x2])
y_valor = np.array([f_x0, f_x1, f_x2])
xp = np.linspace(min(x_valor), max(x_valor), 100)
yp = a * xp**2 + b * xp + c

plt.plot(x_valor, y_valor, 'bo', label='Datos conocidos')
plt.plot(x, f_x, 'ro', label=f'Interpolación cuadrática f({x})={f_x:.2f}')
plt.plot(xp, yp, 'b--', label='Polinomio interpolado')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación Cuadrática (Regla de Cramer)')
plt.legend()
plt.grid(True)
plt.show()