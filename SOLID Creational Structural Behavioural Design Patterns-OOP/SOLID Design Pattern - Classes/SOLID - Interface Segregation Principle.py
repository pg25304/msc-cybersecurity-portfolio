#The Interface Segregation Principle (ISP) in Python encourages designing small, focused interfaces so
#that classes only implement what they actually use. This avoids bloated, catch-all interfaces and keeps
# code clean and maintainable.

from abc import ABC, abstractmethod
class Printable:
    @abstractmethod
    def print_document(self):
        pass
class Scannable:
    @abstractmethod
    def scan_document(self):
        pass
# Classes that implement only the required interfaces
class Printer(Printable):
    def print_document(self):
        print("Printing document...")
#class Scanner(Scannable):
class Scanner(Scannable):
    def scan_document(self):
        print("Scanning document...")
class MultiFunctionPrinter(Scannable,Printable):
    def scan_document(self):
        print("Scanning document...")
    def print_document(self):
        print("Printing document...")



#User code/test
printer = Printer()
printer.print_document()

sscaner = Scanner()
sscaner.scan_document()

multiprinter = MultiFunctionPrinter()
multiprinter.print_document()
multiprinter.scan_document()

"""ISP Violation Example
class Machine(ABC):
    @abstractmethod
    def print_doc(self): pass
    @abstractmethod
    def scan_doc(self): pass

class OldPrinter(Machine):
    def print_doc(self): print("Print OK")
    def scan_doc(self): raise NotImplementedError("Cannot scan")"""



