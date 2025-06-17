#4Za pomocą kodu odwzoruj wykład z pliku f12.png
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3, 0.9, 100)
y1=-x**2+4
y2=np.exp(x)+4
y3=2*np.cos(3*x)
plt.figure(figsize=(8, 6))
plt.plot(x, y1, color='orange', linestyle="--", label=r"$y = -x^{2}+4$")
plt.plot(x, y2, color='green', linestyle=":", label=r"$y = e^{x}+4$")
plt.plot(x, y3, color='violet', linestyle="-", label=r"$y = 2cos(3x)$")


plt.title("Wykres trzech funkcji")
plt.legend(loc='lower right')
plt.grid(True)
plt.xticks(np.arange(-3, 1.1))
plt.show()
