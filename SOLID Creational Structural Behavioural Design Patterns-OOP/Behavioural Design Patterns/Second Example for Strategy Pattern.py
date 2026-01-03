#Import abstract base class and method decorator
from abc import abstractmethod, ABC

# Define the Strategy interface/abstract
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass
 # Concrete strategy
class BookDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.9  # 10% discount for books

class ElectronicsDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.8  # 20% discount for electronics

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price  # No discount

#Item class using the strategy pattern
class Product:
    # Constructor to initialize price and discount strategy
    def __init__(self, price: float, discount_strategy: DiscountStrategy):
        self.price = price
        self.discount_strategy = discount_strategy
     # Method to calculate final price using the strategy
    def final_price(self):
        # Use the strategy to calculate the final price
        return self.discount_strategy.apply_discount(self.price)
    # Static method to calculate total price of a list of items

    def calculate_total_price(product_list: list) -> float:
        total = 0
        for item in product_list:
            total += item.final_price()
        return total
# Example usage
product_list =[
    Product(100, BookDiscount()),
    Product(200, ElectronicsDiscount()),
    Product(50, NoDiscount())
]

print(Product.calculate_total_price(product_list)) # Output: 300.0