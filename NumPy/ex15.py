# Étude complète d'un dataset

import numpy as np

students = np.array([
    [14, 16, 12, 15],
    [10, 13, 11, 12],
    [17, 15, 18, 16],
    [8,  9,  7,  10],
    [13, 14, 15, 12],
    [19, 18, 17, 20],
    [11, 12, 10, 13],
    [15, 16, 14, 15],
    [6,  8,  9,  7],
    [16, 17, 15, 18]
])

# [ Math, Français, Anglais, Informatique ]

# print("dimensions " , students.shape)

moyenne_matiere = students.mean(axis=0)
moyenne_etudiant = students.mean(axis=1)
# print(moyenne_etudiant)
# print(moyenne_matiere)
min_note = students.min()
max_note = students.max()
print("Note minimale :", min_note)
print("Note maximale :", max_note)

moyenne_generale = students.mean()
masque = moyenne_etudiant > moyenne_generale

etudiants_au_dessus  = np.where(masque)[0]
print("Étudiants au-dessus de la moyenne :", etudiants_au_dessus )

classement = moyenne_etudiant.argsort()[::-1]
print(classement)

top3 = classement[:3]
print("Top 3 :", top3)


masque_anomalies = (students < 10) | (students > 18)

anomalies = students[masque_anomalies]

print("Anomalies :", anomalies)


valeurs_uniques  = np.unique(students[0])
print("Valeurs uniques :", valeurs_uniques)