#załaduj dane z pliku hr33.csv jako ramkę danych (Data Frame),
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('hr33.csv', sep = ';')


#• uporządkuj dane, aby dane było zgodne z koncepcją czystych danych,
# cechy liczbowe w typach liczbowych, nagłówki powinny stanowi nazwy kolumn,
df = df.replace(",", ".", regex=True).astype(float)
print(df)

# podziel dane dotyczące trzeciej cechy (lata doświadczenia zawodowego) na 5 koszyków równej szerokości
kolumna = df["Lata_doświadczenia_zawodowego"]
plt.figure(figsize=(7, 5))
plt.hist(kolumna, bins=5, edgecolor='black', rwidth=0.9)
# na podstawie utworzonych koszyków stwórz histogram, tak aby przedziały był domknięte z lewej strony, a prawej otwarte,
plt.xlabel("Lata doświadczenia zawodowego")
plt.ylabel("Liczba obserwacji")
plt.title("Rozkład lat doświadczenia zawodowego")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("zad3.pdf", format="pdf")
plt.show()