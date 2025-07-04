import numpy as np
import pandas as pd
index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]
pop = pd.Series(populations, index=index)
print(pop)
print(pop[('California',2010):('Texas',2000)])
print(pop[[i for i in pop.index if i[1] == 2010]])

print("-------------------------------------BETTER WAY TO DO THIS USING PANDAS--------------------------------")
index = pd.MultiIndex.from_tuples(index)
print(index)
#If we re-index our series with this MultiIndex, we see the hierarchical representation of the data:
print('\n\nIf we re-index our series with this MultiIndex, we see the hierarchical representation of the data:\n')
pop=pop.reindex(index)
print(pop)
print('\n\n The unstack() method will quickly convert a multiply indexed Series into a conventionally indexed DataFrame\n')
pop_df=pop.unstack()
print(pop_df)
print("\n\nthe stack() method provides the opposite operation:\n")
print(pop_df.stack())
pop_df=pd.DataFrame({"total":pop,"under18":[9267089, 9284094,4687374, 4318033,5906301, 6879014]})
print(pop_df)
f_u18=pop_df['under18']/pop_df['total']
print("applying ufunction in multiindex:->\n",f_u18.unstack())
print("\n\nmethods of multiindex creation :->\n")
df=pd.DataFrame(np.random.rand(4,2),index=[['a','a','b','b'],[1,2,1,2]],columns=['data1','data2'])
print(df)
#Similarly, if you pass a dictionary with appropriate tuples as keys, Pandas will automatically recognize this and use a MultiIndex by default:
data = {('California', 2000): 33871648,
        ('California', 2010): 37253956,
        ('Texas', 2000): 20851820,
        ('Texas', 2010): 25145561,
        ('New York', 2000): 18976457,
        ('New York', 2010): 19378102}
print(pd.Series(data))

print("\n\nExplicit MultiIndex constructors ::\n")
print("multiindex from array :-> \n",pd.MultiIndex.from_arrays([['a','a','b','b'],[1,2,1,2]]))
print("from list pof tuples \n",pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)]))
print("from cartesian product :-\n",pd.MultiIndex.from_product([['a', 'b'], [1, 2]]))
print("\n\nMULTIINDEX LEVEL NAMES \n")
pop.index.names=['state','year']
print(pop)

print("\n\nMULTIINDEX FOR COLUMNS \n")
index=pd.MultiIndex.from_product([[2013,2014],[1,2]],names=['year','visit'])
column=pd.MultiIndex.from_product([['bob','guido','sue'],['hr','temp']],names=['subject','type'])
data=np.round(np.random.randn(4,6),1)
data[:,::2]*=10
data+=37
health_data=pd.DataFrame(data,index=index,columns=column)
print(health_data)
print("with this multiindexing we can fetch the entire data of a particular person as :->\n",health_data['guido'])

print("\n\nindexing \n\n")
print(pop)
print(pop['California']) #The MultiIndex also supports partial indexing, or indexing just one of the levels in the index. The result is another Series, with the lower-level indices maintained:
#With sorted indices, partial indexing can be performed on lower levels by passing an empty slice in the first index:4
print(pop[:,2000])
print("indexing in dataframes \n")
print("\n",health_data)
print("\n",health_data['guido','hr']) #feteching guido's hearth rate 
print("\n",health_data.iloc[:2, :2])
print("\n",health_data.loc[:, ('bob', 'hr')])
idx = pd.IndexSlice
print("\n",health_data.loc[idx[:, 1], idx[:, 'hr']])

print("\n\n sorting technique:- sort_index() , sortlevel()\n")
index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']
data=data.sort_index()
print(data)
print(data['a':'b']) # without sorting it would have gine error
print(pop.unstack(level=0)) #level=0 move states to columns
print(pop.unstack(level=1))
print(pop.unstack().stack())
pop_flat = pop.reset_index(name='population')
print("resetting index:->\n",pop_flat)
print(pop_flat.set_index(['state', 'year']))