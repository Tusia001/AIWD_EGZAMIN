#7. Odwzoruj wykres z pliku g12.png. Zapisz docelowy wykres w formacie webp.

import matplotlib.pyplot as plt

godziny_alpha = [9, 10, 12, 13, 14, 16]
winrate_alpha = [58, 55, 60, 64, 63, 67]

godziny_omega = [8, 10, 11, 12, 13, 14, 15]
winrate_omega = [50, 56, 57, 62, 60, 62, 65]

plt.figure(figsize=(8, 6))
plt.scatter(godziny_alpha, winrate_alpha, label='Team Alpha', color='dodgerblue', marker='o', s=100)
plt.scatter(godziny_omega, winrate_omega, label='Team Omega', color='orange', marker='s', s=100)

plt.title('Trening vs Win-Rate w Esportowych Drużynach')
plt.xlabel('Godziny treningu w tygodniu')
plt.ylabel('Win-Rate (%)')
plt.legend(title='Drużyny')
plt.ylim(top=70)
plt.grid(False)

plt.savefig("trening_winrate_wykres.webp", format='webp')
plt.show()
