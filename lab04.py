#lab 4 - Pandas I
import pandas as pd

#zad 1
#Utwórz serię zawierającą następujące wartości: [15, 28, 33, 47, 52, 61]. Następnie:
s = pd.Series([15, 28, 33, 47, 52, 61])

#- Wyświetl wartości serii za pomocą to_numpy()
print(s.to_numpy()) # s.values

#- Wyświetl typ danych zwróconych przez metodę to_numpy()
print(type(s.to_numpy())) # type(s.values)

#- Wyświetl wszystkie elementy większe niż 40 używając filtru logicznego
print(s[s > 40])


#Zadanie 2
#Utwórz serię na podstawie słownika
slownik = {'jabłka': 120, 'gruszki': 85, 'śliwki':
    95, 'banany': 140}
klucz = ['jabłka', 'gruszki', 'śliwki']
s = pd.Series(slownik, index=klucz)
#- Nadaj serii nazwę "Owoce" a indeksowi nazwę "Produkt"
s.name = "Owoce"
s.index.name = "Produkt"

#- Wybierz i wyświetl wartość dla klucza 'gruszki' używając notacji nawiasów kwadratowych
print("Wartość dla 'gruszki':", s['gruszki'])

#- Zmodyfikuj wartość dla klucza 'gruszki' na 110
s['gruszki'] = 110
print("Po modyfikacji 'gruszki':\n", s)

#- Pomnóż całą serię przez 2 i wyświetl wynik
print("Seria pomnożona przez 2:\n", s * 2)


#Zadanie 3 Masz słownik
d = {'klucz1': 50, 'klucz2': 100, 'klucz3': 150}
k = ['klucz0', 'klucz2', 'klucz3', 'klucz4']
seria = pd.Series(d, index=k)

#Utwórz serię korzystając ze słownika oraz listy kluczy jako indeksu. Następnie:

#- Wyświetl utworzoną serię
print(seria)

#- Wyjaśnij, jakie wartości mają klucze 'klucz0' i 'klucz4' i dlaczego
print("\nWartości 'klucz0' i 'klucz4' to NaN, ponieważ te klucze nie istnieją w słowniku, więc nie można było im przypisać wartości.")

#- Nadaj serii nazwę "Wartości" a indeksowi nazwę "Klucz"
seria.name = "Wartości"
seria.index.name = "Klucz"


#Zadanie 4 Utwórz ramkę danych na podstawie poniższych danych:
data = {'Student': ['Anna', 'Bartek', 'Celina', 'Daniel'],
'Matematyka': [4.5, 3.5, 5.0, 3.0],
'Fizyka': [4.0, 4.5, 3.5, 3.0],
'Informatyka': [5.0, 3.0, 4.5, 4.0]}

#Następnie: #- Utwórz ramkę danych z tymi danymi
df = pd.DataFrame(data)

#- Wyświetl kształt ramki danych używając atrybutu shape
print(df.shape)

#- Wyświetl indeks ramki używając atrybutu index
print(df.index)

#- Wyświetl kolumny ramki używając atrybutu columns
print(df.columns)

#- Użyj metody info() do wyświetlenia informacji o ramce danych
print(df.info())

#- Wyświetl liczbę niepustych wartości w każdej kolumnie za pomocą count()
print(df.count())


#Zadanie 5 Używając poniższych danych:
data = {'Kraj': ['Polska', 'Niemcy', 'Francja'],
'Stolica': ['Warszawa', 'Berlin', 'Paryż'],
'Populacja': [38000000, 83000000, 67000000]}

#Utwórz ramkę danych i wykonaj:
kraje = pd.DataFrame(data)

#- Wyświetl początkowy wiersz i początkową kolumnę
print(kraje.iloc[0, 0])

#- Wyświetl wiersz o indeksie 2
print(kraje.iloc[2,:]) #kraj.loc[2,:]

#- Wyświetl kolumnę 'Stolica'
print(kraje['Stolica'])
#- Wyświetl wartość w wierszu o indeksie 1 i kolumnie 'Stolica'
print(kraje.loc[1, 'Stolica'])


#Zadanie 6 Masz ramkę danych ze sprzedażą w regionach:
data = {'Region': ['Północ', 'Południe', 'Wschód', 'Zachód', 'Północ',
'Południe'],
'Produkt': ['A', 'A', 'A', 'A', 'B', 'B'],
'Sprzedaż': [150, 200, 130, 180, 220, 170]}
df = pd.DataFrame(data)

#Wykonaj następujące operacje:
#- Wyświetl kolumnę 'Sprzedaż'
print(df['Sprzedaż'])
#- Wyświetl wiersze, gdzie sprzedaż jest większa niż 180
print(df[df['Sprzedaż'] > 180])


#Zadanie 7 Korzystając z danych z ramki sprzedażowej:
data = {
'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
'Product': ['Electronics', 'Furniture', 'Clothing', 'Electronics',
'Furniture', 'Clothing'],
'Sales_Channel': ['Online', 'Retail', 'Online', 'Wholesale',
'Retail', 'Online'],
'Units_Sold': [120, 80, 200, 150, 90, 300],
'Revenue': [60.5, 45.0, 35.0, 70.0, 50.5, 55.0],
'Profit': [15.2, 12.0, 8.5, 20.5, 13.2, 10.0]
}
sales_df = pd.DataFrame(data)

#Wykonaj:
#- Wyświetl kolumnę 'Revenue'
print(sales_df['Revenue'])

#- Wybierz wiersze, gdzie 'Profit' jest większy niż 15.0
profit = sales_df[sales_df['Profit'] > 15.0]
print(profit)
#- Wyświetl tylko kolumnę Revenue wierszy z poprzedniego punktu.
print(profit['Revenue'])

#- Znajdź i wyświetl wiersz o najwyższym przychodzie (‘Revenue’)
najw = sales_df[sales_df['Revenue'] == sales_df['Revenue'].max()]
print(sales_df)

#- Dodaj nową kolumnę ‘Revenue_per_Unit’, która oblicza przychód na sprzedaną jednostkę (Revenue/Units_Sold)
sales_df['Revenue_per_Unit'] = sales_df['Revenue'] / sales_df['Units_Sold']
print(sales_df)








