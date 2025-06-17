import pandas as pd

data = pd.read_csv('gastro21.csv', header=None).T
data.columns = ["Typ", "Rok", "Wartość"]
data["Rok"] = data["Rok"].astype(int)
data["Wartość"] = data["Wartość"].astype(int)