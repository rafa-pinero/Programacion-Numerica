
import matplotlib.pyplot as plt
import numpy as np

x0, f_x0 = 3, 19
x1, f_x1 = 5, 99
x = 4 

f_x = f_x0 + (f_x1 - f_x0) * (x - x0) / (x1 - x0)

print(f"Valor estimado de f(4) {f_x}")

# Plotting the known points and the interpolated point
x_vals = np.array([x0, x1])
y_vals = np.array([f_x0, f_x1])

plt.plot(x_vals, y_vals, 'bo-', label='Datos conocidos')
plt.plot(x, f_x, 'ro', label=f'Interpolación lineal f({x})={f_x:.2f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación Lineal')
plt.legend()
plt.grid(True)
plt.show()