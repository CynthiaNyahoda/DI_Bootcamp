import pandas as pd

# Read the data into a pandas DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Drop the "EngineSize" and "Length" columns using the drop() method
df.drop(columns=['EngineSize', 'Length'], inplace=True)

# Verify that the columns have been removed
print(df.head())


# SECOND WAY

import pandas as pd

# Read the data into a pandas DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Delete the "EngineSize" and "Length" columns using the del statement
del df['EngineSize']
del df['Length']

# Verify that the columns have been removed
print(df.head())
