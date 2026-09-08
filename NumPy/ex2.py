# Génération d'un jeu de données
import numpy as np

jours = np.arange(1,8)
temperature = np.linspace(16 , 40 , 5)
identifiants = np.random.randint(5)
zeros = np.zeros(5)
ones = np.ones(5, dtype=int)
prix = np.full(5,150)

print(jours)
print(temperature)
print(prix)
print(zeros)
print(ones)
