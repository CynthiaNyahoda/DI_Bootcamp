toppings = []
price = 10

while True:
    topping = input("Enter a pizza topping or 'quit' to exit: ")
    if topping == 'quit':
        break
    toppings.append(topping)
    price += 2.5

print("Toppings on your pizza:", toppings)
print( "total price: $",price)
