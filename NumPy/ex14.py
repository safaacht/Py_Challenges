# Trier et analyser un dataset

import numpy as np

scores = np.array([
    78, 92, 65, 88, 92,
    54, 73, 100, 81, 65,
    47, 89, 76, 58, 95
])

ord_croissant =  np.sort(scores)
ord_decroissant = np.sort(scores)[::-1]

indice_sort = np.argsort(scores)
# print(indice_sort)

top3_indices = indice_sort[-3:]
top3_scores = scores[top3_indices]
print(top3_scores)

duplicate_off = np.unique(scores)
print(duplicate_off)