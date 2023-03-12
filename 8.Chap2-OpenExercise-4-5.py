# Determinant:
# ✅ Look for a command from the numpy documentation (or elsewhere on the Internet) to calculate the matrix determinant.
# ✅ The determinant is a number that does not require a deeper understanding here.
# ✅ Calculate the determinants of the matrices A, B and AB, where... (as photo 1.PNG)
# ✅ and AB stands for matrix product. State that det (AB) = det (A) det (B) can be understood as the product of the numbers (the rounding error can be ignored).

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[-1, 1], [5, 7]])
detA = np.linalg.det(A)
detB = np.linalg.det(B)
(AB) = (A) * (B)
detAB = np.linalg.det(AB)

print(detA)
print(detB)
print(detAB)

# 🐱‍🚀🐱‍👤🐱‍💻🐱‍🐉🐱‍👓🐱‍🏍✨
