import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# Load CSV file into a Pandas DataFrame


sns.violinplot(x="Survived", y="Age", data=df)
plt.show()

sns.swarmplot(x="Pclass", y="Fare", data=df)
plt.show()


sns.barplot(x="Pclass", y="Survived", hue="Sex", data=df)
plt.show()


sns.heatmap(df.corr(), cmap="coolwarm", annot=True)
plt.show()


