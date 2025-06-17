#1
import pandas as pd
df = pd.read_excel('cena_paliwa11.xlsx')
df1 = df[df['Podzaj paliwa']=='Benzyna 95']
df2=pd.pivot_table(df1, index='Miesiące', columns='Rok', values='Wartość', sort =False)
x = df2.index
y1=df2[2015]
y2=df2[2016]
plt.figure(figsize=(8,8))
plt.plot(x, y1, linestyle='--', color='orange', linewidth=3, label='2015')
plt.plot(x, y2, linestyle='--', color='purple', linewidth=2, label='2015')
plt.grid(True)
plt.legend(loc='lower left')
plt.savefig('ds2.png')
plt.show()
