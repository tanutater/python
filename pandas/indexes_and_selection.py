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
print("\n\n-----------------------------------------------------------------Indexers: loc, iloc, and ix-------------------------------------------\n\n")
# These slicing and indexing conventions can be a source of confusion. For example, if your Series has an explicit integer index, an indexing operation such as data[1] will use the explicit indices, while a slicing operation like data[1:3] will use the implicit Python-style index.
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
print("explicit :->",data[1])
print("implicit :->\n",data[1:3])

# NOTE the loc attribute allows indexing and slicing that always references the explicit index:
print("\n\nthe loc attribute allows indexing and slicing that always references the explicit index:\n")
print(data.loc[1])
print(data.loc[1:3])
 
#NOTE The iloc attribute allows indexing and slicing that always references the implicit Python-style index:
print('\n\nThe iloc attribute allows indexing and slicing that always references the implicit Python-style index:\n')
print(data.iloc[1])
print(data.iloc[1:3])
area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
print("\n\nDataFrame:\n",data)
# The individual Series that make up the columns of the DataFrame can be accessed via dictionary-style indexing of the column name:
print("\n\nindividual series that make up the columns of dataframe:->\n",data['area'])
#Equivalently, we can use attribute-style access with column names that are strings
print("\n\nAlternate methond of accessing using attribute :->\n",data.area)
print("\n\n not always useful :-> ",data.area is data['area'])
print("Since dataframe have pop() method so it will point to that instead of the pop column name and will result in false :->",data.pop is data['pop'])

# In particular, you should avoid the temptation to try column assignment via attribute (i.e., use data['pop'] = z rather than data.pop = z).
# data['pop']='z'
# print(data)
data['density']=data['pop']/data['area']
print(data)
print("values:->\n",data.values)
print("\n\ntransposing the entire data:->\n",data.T)
print("values of transposed data :->",data.values[0])
print(data['area'])
print("implicit:->\n",data.iloc[:3, :2])
print("explicit:->\n",data.loc[:'Illinois',:'pop'])
print(data.loc[data.density>100,['density','pop']])
data.iloc[0,2]=90
print(data)