import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
    'os1' : ['SK', 'FR', 'DE', 'PL'],
    'A' : [42, 28, 41, 20],
    'B' : [23, 41, 21, 10],
    'C' : [58, 60, 70, 62],
})

A = df['A']
B = df['B']
C = df['C']
os1 = df['os1']
y =np.arange(len(os1))

plt.figure(figsize=(8, 6))
plt.barh(y, A, color = 'gray', height = 0.25, label='A')
plt.barh(y + 0.25, B, color = 'orangered', height = 0.25, label='B')
plt.barh(y + 0.50, C, color = 'olive', height = 0.25, label='C')

plt.yticks(y + 0.25, os1)  # Centrowanie etykiet względem grupy słupków
plt.title('Wykres')
plt.xlabel('Podpis osi 2', color='green')
plt.ylabel('Podpis osi 1', color='red')

# Siatka i legenda
plt.grid(axis='x', alpha=0.5)
plt.legend()

# Optymalny układ
plt.tight_layout()
plt.show()

