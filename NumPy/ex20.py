import numpy as np

data = np.array([
    [18, 2500, 300],
    [25, 4000, 500],
    [32, 6500, 800],
    [45, 9000, 1200],
    [52, 12000, 1500],
    [60, 18000, 2000]
])

# [âge, salaire, dépenses]

data_max = np.max(data, axis=0)
data_min = np.min(data, axis=0)

data_norm = (data - data_min) / (data_max - data_min)
print(data_norm)

z = (data - data.mean(axis =0)) / data.std(axis =0)

print("Données originales :")
print(data)

print("Moyenne des données originales :")
print(data.mean(axis=0))

print("Moyenne après standardisation :")
print(z.mean(axis=0))

print("Écart-type après standardisation :")
print(z.std(axis=0))