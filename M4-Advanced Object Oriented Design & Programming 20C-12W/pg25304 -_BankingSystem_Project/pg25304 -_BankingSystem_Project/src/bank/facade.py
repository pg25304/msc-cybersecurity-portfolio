"""
Facade Design Pattern in Banking System
This module shows that you know about the Facade Design Pattern in the banking system project.
The Facade pattern (Structural Design pattern) makes it easier for clients to work with multiple parts of a complex subsystem by giving them
a simple interface that doesn't require them to know how the parts work inside.

 Intended Use: A BankingSystemFacade class could wrap BankAccount, TransactionSimulator, and concurrency mechanisms
  and make simple methods like deposit(), withdraw(), and transfer() available.
 -  This makes the client code and subsystem classes less dependent on each other and follows
 the rules of structural design.

Reference:
Gamma, E., Helm, R., Johnson, R. and Vlissides, J., 1994.
Design Patterns: Elements of Reusable Object-Oriented Software.
Addison-Wesley.
"""

class BankingSystemFacade:
    """Skeleton class showing how a facade could unify subsystem access."""
    def __init__(self, account):
        self.account = account
        # In a full implementation, this could also manage TransactionSimulator, locks, etc.

    def deposit(self, amount):
        # Simplified call to underlying BankAccount
        return self.account.deposit(amount)

    def withdraw(self, amount):
        return self.account.withdraw(amount)

    def get_balance(self):
        return self.account.get_balance()