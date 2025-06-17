import pandas as pd
from sqlite3 import connect

paliwo = pd.read_excel('data/cena_paliwa11.xlsx')

ceny = pd.read_excel('data/ceny21.xlsx')

daty1 = pd.read_csv('data/date_sale.csv')
daty1['Sale_Date'] = pd.to_datetime(daty1['Sale_Date'], format='%d-%m-%Y')

daty2 = pd.read_csv('data/date_temp.csv')
daty2['Reading_Date'] = pd.to_datetime(daty2['Reading_Date'])

gastro = pd.read_csv('data/gastro21.csv', header=None).T
gastro.columns = ['Typ', 'Rok', 'Wartość']
gastro['Rok'] = gastro['Rok'].astype(int)
gastro['Wartość'] = gastro['Wartość'].astype(int)

handel = pd.read_excel('data/handel25.xlsx')

kurs = pd.read_csv('data/kurs4.csv', sep=';', decimal=',')

conn = connect('data/lab_readings.db')
query = 'select * from readings'
odczyty = pd.read_sql(query, conn)
odczyty['measurement_time'] = pd.to_datetime(odczyty['measurement_time'])
#print(odczyty[odczyty['measurement_time'].dt.hour == 8])

pogoda = pd.read_csv('data/pogoda25.csv', sep=';')

conn = connect('data/sales_data2.db')
query = 'select * from sales_data'
sprzedaz1 = pd.read_sql(query, conn)
sprzedaz1['date'] = pd.to_datetime(sprzedaz1['date'])

conn = connect('data/sales_data3.db')
query = 'select * from sales'
sprzedaz2 = pd.read_sql(query, conn)
sprzedaz2['sale_date'] = pd.to_datetime(sprzedaz2['sale_date'])

sport = pd.read_csv('data/sport2.csv', sep = '#')
wynag = pd.read_csv('data/wynagrodzenia21.csv', sep =';', decimal = ',')
wynag_long = wynag.melt(id_vars='Wojedództwo', var_name='Rok', value_name='Wynagrodzenie')



