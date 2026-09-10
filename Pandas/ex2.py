import pandas as pd

df = pd.read_csv('Pandas/clients.csv')


# print(df.loc[0:,"nom"])
# print(df.loc[0:,("nom","age" , "ville")])
# print(df.iloc[0:3])
# print(df[df['age'] > 30])
# print(df[df['salaire'] > 6000])
# print(df[df['ville'] == 'Casablanca'])
# print(df[(df['sexe'] == "F") & (df['age'] > 30)])
# print(df[(df['ville'] == 'Casablanca') | (df['ville'] =='Rabat')])
# print(df[df['ville'].isin(['Casablanca', 'Fes', 'Marrakech'])])
# print(df[df["age"].between(25,35)])
# print(df[~(df['ville']== 'Casablanca')])
# print(df.loc[0: ,"ville"])
print(df.iloc[3:6])