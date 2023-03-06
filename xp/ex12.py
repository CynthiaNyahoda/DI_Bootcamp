import pandas as pd
import matplotlib.pyplot as plt

names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

def line_plot(df):
    # filter dataframe to only include cars of toyota company
    filtered_df = df[df['car_name'].str.startswith('toyota', case=False)]
    
    # group by model_year and calculate the mean weight for each year
    grouped_df = filtered_df.groupby('model_year')['weight'].mean().reset_index(name='mean_weight')
    
    # plot the line chart
    fig, ax = plt.subplots(figsize=(8,6))
    ax.plot(grouped_df['model_year'], grouped_df['mean_weight'])
    ax.set_xlabel('Model Year')
    ax.set_ylabel('Mean Weight (lbs)')
    ax.set_title('Change in Mean Weight of Toyota Cars throughout the Years')
    plt.show()

line_plot(df_mpg)

