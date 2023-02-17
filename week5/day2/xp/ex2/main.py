class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight against {other_dog.name}"
        else:
            return f"{other_dog.name} won the fight against {self.name}"
        
dog1 = Dog("Max", 5, 20)
dog2 = Dog("Buddy", 3, 15)
dog3 = Dog("Rocky", 7, 25)

print(dog1.bark())  
print(dog2.run_speed())  
print(dog3.fight(dog1))  
