#Defines an abstract base class named Handler.
#This class represents a generic “handler” in a chain.
from abc import ABC, abstractmethod
class Handler(ABC):
    #The constructor takes an optional successor, which is the next handler in the chain.
    def __init__(self, successor = None):
        #self._successor stores that next handler
        # If no successor is provided, this handler is the end of the chain
        self._successor = successor
#This is the default behavior of a handler.
    def handle(self, request):
        #If there is a successor, it passes the request to that next handler.
        if self._successor:
            return self._successor.handle(request)
        #If there is no successor, it means the request was not handled by any handler in the chain.
        return None
#Concrete handler 1
class ConcreteHandler1(Handler):
    #Overrides the handle method to provide specific handling logic.
    def handle(self, request):
#If the request equals "Request1", this handler takes responsibility and returns a response.
        if request == "Request1":
            return print("ConcreteHandler1 handled the request {request}.")
# If it cannot handle the request, it calls the base class version of handle,
# which automatically passes the request to the next handler in the chain.
        else:
            return super().handle(request)
#Concrete handler 2
class ConcreteHandler2(Handler):
    #Another handler in the chain.
    def handle(self, request):
        if request == "Request2":
            #Handles "Request2" only.
            return (f"ConcreteHandler2 handled the request {request}.")
        else:
            #Otherwise passes the request down the chain.
            return super().handle(request)

#Example usage
if __name__ == "__main__":
    #Creates a chain of handlers:if handler1 cannot handle it send to second one
    #if second one cannot handle it return none
#ConcreteHandler1 → ConcreteHandler2
    handler_chain = ConcreteHandler1(ConcreteHandler2())
    print(handler_chain.handle("Request1"))  # Output: ConcreteHandler1 handled the request Request1.
    print(handler_chain.handle("Request2"))  # Output: ConcreteHandler2 handled the request

#Starts with ConcreteHandler1.
#Handler1 can handle “Request1”, so it returns:
#"ConcreteHandler1 handled Request1"

#ConcreteHandler1 receives "Request2" → cannot handle → passes to successor.
#ConcreteHandler2 receives "Request2" → handles it → returns:
#"ConcreteHandler2 handled Request2"










