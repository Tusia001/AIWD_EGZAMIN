import matplotlib.pyplot as plt
import numpy as np

data = np.array([
[23, 45, 12, 34, 56],
[33, 54, 22, 43, 66],
[12, 34, 15, 28, 39],
[44, 55, 31, 47, 62]
])

days = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek']
hours = ['9–11', '11–13', '13–15', '15–17', '17–19']

plt.figure(figsize=(8, 6))
cax = plt.imshow(data, cmap='Greens')

plt.xticks(ticks=np.arange(len(hours)), labels=hours, rotation=45, ha='right')
plt.yticks(ticks=np.arange(len(days)), labels=days)

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        plt.text(j, i, str(data[i, j]), ha='center', va='center', color='black')

plt.tick_params(axis='both', direction='in', length=3   , width=1, colors='black')

cb = plt.colorbar(cax, orientation='vertical', label='Liczba klientów')
cb.ax.tick_params(direction='in', length=6, width=1, colors='black')

plt.title('Liczba klientów w sklepie wg dnia i godziny')

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')

# Siatka dla lepszej czytelności
plt.grid(True, linestyle='--', alpha=0.7)

# Dobre rozmieszczenie elementów
plt.tight_layout()

# Zapis do pliku TIFF
plt.savefig('liczba_klientow.tiff', format='tiff', dpi=300, bbox_inches='tight')

# Wyświetlenie
plt.show()