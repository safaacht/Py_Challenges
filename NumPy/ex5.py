# Extraction et modification des données

import numpy as np

clients = np.array([
    [1, "Sara", 21, "Youssoufia", 2500],
    [2, "Amine", 25, "Rabat", 4200],
    [3, "Salma", 19, "Marrakech", 1800],
    [4, "Yassine", 30, "Casablanca", 5500],
    [5, "Imane", 27, "Fes", 3500],
    [6, "Omar", 23, "Agadir", 2900]
])

copy_clients = clients.copy()
clients[2][1] = "Safaa"
clients[3][3] = "Safi"
clients[5] = [6, "Ilias" , 21 , "Casablanca" , 2600]
copy_clients[3][4] = "00000"
# print(clients)
print(clients[2:5])
# print(copy_clients)