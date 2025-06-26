import numpy as np
np.random.seed(0)  # seed for reproducibility
# seed with a set value in order to ensure that the same random arrays are generated each time this code is run

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

# Each array has attributes ndim (the number of dimensions), shape (the size of each dimension), and size (the total size of the array):
print(x1,"\n")
print(x2,"\n")
print(x3,"\n")
print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
print("dtype:", x3.dtype)

# itemsize, which lists the size (in bytes) of each array element, and nbytes, which lists the total size (in bytes) of the array:
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")

# accessing 2d array using index
print(x2[0,0])
print(x2[2,-1])


# NOTE unlike Python lists, NumPy arrays have a fixed type. This means, for example, that if you attempt to insert a floating-point value to an integer array, the value will be silently truncated. Don't be caught unaware by this behavior!