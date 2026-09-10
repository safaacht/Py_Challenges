import pandas as pd

df = pd.read_csv('Pandas/clients.csv')
# df2 = df.to_csv('Pandas/test.csv', index=False)
# print(df2)

first_lines = df.head()
last_lines = df.tail()
# print(first_lines)
# print("===========")
# print(last_lines)

shape = df.shape
# print(shape)

label = df.loc[0:,"nom"]
# print(label)

indexes = df.iloc[0:5]
# print(indexes)

# type_donnees = df.info()

statistics = df.describe()
# print(statistics)

# print(df.dtypes)

ville_unique = df['ville'].unique()
# print(ville_unique)

ville_diff = df['ville'].nunique
# print(ville_diff)


clients_par_ville = df.groupby('ville').size()
# print(clients_par_ville)

valeurs_manquantes = df.isna()
print(valeurs_manquantes)