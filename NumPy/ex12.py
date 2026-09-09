# Nettoyage d'un dataset avec valeurs manquantes

import numpy as np

data = np.array([
    22.5,
    23.1,
    np.nan,
    21.8,
    np.nan,
    24.0,
    23.5
])
print(np.isnan(data))
print(np.isfinite(data))
print(np.nanmean(data))
data = np.where(np.isnan(data) , 0 , data)
print(data)