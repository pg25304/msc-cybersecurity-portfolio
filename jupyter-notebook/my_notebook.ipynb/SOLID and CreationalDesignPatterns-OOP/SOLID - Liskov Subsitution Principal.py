"""The Liskov Substitution Principle (LSP) in Python means that subclasses should be able
 to replace their parent classes without breaking the program. If a class Child inherits
 from Parent, then anywhere you use Parent, you should be able to use Child without unexpected behavior.
"""
class Bird:
    def fly(self):
        return "Flying high"
class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying high"

    def let_it_fly(bird: Bird):
        bird.fly()
#Demonstrate Liskov Substitution Principle
if __name__ == "__main__":
    bird = Bird()
    sparrow = Sparrow()
    #Using the base class Bird
    print(bird.fly()) # Output: Flying high
    #Using the subclass Sparrow in place of Bird
    print(sparrow.fly())# Output: Sparrow flying high

#let_it_fly(bird)      # Works fine
#let_it_fly(sparrow)   # Works fine