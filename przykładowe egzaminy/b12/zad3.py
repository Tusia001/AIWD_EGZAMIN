#• załaduj dane z pliku travel12.csv jako ramkę danych (Data frame),

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("travel12.csv", sep=";")

#• uporządkuj dane, aby dane było zgodne z koncepcją czystych danych, cechy liczbowe w typach
# liczbowych, nagłówki powinny stanowi nazwy kolumn,
df.columns = ['Kraj'] + list(df.columns[1:])# Uporządkowanie: ustawienie pierwszej kolumny jako indeks (kraj)
df = df.set_index('Kraj')
df = df.astype(float)# Dane liczbowe jako float


# wybierz dane dot. lat Włoch i Hiszpanii do osobnych zmiennych odpowiednio,
wlochy = df.loc['Włochy']
hiszpania = df.loc['Hiszpania']
print(wlochy, hiszpania)
#stwórz dwa wykresy kołowe na jednym rysunku (układ lewo-prawo)
# na podstawie przefiltrowanych danych, zastosuj na obu wykresach
# odpowiadające kolory wycinków związane z tymisamymi kategoriami,
# (kolory muszą być inne niż domyślne),

colors = ['red', 'blue', 'yellow', 'grey', 'purple']
kategorie=wlochy.index
explode=(0, 0, 0.3, 0, 0)
plt.subplot(1, 2, 1)
#plt.figure(8,6)
plt.pie(wlochy, labels=kategorie, colors=colors, startangle=15,shadow=True, explode=explode, autopct='%1.1f%%')
plt.title("Włochy")
plt.subplot(1, 2, 2)
#xplt.figure(8,6)
plt.pie(hiszpania, labels=kategorie, colors=colors, startangle=15,shadow=True, explode=explode, autopct='%1.1f%%')
plt.title("hiszpania")

# podpisz etykiety wycinków, zaprezentuj części względne z dokładnością do 1 miejsca po przecinku; dodaj tytuły do podwykresów.

plt.tight_layout()
plt.show()