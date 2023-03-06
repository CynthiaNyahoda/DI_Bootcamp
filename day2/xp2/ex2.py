# Explore the data. Print any important summary statistics. Plot the distributions of
# each feature. Plot any important relationships of each feature on the target variable or on each other.
# (You can use Seaborn as well)

import pandas as pd
import seaborn as sns

titanic_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(titanic_url)


print(df.describe())

# plots

sns.histplot(data=df, x='Age')
sns.histplot(data=df, x='Fare')
sns.histplot(data=df, x='SibSp')
sns.histplot(data=df, x='Parch')
sns.countplot(data=df, x='Sex')
sns.countplot(data=df, x='Embarked')
sns.countplot(data=df, x='Pclass')
sns.countplot(data=df, x='Survived')

