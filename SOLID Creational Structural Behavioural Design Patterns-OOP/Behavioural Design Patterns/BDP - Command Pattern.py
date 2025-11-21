from abc import ABC, abstractmethod
#Defines an abstract base class named Command using Python’s ABC module.
class Command(ABC):
    #Marks the following method as abstract—subclasses must implement it.
    @abstractmethod
    #Declares the interface method that commands will execute.
    def execute(self):
        #Placeholder; no implementation in the abstract base class.
        pass
#Creates a concrete command that turns a light on; it inherits from Command.
class LightOnCommand(Command):
    #Constructor that receives a Light object to act upon.
    def __init__(self, light):
        #Stores the Light instance for later use.
        self.light = light
        #Implements the required execute method for this command.
    def execute(self):
        #Calls the Light’s on method when the command executes.
        self.light.on()

#Concrete command class Light
#Defines a simple receiver class representing a light
class Light:
    #Method that turns the light on (simulated by printing).
    def on(self):
        print("The light is ON")

#client code
if __name__ == "__main__":
    #Creates a Light (receiver) instance.
    light =Light()
    #Wraps the action in a command object, linked to the Light.
    command = LightOnCommand(light)
    #Executes the command, which calls light.on() and prints “Light is ON”.
    command.execute()
    #command.light.on() #has same output
#Output:
#The light is ON