import numpy as np  # type: ignore

a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])
cond = np.array([True, False, True, False, True])

new_arr = np.where(cond, a, b)

print(new_arr)
