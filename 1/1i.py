import numpy as np #type: ignore

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

add = np.add(a, b)
sub = np.subtract(a, b)
mul = np.multiply(a, b)
div = np.divide(a, b)

print("Add:", add)
print("Sub:", sub)
print("Mul:", mul)
print("Div:", div)
