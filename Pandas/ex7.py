import pandas as pd

df_porduits = pd.read_csv("Pandas/produits.csv")
df_commandes = pd.read_csv("Pandas/commandes.csv")
df_clients = pd.read_csv("Pandas/clients.csv")

# print(df_clients)

commun1 =df_clients.columns.intersection(df_commandes.columns)
commun2 = df_porduits.columns.intersection(df_commandes.columns)
# print(commun2)


client_commandes = pd.merge(df_clients,df_commandes, on= 'client_id')
# print(client_commandes)
produit_commandes = pd.merge(client_commandes, df_porduits , on= 'produit')
# print(produit_commandes)

jointure1 = pd.merge(df_porduits, df_commandes , on="produit" , how="inner")
# print(jointure1)
jointure2 = pd.merge(df_commandes, df_clients, on="client_id", how="right")
jointure3 = pd.merge(df_commandes,df_clients, on="client_id" , how= 'left' )
jointure4 = pd.merge(df_commandes,df_clients, on="client_id" , how= 'outer')
jointure5 = pd.merge(df_commandes,df_porduits, on="produit"    , how="left")

concatenation = pd.concat([df_clients,df_commandes])
# print(concatenation)
print(df_commandes.shape)
print(concatenation.shape)
print(concatenation.head())
print(concatenation.isna().sum())


