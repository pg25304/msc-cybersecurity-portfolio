#This code demonstrates the Proxy Pattern, a structural design pattern that provides a surrogate or placeholder
# for another object to control access to it.
#Defines the real subject - the actual object that performs expensive operations
#__init__: Constructor that stores the filename and immediately loads the image from disk (expensive operation)
#self.filename: Instance variable storing the image filename
#self.load_image_from_disk(): Immediately invokes the expensive loading operation
class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()

#Simulates expensive I/O operation (resource-intensive)
#This is what the proxy delays until actually needed
#Resource-expensive behavior → reason to use Proxy
    def load_image_from_disk(self):
        print(f"Loading image from disk: {self.filename}")

#The actual display method that the proxy delegates to
#Simple interface method — the Proxy will call this later.
    def display(self):
        print(f"Displaying image: {self.filename}")

#Defines the proxy class that controls access to the RealImage
#Proxy subject - lightweight placeholder with the same interface as RealImage
#Stores filename but self.real_image = None - doesn't create the real object yet
#Concept: Lazy Initialization - defer expensive operations
class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

#Control Access: Checks if real object exists
#Lazy Loading: Only creates RealImage on first display() call
#Delegation: Forwards the display call to the real object
#Subsequent calls reuse the cached object
    def display(self):
        if self.real_image is None:
            #Create the actual RealImage only on first display call.
            self.real_image = RealImage(self.filename)
        #Delegate the display call to the real image
        self.real_image.display()

#Ensures code runs only when script is executed directly (not when imported)
if __name__ == "__main__":
    #Creates proxy instance - no disk loading yet
    proxy_image = ProxyImage("test_image.jpg")

    #Image is not loaded from disk yet
    #First display() call: Proxy creates RealImage, triggering disk load, then displays
    print("Image created. Now displaying the image:")
    proxy_image.display()  # Image is loaded from disk and displayed
    print("Displaying the image again:")
    #Second display() call: Reuses cached RealImage, skips reload (efficiency gain)
    proxy_image.display()  # Image is displayed without loading from disk again


    #Key Concepts Applied
#Lazy Initialization: Defer expensive operations
#Caching: Avoid redundant operations
#Delegation: Proxy forwards requests to real object
#Controlled Access: Proxy manages when operations occur

#Specific Purposes:
#Lazy Loading: The proxy doesn('t create the RealImage object immediately. It only creates it when display() '
#is called for the first time. This saves resources if the image is never displayed.)
#Caching: Once the RealImage is created and loaded from disk, the proxy stores it (self.real_image).
# Subsequent calls to display() reuse the cached object instead of reloading from disk.
#Controlled Access: The proxy controls when the expensive load_image_from_disk() operation occurs,
# protecting the application from unnecessary I/O operations.
#Same Interface: The proxy has the same display() method as RealImage, so the client code treats
# them identically—the client doesn't need to know whether it's using the real object or the proxy.