import numpy as np
import pandas as pd
data=pd.Series([0.23,1,2,4],index=['a','b','c','d'])
print(data)
print(.23 in data)
print('a' in data)
print("printing keyes :- ",data.keys())
print("printing itemes :- ",list(data.items()))

#Series objects can even be modified with a dictionary-like syntax. Just as you can extend a dictionary by assigning to a new key, you can extend a Series by assigning to a new index value:
data['e']=1.25
print(data)
print("slicing explicit index:-> \n",data['a':'d'])
print("slicing by implicit index :->\n",data[0:3])
print("masking :->\n",data[(data>1)&(data<2)])
print("fancy indexing :->\n",data[['a','e']])