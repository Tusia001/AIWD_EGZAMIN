#Odwzoruj wykres z pliku g11.png. Zapisz docelowy wykres w formacie png.

import matplotlib.pyplot as plt
    
godziny_nauki = [2, 3, 4, 5, 6, 7, 8]
wynik_egzaminu = [50, 55, 65, 70, 75, 80, 85]

plt.figure(figsize=(8, 6))
plt.scatter(
    godziny_nauki,
    wynik_egzaminu,
    s=100,
    color='dodgerblue',
    edgecolor='black',
    linewidth=1.5
)

plt.title('Zależność między godzinami nauki a wynikiem egzaminu')
plt.xlabel('Godziny nauki')
plt.ylabel('Wynik egzaminu (%)')
plt.grid(False)

plt.savefig('wykres_g11_odtworzony.png', format='png')
plt.show()
