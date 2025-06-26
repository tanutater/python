# x[start:stop:step]
# If any of these are unspecified, they default to the values start=0, stop=size of dimension, step=1
import numpy as np
x=np.arange(10)
print(x,"\n")
print("first five elements:-> ",x[:5])
print("elements after index 5:-> ",x[5:])
print("middle sub-array :-> ",x[3:7])
print("every other element:-> ",x[: : 2])
print("every other element, starting at index 1 :-> ",x[1::2])
print("all elements, reversed :-> ",x[::-1])
print("reversed every other from index 5 :-> ",x[5::-2])
print("\n\n")
print("MULTIDIMENTIONAL ARRAYS")
x2=np.random.randint(20,size=(3,4))
print(x2)
print("two rows, three columns :-> \n",x2[:2,:3])
print("all rows, every other column :-> \n",x2[:,::2])
print("subarray dimensions can even be reversed together :-> \n",x2[::-1,::-1])
#NOTE Accessing array rows and columns: One commonly needed routine is accessing of single rows or columns of an array. This can be done by combining indexing and slicing, using an empty slice marked by a single colon (:):

print("\nfirst column of x2:-> ",x2[:,0])
print("first row of x2 :->",x2[0,:])
print("first row of x2 :->",x2[0])

# NOTE Subarrays as no-copy views One important–and extremely useful–thing to know about array slices is that they return views rather than copies of the array data. This is one area in which NumPy array slicing differs from Python list slicing: in lists, slices will be copies.
print("printing x2:->\n",x2)
x2_sub=x2[:2,:2]
print("printting sub 2X2 of x2 :-> \n",x2_sub)
x2_sub[0,0]=12
print("changes made in the sub :->\n",x2_sub)
print("changes are also reflected in the main array since no copies are created in numpy array slicing :->\n",x2)
print("\n CREATING COPIES OF ARRAY \n")
x2_sub_copy=x2[:2,:2].copy()
print("copied 2x2 array of x2 :-> \n",x2_sub_copy)
#If we now modify this subarray, the original array is not touched:
x2_sub_copy[0,0]=42
print("modidified copy array :-> \n",x2_sub_copy)
print("printing original x2 it is not modified since modification made in the copied array do not touch the original array :->\n",x2)


print("\n RESHAPING OF ARRAY \n")
grid=np.arange(1,10).reshape(3,3)
print(grid)

x3=np.array([1,2,3])
print("reshaping 1d array to 2d row vector",x3.reshape((1,3)))
print("reshaping 1d array to 2d row vector using newaxis ",x3[np.newaxis,:])
print("reshaping 1d array to 2d column vector using newaxis\n ",x3.reshape((3,1)))
print("reshaping 1d array to 2d column vector using newaxis \n",x3[:,np.newaxis])

#NOTE Concatenation of arrays Concatenation, or joining of two arrays in NumPy, is primarily accomplished using the routines np.concatenate, np.vstack, and np.hstack. np.concatenate takes a tuple or list of arrays as its first argument, as we can see here:

a=np.array([1,2,3])
b=np.array([3,2,1])
print("concatenated array : ",np.concatenate([a,b]))

a2d=np.random.randint(10,size=(3,3))
print("original :- \n",a2d)
print("2d concatenation along the first axis :-\n",np.concatenate([a2d,a2d]))
print("concatenate along the second axis (zero-indexed) :-\n",np.concatenate([a2d,a2d],axis=1))

#For working with arrays of mixed dimensions, it can be clearer to use the np.vstack (vertical stack) and np.hstack (horizontal stack) functions:
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
print("print vertical stack concatinanation :->\n",np.vstack([x, grid]))
y=np.array([[99],[99]])
print(" horizontally stack the arrays:-> \n",np.hstack([grid,y]))

#Splitting of arrays The opposite of concatenation is splitting, which is implemented by the functions np.split, np.hsplit, and np.vsplit
x=[1,2,3,99,99,3,2,1]
print("original array :->",x)
x1,x2,x3=np.split(x,[3,5])
print("splited arrays :=> ",x1,x2,x3)
grid=np.arange(16).reshape((4,4))
print("original :-> \n",grid)
upper,lower=np.vsplit(grid,[2])
print("upper split using vsplit\n",upper)
print("lower split using vsplit \n",lower)
left,right=np.hsplit(grid,[2])
print("left split using hsplit:->\n",left)
print("right split using hsplit:->\n",right)