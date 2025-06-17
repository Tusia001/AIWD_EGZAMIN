import pandas as pd
import matplotlib.pyplot as plt

# załaduj dane z pliku licea11.xlsx jako ramkę danych (Data Frame)
df = pd.read_excel("licea11.xlsx")


# wybierz te pozycje, gdzie wartość jest poniżej 150,
labels = df["Nazwa"]
values = df["Wartość"]

mask = values < 150
filtered_labels = labels[mask]
filtered_values = values[mask]

# stwórz wykres pierścieniowy na podstawie danych z poprzedniego punktu,
# każdy wycinek koła powinien mieć inny kolor niż domyślny, ustaw kąt
# początkowy na 15, obrót zgodnie z ruchem wskazówek zegara,
# wysuń największy wycinek, ustaw widoczność względnych bez miejsc dziesiętnych,

plt.figure(figsize=(8, 6))
kolory = ['olive', 'red', 'blue', 'pink', 'yellow']
explode = [0.1 if val == max(filtered_values) else 0 for val in filtered_values]
plt.pie(filtered_values, labels=filtered_labels, explode=explode, colors=kolory, autopct='%1.0f%%', startangle=15)
circle = plt.Circle((0, 0), 0.4, color = 'white')
p = plt.gcf()
p.gca().add_artist(circle)


# dodaj tytuł do wykresu,

plt.title('Licea z liczbą uczniów poniżej 150', fontsize=14, fontweight='bold')
# dodaj tekst z aktualną datą (może być sztywny tekst) w lewym dolnym rogu wykresu.
plt.text(-2, -1.5, "Data: 2025-06-17", fontsize=10, ha='left', va='bottom')

plt.show()
