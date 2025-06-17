import matplotlib.pyplot as plt

# Dane
labels = ['Odzieżowe', 'Spożywcze', 'Meblowe','Inne']
sizes = [24.8, 13.0, 6.7, 55.5]
colors = ['lightcoral', 'lightskyblue', 'lightgreen','lavender',  ]
explode = (0.1, 0, 0, 0)  # wysunięcie dla 'Odzieżowe'

# Wykres
plt.figure(figsize=(7, 6))
plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    shadow=True,
    startangle=10,
    wedgeprops={'edgecolor': 'gray'}
)

plt.title("Wyniki sprzedaży - II-IV 2017")
plt.axis('equal')  # Równe proporcje
plt.show()
