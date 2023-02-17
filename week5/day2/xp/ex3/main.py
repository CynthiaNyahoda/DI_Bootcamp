import random

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

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    
    def train(self):
        bark_output = self.bark()
        self.trained = True
        return bark_output
    
    def play(self, *dog_names):
        dog_names_str = ", ".join(dog_names)
        print(f"{dog_names_str} all play together")
    
    def do_a_trick(self):
        if self.trained:
            trick_options = [f"{self.name} does a barrel roll",
                             f"{self.name} stands on his back legs",
                             f"{self.name} shakes your hand",
                             f"{self.name} plays dead"]
            trick_output = random.choice(trick_options)
            return trick_output
        else:
            return f"{self.name} is not trained yet"
        
pet_dog = PetDog("Max", 5, 20)

print(pet_dog.train())  
print(pet_dog.trained)  
pet_dog.play("Buddy", "Rocky")  
print(pet_dog.do_a_trick())  