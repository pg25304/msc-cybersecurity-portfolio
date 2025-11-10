#logger program
#Defines a new class called `Logger`.
#This class will manage logging messages in a centralized way.
#This example beautifully demonstrates the Singleton pattern using a shared Logger class.

class Logger:
    _instance = None # class-level variable holds one and only instance of logger initially set to none

    def __new__(cls):
        # This is like checking if the logbook already exists before printing a new one.
        if cls._instance is None:
            print("Creating the Logger instance")
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logs = []  # Initialize shared log list
        return cls._instance

    def log(self, message):
        self.logs.append(message)

    def show_logs(self):
        for entry in self.logs:
            print(entry)

# Test the Singleton behavior
logger1 = Logger()
logger2 = Logger()

logger1.log("System started")
logger2.log("User logged in")

print("Are both loggers the same?", logger1 is logger2)  # ✅ True
logger1.show_logs()  # Shows both messages
""""Why is this Important for Singleton?

The main reason this line exists is to make sure the object creation is done properly and to ensure that only one 
instance of Logger is created, even though Logger is responsible for enforcing the Singleton pattern.

If cls._instance is None, then the code creates a new instance by calling super(Logger, cls).__new__(cls) to actually
 create the object.

After the object is created, it gets assigned to cls._instance, and subsequent calls to Logger() will return the same
 instance (the one stored in cls._instance), enforcing the Singleton behavior. ""#object creation method, cls (conventionally used name for the class itself) refer to class itself (logger)not ins
    # cls = a placeholder that represents the class rather than an instance of the class.
    cls in Context:
When you define a method that works at the class level (like __new__), the first argument is typically a reference 
to the class itself, not an instance. This is different from regular instance methods, where the first argument is
 typically self, which refers to the instance (the actual object created from the class). cls is the class itself,
  in this case, the Logger class. So when __new__ is called, cls will refer to the Logger class, not an object created
   from the class"""

