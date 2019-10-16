import numpy as np
np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))# Three-dimensional array

print("x3 ndim: ", x3.ndim)# ndim (the number of dimensions) 
print("x3 shape:", x3.shape)# shape (the size of each dimension)
print("x3 size: ", x3.size)# size (the total size of the array)

print("dtype:", x3.dtype)# dtype (the data type of the array)

print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")
