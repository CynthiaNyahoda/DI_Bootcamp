class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(cat_list):
    oldest_cat = None
    max_age = 0
    for cat in cat_list:
        if cat.age > max_age:
            oldest_cat = cat
            max_age = cat.age
    return oldest_cat

cat1 = Cat("Fluffy", 3)
cat2 = Cat("Whiskers", 5)
cat3 = Cat("Mittens", 2)

oldest_cat = find_oldest_cat([cat1, cat2, cat3])
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
