#W jednym pliku wykonaj poniższe czynności:
#załaduj dane z pliku koleje11.csv jako ramkę danych (Data frame),

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
kolej = pd.read_csv("koleje11.csv", sep=" ")

#uporządkuj dane, aby dane było zgodne z koncepcją czystych danych,
# cechy liczbowe w typach liczbowych, nagłówki powinny stanowi nazwy kolumn,
kolej2 = kolej.melt(id_vars=["Marka"], value_vars=kolej.columns[1:], var_name="Rok", value_name="Wartość")

#wybierz dane dot. Eurostar i SNCF do osobnych zmiennych odpowiednio,
kolej2["Rok"] = kolej2["Rok"].astype(int)
eurostar = kolej2[kolej2["Marka"] == "Eurostar"]
sncf = kolej2[kolej2["Marka"] == "SNCF"]
plt.subplot(1, 2, 1)
x1 = eurostar["Rok"]
y1 = eurostar["Wartość"]

# stwórz dwa wykresy słupkowe poziome na jednym rysunku (układ lewo - prawo) na podstawie przefiltrowanych danych, na obu osiach pionowych lata,
# dodaj na wykres siatkę, legendę, podpisz etykiety osi, tytuł, ustaw podziałkę na wszystkichosiach ręcznie. Wykres powinien być estetyczny i podpisany. Zapisz wykres w formacie png za pomocą kodu.
plt.barh(x1, y1, label="Eurostar")
plt.yticks(x1)
plt.xticks([0, 5000, 10000])
plt.grid(True)
plt.legend()
plt.ylabel("Rok")
plt.xlabel("Wartość")
plt.subplot(1, 2, 2)
x2 = sncf["Rok"]
y2 = sncf["Wartość"]

plt.barh(x2, y2, label="SNCF")
plt.yticks(x2)
plt.xticks([0, 5000, 10000])
plt.grid(True)
plt.legend()
plt.ylabel("Rok")
plt.xlabel("Wartość")
plt.suptitle("Dane o kolejach")
plt.tight_layout()
plt.savefig("w1.png")
plt.show()


