# Drawing lines:
# ✅ Draw the lines y = 2x + 1, y = 2x + 2 and y = 2x + 3 in the same figure.
# ✅ Use different drawing colors and line types for your graphs to make them stand out in black and white.
# ✅ Set the image title and captions for the horizontal and vertical axes.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

plt.plot(x, y1, "g")
plt.plot(x, y2, "r")
plt.plot(x, y3, "c")

plt.plot(x, y1, linewidth=2, linestyle="-")
plt.plot(x, y2, linewidth=2, linestyle=":")
plt.plot(x, y3, linewidth=2, linestyle="-.")

plt.title('Title')
plt.xlabel('x')
plt.ylabel('y1')
plt.ylabel('y2')
plt.ylabel('y3')

plt.show()

# 🐱‍🚀🐱‍👤🐱‍💻🐱‍🐉🐱‍👓🐱‍🏍✨
