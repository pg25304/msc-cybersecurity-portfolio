from abc import ABC, abstractmethod
# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
# Concrete Strategies : Credit Card strategy
class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using credit card"
# Concrete Strategies : PayPal strategy
class PayPalStrategy(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal"
# Context
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy
    def process_payment(self, amount):
        return self.strategy.pay(amount)
# Example usage
if __name__ == "__main__":
    #Using Credit Card Strategy
    payment_processor =PaymentProcessor(CreditCardStrategy())
    print(payment_processor.process_payment(100))  # Output: Paid $100 using credit card
    #Switching to PayPal Strategy
    payment_processor.set_strategy(PayPalStrategy())
    print(payment_processor.process_payment(200))  # Output: Paid $200 using PayPal