print("reshapeing")

import numpy as np
grid = np.arange(1, 10).reshape((3, 3))
print(grid)

x = np.array([1, 2, 3])
# row vector via reshape
print(x.reshape((1, 3)))
# row vector via newaxis
print(x[np.newaxis, :])
# column vector via reshape
print(x.reshape((3, 1)))
# column vector via newaxis
print(x[:, np.newaxis])

