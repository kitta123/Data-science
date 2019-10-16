import numpy as np
np.random.seed(0)
def compute_reciprocals(values):
	output = np.empty(len(values))
	for i in range(len(values)):
		output[i] = 1.0 / values[i]
	return output
values = np.random.randint(1, 10, size=5)
print(compute_reciprocals(values))
print(1.0 / values)
print(np.arange(5) / np.arange(1, 6))

x = np.arange(9).reshape((3, 3))
print(2 ** x)
