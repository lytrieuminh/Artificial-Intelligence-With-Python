#Note4-Statistical Functions:
import numpy as np

#Many statistical indicators can be calculated from the numerical values in the table. The sum is calculated with the command sum(), which can optionally be given as the second argument the number of the axis over which the sum is calculated:
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
print("\n")
sum1 = np.sum(A)  #The result will be: 1+2+3+4+5+6=21
sum2 = np.sum(A, 0)  #Sum the columns: 1+4  2+5  3+6
sum3 = np.sum(A, 1)  #Sum the rows: 1+2+3  4+5+6
print(sum1)
print("\n")
print(sum2)
print("\n")
print(sum3)
print("\n")

#The product is calculated similarly with the prod() command:
B = np.array([[1, 2, 3], [4, 5, 6]])
print(B)
print("\n")
prod1 = np.prod(B)  #The result will be: 1*2*3*4*5*6=720
prod2 = np.prod(B, 0)  #Multiply the columns: 1*4  2*5  3*6
prod3 = np.prod(B, 1)  #Multiply the rows: 1*2*3  4*5*6
print(prod1)
print("\n")
print(prod2)
print("\n")
print(prod3)
print("\n")

#✨There are also cumulative variants cumsum() and cumprod() for sum and result✨

#The largest and smallest elements are found with the min() and max() commands:
C = np.array([[1, 2, 3], [4, 5, 6]])
print(C)
print("\n")
min1 = np.min(C)  #The element has smallest value: 1
min2 = np.min(C, 0)  #The row has smallest value
min3 = np.min(C, 1)  #The column has smallest value
print(min1)
print("\n")
print(min2)
print("\n")
print(min3)
print("\n")

max1 = np.max(C)  #The element has largest value: 6
max2 = np.max(C, 0)  #The row has largest value
max3 = np.max(C, 1)  #The column has largest value
print(max1)
print("\n")
print(max2)
print("\n")
print(max3)
print("\n")

#The average of the elements is calculated with the function mean(), which can also be assigned to a specific axis:
np.mean(A)
np.mean(A, 0)
np.mean(A, 1)

#The median, ie the "middle" value of the numerical values, is determined by the function median():
np.median(A)
np.median(A, 0)
np.median(A, 1)

#The variance and its standard root deviation measure how far the numbers are from their mean. For these, there are functions var() and std():
np.std(A)
np.std(A, 0)
np.std(A, 1)
np.var(A)
np.var(A, 0)
np.var(A, 1)

#🐱‍🚀🐱‍👤🐱‍💻🐱‍🐉🐱‍👓🐱‍🏍✨