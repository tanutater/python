import numpy as np
x=np.random.random((10,3))
print(x)
Xmean = x.mean(0)
print("mean ",Xmean)
Xcenter=x-Xmean
print("xcenter mean ",Xcenter.mean(0))
x2=np.random.randint(0,10,size=(10,3))
print(x2)
