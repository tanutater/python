import numpy as np
np.random.seed(0)
def compute_reciprocal(value):
  output=np.empty(len(value))
  for i in range (len(value)):
    output[i]=1.0/value[i]
  return output
value=np.random.randint(1,10,size=5)
print(compute_reciprocal(value))
print(1.0 / value)
print(np.arange(5))
print(np.arange(1,6))
print(np.arange(5)/np.arange(1,6))
x=np.arange(9).reshape(3,3)
print(2**x)

x = np.arange(4)
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)  # floor division
print("-x     = ", -x)
print("x ** 2 = ", x ** 2)
print("x % 2  = ", x % 2)
x = np.array([-2, -1, 0, 1, 2])
print("x : ",x)
print("abs(x): ",abs(x))

#This ufunc can also handle complex data, in which the absolute value returns the magnitude:

x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
print("complex value array : ",x)
print("abs(x) complex array which returns the magnitude ",np.abs(x))

theta =np.linspace(0,np.pi,3) #this means to generate 3 equally spaced numbers between 0 and pi syntax linspace(start,stop,num)
print("theta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))

x = [-1, 0, 1]
print("x         = ", x)
print("arcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("arctan(x) = ", np.arctan(x))

print("\n NOTE: just as there is a np.argsort that computes indices of the sort, there is a np.argpartition that computes indices of the partition\n")