#Key creational Design Pattern
# #Singelton Pattern:ensuring a class has only one instance
#usage: managing shared resources like database, logging, or configuration setting.
#It gives everyone one shared object, through a central access point, without letting them create duplicates — even by accident.

"""class Singleton:
    # This is a class-level variable that will store the one and only
    # instance of Singleton.Right now, it’s empty (None)
    _instance = None
    #- __new__ is a special method in Python that controls object creation
    # (before __init__ runs). cls refers to class itself = singleton
    def __new__(cls):
        # - Checks if an instance has already been created.
        if cls._instance is None:
            #- Calls the parent class’s __new__ method to actually create the object.
            cls._instance = super(Singleton, cls).__new__(cls)
            # - Returns the existing instance/previously stored
        return cls._instance

#client code
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)"""






