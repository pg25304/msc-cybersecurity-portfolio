#Defines an interface/base class for US power outlets
#output_voltage() is a placeholder method (no implementation)
class UsPowerOutlet:
    def output_voltage(self):
        pass

#European interface incompatible with US
#Represents a European power outlet
#supply_voltage() returns 230V (European standard voltage)
class EuropeanPowerOutlet:
    def supply_voltage(self):
        return 230  # Voltage in Volts
#Inherits from UsPowerOutlet (so it acts like a US outlet)
#__init__(): Stores a reference to a European socket
#european_outlet is a parameter, not a reference yet.
#european_outlet is a formal parameter — it's a placeholder that will receive the actual European
# socket object when the class is instantiated.
#The actual reference is created when you call the class:
#european_socket = EuropeanPowerOutlet()  # Create the actual socket
#adapter = EuroToUsAdapter(european_socket)  # Pass it as
#output_voltage(): Converts European voltage (230V) to US voltage (115V) by dividing by 2
#This is the Adapter Pattern — it makes incompatible interfaces compatible
class EuroToUsAdapter(UsPowerOutlet):
    def __init__(self, european_outlet):
        self.european_outlet = european_outlet
#The EuroToUsAdapter uses composition:
#It contains a reference to a EuropeanPowerOutlet object via self.european_outlet
#It doesn't inherit from EuropeanPowerOutlet — instead, it stores an instance of it
#When output_voltage() is called, it delegates to self.european_outlet.supply_voltage()

    def output_voltage(self):
        euro_voltage = self.european_outlet.supply_voltage()
        us_voltage = euro_voltage/2  # Simple conversion for illustration
        return us_voltage
#Represents a US electrical device (like a laptop)
#__init__(): Stores the device name
#plug_in(): Accepts a US power outlet and checks if voltage is between 110-120V
#If voltage is in range, device operates normally
#If not, device cannot operate"""

class USDevice:
    def __init__(self, name):
        self.name = name

    def plug_in(self,  us_power_outlet):
        voltage = us_power_outlet.output_voltage()
        if 110<=voltage<=120:
            return f"{self.name} is operating at {voltage}V"
        else:
            return f"{self.name} cannot operate at {voltage}V"

#Creates a European socket (230V)
#Creates an adapter that converts European voltage to US voltage
#Creates a US device (laptop)
#Plugs the device into the adapter
#The adapter converts 230V to 115V, so the laptop operates successfully
#Prints: Laptop is operating at 115.0V

if __name__ == "__main__":
    #Creates a European socket (230V)
    european_socket = EuropeanPowerOutlet()
    #Adapts it to US standard (110V)
    adapter = EuroToUsAdapter(european_socket)
    #When EuroToUsAdapter(european_socket) is called:
    #european_outlet parameter receives the european_socket object
    #self.european_outlet = european_outlet stores that reference as an instance variable
    #Later, output_voltage() uses self.european_outlet.supply_voltage() to access the European socket's method

    us_device = USDevice("Laptop")
    result = us_device.plug_in(adapter)
    print(result)  # Output: Laptop is operating at 115.0V

#So the flow is:
#Parameter european_outlet receives the object
#self.european_outlet stores the persistent reference
#Methods can now access the European socket through self.european_outlet