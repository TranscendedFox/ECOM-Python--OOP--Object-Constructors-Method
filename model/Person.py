class Person:

    def __init__(self, name, last_name, age, height, weight, pets):
        self.__name = name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.__pets = pets

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def print_attributes(self):
        print("Name:", self.__name, ", Last Name:", self.last_name, ", Age:", self.age, ", Height:", self.height, ", Weight:", self.weight)

        if len(self.__pets) > 0:
            print(self.__name, "Pets:")
            for pet in self.__pets:
                pet.print_attributes()

    def add_pet(self, pet):
        self.__pets.append(pet)

    def remove_pet(self, pet_name):
        for pet in self.__pets:
            if pet.name == pet_name:
                self.__pets.remove(pet)
