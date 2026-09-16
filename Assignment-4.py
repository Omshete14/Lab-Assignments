import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8,9])
array2 = np.array([9,8,7,6,5,4,3,2,1])

matrix1 = array1.reshape(3,3)
matrix2 = array2.reshape(3,3)

print("Addition of matrices:", matrix1 + matrix2)