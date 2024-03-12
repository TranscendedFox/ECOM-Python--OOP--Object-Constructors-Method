class Animal:
    def __init__(self, name, species, color, age, weight):
        self.name = name
        self.species = species
        self.color = color
        self.age = age
        self.weight = weight

    def print_attributes(self):
        print("Name:", self.name, ", Species:", self.species, ", Color:", self.color, ", Age:", self.age, ", Weight:", self.weight)
