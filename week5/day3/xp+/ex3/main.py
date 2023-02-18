import random
import string

def generate_random_string(length):
    letters = string.ascii_letters  # contains both uppercase and lowercase letters
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

# generate a random string of length 5
random_string = generate_random_string(5)
print(random_string)
