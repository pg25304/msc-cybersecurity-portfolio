"""from decimal import Decimal
tax_rate = Decimal('7.25')/Decimal(100)
print(tax_rate)"""
class Bird:
    def fly(self):
        pass
class Sparrow(Bird):
    pass
def let_bird_fly(bird: Bird):
    print(bird.fly())
let_bird_fly(Sparrow())
