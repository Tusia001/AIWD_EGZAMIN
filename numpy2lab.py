import numpy as np

# Zadanie 1: Dzielenie elementów tablicy A przez odpowiadające im elementy tablicy B
A = np.array([3, 5, 7, 9])
B = np.array([2, 4, 6, 8])
wynik1 = A / B
print("Wynik 1:", wynik1)

# Zadanie 2: Dodanie skalara do każdego elementu tablicy X
X = np.array([[1, 2, 3], [4, 5, 6]])
skalar = 3
wynik2 = X + skalar
print("Wynik 2:\n", wynik2)

# Zadanie 3: Odejmowanie tablicy D od C
C = np.array([10, 20, 30, 40])
D = np.array([1, 2, 3])
try:
    wynik3 = C - D
except ValueError as e:
    wynik3 = str(e)
print("Wynik 3:", wynik3)

# Zadanie 4: Dodanie v do każdego wiersza M
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([10, 20, 30])
wynik4 = M + v
print("Wynik 4:\n", wynik4)

# Zadanie 5: Dodanie ones do każdego wiersza tablicy Z
Z = np.zeros((3, 4))
ones = np.ones(4)
wynik5 = Z + ones
print("Wynik 5:\n", wynik5)

# Zadanie 6: Mnożenie, gdzie każdy wiersz tablicy A jest pomnożony przez odpowiedni element tablicy B
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20])
wynik6 = A * B[:, np.newaxis]
print("Wynik 6:\n", wynik6)

# Zadanie 7: Konwersja temperatury z Celsjusza na Fahrenheita
temps = np.array([0, 10, 20, 30, 40])
wynik7 = temps * (9/5) + 32
print("Wynik 7:", wynik7)

# Zadanie 8: Pierwiastek kwadratowy z każdego elementu tablicy data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
wynik8 = np.sqrt(data)
print("Wynik 8:\n", wynik8)

# Zadanie 9: Sinus, cosinus i tangens dla kątów
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
sin_values = np.sin(angles)
cos_values = np.cos(angles)
tan_values = np.tan(angles)
print("Wynik 9 - Sinus:\n", sin_values)
print("Wynik 9 - Cosinus:\n", cos_values)
print("Wynik 9 - Tangens:\n", tan_values)

# Zadanie 10: mod
A = np.arange(1, 17).reshape(4,4)
B = np.arange(2,6)
wynik10 = A % B
print("Wynik 10:\n", wynik10)

# Zadanie 11: Maksimum pomiędzy każdym elementem X i odpowiadającym elementem Y
X = np.array([[2, 5, 8], [1, 3, 7], [4, 6, 9]])
Y = np.array([1, 2, 3])
wynik11 = np.maximum(X, Y[:, np.newaxis])
print("Wynik 11:\n", wynik11)

# Zadanie 12: Wartość bezwzględna każdego elementu tablicy values
values = np.array([-3, -2, -1, 0, 1, 2, 3])
wynik12 = np.abs(values)
print("Wynik 12:", wynik12)

# Zadanie 13: Potęgowanie tablicy A do potęgi elementów tablicy B
A = np.arange(1,7).reshape(2,3)
B = np.arange(10, 61, 10).reshape(2,3)
wynik13 = A**A
print("Wynik 13:\n", wynik13)

# Zadanie 14: Logarytm naturalny i logarytm dziesiętny dla probabilities
probabilities = np.array([0.1, 0.01, 0.001, 0.0001])
log_naturalny = np.log(probabilities)
log_dziesietny = np.log10(probabilities)
print("Wynik 14 - Logarytm naturalny:\n", log_naturalny)
print("Wynik 14 - Logarytm dziesiętny:\n", log_dziesietny)

# Zadanie 15: Dodanie wektora kolumnowego v do każdej kolumny tablicy M
M = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([[10], [20]])
wynik15 = M + v
print("Wynik 15:\n", wynik15)



