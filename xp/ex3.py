import numpy as np

# Create a random numpy array with shape (5, 6) and integers between 1 and 100
arr = np.random.randint(low=1, high=101, size=(5, 6))
print("Random array:\n", arr)

# Compute the maximum integer for each row
max_row = np.amax(arr, axis=1)
print("Maximum integer for each row:\n", max_row)
