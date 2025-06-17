import numpy as np
import matplotlib.pyplot as plt
dni = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek']

stacja_a = np.array([100000, 300000, 800000, 200000])
stacja_b = np.array([150000, 250000, 300000, 400000])
stacja_c = np.array([200000, 500000, 400000, 700000])
plt.figure(figsize = (6,4))
plt.plot(dni, stacja_a,linestyle='--' ,color='red', label="Stacja A")
plt.plot(dni, stacja_b, linestyle='dashdot', color='green', label="Stacja B")
plt.plot(dni, stacja_c, linestyle=':', color='blue', label="Stacja C")


plt.xlabel("Dzień tygodnia")
plt.ylabel("Liczba widzów")
plt.title("Oglądalność stacji TV w ciągu 4 dni")

plt.legend()
plt.savefig("stacja_a.jng", format="jpg")
plt.show()