import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
        "Podpis osi 1" : ['PL', 'DE', 'FR', 'SK'],
        'A' : [20, 41, 18, 42],
        'B' : [10, 22, 42, 23],
        'C' : [64, 70, 60, 58],
})

A = df['A']
B = df['B']
C = df['C']
os1 = df['Podpis osi 1']

Y = np.arange(len(os1))
plt.barh(Y, A, color='grey', height=0.25, label='A')
plt.barh(Y+0.25, B, color='orange', height=0.25, label='B')
plt.barh(Y+0.50, C, color='green', height=0.25, label='C')

plt.yticks(Y+0.25, os1)
plt.xlabel('podpis osi 2', color='green')
plt.legend()
plt.title("Wykres")
plt.grid(True)
plt.tight_layout()
plt.show()
