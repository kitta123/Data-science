import numpy as np
def selection_sort(x):
	for i in range(len(x)):
		swap = i + np.argmin(x[i:])
		(x[i], x[swap]) = (x[swap], x[i])
	return x
x = selection_sort(np.array([2, 1, 4, 3, 5]))
print(x)
