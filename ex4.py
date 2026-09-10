import pandas as pd

df = pd.read_csv('Pandas/ventes.csv')

df["chiffre_affaires"] = df["prix"] * df["quantite"]

df["prix_avec_tva"] = df["prix"] * 1.2

df["categorie_prix"] = df["chiffre_affaires"].apply(
    lambda ca: "Faible" if ca < 1000
    else "Moyen" if ca <= 5000
    else "Élevé"
)

df["date"] = pd.to_datetime(df["date"])

df["mois"] = df["date"].dt.month
print(df)