
# 3*5*6
# 3*6*10
import numpy as np


def Mul(a, b):
    a_shape = a.shape
    b_shape = b.shape
    result = np.zeros(a_shape[0] * b_shape[1]).reshape(a_shape[0], b_shape[1])
    for i in range(a_shape[0]):
        for j in range(b_shape[1]):
            for k in range(a_shape[1]):
                result[i][j] += a[i][k] * b[k][j]


    return result


def mul_3d(a, b):
    result_list = []
    for i, j in zip(a,b):
        result_list.append(Mul(i, j))

    return result_list


a = np.random.randint(1,10, size=[3,5,6])
b = np.random.randint(1,10,size=[3,6,10])

print(mul_3d(a,b))

print(np.matmul(a,b))

c = mul_3d(a,b) - np.matmul(a,b)
print(c)