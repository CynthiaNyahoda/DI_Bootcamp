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

#3  changing store number to 2
brand["number of stores"] = 2
print(brand)


# 4. Print a sentence that explains who Zaras clients are.
print("Zara caters to", ", ".join(brand["type_of_clothes"]), "customers with their offerings of clothing.")

# 5. Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"
print(brand)

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
    print(brand)

# 7. Delete the information about the date of creation.
del brand["creation_date"]
print(brand)

# 8. Print the last international competitor.
print("The last international competitor is", brand["international_competitors"][-1])

# 9. Print the major clothes colors in the US.
print("The major clothes colors in the US are", ", ".join(brand["major_color"]["US"]))

# 10. Print the amount of key value pairs (ie. length of the dictionary)
print("The brand dictionary contains", len(brand), "key-value pairs.")

# 11.Print the keys of the dictionary
print("The keys in the brand dictionary are:", brand.keys())

# 12. Create another dictionary called more_on_zara
more_on_zara = {
    "creation_date": 1975, 
    "number_stores": 10000
}
print (more_on_zara)

#13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
print(brand)

#14. Print the value of the key number_stores
print("The value of the key number_stores is:", brand["number_stores"])
