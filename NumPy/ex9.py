import numpy as np

# Analyse par dimension avec axis


ventes = np.array([
    [120, 150, 180, 200],  #produit1
    [90, 110, 130, 160],   
    [200, 180, 220, 250],  
    [75, 100, 95, 120]     
])


somme_pr = np.sum(ventes , axis = 1)

moyenne_pr = ventes.mean(axis = 1)

somme_mois = ventes.sum(axis = 0)

moyenne_mois = ventes.mean(axis = 0)

meilleur_pr  = np.argmax(somme_pr) + 1
meilleur_mois  = np.argmax(somme_mois) + 1


print("Ventes totales par produit :", somme_pr)
print("Ventes moyennes par produit :", moyenne_pr)

print("Ventes totales par mois :", somme_mois)
print("Ventes moyennes par mois :", moyenne_mois)

print("Meilleur produit : Produit", meilleur_pr)
print("Meilleur mois :", meilleur_mois)