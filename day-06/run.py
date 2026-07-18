import numpy as np
# result = np.array([1,2,3,4,5,6,7,8,9,])
# print(result+5)

# #2d array
# ar = np.array([[1,2,3,4,5],
#               [1,2,3,4,5]])
# print(ar+5)


# #3d array 
# arr = np.array([
#     [[1,2],[3,4]],
#     [[5,6],[7,8]]
# ])

# print(arr)
# print(arr.shape)
# print(arr.ndim)
# print(arr.size)
# print(arr.dtype)

# arr = np.array([10,20,30])

# print(arr[0])

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr[1][2])

arr = np.array([10,20,30,40,50])

print(arr[1:4])

x = np.zeros((2,3))
print(x)

ones = np.ones((3,4))
print(ones)