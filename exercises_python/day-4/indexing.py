#one dimensional
import numpy as np
a1=np.array([1,2,3,5,7,8,10])
print(a1.size)
print(a1[5])
print(a1[-5])
print()

#two dimensional
a2=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(a2.size)
print(a2.shape)
print(a2.ndim)
print(a2.itemsize)
print(a2[1,0])
print(a2[2,1])
print(a2[:,1])
print(a2[2,:])