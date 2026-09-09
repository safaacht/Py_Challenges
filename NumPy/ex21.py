import numpy as np

data = np.array([
    [10, 100, 1000],
    [20, 200, 2000],
    [30, 300, 3000]
])

coefficients = np.array([2, 0.5, 10])

reslt = data * coefficients

print(reslt)