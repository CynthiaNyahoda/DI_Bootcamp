class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal_type, quantity=1):
        self.animals[animal_type] = self.animals.get(animal_type, 0) + quantity

    def get_info(self):
        animal_info = []
        for animal_type, quantity in sorted(self.animals.items()):
            animal_info.append(f"{animal_type} : {quantity}")
        return f"{self.name}'s farm\n" + "\n".join(animal_info) + "\n\n    E-I-E-I-0!"

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        animal_types = ', '.join(self.get_animal_types())
        return f"{self.name}'s farm has {animal_types}."

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

