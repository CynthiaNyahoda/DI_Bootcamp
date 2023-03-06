import pandas as pd
import numpy as np

# Create the Series
series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))

# Find the unique values and their frequencies
value_counts = series.value_counts()

print(value_counts)
