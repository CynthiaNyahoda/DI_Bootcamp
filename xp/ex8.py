import pandas as pd
import numpy as np

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})

# Read the data into a pandas DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Join the two dataframes on columns 'fruit' and 'pazham'
merged_df = pd.merge(df1, df2, left_on=['fruit'], right_on=['pazham'])

# Drop the duplicate column 'pazham'
merged_df = merged_df.drop('pazham', axis=1)

# Print the resulting dataframe
print(merged_df)
