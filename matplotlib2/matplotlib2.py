#2 . Odwzoruj wykres z pliku f92.png. Zapisz docelowy wykres w formacie tiff.
import matplotlib.pyplot as plt


predkosc = [40, 60, 80, 100, 120]
samochod_osobowy = [8.5, 7.2, 6.3, 5.8, 6.1]
suv = [9.5, 8.7, 7.9, 7.2, 7.5]
ciezarowka = [12, 11, 10, 10.5, 9]

plt.figure(figsize=(8, 6))

plt.scatter(predkosc, samochod_osobowy, label='Samochód osobowy', color='green', marker='s', s=100)
plt.scatter(predkosc, suv, label='SUV', color='orange', marker='D', s=100)
plt.scatter(predkosc, ciezarowka, label='Ciężarówka', color='brown', marker='^', s=100)

plt.title('Zużycie paliwa vs prędkość dla różnych typów pojazdów')
plt.xlabel('Prędkość [km/h]')
plt.ylabel('Zużycie paliwa [l/100km]')
plt.legend(title='Typ pojazdu')
plt.grid(True)


plt.savefig('zuzycie_paliwa_wykres.tiff', format='tiff')
plt.show()

