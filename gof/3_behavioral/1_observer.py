from abc import ABC, abstractmethod

class Subscriber(ABC):

    @abstractmethod
    def update(self, message):
        pass

class Publisher:
    def __init__(self):
        self._subscribers: list[Subscriber] = []  # This where references to all the observers are being kept
                                                  # This is a one-to-many relationship: one publisher can be
                                                  # followed by many subscribers

    def add_subscriber(self, subsrciber: Subscriber):
        # Add the observer to the list if it is not already there
        if subsrciber not in self._subscribers:
            self._subscribers.append(subsrciber)

    def remove_subscriber(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, message: str):
        # Trigger the update for all observers
        for subscriber in self._subscribers:
            subscriber.update(message)

# Observer implementation
class SubscriberImplementation(Subscriber):
    def __init__(self, subscriber_name: str):
        self.subscriber_name = subscriber_name

    def update(self, message: str):
        print(f"{self.subscriber_name}: {message}")

# Example usage
event_publisher = Publisher()

sub_a = SubscriberImplementation("Subscriber A")
sub_b = SubscriberImplementation("Subscriber B")

event_publisher.add_subscriber(sub_a)
event_publisher.add_subscriber(sub_b)

event_publisher.notify_subscribers("Event 1\n")

event_publisher.remove_subscriber(sub_a)

event_publisher.notify_subscribers("Event 2\n")

