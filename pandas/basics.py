import pandas as pd
import numpy as np
# A Pandas Series is a one-dimensional array of indexed data
# NOTE :-> Notice that when slicing with an explicit index (i.e., data['a':'c']), the final index is included in the slice, while when slicing with an implicit index (i.e., data[0:2]), the final index is excluded from the slice.
data=pd.Series([1,.25,.34,.67])
print(data)
print("printing values of the seried using .values: ",data.values)
print("printing indices of the seried using .index: ",data.index)

# accessing using index
print("element at index 1:-> ",data[1])
print("element between index 1 and 3: ->\n",data[1:3])

#he Pandas Series has an explicitly defined index associated with the values
d=pd.Series([1,0.25,0.34,0.55],index=['a','b','c','d'])
print(d)
print(d['a'])
print("explicit declaration of index in characters :->\n",d['a':'c'])
#index can also be in random order
d=pd.Series([1,2,3,4],index=[5,4,3,1])
print(d)
print(d[5])
print("integer not sorted and 3 comes after 5 in our indexing so pandas cannot find and returns an empty list :->\n",d[5:3])
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
print("series created from a dictionary :->\n",population)
print(population['California'])
print(population['California': 'Florida'])
d=pd.Series([0,1,2,3,4],index=[0,1,2,3,4])
print(d)
print(d[0:4])
print("different ways of creating series :\n ",pd.Series(5, index=[100, 200, 300]))
print("data can be a dictionary, in which index defaults to the dictionary keys:\n",pd.Series({2:'a', 1:'b', 3:'c'}))
print(pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2]))

#NOTE: If a Series is an analog of a one-dimensional array with flexible indices, a DataFrame is an analog of a two-dimensional array with both flexible row indices and flexible column names
area_dict={'California':423967,'Texas':695662,'New York':141297,'Florida':170312,'Illinois':149995}
area=pd.Series(area_dict)
states=pd.DataFrame({'population':population,'area':area})
print(states)
print("printing index of DataFrame ",states.index)
print("\n\nDataFrame has a columns attribute, which is an Index object holding the column labels:",states.columns)
print("\n\nWhere a dictionary maps a key to a value, a DataFrame maps a column name to a Series of column data:->\n",states['area'])

print("\n single data frame\n",pd.DataFrame({'population':population}))
print("\n single data frame\n",pd.DataFrame(population,columns=['population']))
data=[{'a':i,'b':2*i}for i in range(5)]
print("\n\n dataframes from a list \n",pd.DataFrame(data))
print("\n\nEven if some keys in the dictionary are missing, Pandas will fill them in with NaN\n",pd.DataFrame([{'a':1,'b':2},{'b':3,'c':4}]))
print(pd.DataFrame(np.random.rand(3,2),columns=['foo','bar'],index=('a','b','c')))
A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
print("\n\n dataframes from structured numpy array ",pd.DataFrame(A))
ind=pd.Index([2,3,4,5,6,7])
print(ind)
print(ind[1])
print(ind[::2])
print(ind.size, ind.shape, ind.ndim, ind.dtype)
indA=pd.Index([1,2,3,5,6,7,9])
indB=pd.Index([1,2,3,4,5,6,7,8])
print("intersection of indexa and indexb: ",indA.intersection(indB))
print("union of indexa and indexb: ",indA.union(indB))
print("diff of indexa and indexb: ",indA.difference(indB))
print("symmetric_diff of indexa and indexb: ",indA.symmetric_difference(indB))