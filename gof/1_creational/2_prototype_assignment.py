from abc import ABC, abstractmethod
import copy

# Assignment 1) Create an abstract class Prototype(ABC)
#   It should have an @abstractmethod `clone` without implementation.
#
#  YOUR ANSWER GOES BELOW

class Prototype(ABC):
    @abstractmethod
    def clone(self) -> 'Prototype':
        pass


# Assignment 2) Create a class `Product` that inherits `Prototype`
#   `__init__()` method should take parameter `name: str` and set it as member variable. 
#               Also set member variables `category` with an empty string and `price` with value 0.0 
#   The class should also contain methods `set_category`, `set_price`, `clone`, and `__str__`
#   Implement the set methods (for ex: self.category = ...), they should return self.
#   `clone` method should return a copy of the Product
#   `__str__` method should return a string representation of the class. You can use this f'{{name: "{self.name}", category: "{self.category}", price: {self.price}}}'
#
#  YOUR ANSWER GOES BELOW
class Product(Prototype):
    def __init__(self, name:str):
        self.name = name
        self.category = ''
        self.price = 0.0

    def set_category(self, category:str) ->'Product':
        self.category = category
        return self

    def set_price(self, price:float)->'Product':
        self.price = price
        return self

    def clone(self) -> 'Product':
        return copy.deepcopy(self)
        
    def __str__(self) -> str:
        return f'{{name: "{self.name}", category: "{self.category}", price: {self.price}}}'

# Assignment 3) Create a class `ProductCatalog` that inherits `Prototype`
#   The class should contain methods `__init__`, `add_product`, `clone`, and `__str__`
#   `__init__` initializes an empty dict `products` and a `product_count` set to 0
#   `add_product` should take one product as a parameter and it adds it to the dict `products`. 
#       Use the variable `product_count` as the key and increment the count by 1. Return self.
#
#   `clone` should return a deepcopy of the ProductCatalog
#
#   `__str__` should create a string representation of the class
#   You can use the following algorithm for creating the string representation
#       product_strs = {k: str(v) for k, v in self.products.items()}
#       return str(product_strs)
#
#  YOUR ANSWER GOES BELOW
class ProductCatalog(Prototype):
    def __init__(self):
        self.products = {}
        self.product_count = 0
    
    def add_product(self, product: str) ->'ProductCatalog':
        self.product_count += 1
        self.products[self.product_count] = product
        return self

    def clone(self) ->'ProductCatalog':
        return copy.deepcopy(self)

    def __str__(self) -> str:
        product_strs = {k: str(v) for k,v in self.products.items()} # dictionary comprehension
        return str(product_strs)

# Assignment 4) Show how the classes and cloning works.
# Create two Products and set their categories and prices.
# Clone the first product and set a new price for it.
# Create a ProductCatalog of the products you created.
# Clone the ProductCatalog and add a fourth product to it.
# Print both product catalogs in their own lines.
#
#  YOUR ANSWER GOES BELOW

product_1 = Product('banana').set_category('food').set_price(2.0)
print(product_1)

product_2 = Product('ice cream').set_category('food').set_price(5)
print(product_2)

product_3 = product_1.clone().set_price('1.35')
print(product_3)

ProductCatalog_1 = ProductCatalog()
ProductCatalog_1.add_product(product_1.name)
ProductCatalog_1.add_product(product_2.name)
ProductCatalog_1.add_product(product_3.name)
ProductCatalog_2 = ProductCatalog_1.clone().add_product(product_2.name)
print(ProductCatalog_1)
print(ProductCatalog_2)


