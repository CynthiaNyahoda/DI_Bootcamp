class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} was born into the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"The {self.last_name} family members are:")
        for member in self.members:
            print(member['name'])
            
# initial members data
members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

#  Family instance
my_family = Family('Smith', members)

# adding a new child to the family
my_family.born(name='John', age=0, gender='Male')

# checking if a family member is over 18
print(my_family.is_18('Michael'))  # True
print(my_family.is_18('John'))     # False


my_family.family_presentation()
