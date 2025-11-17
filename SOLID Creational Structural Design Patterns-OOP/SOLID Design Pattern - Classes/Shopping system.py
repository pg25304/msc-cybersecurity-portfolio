#class order; - initializing items as an empty list because the cart starts empty.
# Order class: Manages cart items and calculates total price
class Order:
    def __init__(self):
        #Attribute (self.items):A list that belongs to the Order object — it stores all the products added to the cart
        self.items = []
    #Add a product to the cart, item is a single product
    def add_item(self, item):
        self.items.append(item)
    #sum up price for all items in the cart
    def calculate_total(self):
        return sum(item.price for item in self.items)
#Product class: Represents an item with name and price
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


#ABC means any inherited subclass must implement these methods-or you cannot use it
#OCP-open close principle-a new crypto payment can be added without modifying the original code
#LSP-Liscov subsitution principal- Any subclass of PaymentMethod can be used interchangeably
# without breaking the system.

from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod #marks pay() must be implemented by sub classes
    def pay(self, amount):
    #a signal to developers:
    #This method is meant to be overridden in a subclass. If you try to use it directly,
    #it will crash."""
        raise NotImplementedError
#sub classes OCP - - Each subclass implements the pay method differently
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"processing credit card payment of ${amount}")

class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"processing cash payment of ${amount}")

#this payment method has implemented after the completion and test of the code to illustrate OCP
class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Processing crypto payment of ${amount}")
#PaymentProcessor Use the Abstraction, accepting any object that implement PaymentMethod
class PaymentProcessor():
    def proces_payment(self, payment_method: PaymentMethod, amount):
        payment_method.pay(amount)

#Example of class order usage
order =Order()
order.add_item(Product("Book", 20))
order.add_item(Product("Pen", 5))
total = order.calculate_total()
print(f"Total: ${total}")



#Test
processor = PaymentProcessor()
processor.proces_payment(CreditCardPayment(),50)
processor.proces_payment(CashPayment(), 100)


#SRP: Order class only manage items and totals
#OCP: a payment method like CryptoPayment can be easily implemented without modifying current codes
#LSP: all payment method could use interchangeably
#ISP: PaymentMethod interface is clean and focused
#DIP: PaymentProcessor depends on PaymentMethod, not concrete classes