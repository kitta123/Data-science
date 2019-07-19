import numpy as np
np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))# Three-dimensional array
x = np.arange(10)

print(x)

print(x[:5])# first five elements
print(x[5:])# elements after index 5
print(x[4:7])# middle subarray
print(x[::2])# every other element
print(x[1::2])# every other element, starting at index 1
print(x[::-1])# all elements, reversed
print(x[5::-2])# reversed every other from index 5

#Multidimensional subarrays

print(x2[:2, :3])# two rows, three columns
print(x2[:3, ::2])# all rows, every other column

#subarray dimensions can even be reversed together
print(x2[::-1, ::-1])

print(x2[0]) # equivalent to x2[0, :]

#Let’s extract a 2×2 subarray from this:
x2_sub = x2[:2, :2]
print(x2_sub)

#modify this subarray:

x2_sub[0, 0] = 99
print(x2_sub)

print(x2)

#Creating copies of arrays

x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)

#modify this subarray:
x2_sub_copy[0, 0] = 42
print(x2_sub_copy)

print(x2)


