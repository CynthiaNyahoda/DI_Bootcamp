#Question 1

total_cost = 0

while True:
    age = int(input("What is the age of the next person: "))
    if age <= 0:
        break
    if age < 3:
        cost = 0
    elif age < 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost

print("Total cost of tickets: $",  total_cost)




#Question 2
teens = ['John', 'Jane', 'Tom', 'Sophie']
final_teens = []

for teen in teens:
    age = int(input(f"What is the age of {teen}: "))
    if age < 16 or age > 21:
        continue
    final_teens.append(teen)

print("Final list of teenagers:", final_teens)



