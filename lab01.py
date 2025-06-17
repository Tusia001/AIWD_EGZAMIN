numbers = [3, 7, 2, 8, 5, 10]
print(numbers)
numbers.append(12)
numbers.remove(7)
numbers.sort()
print(min(numbers))
print(numbers)

# lish com
numbers = [12, 5, 8, 3, 17, 24, 1, 9]
even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)

# 1.3
numbers1 = [1, 2, 3, 4, 5]
kwadraty = [i ** 2 for i in numbers1]
print(kwadraty)

# 1.4
slowa = ['Python', 'is', 'great']
dlugosc = [len(i) for i in slowa]
print(dlugosc)

# 1.5
values = [4, 2, 8, 4, 2, 9, 1, 8]
unikalne = []
[unikalne.append(num) for num in values if num not in unikalne]
print(list(dict.fromkeys(values)))
print(unikalne)

# 1.6
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
srodkowy_element = matrix[1][1]
print(srodkowy_element)

suma_elementów = sum(sum(wiersz) for wiersz in matrix)
print(suma_elementów)

# KROTKI
# 1.7
data = (10, 20, 30, 40, 50)
a = list(data)
a[1] = 25
data = tuple(a)
print(data)

cortinates = (15.5, 42.3)
x, y = cortinates
print(x, y)

a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)
print(3 in a)

# slowniki
# 10
student = {"name": "Anna", "age": 22, "major": "Computer Science"}

student["grades"] = [4.5, 5.0, 3.5]

student["age"] = 23

del student["major"]

# 11
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = {word: words.count(word) for word in set(words)}
print(word_counts)

# 12
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# slownik zagniezdzony
# 13
students = {
    "Alice": {"math": 4, "english": 5, "history": 3},
    "Bob": {"math": 3, "english": 3, "history": 4}
}

students["Charlie"] = {"math": 5, "english": 4, "history": 5}
average_grades = {student: sum(grades.values()) / len(grades) for student, grades in students.items()}
averages = {name: sum(grades.values() / len(grades)}
print(average_grades)

# 14
colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
reversed_colors = {value: key for key, value in colors.items()}
print(reversed_colors)

# 15
numbers = {"a": 2, "b": 3, "c": 4}
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)
