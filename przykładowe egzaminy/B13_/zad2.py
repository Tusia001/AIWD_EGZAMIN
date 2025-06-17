#załaduj dane z pliku parki13.db jako ramkę danych (Data Frame),
import pandas as pd
from sqlite3 import connect
import matplotlib.pyplot as plt

conn = connect('parki13.db')

#• wybierz dane tylko za 2016 rok do oddzielnej zmiennej,
data = pd.read_sql("""
    SELECT Nazwa, Wartosc
    FROM DANE
    WHERE Rok = 2016 AND [Tereny zieleni] = 'parki spacerowo - wypoczynkowe'
""", con=conn)
#• wybierz następnie z danych 5 dowolnych województw,
wybrane = ['DOLNOŚLĄSKIE', 'MAŁOPOLSKIE', 'MAZOWIECKIE', 'POMORSKIE', 'WIELKOPOLSKIE']
data = data[data["Nazwa"].isin(wybrane)]

#• stwórz wykres kołowy na podstawie przefiltrowanych danych, (kolory wycinków muszą być inneniż domyślne),
#• podpisz etykiety wycinków, zaprezentuj części względne z dokładnością do 1 miejsca po przecinku.
labels = data["Nazwa"]
values = data["Wartosc"]
colors = ['tomato', 'goldenrod', 'mediumseagreen', 'skyblue', 'orchid']

plt.pie(
    values,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Udział parków w województwach (2016)")
plt.tight_layout()
plt.savefig("zad2.svg", format="svg")
plt.show()
