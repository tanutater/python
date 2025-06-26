import numpy as np
def selection_sort(x):
  for i in range(len(x)):
    swap=i+np.argmin(x[i:])
    x[i],x[swap]=x[swap],x[i]
  return x
def bogo_sort(x):
  while np.any(x[:-1]>x[1:]):
    np.random.shuffle(x)
  return x
x=np.array([5,4,3,2,1])
print("selection_sort(x):-> ",selection_sort(x))
print("bogo_sort(x):-> ",bogo_sort(x))
print("np.sort(x):-> ",np.sort(x))
print("np.argsort(x): returns the indices of the sorted elements:",np.argsort(x))

# sorting along rows and columuns 
print("\n sorting along rows and columns\n")
rand=np.random.RandomState(42)
x=rand.randint(0,10,(4,6))
print(x)
# or 
np.random.seed(42)
x=np.random.randint(0,10,(4,6))
print(x)

print("sort each column of x axis=0 :->\n",np.sort(x,axis=0))
print("sort each row of x axis=1 :->\n",np.sort(x,axis=1))
print("Sorts the whole array flat axis=None :->\n",np.sort(x,axis=None))


#partial sort : Sometimes we're not interested in sorting the entire array, but simply want to find the k smallest values in the array. NumPy provides this in the np.partition function. np.partition takes an array and a number K; the result is a new array with the smallest K values to the left of the partition, and the remaining values to the right, in arbitrary order:

print("\n PARTIAL SORT K SMALLEST ELEMENTS \n")
# x=np.random.randint(0,10,10)
x=np.array([7, 2, 3, 1, 6, 5, 4])
print(" 3 smallest elements ", np.partition(x,3))

x=np.random.randint(0,10,size=(3,4))
print("partitioning along axis in multidimensional array :-> \n",np.partition(x,2,axis=1))