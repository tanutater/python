import numpy as np
import pandas as pd
rng=np.random.RandomState(42)
ser=pd.Series(rng.randint(0,10,4))
print(ser)
df=pd.DataFrame(rng.randint(0,10,(4,3)),columns=['A','B','C'],index=['a','b','c','d'])
print(df)
print("applying numpy unfunc on pandas returns another pandas object :-> ",np.exp(df))
print(np.sin(df * np.pi / 4))

area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193,
                        'New York': 19651127}, name='population')
print("this results in the union of the indexes present in the area and dictionary :->\n",population/area)
print("to conform let us print the union of area and population:-> ",area.index.union(population.index))

a=pd.Series([2,4,6],index=[0,1,2])
b=pd.Series([1,3,5],index=[1,2,3])
print(a+b)
print("\n\nthe same a+b ann also be done using a.add(b) and allows optional explicit specification of the fill value for any elements in A or B that might be missing:->\n ",a.add(b))
print("to remove the NaN we can use a.add(b,fill_value=0):->\n",a.add(b,fill_value=0))

a=pd.DataFrame(rng.randint(0,20,(2,2)),columns=list('ab'))
print("dataframe a:->\n",a)
b = pd.DataFrame(rng.randint(0, 10, (3, 3)),columns=list('bac'))
print("dataframe :->\n",b)
print("addition of dataframe a+b:->\n",a+b)
fill=a.stack().mean()
# It reshapes the DataFrame from a 2D table into a 1D Series, where:The row index becomes a MultiIndex: (original row label, column label)The values remain unchanged
print(a.add(b,fill_value=fill))
a=rng.randint(10,size=(3,4))
print(a-a[0])
df=pd.DataFrame(a,columns=list('pqrs'))
print(df-df.iloc[0])
print("\n\nIf you would instead like to operate column-wise, you can use the object methods mentioned earlier, while specifying the axis keyword:\n",df.subtract(df['r'], axis=0))