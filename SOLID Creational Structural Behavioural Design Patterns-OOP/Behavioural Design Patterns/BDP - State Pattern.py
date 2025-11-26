#- Defines an abstract base class called State. It serves as a blueprint for all concrete states.
from abc import ABC, abstractmethod
class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

#- Defines a concrete state class that inherits from State

class ConcreteStateA(State):
    #Implements the required method for this state.
    def handle(self):
        #Prints a message showing that State A is being handled.
        print("Handling request in ConcreteStateA")

#- Defines another concrete state class that inherits from State
class ConcreteStateB(State):
    def handle(self):
        print("Handling request in ConcreteStateB")

#- Defines the Context class, which maintains a reference to a State object. This is the object
# whose behavior changes depending on its current state.

class Context:
    #Constructor that initializes the context with a given state.
    def __init__(self, state: State):
        #Stores the current state inside the context.
        self.state = state
    #Method to change the current state of the context.
    def set_state(self, state: State):
        #Updates the stored state reference.
        self.state = state
    #Method that delegates work to the current state.
    def request(self):
        #- Calls the handle method of whichever state is currently set.
        self.state.handle()

#Client code demonstrating the State pattern in action.
if __name__ == "__main__":
    #- Creates a Context object with its initial state set to ConcreteStateA.
    context = Context(ConcreteStateA())
    #- Calls request(), which delegates to ConcreteStateA.handle(). Prints “Handling State A”.
    context.request()  # Output: Handling request in ConcreteStateA
    #Changes the state of the context to ConcreteStateB.
    context.set_state(ConcreteStateB())
    #Calls the request method again, now delegating to ConcreteStateB's handle method.
    context.request()  # Output: Handling request in ConcreteStateB
