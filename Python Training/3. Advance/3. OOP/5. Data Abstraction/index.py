# Data Abstraction
"""Data abstraction in Python refers to the concept of hiding the complex implementation details of a class and exposing
 only the essential features and interfaces to the users."""

""" Abstraction is used to hide the internal functionality of the function from the users. The users only interact with 
 the basic implementation of the function, but inner working is hidden. User is familiar with that "what function does" 
 but they don't know how it does."""

# Why Abstraction is Important?
""" In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity.
 It also enhances the application efficiency. """

""" In Python, data abstraction can be achieved through the use of classes and methods, specifically by:

1. Encapsulation: Using private(__) and protected(_) attributes and methods.
    Encapsulation helps in data abstraction by restricting direct access to some of the object's components, 
    which can be achieved using private (__) and protected (_) attributes and methods."""


class Employee:
    def __init__(self, name, age, salary):
        self.__name = name  # Private attribute
        self._age = age  # Protected attribute
        self.salary = salary  # Public attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            raise ValueError("Age must be positive")

    def get_salary(self):
        return self.salary

    def increment(self, amount):
        self.salary += amount
        return self.salary


emp1 = Employee("John Doe", 30, 50000)
print(emp1.get_name())  # Output: John Doe
emp1.set_age(31)
print(emp1.get_age())  # Output: 31

"""
2. Abstract Classes and Methods: Using the abc module to create abstract base classes.
    Abstract classes and methods are a way to achieve data abstraction by defining a class that cannot be instantiated 
    and must be subclassed by other classes. Abstract methods in these classes must be implemented by any subclass.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


# animal = Animal()  # This will raise an error as Animal is an abstract class
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
