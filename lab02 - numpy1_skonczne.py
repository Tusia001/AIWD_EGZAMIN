import numpy as np
#numpy1
#1. Utwórz tablicę jednowymiarową zawierającą liczby parzyste od 0 do 20.
zad_1 = np.arange(0, 21, 2)
print(zad_1)

#2. Stwórz macierz 4×4 wypełnioną liczbami od 1 do 16 i wyświetl jej wymiar oraz kształt
zad_2 = np.arange(1, 17).reshape(4, 4)
wymiar = zad_2.ndim
kszatł = zad_2.shape

#3 Utwórz tablicę 5×5 wypełnioną liczbami od 1 do 25 i znajdź wartość maksymalną oraz minimalną.
zad_3 = np.arange(1, 26).reshape(5, 5)
mini = zad_3.min()
max = zad_3.max()

#4. Utwórz tablicę zawierającą 10 równomiernie rozłożonych wartości z przedziału [0,1]
zad_4 = np. linspace(0, 1, num = 10)

#5. Stwórz macierz jednostkową o wymiarach 3×3.
zad_5 = np.eye(3,3)

#6 Utwórz tablicę o wymiarach 3×4 zawierającą liczby od 1 do 12, a następnie zmień jej kształt na 2×6 bez modyfikacji danych
zad_6 = np.arange(1, 13).reshape(3, 4)
zad_6.reshape(2, 6)

#7 Utwórz dwie tablice: pierwszą zawierającą liczby od 1 do 5, a drugą zawierającą liczby od 6 do 10. Połącz je w jedną tablicę.

zad7a = np.arange(1,6)
zad7b = np.arange(6, 11)
zad7 = np.concatenate((zad7a, zad7b))

#8. Stwórz tablicę 3×3 wypełnioną zerami, a następnie zmień wszystkie elementy na przekątnej na wartość 1.

zad8 = np.zeros((3,3))
np.fill_diagonal(zad8, 1)

#9. Wygeneruj tablicę 10×10 zawierającą wartości od 0 do 99, a następnie wyodrębnij z niej podobszar 5×5 ze środka tablicy.
zad_9 = np.arange(0, 100).reshape(10, 10)
zad_9v = zad_9[3:8, 3:8]

#zad10 Utwórz tablicę zawierającą wartości ‘[5, 2, 8, 1, 9, 3, 7, 4, 6, 0]‘, a następnie znormalizuj ją tak, aby wartości były w przedziale [0, 1].
zad_10 = np.array([5, 2, 8, 1, 9, 3, 7, 4, 6, 0])
zad_10 = (zad_10 - zad_10.min()) / (zad_10.max() - zad_10.min())


#11. Utwórz dwie tablice: wektor ‘[1, 2, 3, 4, 5]‘ oraz macierz ‘[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]‘. Wykonaj operację dodawania wykorzystując broadcasting.
vec = np.array([1, 2, 3, 4, 5])
mat = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
zad11 = vec + mat

#12. Utwórz tablicę 4×4 wypełnioną liczbami od 1 do 16, a następnie transponuj ją.
zad12 = np.arange(1, 17).reshape(4, 4).T

#13. . Stwórz dwie tablice: pierwszą o kształcie (2,3) zawierającą liczby od 1 do 6, drugą o kształcie (3,4) zawierającą liczby od 1 do 12, a następnie wykonaj ich mnożenie
# macierzowe.
A = np.arange(1, 7).reshape(2, 3)
B = np.arange(1, 13).reshape(3, 4)
result = np.dot(A, B)  # lub: A @ B

#14. Utwórz tablicę (10,10) wypełnioną liczbami od 1 do 100 i oblicz sumę dla każdego wiersza oraz każdej kolumny.
zad14 = np.arange(1, 101).reshape(10,10)
sum_col = zad14.sum(axis=0)
sum_row = zad14.sum(axis=1)

#15. Utwórz wektor ‘[3, 8, 2, 5, 1, 4, 9, 7, 6, 0]‘, a następnie zamień wszystkie wartości mniejsze od średniej na 0.
zad15 = np.array([3, 8, 2, 5, 1, 4, 9, 7, 6, 0])
zad15[zad15<zad15.mean()] = 0
print(zad15)

#16. Stwórz dwie tablice: wektor ‘[10, 20, 30]‘ i macierz ‘[[1], [2], [3], [4]]‘, które można dodać dzięki mechanizmowi broadcastingu, i wykonaj dodawanie.
vec = np.array([10, 20, 30])
mat = np.array([[1], [2], [3], [4]])
result_16 = mat + vec
print(result_16)

#17. Utwórz macierz 5×5 zawierającą liczby ‘[8, 3, 9, 5, 1, 7, 2, 0, 6, 4, 15, 13, 19, 12, 11, 17, 14, 10, 16, 18, 25, 21, 23, 20, 22]‘, a następnie posortuj ją wzdłuż wierszy.data = [8, 3, 9, 5, 1, 7, 2, 0, 6, 4, 15, 13, 19, 12, 11, 17, 14, 10, 16, 18, 25, 21, 23, 20, 22]
data = [8, 3, 9, 5, 1, 7, 2, 0, 6, 4, 15, 13, 19, 12, 11, 17, 14, 10, 16, 18, 25, 21, 23, 20, 22]
zad_17 = np.array(data).reshape(5, 5)
sorted_rows = np.sort(zad_17, axis=1)
print(sorted_rows)

#18. Utwórz tablicę trójwymiarową (2×3×4) wypełnioną zerami i sprawdź liczbę wymiarów oraz liczbę elementów.
zad_18 = np.zeros((2, 3, 4))
print(zad_18.ndim)
print(zad_18.size)

#19. Utwórz dwie tablice o kształtach (3,1) zawierającą wartości ‘[[2], [4], [6]]‘ i (1,4) zawierającą wartości ‘[[1, 3, 5, 7]]‘, a następnie użyj broadcastingu do utworzenia tablicy 3×4 będącej ich iloczynem.
A = np.array([[2], [4], [6]])
B = np.array([[1, 3, 5, 7]])
result_19 = A * B
print(result_19)

#20. Utwórz tablicę 6×6 zawierającą liczby od 1 do 36, a następnie zmień jej kształt na (3, 4, 3) i oblicz średnią wzdłuż każdej osi.
zad_20 = np.arange(1, 37).reshape(6, 6)
reshaped_20 = zad_20.reshape(3, 4, 3)
print(reshaped_20.mean(axis=0))
print(reshaped_20.mean(axis=1))
print(reshaped_20.mean(axis=2))