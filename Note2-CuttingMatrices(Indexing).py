#Note2-Cutting Matrices (Indexing):
import numpy as np

#The two-dimensional array is indexed (cut) by two indexes within one square bracket:
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
print(A[0, 0])
print(A[0, 1])
print("\n")

#The three-dimensional array is cut with three indexes, respectively.
#The colon can also be used to create index spaces with the start: end: step syntax, so that the intersection no longer targets the end.
#The index spacing can be used to index both rows and columns:
B = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(B)
print("\n")

print(B[0:6:1])  #print[1 2 3 4 5 6]
print(B[0:6:2])  #print[1 3 5]
print("\n")

#Items can be updated with a combination of an signing statement and a cut:
C = np.array([[1, 2, 3], [4, 5, 6]])
print(C)
print("\n")

C[0, 0] = 17
print(C)
print("\n")

#":" reads all columns
C[1, :] = [11, 12, 13]
print(C)
print("\n\n")

#🐱‍🚀🐱‍👤🐱‍💻🐱‍🐉🐱‍👓🐱‍🏍✨
#Deleting a row and column is done with the delete command, to which information about the index of the row / column to be deleted and the dimension of the deletion operation must be passed (0 = for rows, 1 = for columns):
#🚨 A single item cannot be removed as it would make holes in the matrix
D = np.array([[1, 2, 3], [4, 5, 6]])
print(D)
print("\n")
D = np.delete(D, [0], 0)  #cut the first row away
print(D)
print("\n")
#🚨 A single item cannot be removed as it would make holes in the matrix
E = np.array([[1, 2, 3], [4, 5, 6]])
print(E)
print("\n")
E = np.delete(E, [1], 1)  #cut the second column away
print(E)
print("\n")

#🐱‍🚀🐱‍👤🐱‍💻🐱‍🐉🐱‍👓🐱‍🏍✨
#The table can be traversed (iterated) in many different ways:
A = np.array([1, 2, 3, 4, 5, 6])
print(A)
print("\n")
#Option1:
A = A.reshape(2, 3)
n, m = np.shape(A)
for i in range(n):
  print("Row", i, "is", A[i, :])
print("\n")
#Option2:
for j in range(m):
  print("Column", j, "is", A[:, j])
print("\n")
#Option3:
for i in range(n):
  for j in range(m):
    print("Element", i, j, "is", A[i, j])
print("\n")

#Another way to iterate the table item by item is to use a single iteration structure. This is especially useful for high-dimension arrays:
B = np.array([1, 2, 3, 4, 5, 6])
print(B)
print("\n")
for a in np.nditer(B):
    print(a)

#🐱‍🚀🐱‍👤🐱‍💻🐱‍🐉🐱‍👓🐱‍🏍✨