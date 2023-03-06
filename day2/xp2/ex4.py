# Split the data into train and test sets.
# Do it randomly and also do it by a certain feature. Explain why you chose that feature.
# Don’t forget about stratifying the target variable

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('Survived', axis=1), df['Survived'], test_size=0.2, random_state=42)



# Create an instance of StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

# Split the data into training and testing sets based on the 'Sex' column
for train_index, test_index in split.split(df, df['Sex']):
    X_train = df.loc[train_index].drop('Survived', axis=1)
    X_test = df.loc[test_index].drop('Survived', axis=1)
    y_train = df.loc[train_index]['Survived']
    y_test = df.loc[test_index]['Survived']
