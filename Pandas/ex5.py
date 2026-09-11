import pandas as pd

df = pd.read_csv('Pandas/ventes.csv')


df["chiffre_affaires"] = df["prix"] * df["quantite"]
chiffre_affaires_total = df["chiffre_affaires"] .sum()
chiffre_affaires_moyenne = df["chiffre_affaires"] .mean()

# print(df["chiffre_affaires"].describe())


# Analyse par ville
ca_total_par_ville = df.groupby("ville")["chiffre_affaires"].sum()
ca_moyenne_par_ville = df.groupby("ville")["chiffre_affaires"].mean()

# print(ca_moyenne_par_ville)

ventes_par_ville = df.groupby("ville").size()
# print(ventes_par_ville)


# Analyse par produit
quantite_par_produit = df.groupby("produit")["quantite"].sum()
# print(quantite_par_produit)

ca_total_produit = df.groupby("produit")["chiffre_affaires"].sum()
# print(ca_par_produit)

produit_generant = ca_total_produit.idxmax()
# print(produit_generant , ": " ,ca_total_produit.max())

# Analyse avancée
print(df.groupby("ville").agg({
    "quantite" : ["sum" , "max"],
    "prix" : ["max", "min" , "sum"]
}))