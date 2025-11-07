#The UserLoginManager class uses the Singleton pattern to ensure that there is
class UserLoginManager:
    #The class-level variable _instance is used to store the unique instance of the class.
    _instance = None
#The __new__ method checks whether an instance of the class has already been created. If not,
# it creates one and initializes user = None to represent no user being logged in.
    def __new__(cls):
        if cls._instance is None:
            print("Creating UserLoginManager instance")
            cls._instance = super(UserLoginManager, cls).__new__(cls)
            cls._instance.user = None
        return cls._instance
    #The login method allows a user to log in by setting the user attribute. If there’s already a user logged in,
    # it prevents a new login.
    def login(self, username ):
        if self.user is None:
            self.user = username
            print(f"User {self.user} logged in.")
        else:
            print(f"Already logged in as {self.user}, No new login allowed")
    #The logout method logs out the user and resets the user attribute to None.
    def logout(self):
        if self.user:
            print(f"user {self.user} logged out.")
            self.user = None
        else:
            print(f"No user is logged in.")
    #The get_current_user method returns the current logged-in user, or indicates that no user is logged in.
    def get_current_user(self):
        return self.user if self.user else "No user logged in."


#Test Singleton behaviour
#Creating two instances, When you create two instances (manager1 and manager2), both will refer
# to the same instance because of the Singleton pattern.
manager1 = UserLoginManager()
manager2 = UserLoginManager()
#Even though we try to log in with two different users (Alice and Bob), only the first login (Alice) will succeed.
# The second attempt will print a message saying the user is already logged in.
#log in with manager1
manager1.login("Alice")
#log in with manager2
manager2.login("Parisa")


# Checking the current logged-in user through both manager1 and manager2
print(f"Current user through mnager1: {manager1.get_current_user()}") #output should be Alice
print(f"Current user through mnager2: {manager2.get_current_user()}")#output should be Alice

#The test manager1 is manager2 will return True, confirming that both instances refer to the same object.
print(f"are both instance the same? {manager1 == manager2}")#output True

#loging out manager 1
manager1.logout()

#checking current user after logging out
print(f"current user after logout: {manager2.get_current_user()}")
