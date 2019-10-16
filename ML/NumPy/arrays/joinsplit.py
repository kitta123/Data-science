import numpy as np
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y]))

z = [99, 99, 99]
print(np.concatenate([x, y, z]))

#for two-dimensional arrays
grid = np.array([[1, 2, 3],[4, 5, 6]])
# concatenate along the first axis
print(np.concatenate([grid, grid]))
# concatenate along the second axis (zero-indexed)
print(np.concatenate([grid, grid], axis=1))

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],[6, 5, 4]])
# vertically stack the arrays
print(np.vstack([x, grid]))

# horizontally stack the arrays
y = np.array([[99],[99]])
print(np.hstack([grid, y]))

#Spilting of arrays:-
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

#Notice that N split points lead to N + 1 subarrays.

grid = np.arange(16).reshape((4, 4))
print(grid)
#np.vspilt
upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)
#np.hsplit
left, right = np.hsplit(grid, [2])
print(left)
print(right)
