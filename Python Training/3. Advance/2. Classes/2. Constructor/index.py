# 2. __init__ is a constructor which allow us to create variables in class.

"""In Python, a constructor is a special method that is called when an instance (object) of a class
is created. The constructor method is
defined using the __init__ method. It allows you to initialize the object's attributes with specific values
when the object is created.
"""

"""The primary use of a constructor is to initialize the attributes of a class when an object is created. 
This ensures that the object is in a valid state right from the start."""

# From FreeCodeCamp https://www.freecodecamp.org/news/python-attributes-class-and-instance-attribute-examples/
""" Class attributes remain the same for every object and are defined outside the __init__() function. 
Instance attributes are somewhat dynamic because they can have different values in each object."""
# From InterviewBit
""" __init__ is a constructor method in Python and is automatically called to allocate memory when a new object/instance is created. 
All classes have a __init__ method associated with them. It helps in distinguishing methods and attributes of a class 
from local variables."""

class Person:
    # 👇 Class Attributes
    no_of_legs = 2

    def __init__(self):
        # 👇 Instance Variables or Instance attributes
        self.name = "Jordan"
        self.age = 20
        self.location = "USA"

    def user_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Location: {self.location}")


# Object 1
jordan = Person()
jordan.user_info()
print(jordan.no_of_legs)

# Object 2
Deepak = Person()
Deepak.user_info()
print(Deepak.no_of_legs)
