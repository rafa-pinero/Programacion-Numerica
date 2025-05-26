import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 200)

y1 = x**2 + 7*x + 2
y2 = np.sin(x) + 6*x + 3
y3 = np.sqrt(np.abs(x)) + 4*x

plt.figure(figsize=(10, 6))
plt.plot(x, y1, color='red',linestyle='--',label=r"$x^2 + 7x + 2$")
plt.plot(x, y2, color='purple',linestyle='-',label=r"$\sin(x) + 6x + 3$")
plt.plot(x, y3, color='green',linestyle='-.',label=r"$\sqrt{|x|} + 4x$")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfica de 3 funciones")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()
plt.grid()

plt.show()
