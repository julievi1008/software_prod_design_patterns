'''
Builder pattern allows constructions of a complex objects step by step.

Examples:
    - Document converter. For example: converter.set_format("PDF).set_file("document.pdf").convert("HTML")
    - SQL query builder. For example: sqlbuilder.table("customers").fields("*").operation("find").limit(3)
    - Pandas dataframe: df.apply(...).set_index("Name")
'''

from abc import ABC, abstractmethod

###
# Base class for vehicle
###
class Vehicle:
    def __init__(self):
        self.wheels = None
        self.seats = None
        self.engine = None

###
# Builder for vehicles
###
        # 26'
class VehicleBuilder():
    def __init__(self):
        self.vehicle = Vehicle()

    def set_wheels(self, value):
        self.vehicle.wheels = value
        return self

    def set_seats(self, value):
        self.vehicle.seats = value
        return self
    
    def set_engine(self, value):
        self.vehicle.engine = value
        return self
    
    def build(self):
        return self.vehicle

###
# Usage
###

builder = VehicleBuilder()

# Method chaining
normal_car = builder.set_wheels(4).set_seats(5).set_engine("electric").build()

print(f"Car wheels: {normal_car.wheels}, seats: {normal_car.seats}")


# Alternatively, the chaining could be represented this way:
# (Notice how \ is used at the end of the line to move the code to next line)
normal_car = builder\
            .set_wheels(4)\
            .set_seats(5)\
            .set_engine("electric")\
            .build()
