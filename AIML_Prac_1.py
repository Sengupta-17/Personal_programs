import numpy as sp
#q1
arr=sp.array([1,3,4])
print(arr)
#q2
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.dtype)
#q3
a=sp.array([4,2,6])
a=sp.int64(a)
b=sp.array([10,56,32])
b=sp.int64(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
#q4
import numpy as sp
arr=sp.array([[10,56,32],[32,41,13]])
print(arr[:,2])
print(arr[0,:])