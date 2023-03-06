import pandas as pd
import seaborn as sns

titanic_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(titanic_url)

# checking for missing values
print(df.isna().sum())

# Cabin column, as it has many missing values and may not be useful


# To make the categorical features numeric, we can use one-hot encoding for the nominal features and ordinal encoding for the ordinal feature

# One-hot encoding for Sex and Embarked
df = pd.get_dummies(df, columns=['Sex', 'Embarked'])

# Ordinal encoding for Pclass
df['Pclass'] = df['Pclass'].map({1: 'first', 2: 'second', 3: 'third'})
df['Pclass'] = pd.Categorical(df['Pclass'], categories=['first', 'second', 'third'], ordered=True)
df['Pclass'] = df['Pclass'].cat.codes


# To scale the continuous features, we can use standardization or normalization:


# Standardization of Age and Fare
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# We can also categorize the Age and Fare columns, by binning them into age groups and fare ranges

# Binning of Age and Fare
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 18, 35, 60, 100], labels=['child', 'young adult', 'adult', 'senior'])
df['FareRange'] = pd.cut(df['Fare'], bins=bins, labels=labels)
