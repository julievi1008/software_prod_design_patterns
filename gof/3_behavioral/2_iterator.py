"""Iterator example.

Iterator is a behavioral pattern that allows traversing items in a collection 
without exposing the collections underlying structure. It encapsulates this 
behavior into an iterator object.
"""
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class WordCollectionIterator(Iterator):
    """The iterator object. Holds the logic of how the collection is traversed. Inherits Iterator.

    Attributes:
        _position: Marks the current position of the iterator.
        _reverse: A flag to indicate direction of travel.
    """
    _position: int  
    _reverse: bool # type hint not class variable =)))

    def __init__(self, collection: Any, reverse: bool = False) -> None:
        """Initialize the iterator
        
        Args:
            collection: The collection of items.
            reverse: Direction of travel. Defaults to False.
        """

        self._collection = collection # instance variable
        self._reverse = reverse

        # Mark the starting position based on the direction the user wants to travel.
        if reverse:
            self._position = -1
        else:
            self._position = 0


    def __next__(self) -> str:
        """Get the next item in the collection.

        If you want to create a custom iterator this is the method you will use to code the logic for traversing
        your collection.
        
        Returns:
            The next item.

        Raises:
            StopIteration: When there is no more items in the collection.
        """

        try:
            item = self._collection[self._position]

            # Either increment or decrement the current position based on the _reverse flag.
            if self._reverse:
                self._position -= 1
            else:
                self._position += 1
        except IndexError:
            # When there is no more items, raise an exception.
            raise StopIteration()

        return item

    def __iter__(self) -> "WordCollectionIterator":
        """Returns the iterator itself. This is a python convention and some iteration tools might use it."""
        return self




class WordCollection(Iterable):
    """Example collection that can be iterated through. Inherits Iterable."""

    def __init__(self, collection: list[str]) -> None: # from __future__ import annotations
        """Initialize a WordCollection.
        
        Args:
            collection: A list of words.
        """
        self._collection = collection
        

    def __getitem__(self, index: int) -> str:
        """Returns the item in a given position.

        This allows 'collection[index]' style accessing to items.
        We use this in the WordCollectionIterator.__next__() method.
        
        Args:
            index: Position of the item.

        Returns:
            The item.
        """
        return self._collection[index]

    def __iter__(self) -> WordCollectionIterator:
        """Get the forwards iterator made from the WordCollection."""
        return WordCollectionIterator(self)
    
    def get_reverse_iterator(self) -> WordCollectionIterator:
        """Get the reverse iterator made from the WordCollection."""
        return WordCollectionIterator(self, True)


###
# Usage
###

# Initializing the WordCollection.
collection = WordCollection(["first", "second", "third", "fourth"])  

# Now we can loop (iterate) through the WordCollection.
for item in collection:
    print(item)
    
print('------------------------------------1')

# Reverse order.
for item in collection.get_reverse_iterator():
    print(item)

print('------------------------------------2')

# This is kind of what happens when you loop through the collection in a for loop.
collection_iterator = collection.__iter__()
while True:
    try:
        print(collection_iterator.__next__())
    except StopIteration:
        print("No more words to print\n")  # Demonstrates when the StopIteration is raised.
        break
print('------------------------------------3')

#print(WordCollectionIterator(["first", "second", "third", "fourth"])._reverse)

#1'15
#software requirements -base on that-> testing cases --> actually implement a code.
