# numpy arrays of constant (resp. random) values

import numpy as np

# array of ones
a = np.ones((3, 2))

# array of zeros
b = np.zeros((2, 4))

# array of randomly generated values
c = np.random.random(3)

# array of fixed (constant) values
d = np.full((2, 3), 12)


print(a)
print(b)
print(c)
print(d)
