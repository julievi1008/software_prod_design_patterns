from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

# Assignment 1) Create class SQL()
#   It should be a @dataclass and have these fields:
#   fields (list), database (str), table (str)
#   This is your "product" at which we will be "building" with the class created next
#  YOUR ANSWER GOES BELOW

@dataclass
class SQL:
    fields: list[str] #= field(default_factory=list) -> TypeError: non-default argument 'database' follows default argument
    database: str
    table: str

# Assignment 2) Create class SQLBuilder(ABC)
#   This class is an abstract class as we pass and inherit ABC to it. This will be your builder class.
#   When you init the class with __init__(self) it should create new SQL() object and assign it to a member variable
#   the class should also have these methods: set_database, set_table, add_field
#       Implement the functionality of these methods (for ex: self.sql.database = ...) and all methods should return self
#   Create also one @abstractmethod called build_query which should just return pass
# YOUR ANSWER GOES BELOW

class SQLBuilder(ABC):
    def __init__(self):
        self.sql = SQL(fields=[], database='', table='')

    def set_database(self, database:str) -> 'SQLBuilder':
        self.sql.database = database #f'CREATE DATABASE IF NOT EXISTS {database_name};'
        return self
    def set_table(self, table:str) -> 'SQLBuilder':
        self.sql.table = table #f'CREATE TABLE IF NOT EXISTS {table_name} ({table_name}_id INT);'
        return self
    def add_field(self, field: list[str]) -> 'SQLBuilder':
        self.sql.fields.append(field)
        return self
    
    @abstractmethod
    def build_query(self):
        pass

# Assignment 3) Create class SQLBuilderReader(SQLBuilder)
#   This class should have only one method and that is to override the build_query method created in the inherited SQLBuilder
#   build_query method should return back this kind of string constructed from the self.sql:
#       pseudocode: "SELECT {fields} FROM {table}"
#       real example: "SELECT userId, name, age FROM User"
# YOUR ANSWER GOES BELOW
    
class SQLBuilderReader(SQLBuilder):
    def build_query(self) -> str:
        fields_str = ', '.join(self.sql.fields)
        return f'SELECT {fields_str} FROM {self.sql.table}'
    

# Assignment 4) Demonstrate the usage of your SQLBuilderReader class
#   Assign your SQLBuilderReader class to a variable and call the methods using method chaining to set a database, table, couple fields.
#   Example of method chaining reader.set_database("sales_system").table("User").add_field("userId")
#   Finally, print the result of calling the build_query() function
# YOUR ANSWER GOES BELOW

reader = SQLBuilderReader()
sq1_reader_1 = reader.set_database("sales_system")\
                     .set_table("User")\
                     .add_field("userId")\
                     .add_field('name')\
                     .add_field('age')
#print(sq1_reader_1)
print(sq1_reader_1.build_query()) # build_query must be at the end


# Note that the inheritance of SQLBuilderReader is not part of the builder pattern and this is exercise
# also utilizes parts of the factory pattern. Classically, the builder pattern only builds the containing object
# and has a method to return the object back.