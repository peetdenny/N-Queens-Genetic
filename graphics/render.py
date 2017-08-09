import matplotlib.pyplot as plt
import numpy as np

nrows, ncols = 9,9
image = np.zeros(nrows*ncols)

image = image.reshape((nrows, ncols))

plt.matshow(image)
plt.show()
