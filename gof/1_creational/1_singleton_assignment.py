from enum import Enum, auto

class Status(Enum):
    stopped = auto()
    playing = auto()
    paused = auto()

# Assignment 1)
    # Create singleton class AudioPlayer with a member variable `_instance` which is set to None. 
    # Define a `__new__(cls)` method which checks if the class already has `_instance` set.
    # If it is not set, create the `_instance` and also initialize member variables `track` and `status` for the `_instance`. 
    #   `track` should be an empty string.
    #   `status` should have the value stopped from the above enum `Status`
    # Lastly the method should return the `_instance`
    # In this case the class does not need an `__init__` method.
    
# Assignment 2)
    # Create methods `play(self, track: str)`, `stop(self)`, and `pause(self)`.
    # The play method should:
    #   - set the member variable `track` to what is passed as an argument in the method call, 
    #   - set member variable `status` to the appropriate value from the `Status` enum,
    #   - and print "Playing {track}".
    # The stop method should: 
    #   - check if `track` is set, 
    #   - if it is set then it 
    #       - sets `track` to an empty string, 
    #       - sets `status` to the appropriate value from the `Status` enum,
    #       - prints "Stopped {track}".
    #   - If there is no `track` set then the method prints "No track is playing"
    # The pause method should:
    #   - check if `track` is set and `status` is `Status.playing`
    #   - if they are then set status to the appropriate `Status` and print "Paused {track}"
    #   - else just print "No track is playing"

# For assignments 1 and 2
# YOUR ANSWER GOES BELOW
class AudioPlayer:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(AudioPlayer, cls).__new__(cls)
            cls._instance.track = ''
            cls._instance.status = Status.stopped
        return cls._instance
    
    def play(self, track: str) ->None:
        self.track = track
        self.status = Status.playing
        print(f'Playing {self.track}')

    def stop(self) -> None:
        if self.track:
            print(f'Stopped {self.track}')
            self.track = ''
            self.status = Status.stopped
        elif not self.track:
            print("No track is playing")

    def pause(self) -> None:
        if self.track and self.status == Status.playing:
            self.status == Status.paused
            print(f'Paused {self.track}')
        else:
            print("No track is playing")


# Assignment 3)
# Demonstrate the usage of the AudioPlayer class and prove it is a singleton.
# Create two instances of the AudioPlayer. Start playing a track with player 1 and stop it with player 2.
# Pause the player 1 to see if it pauses or not.

# YOUR ANSWER GOES BELOW

player1 = AudioPlayer()
player1.play('STAY')

player2 = AudioPlayer()
player2.stop()

player1.pause()

print(player1 == player2) # -> True: There's only 1 instance regardless of how many players we create