import numpy as np

A = np.array([1, 2, 3])
B = np.array([2, 4, 6])
C = np.array([3, 1, 0])

produit_scalaire = np.dot(A, B)

print(produit_scalaire)

norm_A = np.linalg.norm(A)
norm_B = np.linalg.norm(B)

similarite = np.dot(A, B) / (
    np.linalg.norm(A) * np.linalg.norm(B)
)

print(similarite)

vecteurs = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 1, 0],
    [1, 2, 2]
])

reference = vecteurs[0]

similarites = np.dot(vecteurs, reference) / (
    np.linalg.norm(vecteurs, axis=1) * np.linalg.norm(reference)
)

print(similarites)

plus_similaire = np.argmax(similarites)

print("Élément le plus similaire :", plus_similaire)