'''
Similar to factory method, but more advanced / complex, as is about creating families of related products.

Examples:
    - GUI (Component -> Button, Textfield, TextArea...)
    - API integration
    - Game development (BaseLevel -> Level1, GameClient -> SingleplayerGameClient, MultiplayerGameClient ...)
'''

# abc = Abstract Base Class, it is the base Python package for creating abstract classes
from abc import ABC, abstractmethod

###
# Vehicle and Accessory classes
###
class Vehicle(ABC):
    @abstractmethod
    def type(self):
        pass

class Car(Vehicle):
    def type(self):
        return "Car"

class Truck(Vehicle):
    def type(self):
        return "Truck"


class Accessory(ABC):
    @abstractmethod
    def description(self):
        pass

class CarAccessory(Accessory):
    def description(self):
        return "Car Accessory"

class TruckAccessory(Accessory):
    def description(self):
        return "Truck Accessory"


###
# Abstract Factory Interface
###
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

    @abstractmethod
    def create_accessory(self):
        pass

###
# Concrete Factories
###
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

    def create_accessory(self):
        return CarAccessory()

class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()

    def create_accessory(self):
        return TruckAccessory()

###
# Usage
###

car_factory = CarFactory()

car = car_factory.create_vehicle()
car_accessory = car_factory.create_accessory()

print(f"Car is: {car.type()} and accessory: {car_accessory.description()}")