# Draw a dot pattern:
# ✅ Create a numpy table x that contains the values 1,2,3,4,5,6,7,8,9.
# ✅ Create another table y with the values ​​-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78.
# ✅ Draw the scattering pattern of the points (x, y). Use the + symbol to represent points.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([-0.57, -2.57, -4.80, -7.36, -
             8.78, -10.52, -12.85, -14.69, -16.78])

plt.scatter(x, y, color="r", marker="+", label="Points")
plt.show()

# 🐱‍🚀🐱‍👤🐱‍💻🐱‍🐉🐱‍👓🐱‍🏍✨
