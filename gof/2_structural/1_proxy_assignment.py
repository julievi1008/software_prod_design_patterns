# Assignment 1) Create class UserDatabase
#   It should have three methods:
#       add_user(self, user_id : int, username : str): Make it just print that user was added.
#       remove_user(self, user_id : int, username : str): Make it just print that user was removed.
#       get_user(self, user_id : int, username : str): Make it just print that user was fetched.
# WRITE YOUR ANSWER BELOW
class UserDatabase:
    def add_user(self, user_id : int, username : str):
        print('User was added.')
    def remove_user(self, user_id : int, username : str):
        print('User was removed.')
    def get_user(self, user_id : int, username : str):
        print('User was fetched.')



# Assignment 2) Create class AdminUser
#   It should have three methods:
#       __init__(self, user_database : UserDatabase): Store the passed user_database into a member variable.
#       add_user(self, user_id : int, username : str): Call the add_user method of the stored member variable.
#       remove_user(self, user_id : int): Call the remove_user method of the stored member variable.
#       get_user(self, user_id : int): Call the get_user method of the stored member variable.
# WRITE YOUR ANSWER BELOW
class AdminUser:
    def __init__(self, user_database : UserDatabase):
        self.db = user_database

    def add_user(self, user_id: int, username: str):
        self.db.add_user(user_id, username)

    def remove_user(self, user_id: int, username: str):
        self.db.remove_user(user_id, username)

    def get_user(self, user_id: int, username: str):
        self.db.get_user(user_id, username)
    

# Assignment 3) Create class NormalUser
#   It should have three methods:
#       __init__(self, user_database : UserDatabase): Store the passed user_database into a member variable.
#       add_user(self, user_id : int, username : str): raise PermissionError("") with a message stating that normal user cannot add other users.
#       remove_user(self, user_id : int): raise PermissionError("") with a message stating that normal user cannot remove other users.
#       get_user(self, user_id : int): Call the get_user method of the stored member variable.
# WRITE YOUR ANSWER BELOW
class NormalUser:
    def __init__(self, user_database : UserDatabase):
        self.db = user_database
    def add_user(self, user_id: int, username: str):
        raise PermissionError('you are not allowed to add another user')
    def remove_user(self, user_id: int, username: str):
        raise PermissionError('you are not allowed to remove another user')
    def get_user(self, user_id: int, username: str):
        self.db.get_user(user_id, username)

# Assignment 4) Usage
#   Create new instance of the class UserDatabase()
#   Create one instance of AdminUser and NormalUser, passing the created user database variable to both constructors
#   Try to add a user through the admin instance (should be OK)
#   Try to add a normal user through the normal user instance (should be OK) # do you mean get a user?
#   Try to add a a user through the normal user instance (should raise a PermissionError)
# WRITE YOUR ANSWER BELOW
user_db = UserDatabase()
admin = AdminUser(user_db)
norm_user = NormalUser(user_db)
admin.add_user(1,'Vi')
norm_user.get_user(1,'Vi')
norm_user.add_user(1, 'Vi')
