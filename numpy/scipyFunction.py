import numpy as np
from scipy import special
#If you want to compute some obscure mathematical function on your data, chances are it is implemented in scipy.special
# Gamma functions (generalized factorials) and related functions
x = [1, 5, 10]
print("gamma(x)     =", special.gamma(x))
print("ln|gamma(x)| =", special.gammaln(x))
print("beta(x, 2)   =", special.beta(x, 2))
# Error function (integral of Gaussian)
# its complement, and its inverse
x = np.array([0, 0.3, 0.7, 1.0])
print("erf(x)  =", special.erf(x))
print("erfc(x) =", special.erfc(x))
print("erfinv(x) =", special.erfinv(x))

#AGGREGATE FUNCTION\
x=np.arange(1,6)
print(x)
print("aggregate funtion reduce :-> ",np.add.reduce(x))
print("aggregate funtion reduce :-> ",np.multiply.reduce(x))

#If we'd like to store all the intermediate results of the computation, we can instead use accumulate:
print("aggregate function accumulate :-> ",np.add.accumulate(x))
print("aggregate function accumulate :-> ",np.multiply.accumulate(x))

#Outer products Finally, any ufunc can compute the output of all pairs of two different inputs using the outer method. This allows you, in one line, to do things like create a multiplication table:
x=np.arange(1,6)
print("original : -> \n",x)
print("outer function :-\n",np.multiply.outer(x,x))
print("outer function :-\n",np.add.outer(x,x))