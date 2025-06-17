import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
miesiace = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień']
sprzedaz_a = np.array([520000, 690000, 750000, 730000])
sprzedaz_b = np.array([390000, 540000, 710000, 660000])
sprzedaz_c = np.array([280000, 370000, 190000, 210000])
df = pd.DataFrame({
    "Miesiąc": miesiace,
    "Gra A": sprzedaz_a,
    "Gra B": sprzedaz_b,
    "Gra C": sprzedaz_c
})
plt.figure(figsize=(8, 6))# Tworzenie wykresu
# Wykres punktowy (scatter)
plt.scatter(df["Miesiąc"], df["Gra A"], label="Gra A", color="brown", marker="o", s=200)
plt.scatter(df["Miesiąc"], df["Gra B"], label="Gra B", color="darkgray", marker="<", s=200)
plt.scatter(df["Miesiąc"], df["Gra C"], label="Gra C", color="steelblue", marker="s", s=200)
plt.xlabel("Miesiąc")
plt.ylabel("Liczba kopii")
plt.title("Liczba sprzedanych kopii popularnych gier komputerowych")
plt.legend()
plt.ylim(100000, 800000)
plt.xticks(rotation=45)
plt.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("wykres_z_siatka.jpg", format="jpg")
plt.show()
