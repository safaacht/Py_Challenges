import numpy as np

temperatures = np.array([22, 25, 19, 28, 24, 30, 21])

moyenne = temperatures.mean()
print("Température moyenne :", '%.2f' % moyenne)

jour_plus_chaud = temperatures.argmax() +1   # l'index du max
print("Jour le plus chaud :", jour_plus_chaud)

jour_plus_froid = temperatures.argmin() + 1    # l'index du max
print("Jour le plus froid :", jour_plus_froid)

sup_moy = temperatures[temperatures > moyenne]   
print("Températures supérieures à la moyenne :", sup_moy)

amplitude = np.max(temperatures) - np.min(temperatures)
print("Amplitude thermique :", amplitude)

diff = np.diff(temperatures)
print(diff)