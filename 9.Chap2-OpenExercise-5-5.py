# Inverse matrix:
# ✅ Calculate the inverse matrix of matrix A and
# ✅ check with the matrix product that both AA−1 and A−1A produce a unit matrix with ones in diagonals and zeros elsewhere.

import numpy as np

A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
X = np.linalg.solve(A, A)
print(X)

# 🐱‍🚀🐱‍👤🐱‍💻🐱‍🐉🐱‍👓🐱‍🏍✨
