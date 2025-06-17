#3. Za pomocą kodu odwzoruj wykład z pliku f11.png
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3, 0.9, 100)
y1=np.exp(4*x)
y2=2*np.cos(3*x)
y3=x**2+4
plt.figure(figsize=(8, 6))
plt.plot(x, y1, color='red', linestyle=":", label=r"$y = e^{4x}$")
plt.plot(x, y2, color='blue', linestyle="-", label=r"y = 2cos(3x)")
plt.plot(x, y3, color='green', linestyle="--", label=r"$y=x^2+4$")

plt.legend()
plt.grid(True)
plt.title("Wykres trzech funkcji")
plt.xticks(np.arange(-3, 1.1))
plt.show()
