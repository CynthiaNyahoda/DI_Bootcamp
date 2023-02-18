import random

def guess_number(user_input):
    random_number = random.randint(1, 100)
    if user_input == random_number:
        print("Congratulations! You guessed the right number!")
    else:
        print("Sorry, better luck next time!")
