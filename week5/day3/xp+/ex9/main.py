from faker import Faker

fake = Faker()  # initializing the faker object

users = []  # creating an empty list to store the users

def add_user():
    """Add a new user to the list."""
    name = fake.name()
    address = fake.address()
    language_code = fake.language_code()
    user = {'name': name, 'address': address, 'language_code': language_code}
    users.append(user)

add_user()
for i in range(10):
    add_user()
print(users)

