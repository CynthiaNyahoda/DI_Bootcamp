#EXERCISE 7
fruits = input("Please enter your favorite fruit(s), separated by spaces: ").split()
print(fruits)
while True:
    user_input = input("Please enter the name of a fruit: ")
    if user_input in fruits:
        print("You chose one of your favorite fruits! Enjoy!")
    
    else:
        print("You chose a new fruit. I hope you enjoy.")
        break