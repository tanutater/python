import numpy as np
# Create a length-10 integer array filled with zeros
arr=np.zeros(10, dtype=int)
print(arr)

# Create a 3x5 floating-point array filled with ones
print(np.ones((3, 5), dtype=float))

# Create a 3x5 array filled with 3.14
print(np.full((3, 5), 3.14))

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
print(np.arange(0, 20, 2))

# Create an array of five values evenly spaced between 0 and 1
print(np.linspace(0, 1, 5))

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
print(np.random.random((3, 3)))

# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
print(np.random.normal(0, 1, (3, 3)))

# Create a 3x3 array of random integers in the interval [0, 10)
print(np.random.randint(0, 10, (3, 3)))

# Create a 3x3 identity matrix
print(np.eye(3))

# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that memory location
print(np.empty(3))


