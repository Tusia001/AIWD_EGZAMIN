'''Na bazie danych z pliku footfall_shopping_centers.csv stwórz ramkę danych. Przekształć ją do postaci długiej (long data) z wykorzystaniem pd.melt. Wykonaj wykres
punktowy. Zadbaj o jego podpisanie i estetykę. Zapisz powstały wykres w formacie png.
Porównaj podejście z zadaniem nr 4.'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("footfall_shopping_centers.csv")

df['date'] = pd.to_datetime(df['date'])

df_melted = pd.melt(
    df,
    id_vars='date',
    value_vars=['mall_A', 'mall_B', 'mall_C'],
    var_name='mall',
    value_name='visitors'
)

plt.figure(figsize=(10, 6))
for mall, data in df_melted.groupby('mall'):
    plt.plot(data['date'], data['visitors'], marker='o', linestyle='--', label=mall.replace('_', ' ').title())

plt.title('Frekwencja w centrach handlowych (podejście: long data)')
plt.xlabel('Data')
plt.ylabel('Liczba odwiedzających')
plt.xticks(rotation=45)
plt.legend(title='Centrum handlowe')
plt.grid(True)
plt.tight_layout()

plt.savefig("footfall_wykres_long.png", format='png')
plt.show()
