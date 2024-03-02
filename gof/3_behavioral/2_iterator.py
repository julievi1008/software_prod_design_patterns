"""Iterator example.

Iterator is a behavioral pattern that allows traversing items in a collection 
without exposing the collections underlying structure. It encapsulates this 
behavior into an iterator object.
"""

from collections.abc import Iterable, Iterator
from typing import Any


class WordCollectionIterator(Iterator):
    """The iterator object. Holds the logic of how the collection is traversed. Inherits Iterator.

    Attributes:
        _position: Marks the current position of the iterator.
        _reverse: A flag to indicate direction of travel.
    """
    _position: int  
    _reverse: bool

    def __init__(self, collection: Any, reverse: bool = False) -> None:
        """Initialize the iterator
        
        Args:
            collection: The collection of items.
            reverse: Direction of travel. Defaults to False.
        """

        self._collection = collection
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

    def __init__(self, collection: list[str]) -> None:
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



def word_collection_example():
    # Initializing the WordCollection.
    collection = WordCollection(["first", "second", "third", "fourth"])  

    # Now we can loop (iterate) through the WordCollection.
    for item in collection:
        print(item)
        
    print()

    # Reverse order.
    for item in collection.get_reverse_iterator():
        print(item)

    print()

    # This is kind of what happens when you loop through the collection in a for loop.
    collection_iterator = collection.__iter__()
    while True:
        try:
            print(collection_iterator.__next__())
        except StopIteration:
            print("No more words to print\n")  # Demonstrates when the StopIteration is raised.
            break



class FileReaderIterator(Iterator):
    """FileReaderIterator for iterating through text files.

    Attributes:
        _position: Marks the current position of the iterator.
    """
    _position: int

    def __init__(self, file_path: str) -> None:
        """Initialize the iterator.
        
        Args:
            file_path: Path to the file.
        """
        self._file = open(file_path, 'r')
        self._position = 0

    def __next__(self) -> str:
        """Logic for getting the next item."""
        line = self._file.readline()  # Reads the next line from the file.

        # `readline()` returns an empty line when the end is reached,
        # which is why we do this part a bit different.
        if not line:
            self._file.close()
            raise StopIteration()
        return line.strip()  # `.strip()` for stripping the new line characters

    def __iter__(self) -> "FileReaderIterator":
        return self


class FileReader(Iterable):
    """Object that holds only the path to a file.
    
    Attributes:
        _file_path: String representation of the file path.
    """
    def __init__(self, file_path: str) -> None:
        """Initialize FileReader."""
        self._file_path = file_path

    def __iter__(self) -> FileReaderIterator:
        """Create the iterator."""
        return FileReaderIterator(self._file_path)



# Usage
def filereader_example():
    file_reader = FileReader("./example.txt")

    for line in file_reader:
        print(line)


if __name__ == "__main__":
    word_collection_example()
    filereader_example()

