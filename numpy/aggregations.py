import numpy as np
big_array = np.random.rand(1000000)
L = np.random.random(100)
print("slow compared to np.sum",sum(L))
print("fast ",np.sum(L))
print("min and max ",min(big_array), max(big_array))
print("min and max ",np.min(big_array), np.max(big_array))
print(big_array.min(), big_array.max(), big_array.sum())
m=np.random.random((3,4));
print("multidimentional array :-> \n",m)
print(m.sum())
print("minimum value within each column by specifying axis=0 ",m.min(axis=0))
print(" maximum value within each row:",m.max(axis=1))

