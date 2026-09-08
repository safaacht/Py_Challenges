# Analyse d'un dataset multidimensionnel
import numpy as np

clients = np.array([ [21 , 1034.45 , 8 , 4871.99],
                    [51 , 134.0, 1 , 371.80],
                    ])

print(clients.shape)
print(clients[0][-1])
print(clients[0:1 , -3:])

total_clients = len(clients)

print(total_clients)
