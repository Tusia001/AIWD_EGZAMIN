import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3, 3, 500)# Dane x
y = x**2 + 5*x - (1 - x**2) / (1 + x**2)
# Tworzenie wykresu z tłem
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor('cornflowerblue') # tło całej figury
ax.set_facecolor('ivory') # tło samego wykresu
# Wykres funkcji z przerywaną linią i niestandardowym kolorem
ax.plot(
    x, y,
    label=r'$y = x^2 + 5x - \frac{1 - x^2}{1 + x^2}$',
    color='teal',
    linestyle='--',
    linewidth=2
)
ax.set_title("Upiększony wykres funkcji", fontsize=16, fontweight='bold')
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("y", fontsize=12)
# Siatka i legenda
ax.grid(True, linestyle=':', linewidth=0.7)
ax.legend()

plt.tight_layout()# Dopasowanie układu
# Zapis do pliku WEBP
plt.savefig("ladny_wykres_funkcji.webp", format="webp")
plt.show()# Wyświetlenie wykresu
