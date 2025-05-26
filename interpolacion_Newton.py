import matplotlib.pyplot as plt
import numpy as np

x_valor = np.array([1, 2, 3, 5, 7])
y_valor = np.array([3, 6, 19, 99, 291])

def diferencias_divididas(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:] = (coef[j:] - coef[j-1:-1]) / (x[j:] - x[:n-j])
    return coef

def polinomio(x_dato, coeffs, x):
    n = len(coeffs)
    resultado = coeffs[0]
    for i in range(1, n):
        term = coeffs[i]
        for j in range(i):
            term *= (x - x_dato[j])
        resultado += term
    return resultado

coeffs = diferencias_divididas(x_valor, y_valor)

x_plot = np.linspace(min(x_valor), max(x_valor), 200)
y_plot = [polinomio(x_valor, coeffs, xi) for xi in x_plot]

plt.figure()
plt.plot(x_valor, y_valor, 'bo', label='Datos conocidos')
plt.plot(x_plot, y_plot, 'g-', label='Interpolación de Newton')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación de Newton (Grado 4)')
plt.legend()
plt.grid(True)
plt.show()
