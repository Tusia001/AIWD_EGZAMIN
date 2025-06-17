#załaduj dane z pliku sprzedaz12.xlsx jako ramkę danych (Data Frame),
from operator import index

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("sprzedaz12.xlsx")

#stwórz wykres słupkowy pogrupowany poziomy na podstawie danych z pliku,
pivot = df.pivot(index='Rok', columns='Produkt', values='Sprzedaż')
produkty = pivot.columns
sprzedaz = pivot.values
rok = pivot.index
y = range(len(rok))
colors = ['olive', 'yellow', 'blue']
bar_width = 0.25
plt.figure(figsize=(8, 6))
for i, produkt in enumerate(produkty):
    plt.barh(
        [pos + i * bar_width for pos in y],
        pivot[produkt],
        height=bar_width,
        label=produkt,
        color=colors[i]
    )


plt.yticks([pos + bar_width for pos in y], rok)
plt.xlabel("Sprzedaż")
plt.ylabel("Rok")
plt.title("Sprzedaż owoców w latach")

# dodaj tekst z aktualną datą (może być tekst na sztywno) w prawym górnym roku wykresu
#plt.annotate("17-06-2024",xy=(1800,2017.5),  fontsize=10)
#plt.text(0,0,"data")
plt.annotate(
    "Data: 2025-06-17",
    xy=(1, 1), xycoords='axes fraction',
    ha='right', va='top',
    fontsize=9
)


# dodaj na wykres siatkę (poziome i pionowe linie).
plt.grid(True, linestyle='--', alpha=0.6)
# dodaj legendę po prawej stronie po środku.
plt.legend()
plt.tight_layout()

plt.show()
