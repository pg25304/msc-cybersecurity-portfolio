
#•	Subject Interface: Defines the Subject interface with methods to attach, and notify observers.
#Subject class represents the Subject in the Observer pattern, which is observed by one or more Observer objects.
class Subject:
# Initializes the Subject object and creates an empty list _observers to store references to attached observers.
    def __init__(self):
        self._observers = []
# Attaches an observer to the Subject by adding it to the _observers list.
#attach()is a method to register an observer.
    def attach(self, observer):
        self._observers.append(observer)
#notify()is a method to tell every registered observer that something changed.
# Notifies all attached observers - # The notify() method loops through all registered observers and calls
# their update() method, notifying them of any state changes in the Subject.
    def notify(self):
#iterates over every observer in the list.
        for observer in self._observers:
#calls the observer’s update method, passing the subject itself (self) so observers can inspect state if needed.
#This is a push-pull hybrid: the subject “pushes” itself as a reference and observers can “pull” data from it.
#This self parameter is the actual Subject object created in user code (called subject)
            observer.update(self)

# Observer Interface: Defines the Observer interface with an update method.
## Observer class - This is an abstract class that represents the base class for all Observer objects.
# The update() method is defined as a placeholder in the abstract Observer class.
# Actual behaviour will be implemented by concrete subclasses.
#class Observer: defines a base class that describes the interface observers should implement.
class Observer:
#update() is a method signature — concrete observer classes should override this to react to notifications.
    def update(self, subject):
#means “do nothing” here; it's a placeholder.
        pass
#ConcreteObserver is an actual implementation of Observer.
class ConcreteObserver(Observer):
#Its update() method prints a message when notified. In a real app you’d
# replace print with whatever reaction is required (update UI, log, recalc, etc).
    def update(self, subject):
        print("Observer notified of subject state change.")

# Example usage
#ensures the following block runs when the file is executed directly, not when it's imported as a module.
if __name__ == "__main__":
    #creates a Subject instance.
    subject= Subject()
    #creates an observer.
    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()
    #registers observer1 and 2 with the subject.
    subject.attach(observer1)
    subject.attach(observer2)
    # Simulate a state change in the subject
    #calls notify so every attached observer (only observer1 here) gets its update() called.
    # If both were attached, you'd see two prints.
    subject.notify()  # Output: Observer notified of subject state change. (twice)
