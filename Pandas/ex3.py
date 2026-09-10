import pandas as pd

df = pd.read_csv('Pandas/clients_dirty.csv')

valeurs_manquantes = df.isna()
# print(valeurs_manquantes)

doublons = df.duplicated()
# print(doublons)

df = df.drop_duplicates()

df['nom'] = df['nom'].str.strip()
df['ville'] = df['ville'].str.strip()
df["ville"] = df['ville'].str.lower()

df = df.replace('N/A' , pd.NA)
df = df.fillna(0)

df['age'] = df['age'].astype(int)

df['salaire'] = df['salaire'].str.replace('DH' , "")
df['salaire'] = pd.to_numeric(df['salaire'])

df.loc[df["salaire"] < 0, "salaire"] = pd.NA

df['date_inscription'] = pd.to_datetime(df['date_inscription'] )

# print(df.dtypes)
# print(df.shape[0])
print(df)