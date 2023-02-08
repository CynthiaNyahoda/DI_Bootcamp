# creating a dictionary
brand = { 
"name": "Zara", 
"creation_date": 1975, 
"creator_name": "Amancio Ortega Gaona", 
"type_of_clothes": ["men", "women", "children", "home"], 
"international_competitors": ["Gap", "H&M", "Benetton"], 
"number_stores": 7000, 
"major_color": {
     "France": ["blue"], 
    "Spain": ["red"], 
    "US": ["pink", "green"]
}
    
}

#  changing store number to 2
brand["number of stores"] = 2



# Print a sentence that explains who Zara's clients are
print(f"'name' offers clothing for 'type_of_clothes' and serves clients of all ages.")

