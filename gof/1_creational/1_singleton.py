'''The singleton pattern limits the instantiation of the class to only one instance.

Thus, in the example Settings class implementation below,
there can only be one Settings class sharing the same member variable information in the whole system.

Examples:
    - App settings
    - Logging errors & information
    - Database
    - Caching
'''

# https://batnamv.medium.com/design-pattern-li%E1%BB%87u-b%E1%BA%A1n-c%C3%B3-th%E1%BB%B1c-s%E1%BB%B1-hi%E1%BB%83u-v%E1%BB%81-singleton-pattern-a88aede760f6
# https://dev.to/mustafaelghrib/how-to-implement-a-logging-system-with-the-singleton-pattern-using-python-5b32 
# https://github.com/priyankmishraa/linkedin-posts/blob/main/logging-singleton/main.py 
class Setting():
    """Setting class without singleton pattern"""
    def __init__(self):
        """Typical __init__.

        Initializes the class with some values. In this case it's an empty dict.
        """
        self.values = {}

    def set_setting(self, key, value):
        """Basic setter for values variable."""
        self.values[key] = value

    def get_setting(self, key):
        """Basic getter for values variable."""
        return self.values[key]


class SingletonSetting():
    """Setting class with singleton


    Attributes:
        _instance: Holds the only instance of this class that is available for your 
                    program.
    """
    _instance = None

    def __new__(cls):
        """This is the magic of this pattern. 
        
        Check if _instance exists, if it doesn't then create it. Then return the 
        _instance.
        """
        if not cls._instance:
            cls._instance = super(SingletonSetting, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize member variables for the class.

        Checks if the values already exist, so we don't delete values in case the 
        _instance already exists and has some values.
        """
        if not hasattr(self, "values"):
            self.values = {}

    def set_setting(self, key, value):
        """Basic setter for values variable."""
        self.values[key] = value

    def get_setting(self, key):
        """Basic getter for values variable."""
        return self.values[key]

###
# Usage
###
if __name__ == "__main__":
    # With Setting class, which is NOT a singleton.
    setting1 = Setting()
    setting1.set_setting("example", "value")

    setting2 = Setting()
    setting2.set_setting("example", "Totally another value")

    print("setting1.values['example']: " + setting1.get_setting("example"))
    print("setting2.values['example']: " + setting2.get_setting("example"))
    print(f'setting1 without singleton: {id(setting1)}')
    print(f'setting2 without singleton: {id(setting2)}')
    print(setting1 is setting2)

    print()

    # With SingletonSetting
    singleton1 = SingletonSetting()
    singleton1.set_setting("example", "value")

    singleton2 = SingletonSetting()
    singleton2.set_setting("example", "Totally another value")

    print("singleton1.values['example']: " + singleton1.get_setting("example"))
    print("singleton2.values['example']: " + singleton2.get_setting("example"))
    print(f'setting1 with singleton: {id(singleton1)}')
    print(f'setting2 with singleton: {id(singleton2)}')
    print(singleton1 is singleton2)

