'''
Prototype is used for cloning / copying existing objects.

Examples:
    - Graphic editors: Create multiple different rectangles with different colors etc...
    - Game development: Clone characters, trees, buildings...
'''

import copy

class Car():
    def __init__(self):
        self.manufacturer = None
        self.color = None
    
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
        return self
    
    def set_color(self, color):
        self.color = color
        return self
    
    def clone(self):
        return copy.deepcopy(self)


###
# Usage
###

tesla_green = Car().set_manufacturer("Tesla").set_color("Green")
print(tesla_green.color)

tesla_red = tesla_green.clone().set_color("Red")
print(tesla_red.color)
print(tesla_green.color)