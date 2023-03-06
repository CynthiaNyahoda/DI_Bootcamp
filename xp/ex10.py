import urllib.request

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
filename = "auto-mpg.data"

urllib.request.urlretrieve(url, filename)

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

# Define the scatter_plot function
def scatter_plot(df):
    plt.scatter(df["displacement"], df["acceleration"])
    plt.xlabel("Displacement")
    plt.ylabel("Acceleration")
    plt.title("Displacement vs Acceleration")
    plt.show()

# Call the scatter_plot function with the df_mpg dataframe
scatter_plot(df_mpg)
