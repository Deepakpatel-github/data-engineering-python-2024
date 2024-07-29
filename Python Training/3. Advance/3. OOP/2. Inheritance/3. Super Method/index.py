class Animal:
    var = 0

    def __init__(self, breed, size, color, speed):
        self.breed = breed
        self.size = size
        self.color = color
        self.speed = speed
        Animal.var += 1
        print("Parent Constructor")
        print(
            f"Breed: {self.breed}, Size: {self.size}, Color: {self.color}, Speed: {self.speed}"
        )

    @classmethod
    def get_var(cls):
        print(cls.var)

# Super method is used to call parent class constructor to the child class.
class Dog(Animal):
    def __init__(self, animal_name, breed, size, color, speed):
        # 👇 Calling Parent Class Constructor
        super().__init__(breed, size, color, speed)
        self.animal_name = animal_name
        print(f"Name: {self.animal_name}")

    def object_info(self):
        print(f" ~ Object Information ~")
        print(f"Animal name: {self.animal_name}")
        print(f"Breed name: {self.breed}")
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")
        print(f"Speed: {self.speed} Km/h")

    @staticmethod
    def bark():
        print("woff woff")


buddy = Dog("Dog", "IDK", 40, "blue", 50)
buddy1 = Dog("Dog1", "IDK1", 1, "blu1e", 1)
buddy2 = Dog("Dog2", "IDK2", 2, "blue2", 2)
buddy.object_info()
buddy.bark()
buddy.get_var()
buddy1.get_var()
buddy2.get_var()
buddy.get_var()
