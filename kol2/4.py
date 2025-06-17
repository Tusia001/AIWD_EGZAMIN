import matplotlib.pyplot as plt
import numpy as np
labels = [0, 1, 2, 3, 4]
A = np.array([50, 45, 48, 46, 44])
B = np.array([60, 55, 52, 53, 56])
C = np.array([55, 60, 62, 61, 58])

y = np.arange(len(labels))# Pozycje słupków

# Tworzenie wykresu poziomego słupkowego pogrupowanego (stacked)
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(y, A, color='tab:blue', label='A')
ax.barh(y, B, left=A, color='tab:green', label='B')
ax.barh(y, C, left=A + B, color='mediumorchid', label='C')

# Etykiety i tytuł
ax.set_xlabel('Wartości')
ax.set_title('Wykres słupkowy pogrupowany')
ax.set_yticks(y)
ax.set_yticklabels(labels)
ax.legend()

plt.tight_layout()

plt.savefig("wykres_slupkowy_pogrupowany.pdf", format="pdf")

plt.show()
