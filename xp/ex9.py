import pandas as pd

df = pd.DataFrame(["STD,City\tState",
                   "33,Kolkata\tWest Bengal",
                   "44,Chennai\tTamil Nadu",
                   "40,Hyderabad\tTelengana",
                   "80,Bangalore\tKarnataka"], columns=['row'])

# Split the 'row' column on both comma and tab separators
df = df['row'].str.split('[,\t]', expand=True)

# Rename the columns
df = df.rename(columns={0: 'STD', 1: 'City', 2: 'State'})

# Display the result
print(df)
df = df.drop(0)
