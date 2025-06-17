import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(2, 5, 500)
y = (np.sin(x)**2) / (1 + x**2)
fig, ax = plt.subplots(figsize=(10, 6))# Tworzenie figury
# Wykres funkcji
ax.plot(x, y, color='#003366', linewidth=2.5, label=r"$y = \frac{\sin^2(x)}{1 + x^2}$")
ax.fill_between(x, y, color='#66b3ff', alpha=0.3)# Gradient pod wykresem


ax.set_title(r"Wykres funkcji $y = \frac{\sin^2(x)}{1 + x"
             r"^2}$ na przedziale $[2, 5]$", fontsize=16, weight='bold')
ax.set_xlabel("x", fontsize=13)
ax.set_ylabel("y", fontsize=13)
ax.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)# Siatka
# Personalizacja osi
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)
ax.tick_params(axis='both', which='major', labelsize=11)
ax.legend(loc='upper right', fontsize=12, frameon=False)# Legenda
# Zapis wykresu do pliku webp
plt.tight_layout()
plt.savefig("wykres_funkcji.webp", format="webp", dpi=300)
plt.show()
