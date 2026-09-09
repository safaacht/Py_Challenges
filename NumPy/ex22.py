import numpy as np

data = np.array([
    [10, 100, 1000],
    [20, 200, 2000],
    [30, 300, 3000]
])

client_reference = data[0]

distances = np.sqrt(np.sum((data - client_reference) ** 2, axis=1))

print(distances)