import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych
df = pd.read_excel("sprzedaz12.xlsx")

# Przekształcenie danych do formatu tabela: wiersze = lata, kolumny = produkty
pivot = df.pivot(index="Rok", columns="Produkt", values="Sprzedaż")

# Parametry wykresu
produkty = pivot.columns
lata = pivot.index
x = range(len(lata))

# Szerokość pojedynczego słupka
bar_width = 0.25

# Kolory dla każdego produktu (nie domyślne)
colors = ['tomato', 'goldenrod', 'mediumseagreen']

# Tworzenie wykresu
plt.figure(figsize=(8, 5))

for i, produkt in enumerate(produkty):
    plt.bar(
        [pos + i * bar_width for pos in x],
        pivot[produkt],
        width=bar_width,
        label=produkt,
        color=colors[i]
    )

# Oś X – środek grup słupków
plt.xticks([pos + bar_width for pos in x], lata)
plt.xlabel("Rok")
plt.ylabel("Sprzedaż")
plt.title("Sprzedaż owoców w latach")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# Wyświetlenie wykresu
plt.show()
