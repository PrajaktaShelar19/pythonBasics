from Car import Car
from Driver import Driver


class Cat:

   #  def __init__(self):
    # print("pass")

    def __init__(self, name, age):
        self.name = name
        self.age = age

My_cat = Cat("Prajakta", 31)

My_Car = Car("Toyota", "camry", 2014)
My_Driver = Driver("Prajakta", 31)

print(f"My name is {My_Driver.name} and age is {My_Driver.age} years old")
print(f"I like this car - {My_Car.make} {My_Car.model} {My_Car.year}")

#Reusability with multiple objects
friends_Car = Car("Skoda", "Rapid" , 2015)
My_Friends_Driver = Driver("priya", 28)

print(f"My {My_Friends_Driver.age} years old friend {My_Friends_Driver.name} is driving {friends_Car.make} {friends_Car.model} {friends_Car.year}")

#wheels is global access
print(f"My car has {My_Car.Wheels} wheels")
print(f"My friends car has {friends_Car.Wheels} wheels")

# Notes:
# Classes are the blueprints for creating objects in Python.
# They define the structure and behavior of the objects.
# To define a class, we use the class keyword followed by the class name and colon.
# The class body includes attributes and methods that define the class behavior.