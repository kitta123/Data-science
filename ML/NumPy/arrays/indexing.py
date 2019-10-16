import numpy as np
np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))# Three-dimensional array

print(x1)
print(x1[0])
print(x1[-1])

x1[0] = 3.14159 # this will be truncated!
print(x1)

print(x2)
print(x2[0,0])
print(x2[2,-1])

x2[1,2]=15 #You can also modify values using any of the above index notation
print(x2)
