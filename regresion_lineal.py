import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

url = "https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv"
datos = pd.read_csv(url)

datos_numericos = datos.select_dtypes(include='number')

Xi = datos_numericos.iloc[0]
Yi = datos_numericos.iloc[1]

suma_xi = Xi.sum()
suma_yi = Yi.sum()
suma_xiyi = (Xi * Yi).sum()
suma_xi2 = (Xi ** 2).sum()
cuadrado_sumaxi = suma_xi ** 2
n = len(Xi)

a = (n * suma_xiyi - suma_yi * suma_xi2) / (cuadrado_sumaxi - n * suma_xi2)
b = (suma_xi * suma_xiyi - suma_yi * suma_xi2) / (cuadrado_sumaxi - n * suma_xi2)

tiempo1 = a + (b * 15)
tiempo2 = a + (b * 30)
tiempo3 = a + (b * 50)

print(f"y = {a:.3f} + {b:.3f}x")
print(f"Salario después de 15 años = {tiempo1:.3f}")
print(f"Salario después de 30 años = {tiempo2:.3f}")
print(f"Salario después de 50 años = {tiempo3:.3f}")

x_vals = np.array([0, 60])  
y_vals = a + b * x_vals

x_pred = np.array([15, 30, 50])
y_pred = a + b * x_pred

plt.plot(x_vals, y_vals, 'b-', label='Línea de regresión')
plt.plot(x_pred, y_pred, 'ro', label='Predicciones')
plt.title('Regresión Lineal del Salario')
plt.xlabel('Experiencia en años')
plt.ylabel('Salario')
plt.grid(True)
plt.legend()
plt.show()


