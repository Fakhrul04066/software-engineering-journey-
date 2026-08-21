import numpy as np
x= np.array([[10,23],
             [40,-23]])
y=np.array([[-29,34],
            [56,10]])
print("Addtion:- ")
print(x+y)
print()

print("Sub:-")
print(x-y)

#multiplication x*y (element by element)

print()
print("Matrix Multiplication- ")
print(x@y)

#division element by element x/y .For floor value x//y
#for exponention x**y

#transpose
print(x.transpose())