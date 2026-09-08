# Analyse automatique des performances
import numpy as np


ventes = np.array([
    [1200, 10],
    [2500, 5],
    [1800, 15],
    [3200, 8],
    [950, 20],
    [4100, 7],
    [2750, 12],
    [1600, 10]
])

montants =ventes[: , 0]
remise = ventes[: , 1]

tva =( montants  *20 )/ 100

# print(tva)

ca_apres_remise = montants - (montants * remise / 100)
# print(ca_apres_remise)

ca_avec_tva = ca_apres_remise + (ca_apres_remise * 20/100)
print(ca_avec_tva)

