import pandas as pd

# Read the data from the URL into a DataFrame
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url)

# Print how many columns are of each datatype
print(df.dtypes.value_counts())

# Change the column name "Type" to "TypeOfCar" and print the head of the dataframe
df = df.rename(columns={'Type': 'TypeOfCar'})
print(df.head())

# Print how many values are missing from each column
print(df.isnull().sum())

# Print which column has the most missing values
print(df.isnull().sum().idxmax())


