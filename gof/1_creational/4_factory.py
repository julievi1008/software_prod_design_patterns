'''
The factory method provides an interface for creating objects, but allows subclasses to alter
the type of objects created.

Examples:
    - GUI (Component -> Button, Textfield, TextArea...)
    - API integration
    - Game development (BaseLevel -> Level1, GameClient -> SingleplayerGameClient, MultiplayerGameClient ...)
'''

# abc = Abstract Base Class, it is the base Python package for creating abstract classes
from abc import ABC, abstractmethod

###
# Superclass for all vehicles
###
class Vehicle(ABC):
    @abstractmethod
    def type(self):
        pass
    
    @abstractmethod
    def sound(self):
        pass

###
# Concrete implementation of a Car
###
class Car(Vehicle):
    def type(self):
        return "Car"
    def sound(self):
        return "Tuut"

###
# Concrete implementation of a Truck
###
class Truck(Vehicle):
    def type(self):
        return "Truck"
    def sound(self):
        return "TÖÖT"

###
# Factory class which will create the vehicles
###
class VehicleFactory:
    # Factory usually has a single method that initializes and returns the class
    def get_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError(f"Vehicle type {vehicle_type} not supported")

###
# Usage example
###
factory = VehicleFactory()

car = factory.get_vehicle("car")
print(f"Car type is: {car.type()} that makes this sound: {car.sound()}")

truck = factory.get_vehicle("truck")
print(f"Truck type is: {truck.type()} that makes this sound: {truck.sound()}")

###
# Advanced usage example
###

# We could even utilize enums for "car" and "truck"
from enum import Enum
class CarType(Enum):
    CAR = "car"
    TRUCK = "truck"

car = factory.get_vehicle(CarType.CAR.value)
print(f"Car type is: {car.type()} that makes this sound: {car.sound()}")