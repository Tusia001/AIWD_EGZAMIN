import pandas as pd
import matplotlib.pyplot as plt
# Wczytanie danych z pliku (z drugim wierszem jako nagłówkiem)
olympics_df = pd.read_csv("olympics.csv", header=1)

# Wybór 5 dowolnych krajów – np. od 1 do 5 (indeksy w pliku zaczynają się od 0, ale pierwszy to nagłówki)
selected_df = olympics_df.iloc[1:6]

# Pobranie nazw krajów i liczby zdobytych medali na Letnich Igrzyskach (kolumna 'Total')
countries = selected_df['Unnamed: 0']
summer_medals = selected_df['Total']

# Tworzenie wykresu kołowego
plt.figure(figsize=(8, 8))
plt.pie(
    summer_medals,
    labels=countries,
    autopct='%.2f%%',         # Procenty z dokładnością do dwóch miejsc po przecinku
    startangle=90,            # Początek wykresu od góry
    colors=plt.cm.Set3.colors # Ładna paleta kolorów
)
# Tytuł wykresu
plt.title("Udział wybranych krajów w liczbie medali na Letnich Igrzyskach")
plt.axis('equal')  # Proporcje równego koła
# Zapis wykresu do pliku .tif
plt.savefig("medale_letnie_wykres.tif", format="tiff")
# Wyświetlenie wykresu
plt.show()
