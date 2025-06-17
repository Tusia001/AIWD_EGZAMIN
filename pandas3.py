# SKONCZYC
# Zadanie 1: Obliczanie miar położenia
# Utwórz ramkę danych zawierającą informacje o wynikach egzaminów studentów i oblicz
# średnią arytmetyczną, medianę i modę dla każdej kolumny.

import pandas as pd
# Utwórz ramkę danych
dane_studentow = pd.DataFrame({
'Student': ['Anna', 'Bartek', 'Celina', 'Dawid', 'Ewa', 'Filip',
'Gosia', 'Hubert'],
'Matematyka': [85, 90, 78, 92, 88, 76, 94, 85],
'Fizyka': [76, 88, 90, 75, 82, 84, 91, 76],
'Informatyka': [92, 85, 88, 95, 80, 75, 89, 92]
})
# Oblicz średnią, medianę i modę dla kolumn z ocenami
print('srednia matematyka', dane_studentow['Matematyka'].mean())
print('mediana fizyka ', dane_studentow['Fizyka'].median())
#print(dane_studentow.mode()

# skonczyc Zadanie 2: Porównanie miar położenia
#Stwórz dwie serie danych o różnych rozkładach i porównaj dla nich średnią, medianę i dominantę.

import pandas as pd
# Utwórz dwie serie danych
dane_symetryczne = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90])
dane_skosne = pd.Series([10, 15, 18, 20, 22, 25, 30, 80, 90])
# Oblicz i porównaj miary położenia

# Obliczenia dla danych symetrycznych
srednia_sym = dane_symetryczne.mean()
mediana_sym = dane_symetryczne.median()
moda_sym = dane_symetryczne.mode()

# Obliczenia dla danych skośnych
srednia_sko = dane_skosne.mean()
mediana_sko = dane_skosne.median()
moda_sko = dane_skosne.mode()

# Wyświetlenie wyników
print("DANE SYMETRYCZNE:")
print("Średnia:", srednia_sym)
print("Mediana:", mediana_sym)
print("Moda:", moda_sym.tolist())

print("\nDANE SKOŚNE:")
print("Średnia:", srednia_sko)
print("Mediana:", mediana_sko)
print("Moda:", moda_sko.tolist())

#Zadanie 3: Analiza kwartyli
#Stwórz ramkę danych z informacjami o cenach produktów i oblicz kwartyle dla tych cen
import pandas as pd
# Utwórz ramkę danych z cenami produktów
ceny_produktow = pd.DataFrame({
'Produkt': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
'Cena': [25, 35, 40, 45, 50, 55, 60, 75, 90, 120]
})

# Oblicz kwartyle cen / zrobbic wg lekcji

kwartyl_1 = ceny_produktow['Cena'].quantile(0.25)  # Pierwszy kwartyl (Q1)
mediana = ceny_produktow['Cena'].median()          # Mediana (Q2)
kwartyl_3 = ceny_produktow['Cena'].quantile(0.75)  # Trzeci kwartyl (Q3)

# Wyświetl wyniki
print("Pierwszy kwartyl (Q1):", kwartyl_1)
print("Mediana (Q2):", mediana)
print("Trzeci kwartyl (Q3):", kwartyl_3)

#Zadanie 4: Miary zmienności
#Utwórz ramkę danych z wynikami pomiarów i oblicz różne miary zmienności: rozstęp,
#odchylenie standardowe i wariancję.
import pandas as pd
# Utwórz ramkę danych z wynikami pomiarów
pomiary = pd.DataFrame({
'Próbka': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
'Wynik1': [45, 47, 49, 51, 46, 48, 50, 52],
'Wynik2': [120, 150, 110, 190, 200, 115, 140, 180]
})
# Oblicz miary zmienności dla każdej kolumny z wynikami
for kol in ['Wyniki1', 'Wyniki2']:
    print(f"\n{kol}: ")
    print(" Rozstęp ", pomiary[kol].max()-pomiary[kol].min())
    print(" Odchylenie standardowe: ", pomiary[kol].std())
    print(" Wariacja: ", pomiary[kol].vear(), "\n")


# Uzupełnij kod

#Zadanie 5: Analiza asymetrii i koncentracji
#Stwórz trzy różne serie danych (o asymetrii lewostronnej, symetryczne i o asymetrii
#prawostronnej) i oblicz dla nich współczynniki asymetrii i kurtozy.
import pandas as pd
import numpy as np
# Utwórz trzy serie danych o różnych rozkładach
dane_lewostronne = pd.Series([90, 85, 82, 81, 80, 79, 75, 70, 65, 50])
dane_symetryczne = pd.Series([50, 60, 65, 70, 75, 80, 85, 90, 95, 100])
dane_prawostronne = pd.Series([50, 55, 60, 65, 70, 75, 76, 78, 85, 95])
# Oblicz współczynniki asymetrii i kurtozy
# Uzupełnij kod
