

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8, 'cynara':5}


total_cost = 0


for member, age in family.items():

    if age < 3:
        ticket_price = 0
    elif age >= 3 and age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
   
    print(f"{member} has to pay ${ticket_price}")
    
    
    total_cost += ticket_price


print(f"The family's total cost for the movies is ${total_cost}")
