from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class WordCollectionIterator(Iterator):
    _position: int  
    _reverse: bool # type hint =))) not class variable =)))

    def __init__(self, collection: Any, reverse: bool = False) -> None:
        self._collection = collection 
        self._reverse = reverse # instance variable

        if reverse:
            self._position = -1
        else:
            self._position = 0

    def __next__(self) -> str:
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
    def __init__(self, collection: list[str]) -> None: # from __future__ import annotations

        self._collection = collection
        
    def __getitem__(self, index: int) -> str:
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
