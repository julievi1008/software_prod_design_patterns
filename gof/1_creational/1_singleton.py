'''
The singleton pattern limits the instantiation of the class to only one instance.

Thus, in the example Settings class implementation below,
there can only be one Settings class sharing the same member variable information in the whole system.

Examples:
    - App settings
    - Logging errors & information
    - Database
    - Caching
'''

class Settings:
    _instance = None

    def __new__(cls):
        # If no instance is found, create it
        if not cls._instance:
            cls._instance = super(Settings, cls).__new__(cls)
        # Otherwise return the existing instance
        return cls._instance

    def __init__(self):
        # Initialize member variables only once
        if not hasattr(self, 'values'):
            self.values : dict = {}

    def set(self, key, value):
        self.values[key] = value
        return self
    
    def get(self, key):
        return self.values.get(key)
    
    def save(self):
        pass

###
# Usage
###
settings1 = Settings()
settings1.set("app_name", "Test app")
settings2 = Settings()

print(settings1.get("app_name"))
print(settings2.get("app_name"))