#Na bazie danych z pliku ecom_campaigns.csv wykonaj wykres punktowy. Zadbaj o jego
#podpisanie i estetykę. Zapisz powstały wykres w formacie webp

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ecom_campaigns.csv")

plt.figure()
plt.scatter(df['visits_campaign_A'], df['orders_campaign_A'], label='Kampania A', marker='o', color='blue')
plt.scatter(df['visits_campaign_B'], df['orders_campaign_B'], label='Kampania B', marker='o', color='green')
plt.scatter(df['visits_campaign_C'], df['orders_campaign_C'], label='Kampania C', marker='o', color='red')

plt.title('Zamówienia względem wizyt dla kampanii marketingowych')
plt.xlabel('Liczba wizyt')
plt.ylabel('Liczba zamówień')
plt.legend(title='Kampania')
plt.grid(True)

plt.savefig('ecom_campaigns_wykres.webp', format='webp')
plt.show()



