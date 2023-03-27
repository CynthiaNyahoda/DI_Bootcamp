import sqlite3
import requests
import random

# Make an HTTP GET request to the API endpoint
response = requests.get("https://restcountries.com/v2/all")

# Parse the response to extract the required attributes for the 10 random countries
countries_data = response.json()
countries = random.sample(countries_data, 10)  # Select 10 random countries

# Using a database connection library to connect to the database and create a table to store the countries' data
conn = sqlite3.connect('countries.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE countries
                  (id INTEGER PRIMARY KEY,
                   name TEXT,
                   capital TEXT,
                   flag TEXT,
                   subregion TEXT,
                   population INTEGER)''')

# Iterate over the 10 random countries and insert the values of the attributes into the database table
for i, country in enumerate(countries):
    name = country['name']
    capital = country['capital']
    flag = country['flag']
    subregion = country['subregion']
    population = country['population']

    cursor.execute("INSERT INTO countries VALUES (?, ?, ?, ?, ?, ?)", (i+1, name, capital, flag, subregion, population))

# Commit the changes to the database and close the connection
conn.commit()
conn.close()
