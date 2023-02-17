class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']} can {member['power']}.")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old and cannot use their power.")
        else:
            raise Exception(f"{name} is not a member of the {self.last_name} family.")

    def incredible_presentation(self):
        super().family_presentation()
        print("The Incredibles:")
        for member in self.members:
            print(f"{member['incredible_name']} - {member['power']}")
# initial members data
members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

# create a TheIncredibles instance
my_incredibles = TheIncredibles('Parr', members)

# use the power of a family member over 18 years old
my_incredibles.use_power('Michael')  


# print the incredible presentation of the family
my_incredibles.incredible_presentation()


# add a new child to the family with an unknown power
my_incredibles.born(name='Jack', age=0, gender='Male', power='Unknown Power', incredible_name='Unknown')

# print the incredible presentation of the family again
my_incredibles.incredible_presentation()

