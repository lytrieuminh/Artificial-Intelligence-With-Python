#Note3-Calculations with Matrices:
import numpy as np

#As with regular numbers, calculations can also be performed on matrices:
A = np.array([[1, 2], [3, 4]])
B = np.array([[3, 9], [4, -1]])
print(A + B)
print("\n")
print(A - B)
print("\n")

#Multiplication and division also work with the same idea:
print(A * B)
print("\n")
print(A / B)
print("\n")

#In addition to the basic calculations, the application of elementary functions to the matrix is done item by item:
np.sqrt(A)  # the square root of each item
np.sin(A)
np.cos(A)
np.tan(A)
np.log(A)
np.exp(A)
np.log10(A)
np.log2(A)

#Comparison operators also target matrices by item:
A > 1
A <= 0

#Operators can be used at the same time as the cut to select only items from a table that fulfill any of the conditions:
A = np.array([1, 2, 3, 4, 5, 6, 7])
B = A[A > 3]
print(B)
print("\n")

#You can create a large matrix that contains the desired number for each item (or use the full () command):
T = 5 * np.ones((10, 10))
print(T)
print("\n")

#Check photo 2.PNG
A = np.array([[2, 1], [-4, 3]])
B = np.array([11, 3])
X = np.linalg.solve(A, B)
print(X)
print("\n")
#If necessary, the inverse matrix is ​​determined by the command inv () and can be used to check that the solution is correct:
Ainv = np.linalg.inv(A)
print(np.matmul(Ainv, B))

#🐱‍🚀🐱‍👤🐱‍💻🐱‍🐉🐱‍👓🐱‍🏍✨