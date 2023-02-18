import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Loading the JSON string into a Python dictionary
data = json.loads(sampleJson)

# Accessing the nested "salary" key
salary = data['company']['employee']['payable']['salary']
print("Salary:", salary)

# Adding a "birth_date" key at the same level as the "name" key
data['company']['employee']['birth_date'] = "1990-01-01"

# Saving the updated dictionary as JSON to a file
with open('output.json', 'w') as f:
    json.dump(data, f)

print("JSON data saved to output.json")
