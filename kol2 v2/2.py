import pandas as pd
import matplotlib.pyplot as plt
# Wczytanie danych z pliku Excel
df = pd.read_excel('film15.xlsx')

# Filtrowanie danych tylko dla filmów typu "comedy"
comedy_df = df[df['Type'] == 'comedy']

# Tworzenie wykresu słupkowego
plt.figure(figsize=(10, 6))
plt.bar(comedy_df['Year'], comedy_df['Value'], color='skyblue')

# Dodanie tytułu i etykiet osi
plt.title('Produkcja filmów komediowych w latach')
plt.xlabel('Rok')
plt.ylabel('Liczba filmów')

# Dodanie siatki z liniami poziomymi
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Zapisanie wykresu do pliku PDF
plt.savefig('wykres_komedie.pdf', format='pdf')
plt.show()
