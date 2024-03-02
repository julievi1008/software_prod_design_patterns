'''
With observer pattern you can notify multiple subscribers of an event or a 
change somewhere else in your application.

Examples:
    - UI events. E.g. clicking a button
    - Social media notifications
'''
from abc import ABC, abstractmethod

class Observer(ABC):
    """Abstract Observer class that will be implemented later."""

    @abstractmethod
    def update(self, message: str):
        pass

class Publisher:
    """Class for the Publisher.
    
    Holds a list of observers and provides functionality to add, remove and notify the 
    observers. This is a one-to-many relationship. One publisher can be followed by 
    many subscribers.
    """
    def __init__(self):
        """Initialize the Publisher object with an empty list of observers."""
        self._observers: list[Observer] = []

    def add_observer(self, observer: Observer):
        """Add an observer to the list if it is not already there"""
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        """Remove an observer from the list."""
        self._observers.remove(observer)

    def notify_observers(self, message: str):
        """Trigger the update method of all observers."""
        for observer in self._observers:
            observer.update(message)

class ObserverImplementationA(Observer):
    """Implementation of the Observer class.

    This is the actual class that will be added to the publishers list.
    """
    def __init__(self, subscriber_name: str):
        self.subscriber_name = subscriber_name

    def update(self, message: str):
        """Holds the logic of what the observer should do when it is notified."""
        print(f"{self.subscriber_name}: {message}")

class ObserverImplementationB(Observer):
    """A different implementation.

    It can still observe the Publisher because it inherits the Observer.
    """
    def __init__(self, subscriber_name: str, data: str):
        self.subscriber_name = subscriber_name
        self.data = data

    def update(self, message: str):
        """This is again a different implementation."""
        if message == "Event 2":
            self.data = "Data was modified"

        print(f"{self.subscriber_name} has data:\n{self.data}")



if __name__ == "__main__":
    event_publisher = Publisher()

    observer_a = ObserverImplementationA("Observer A")
    observer_b = ObserverImplementationA("Observer B")
    observer_c = ObserverImplementationB("Observer C", "Some data")

    event_publisher.add_observer(observer_a)
    event_publisher.add_observer(observer_b)
    event_publisher.add_observer(observer_c)

    event_publisher.notify_observers("Event 1")
    print()

    event_publisher.remove_observer(observer_a)

    event_publisher.notify_observers("Event 2")
