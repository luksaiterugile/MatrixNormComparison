import numpy as np
import matplotlib.pyplot as plt
import random

norm_array = []
reverse_norm_array = []
for i in range(10000):
  random_array = np.random.uniform(-1, 1, size=(18))
  random_matrix = random_array.reshape(3,6)
  norm = np.linalg.norm(random_matrix)
  norm_array.append(norm)
  reverse_matrix = np.linalg.pinv(random_matrix)
  reverse_norm = np.linalg.norm(reverse_matrix)
  reverse_norm_array.append(reverse_norm)


plt.hist(norm_array, label = "Random matrix rates", bins=50)
plt.hist(reverse_norm_array, label = "Pseudo-inverse matrix norms", bins=50)
plt.legend()  
plt.savefig('matrix_comparison_histogram.png')

print("Maximum of random matrix norms:", max(norm_array))
print("Maximum of pseudo-inverse matrix norms:",max(reverse_norm_array))