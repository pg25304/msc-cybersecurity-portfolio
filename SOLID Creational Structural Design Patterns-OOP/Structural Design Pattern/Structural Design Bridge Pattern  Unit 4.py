#Bridge Pattern program based on structural design
#abstract Device class
from abc import ABC, abstractmethod
#Abstract interface for controlling devices
#Stores a reference to a Device (the bridge link)
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
    
#concrete device classes
class TV(Device):
   def turn_on(self):
       print("TV is on")
   def turn_off(self):
       print("TV is off")

class Radio(Device):
    def turn_on(self):
        print("Radio is on")
    def turn_off(self):
        print("Radio is off")


#abstract RemoteControl class
#Abstract interface for controlling devices
#Stores a reference to a Device (the bridge link)
class RemoteControl(ABC):
    def __init__(self, device: Device):
        self.device = device
    @abstractmethod
    def on(self):
        pass
    @abstractmethod
    def off(self):
        pass
#concrete RemoteControl classes
#The RemoteControl holds a reference to Device and delegates calls to it. This is the bridge
# that connects the two hierarchies.
class BasicRemoteControl(RemoteControl):
    def on(self):
        self.device.turn_on()
    def off(self):
        self.device.turn_off()

class AdvancedRemoteControl(RemoteControl):
    def on(self):
        print("Advanced Remote turn device on")
        self.device.turn_on()
    def off(self):
        print("Advanced Remote turn device off")
        self.device.turn_off()


#client code/test
"""When code is inside a block that starts with if __name__ == "__main__":,
 it will only be executed if the file is being run directly, not if it's imported as a module."""
if __name__ == "__main__":

    #Creating device instances TV and Radio classes and assigning remote controls
    tv = TV()
    radio = Radio()
    remote1 = BasicRemoteControl(tv)
    remote2 = AdvancedRemoteControl(radio)
    #Using remote controls to operate devices
    tv.turn_on()
    tv.turn_off()
    radio.turn_on()
    radio.turn_off()

"""🔹 Bridge Pattern Solution
The Bridge Pattern solves this by:
- Separating abstraction (RemoteControl) from implementation (Device)
- Allowing remotes to control any device via a shared interface
- Enabling independent extension of remotes and devices
"""
""" How It Solves the Problem
- Decoupling: RemoteControl doesn’t care what kind of device it controls — it just calls turn_on() and turn_off().
- Flexibility: You can add new remotes (e.g., VoiceRemoteControl) or new devices (e.g., SmartSpeaker) without modifying
 existing classes.
- Scalability: You avoid multiplying classes for every remote-device combination.
"""