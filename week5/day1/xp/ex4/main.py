class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            if animal[0] in sorted_animals:
                sorted_animals[animal[0]].append(animal)
            else:
                sorted_animals[animal[0]] = [animal]
        return sorted_animals
    
    def get_groups(self):
        sorted_animals = self.sort_animals()
        for key, value in sorted_animals.items():
            print(key + ":")
            for animal in value:
                print("\t" + animal)

# Creating an object called ramat_gan_safari and call all the methods.
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Adding animals to the zoo
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Cat")

# Getting the list of animals in the zoo
ramat_gan_safari.get_animals()

# Selling an animal
ramat_gan_safari.sell_animal("Tiger")

# Getting the sorted list of animals
sorted_animals = ramat_gan_safari.sort_animals()
print("Sorted animals:")
print(sorted_animals)


ramat_gan_safari.get_groups()
