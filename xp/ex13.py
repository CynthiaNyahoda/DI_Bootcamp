import pandas as pd
import matplotlib.pyplot as plt

# Load the auto-mpg dataset
names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

# Create the scatter plot
plt.scatter(df_mpg["horsepower"], df_mpg["mpg"])
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.title("Relationship between Horsepower and MPG")
plt.show()

print(df_mpg)
