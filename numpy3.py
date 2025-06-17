#lab03 - 19.03 -numpy3

import numpy as np

# 1. Zamiana na wielkie litery
arr1 = np.array(["python", "NumPy", "data science", "machine learning"])
upper_arr1 = np.char.upper(arr1)
print("1:", upper_arr1)

# 2. Zamiana na małe litery i formatowanie tytułowe
arr2 = np.array(["PYTHON", "NUMPY", "DATA SCIENCE"])
lower_arr2 = np.char.lower(arr2)
title_arr2 = np.char.title(lower_arr2)
print("2:", title_arr2)

# 3. Połączenie dwóch tablic i dodanie spacji
arr3_1 = np.array(["machine", "deep"])
arr3_2 = np.array([" learning", " networks"])
joined_arr3 = np.char.add(arr3_1, arr3_2)
print("3:", joined_arr3)

# 4. Rozdzielenie tekstu po separatorze
arr4 = np.array(["python.data.science", "machine.learning"])
split_arr4 = np.char.split(arr4, ".")
print("4:", split_arr4)

# 5. Usunięcie białych znaków
arr5 = np.array([" python ", " numpy ", " pandas "])
stripped_arr5 = np.char.strip(arr5)
print("5:", stripped_arr5)

# 6. Iloczyn skalarny
a = np.array((2, 4, 6))
b = np.array((1, 3, 5))
dot_product = np.dot(a, b) #print(a@b)
print("6:", dot_product)

# 7. Mnożenie macierzowe
A = np.array([[2, 3], [1, 4]])
B = np.array([[5, 1], [2, 6]])
matrix_multiplication = np.matmul(A, B) #print(A@B)
print("7:", matrix_multiplication)

# 8. Rozwiązanie układu równań
A = np.array([[4, 2], [3, 5]])
B = np.array([8, 7])
solution_eq = np.linalg.solve(A, B)
print("8:", solution_eq)

# 9. Wyznacznik i macierz odwrotna
M = np.array([[6, 2], [3, 9]])
det_M = np.linalg.det(M)
inv_M = np.linalg.inv(M)
print("9:", det_M, inv_M)
print(M@np.linalg.inv(M))

# 10. Iloczyn zewnętrzny i wartości własne
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
outer_product = np.outer(v1, v2)
eig_values, eig_vectors = np.linalg.eig(outer_product)
print("10:", outer_product, eig_values, eig_vectors)

# 11. Indeksy i wartości elementów niezerowych
arr11 = np.array([[0, 5, 0], [2, 0, 3], [0, 0, 7]])
nonzero_indices = np.nonzero(arr11)
nonzero_values = arr11[nonzero_indices]
print("11:", nonzero_indices, nonzero_values)

#12. Zastąpienie wartości ujemnych
data = np.array([-3, 4, -1, 6, -8, 2])
replaced_data = np.where(data < 0, -99, data)
print("12:", replaced_data)

#13. Tworzenie tablicy
indices = np.array([2, 0, 1, 2, 0])
options = [np.array([10, 20, 30, 40, 50]),np.array([60, 70, 80, 90, 100]),
np.array([110, 120, 130, 140, 150])]

chosen_values = np.choose(indices, options)
print("13:", chosen_values)

# 14. Zmiana wartości na podstawie warunków
matrix = np.array([[5, 12, 8], [3, 7, 9], [15, 4, 2]])
conditions = [matrix < 5, (matrix >= 5) & (matrix <= 10), matrix > 10]
choices = [0, 50, 100]
modified_matrix = np.select(conditions, choices)
print("14:", modified_matrix)

# 15. Zmiana wartości
values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
np.putmask(values, values % 2 == 0, 0)
np.put(values, [0, 4, 8], [100, 200, 300])
print("15:", values)

'''Laboratorium NumPy II
Lista zadań
1. Mając tablicę A = np.array([3, 5, 7, 9]) oraz tablicę B = np.array([2, 4, 6, 8]),
wykonaj operację dzielenia elementów tablicy A przez odpowiadające im elementy
tablicy B.
2. Dla tablicy X = np.array([[1, 2, 3], [4, 5, 6]]) oraz skalara 3, dodaj skalar
do każdego elementu tablicy X.
3. Utwórz tablicę C = np.array([10, 20, 30, 40]) oraz jednowymiarową tablicę
D = np.array([1, 2, 3]). Spróbuj wykonać odejmowanie D od C. Wyjaśnij
wynik lub błąd, który wystąpił.
4. Mając tablicę dwuwymiarową M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
oraz jednowymiarową tablicę v = np.array([10, 20, 30]), dodaj v do każdego
wiersza M.
5. Dla tablicy Z = np.zeros((3, 4)) oraz tablicy ones = np.ones(4), wykonaj
operację dodawania ones do każdego wiersza tablicy Z.
6. Mając tablicę A = np.array([[1, 2, 3], [4, 5, 6]]) oraz tablicę B
B = np.array([10, 20]), wykonaj mnożenie, gdzie każdy wiersz tablicy A jest
pomnożony przez odpowiedni element tablicy B.
7. Dla tablicy temps = np.array([0, 10, 20, 30, 40]) (temperatury w stopniach
Celsjusza), zamień je na stopnie Fahrenheita używając wzoru F = C ·
9
5 + 32.
8. Mając tablicę data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), znajdź
pierwiastek kwadratowy z każdego elementu używając funkcji uniwersalnej.
9. Dla tablicy angles = np.array([0, π/6, π/4, π/3, π/2]), oblicz sinus, cosinus i
tangens dla każdego kąta.
10. Utwórz dwie tablice: A = np.array([[1, 2], [3, 4]]) oraz B = np.array([5, 6]),
a następnie wykonaj operację dzielenia modulo (%) każdego wiersza A przez tablicę
B.
11. Dla tablicy X = np.array([[2, 5, 8], [1, 3, 7], [4, 6, 9]]) oraz tablicy
Y = np.array([1, 2, 3]), znajdź maksimum pomiędzy każdym elementem X i
odpowiadającym elementem Y (zastosuj broadcasting).
12. Mając tablicę values = np.array([-3, -2, -1, 0, 1, 2, 3]), użyj funkcji uniwersalnej do znalezienia wartości bezwzględnej każdego elementu.
1
13. Dla tablicy A = np.array([[1, 2, 3], [4, 5, 6]]) i tablicy B
B = np.array([[10, 20, 30], [40, 50, 60]]), wykonaj operację potęgowania,
gdzie każdy element tablicy A jest podniesiony do potęgi odpowiadającego elementu
tablicy B.
14. Mając tablicę probabilities = np.array([0.1, 0.01, 0.001, 0.0001]), oblicz
logarytm naturalny i logarytm dziesiętny dla każdego elementu.
15. Dla tablicy dwuwymiarowej M = np.array([[1, 2, 3], [4, 5, 6]]) oraz wektora kolumnowego v = np.array([[10], [20]]), dodaj wektor v do każdej kolumny M (zwróć uwagę na kształt tablicy v).
2'''