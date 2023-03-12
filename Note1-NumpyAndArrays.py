# Note1-NumpyAndArrays:
import numpy as np

# print an array looks like this:
# [0. 0. 0. 0. 0.]
A = np.zeros(5)
print(A)
np.shape(A)
print("\n")

# print an array looks like this:
# [[0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0.]]
A1 = np.zeros((4, 5))  # 4 rows, 5 columns
print(A1)
np.shape(A1)
print("\n")

# print an array looks like this:
# [[1. 1. 1.]
# [1. 1. 1.]]
B = np.ones((2, 3))  # 2 rows, 3 columns
print(B)
np.shape(B)
print("\n")

# print an array looks like this:
# [[11 11 11 11 11 11 11 11]
# [11 11 11 11 11 11 11 11]
# [11 11 11 11 11 11 11 11]
# [11 11 11 11 11 11 11 11]
# [11 11 11 11 11 11 11 11]
# [11 11 11 11 11 11 11 11]
# [11 11 11 11 11 11 11 11]]
C = np.full((7, 8), 11)  # 7 rows, 8 columns
print(C)
np.shape(C)
print("\n")

# 🐱‍🚀🐱‍👤🐱‍💻🐱‍🐉🐱‍👓🐱‍🏍✨
# linspace() works by passing  an initial value, an end value, and the number of elements to it
# The result is thus 10 elements between the start and end values, including the endpoints.
x1 = np.linspace(0, 5, 10)
print(x1)
print("\n")

# arange() in turn takes the step length as the third parameter
# an array created with arange() does not reach a final value (so it works like range())
x2 = np.arange(0, 5, 0.2)
print(x2)
print("\n")

# random() command produces random numbers evenly distributed over a semi-open interval [0.0, 1.0]. So these are decimal numbers
x3 = np.random.randn(13)
print(x3)
print("\n")

# Random integers between [a, b] can be generated with the command randint()
# Note how the endpoint is not included here, so the second parameter must be b+1
a = 1
b = 6
amount = 10
noppa1 = np.random.randint(a, b + 1, amount)
print(noppa1)
print("\n")

a = 3
b = 7
amount = 12
noppa2 = np.random.randint(a, b + 1, amount)
print(noppa2)

# 🐱‍🚀🐱‍👤🐱‍💻🐱‍🐉🐱‍👓🐱‍🏍✨
