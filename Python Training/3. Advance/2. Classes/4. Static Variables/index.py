'''Static variables, also known as class variables, are variables that are shared among
all instances of a class. They are not tied to any specific instance, but rather
to the class itself. Static variables serve several important purposes in object-oriented programming:

Uses of Static Variables
Shared Data Across Instances:

Static variables can hold data that should be shared among all instances of a class.
For example, a counter that tracks the number of instances created.'''

class Car:
    # 👇 Static variable
    num_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # 👇 Accessing static variable
        Car.num_cars += 1


# Creating instances of Car
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

print("Number of cars created:", Car.num_cars)  # 2
Car.num_cars = 80
car1.num_cars=50
car3 = Car('','')
car4 = Car('','')
print(car1.num_cars)
print(car2.num_cars)
print(car3.num_cars)
print(car4.num_cars)
print(Car.num_cars)