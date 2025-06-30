import numpy as np
import pandas as pd
vals2 = np.array([1, np.nan, 3, 4]) 
print(vals2.dtype)
#NOTE :->You should be aware that NaN is a bit like a data virus–it infects any other object it touches. Regardless of the operation, the result of arithmetic with NaN will be another NaN:
print("any operation with NaN results into NaN:-> ",1+np.nan)
print("any operation with NaN results into NaN:-> ",0*np.nan)
print(vals2.sum())
print(vals2.max())
print(vals2.min())
print("some special aggregations that will ignore these missing values:-> ",np.nansum(vals2))
print("some special aggregations that will ignore these missing values:-> ",np.nanmin(vals2))
print("some special aggregations that will ignore these missing values:-> ",np.nanmax(vals2))
print(pd.Series([1, np.nan, 2, None]))
x=pd.Series(range(2),dtype=int)
print(x)
print("dtype of x:->",x.dtype)
x[0]=None
print(x)
print("dtype of x after changing one of its value to none:-> ",x.dtype)
#NOTE Keep in mind that in Pandas, string data is always stored with an object dtype.

print("\n\nNOTE:->  Keep in mind that in Pandas, string data is always stored with an object dtype.\n\n")
data = pd.Series([1, np.nan, 'hello', None])
print(data.isnull())
print([data.notnull()])
y=data[data.notnull()]
print(y)
#In addition to the masking used before, there are the convenience methods, dropna() (which removes NA values) and fillna() (which fills in NA values). For a Series, the result is straightforward:
print(data.dropna())
print(data.fillna(-1))
s=pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])
print(s)
print("dropna in dataframes returns the row with no none values or a empty list:->\n",s.dropna())
print("dropna in dataframes returns the col (with the help of axis) with no none values or a empty list:->\n",s.dropna(axis='columns'))

#But this drops some good data as well; you might rather be interested in dropping rows or columns with all NA values, or a majority of NA values. This can be specified through the how or thresh parameters, which allow fine control of the number of nulls to allow through.   The default is how='any', such that any row or column (depending on the axis keyword) containing a null value will be dropped. You can also specify how='all', which will only drop rows/columns that are all null values:
s[3]=np.nan
print(s)
print("drop rows/columns that are all null values:-\n",s.dropna(axis='columns',how="all"))
print("thresh parameter lets you specify a minimum number of non-null values for the row/column to be kept:\n",s.dropna(axis='rows',thresh=3))

#NOTE fillna() method, which returns a copy of the array with the null values replaced.

data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
print("data->\n",data)
print("filling nan values using fillna():->\n",data.fillna(0))

print("filling nan values using ffill forward fill i.e. fills from the previous non null value here b values filled from a :->\n",data.ffill())
print("filling nan values using bfill backward fill i.e. fills from the next non null value here b values filled from a :->\n",data.bfill())
print(s)
print(s.fillna(method='ffill', axis=1))

#NOTE Notice that if a previous value is not available during a forward fill, the NA value remains.