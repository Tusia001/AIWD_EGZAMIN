import pandas as pd
import matplotlib.pyplot as plt
from PIL.ImageOps import scale

# Przybliżone dane ręczne, pasujące do wysokości słupków z obrazu
# Wpisujemy tyle wartości, ile wskazuje liczba pomiarów na wykresie
czasy_reakcji = (
    [50] * 90 +     # 0–100 ms → 90 pomiarów
    [150] * 35 +    # 100–200 ms → 35
    [250] * 15 +    # 200–300 ms → 15
    [350] * 10 +    # 300–400 ms → 10
    [450] * 5 +     # 400–500 ms → 5
    [550] * 3 +     # 500–600 ms → 3
    [650] * 2 +     # 600–700 ms → 2
    [800] * 2       # 700–850 ms → 2
)

# Tworzymy ramkę danych
df = pd.DataFrame({'Czas reakcji (ms)': czasy_reakcji})

# Tworzymy wykres
plt.figure(figsize=(10, 7))

plt.hist(
    df['Czas reakcji (ms)'],
    bins=[0, 100, 200, 300, 400, 500, 600, 700, 850],
    #edgecolor='black',
    color='tab:blue'
)

plt.title('Histogram czasów reakcji', fontweight='bold')
plt.xlabel('Czas reakcji (ms)')
plt.ylabel('Liczba pomiarów')
plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.6)

plt.tight_layout()
plt.savefig('histogram_reakcji.webp', format='webp', dpi=300)
plt.show()
