#załaduj dane z pliku handel15.xlsx jako ramkę danych (Data Frame),
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel("handel15.xlsx")

#stwórz wykres słupkowy poziomy poziomy wybierając dane tylko za sklepy, każdy słupek w
# innym kolorze (oś pionowa lata, oś pozioma wartość)

sklepy_df = df[df["Wyszczególnienie"] == "sklepy"]


kolory = ['green', 'orange', 'blue', 'pink', 'purple']

# Tworzenie wykresu słupkowego poziomego
plt.figure(figsize=(8, 5))
plt.barh(sklepy_df['Rok'].astype(str), sklepy_df['Wartosc'], color=kolory)


#• dodaj na wykres tekst ze swoim numerem legitymacji w prawym górnym rogi
#plt.text(1.0, 1.05, 'Numer legitymacji: 123456', transform=plt.gca().transAxes, ha='right', va='top', fontsize=12, fontweight='bold')
#• dodaj na wykres siatkę i legendę
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(['Liczba sklepów'], loc='lower right')
plt.title('Numer: 181166', loc='right', va='top')
plt.xlabel('Wartość [ob.]')
plt.ylabel('Rok')
plt.tight_layout()
plt.savefig("zad2.webp", format="webp")
plt.show()