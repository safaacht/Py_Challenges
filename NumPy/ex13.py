#  Nettoyage et validation des données

import numpy as np

data = np.array([
    22.5,
    25.0,
    -5.0,   
    30.2,
    np.nan,  
    27.8,
    150.0,     
    23.4,
    -10.0,  
    28.5,
    np.nan,  
    200.0      
])

masque_invalide = (np.isnan(data)) | (data < 0) | (data >= 120) 

position_invalide = np.where(masque_invalide)

nb_invalide = np.sum(masque_invalide)

data_nettoyee = np.where(masque_invalide , 0 ,data)

print("AVANT :")
print(data)
print("Num d'invalide : " , nb_invalide)
print("================")
print("APRES :")
print("Data nettoyee : ")
print(data_nettoyee)
