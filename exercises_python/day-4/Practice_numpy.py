# to install numpy-pip install numpy
import numpy as np
list1=[1, 2, 3, 4, 5]
array1= np.array(list1)
print(array1)
print(type(array1))
print()

list2=[1, 3.5, 4, 6, 7]
array2= np.array(list2, dtype=float)
print(array2)
print(type(array2))
print()

list3=[1, 3,6, "hello", 7]
array3= np.array(list3)
print(array3)
print(type(array3))
print(array1.ndim)
print()

#two dimensional array
list4=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array4= np.array(list4)
print(array4)
print(array4.ndim)
print(type(array4))
print()


#print range array
a=np.arange(1,11)
print(a)
print()


#two dimensional
b=np.arange(1,7).reshape((2,3))
print(b)
print()

#attributes of numpy array
# 1-ndim
# 2-shape
# 3-size
# 4-dtype
# 5-iteamsize
b=np.arange(1,7).reshape((2,3))
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)
print(b.itemsize)

