import random

def compare_numbers(num):
    random_num = random.randint(1, 100)
    if num == random_num:
        print("Success! Both numbers are " + str(num) + ".")
    else:
        print("Fail. The number " + str(num) + " is not the same as the random number " + str(random_num) + ".")

compare_numbers(50)
