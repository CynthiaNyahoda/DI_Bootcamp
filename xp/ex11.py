import pandas as pd
import matplotlib.pyplot as plt
import urllib.request

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
filename = "auto-mpg.data"

urllib.request.urlretrieve(url, filename)

# Load the data
names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

# Define the bar_plot function
def bar_plot(df):
    toyota_df = df[(df["car_name"].str.contains("toyota", case=False)) & (df["model_year"] == 78)]
    plt.bar(toyota_df["cylinders"], toyota_df["cylinders"].count())
    plt.xticks(toyota_df["cylinders"].unique())
    plt.xlabel("Cylinders")
    plt.ylabel("Number of Cars")
    plt.title("Number of Toyota Cars with Different Cylinder Counts in 1978")
    plt.show()

# Call the bar_plot function with the df_mpg dataframe
bar_plot(df_mpg)

