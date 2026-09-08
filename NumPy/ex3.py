# Analyse des notes d'étudiants
import numpy as np

notes = np.array([[12.5 , 20 , 15.5 , 19 , 10.75 , 11],
                  [11 , 10 , 16.25 , 18 , 13.5 , 15],
                  [14 , 7 , 14.5 , 8 , 0.75 , 1]
                  ])
                  

moyenne = notes.mean(axis=0)
print("Moyennes : ", moyenne)

meilleurs_notes = notes.max(axis=0)
print("Meilleures notes :",meilleurs_notes)

mauvaises_notes = notes.min(axis=0)
print("Plus faibles notes :", mauvaises_notes)

ecart = meilleurs_notes - mauvaises_notes
print('Ecart: ', ecart)

# notes supérieures à la moyenne
comparaison = notes > moyenne
print("Notes supérieures à la moyenne :")
print(comparaison)