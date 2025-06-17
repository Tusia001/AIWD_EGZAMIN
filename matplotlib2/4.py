#4. Na bazie danych z pliku footfall_shopping_centers.csv wykonaj wykres punktowy. Zadbaj o jego podpisanie i estetykę. Zapisz powstały wykres w formacie eps

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("footfall_shopping_centers.csv")

df['date'] = pd.to_datetime(df['date'])

plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['mall_A'], marker='o', linestyle='--', label='Centrum Handlowe A')
plt.plot(df['date'], df['mall_B'], marker='s', linestyle='--', label='Centrum Handlowe B')
plt.plot(df['date'], df['mall_C'], marker='^', linestyle='--', label='Centrum Handlowe C')

plt.title('Frekwencja w centrach handlowych na przestrzeni czasu')
plt.xlabel('Data')
plt.ylabel('Liczba odwiedzających')
plt.xticks(rotation=45)
plt.legend(title='Centrum handlowe')
plt.grid(True)
plt.tight_layout()

plt.savefig("footfall_wykres.eps", format='eps')
plt.show()
