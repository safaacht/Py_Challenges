# Détection des valeurs anormales

import numpy as np

# Mesures normales + quelques valeurs extrêmes
temperature = np.array([
    22.5, 23.1, 21.8, 22.9, 23.4,
    22.7, 24.0, 21.9, 85.0, 23.2,  # 85 = valeur anormale
    22.6, 23.0, -20.0, 22.8, 23.5  # -20 = valeur anormale
])

val_normal = temperature[temperature > 0]
suspectes = temperature[np.where((temperature < 0) | (temperature > 50 ))]
position_suspectes = np.argwhere((temperature < 0) | (temperature > 50 ))

hors_seuil = len(suspectes)
print(position_suspectes)