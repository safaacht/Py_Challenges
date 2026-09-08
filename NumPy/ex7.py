# Challenge 7 — Analyse statistique d'un dataset

import numpy as np

salaires = np.array([
    2500,
    3200,
    2800,
    4500,
    3900,
    5200,
    6100,
    3000,
    3500,
    4800
])

moyenne = salaires.mean()

maximum = salaires.max()
minimum = salaires.min()

ecart = salaires.std()

median = np.median(salaires)

variance = np.var(salaires)

Q1 = np.percentile(salaires , 25)
Q2 = np.percentile(salaires , 50)
Q3 = np.percentile(salaires , 75)

print(ecart)
print(median)
print(moyenne)
print(Q1)
print(Q2)
print(Q3)
print(variance)
print(maximum)
print(minimum)
