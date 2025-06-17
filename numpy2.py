import numpy as np

# 1. Dzielenie elementów tablicy A przez elementy tablicy B
A = np.array([3, 5, 7, 9])
B = np.array([2, 4, 6, 8])
print(A / B)

# 2. Dodanie skalara 3 do każdego elementu tablicy X
X = np.array([[1, 2, 3], [4, 5, 6]])
print(X + 3)

# 3. Próba odejmowania tablicy D od C (broadcasting lub błąd)
C = np.array([10, 20, 30, 40])
D = np.array([1, 2, 3])
# print(C - D)  # powoduje ValueError: operands could not be broadcast together

# 4. Dodanie wektora v do każdego wiersza macierzy M
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([10, 20, 30])
print(M + v)

# 5. Dodanie jednowymiarowej tablicy ones do każdego wiersza tablicy Z
Z = np.zeros((3, 4))
ones = np.ones(4)
print(Z + ones)

# 6. Mnożenie wierszy tablicy A przez odpowiednie elementy tablicy B
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20])
print(A * B[:, np.newaxis])

# 7. Konwersja temperatur z Celsjusza na Fahrenheita
temps = np.array([0, 10, 20, 30, 40])
F = temps * 9 / 5 + 32
print(F)

# 8. Pierwiastkowanie każdego elementu tablicy data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.sqrt(data))

# 9. Obliczenie sinusa, cosinusa i tangensa dla wartości w tablicy angles
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print(np.sin(angles))
print(np.cos(angles))
print(np.tan(angles))

# 10. Dzielenie modulo każdego wiersza A przez tablicę B
A = np.array([[1, 2], [3, 4]])
B = np.array([5, 6])
print(A % B)

# 11. Maksimum pomiędzy każdym elementem X i odpowiadającym elementem Y (broadcasting)
X = np.array([[2, 5, 8], [1, 3, 7], [4, 6, 9]])
Y = np.array([1, 2, 3])
print(np.maximum(X, Y))

# 12. Wartość bezwzględna każdego elementu tablicy values
values = np.array([-3, -2, -1, 0, 1, 2, 3])
print(np.abs(values))

# 13. Potęgowanie elementów A do potęgi elementów B
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[10, 20, 30], [40, 50, 60]])
print(A ** B)

# 14. Logarytm naturalny i dziesiętny z każdego elementu tablicy probabilities
probabilities = np.array([0.1, 0.01, 0.001, 0.0001])
print(np.log(probabilities))
print(np.log10(probabilities))

# 15. Dodanie wektora kolumnowego v do każdej kolumny tablicy M
M = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([[10], [20]])
print(M + v)
