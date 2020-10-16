import numpy as np
'''Creating Array'''
data = np.array([1,2,3,4])
print(data)


print("------------Version of the NumPy-------")
print(np.__version__)

print("-----check type------")
print(type(data))

print("-----------Using Tuple-------")
data1 = np.array((1,2,3,1,2,3))
print(data1)
print("----------------------2D Array---------------")
#-----------------------------------2D Array-----
twod = np.array([[1,2,3,4],[5,6,7,8]])
print(twod)

#----------------------Array Indexing----------
print("----------------Array Indexing----------------")
aindex = np.array([1,2,3,4])
print(aindex[0])


#-------------------------------Matrix product
print("----------------------Matrix product------------------------")
m1 = np.array([[1,2],[3,4]], ndmin=2)
m2 = np.array([[5,6],[7,8]], ndmin=2)
result = np.matmul(m1, m2)
print(result)


#-------------------------------Element-wise matrix multiplication

print("-----------------Element-wise matrix multiplication-----------------------")
m1 = np.array([[1,2],[3,4]], ndmin=2)
m2 = np.array([[5,6],[7,8]], ndmin=2)
result = np.multiply(m1, m2)
print(result)

#---------------------------------Dot product

'''These are the following specifications for numpy.dot:

When both a and b are 1-D (one dimensional) arrays-> Inner product of two vectors (without complex conjugation)
When both a and b are 2-D (two dimensional) arrays -> Matrix multiplication
When either a or b is 0-D (also known as a scalar) -> Multiply by using numpy.multiply(a, b) or a * b.
When a is an N-D array and b is a 1-D array -> Sum product over the last axis of a and b.
When a is an N-D array and b is an M-D array provided that M>=2 -> Sum product over the last axis of a and the second-to-last axis of b:
Also, dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])'''

print("-----------------Dot------------------")
array1=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3)
array2=np.array([[9,8,7],[6,5,4],[3,2,1]],ndmin=3)
result=np.dot(array1,array2)
print(result)