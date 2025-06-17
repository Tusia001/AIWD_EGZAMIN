#załaduj dane z pliku parki33.xlsx jako ramkę danych (Data Frame),
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('parki33.xlsx')

#• wybierz dane tylko za 2016 rok do oddzielnej zmiennej,
df_2016 = df[(df['Rok']==2016) & (df["Nazwa"] != "POLSKA")]

#• wybierz następnie z danych 5 dowolnych województw,
wojewodztwa = df_2016.head(5)
print(wojewodztwa)
#• stwórz wykres kołowy na podstawie przefiltrowanych danych, (kolory wycinków muszą być inne niż domyślne),
labels = wojewodztwa['Nazwa']
values = wojewodztwa['Wartosc']
colors = ['red', 'blue', 'green', 'purple', 'yellow']
explode = (0.1, 0, 0, 0.1, 0)
plt.pie(values, labels=labels, explode = explode, colors=colors, startangle=15, autopct='%1.1f%%')
plt.axis('equal')
plt.show()

#• podpisz etykiety wycinków, zaprezentuj części względne z dokładnością do 1 miejsca po przecinku