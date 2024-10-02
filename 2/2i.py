import numpy as np  # type: ignore

def add_10(x):
    return x + 10

ufunc_add_10 = np.frompyfunc(add_10, 1, 1)

arr = np.array([1, 2, 3, 4, 5])
result = ufunc_add_10(arr)

print(result)
