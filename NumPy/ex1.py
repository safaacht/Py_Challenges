import numpy as np 
# Analyse d'un tableau de ventes

numbers = np.array([[233.0, 494.0, 56.44, 100.0, 499.5],
                    [213.0, 494.0, 51.44, 100.0, 489.5]])

print(numbers.shape)
print(numbers.ndim)
print(numbers.size)
print(numbers.dtype)
print(numbers[0][0])
print(numbers[1][-1])

print(numbers.min())
print(numbers.max())
print(numbers.mean())
