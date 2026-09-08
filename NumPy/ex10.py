# Filtrer un dataset avec des conditions

import numpy as np
# (âge, salaire, ancienneté, dépenses)

clients = np.array([
    [22, 2500, 1, 1200],
    [45, 3200, 3, 1500],
    [30, 4500, 6, 2000],
    [28, 3800, 4, 1700],
    [35, 5200, 10, 2500],
    [24, 2800, 2, 1300]
])

filtred = clients[(clients[: , 0] > 30) & (clients[: , 1] >=3200)]

print(filtred)
print("Nombre :", len(filtred))