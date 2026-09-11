import pandas as pd

df = pd.read_csv("Pandas/employes.csv")

salaire_moyenne_departement = df.groupby("departement")["salaire"].mean()
# print(salaire_moyenne_departement)

df["salaire_moyenne_departement"] = (df.groupby("departement")["salaire"].transform("mean"))
# print(df)

df["ecart_au_salaire_moyen"] = df["salaire"] - df["salaire_moyenne_departement"]

df["performance_moyenne"] = df.groupby("departement")["performance"].transform("mean")

max_salaire_par_departement = df[df["salaire_moyenne_departement"]< df["salaire"]]
# print(max_salaire_par_departement)

statistics = df.groupby("departement").agg({
    "salaire" : ["max" , "min"],
    "performance" : ["max" , "min"]
})
# print(statistics)

df["niveau_performance"] = df["performance"].apply(lambda nv: "Faible" if nv <30 else "Moyenne" if nv < 85 else "Bonne" )
print(df)