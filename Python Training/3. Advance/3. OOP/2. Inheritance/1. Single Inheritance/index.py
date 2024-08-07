# Super / Parent / Base Class
class Animal:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def animal_info(self):
        print(f"Animal Name is: {self.animal_name}")


# Child / Derived / Sub Class
class Dog(Animal):
    def __init__(self, name, animal_age):
        super().__init__(name)
        self.animal_age = animal_age
    def bark(self):
        print(f"woff woff, my age is {self.animal_age} yrs.")


dog = Animal("Dog")
buddy = Dog("Buddy", 16)

dog.animal_info()
buddy.animal_info()
buddy.bark()
