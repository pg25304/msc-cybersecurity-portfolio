#logger program
#Defines a new class called `Logger`.
#This class will manage logging messages in a centralized way.
#This example beautifully demonstrates the Singleton pattern using a shared Logger class.

class Logger:
    _instance = None # class-level variable holds one and only instance of logger initially set to none
#object creation method, cls refer to class itself (logger)not instance
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
