import numpy as np

a = np.array([1, 2, 3, np.nan, 5, 6, 7, np.nan])

# Use boolean indexing to drop NaN values
a = a[~np.isnan(a)]

print(a)