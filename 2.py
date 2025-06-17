#W jednym pliku wykonaj poniższe czynności: ● załaduj dane z pliku ceny23.csv jako ramkę danych (Data Frame),
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('ceny23.csv', sep=";", decimal=",")

#● stwórz wykres liniowy za pomarańcze, kolor i styl linii mają być inne niż domyślne
df1=df[df["Rodzaje towarów i usług"].str.contains('pomarańcze')]
plt.figure(figsize=(10,8))
plt.plot(df1['Miesiące'], df1['Wartosc'], linestyle='--', color='orange', linewidth=4, label)


