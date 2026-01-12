#src/bank/account.py - pg25304
#import custom exceptions for error handling
from bank.exceptions import InvalidAmountError, InsufficientFundsError
#for thread-safe operations(locks)
import threading
#by auto‑generating __init__,__repr__,__eq__, make class easier to maintain
from dataclasses import dataclass, field
@dataclass
class BankAccount:
    account_number: str
    _balance: float = 0.0
    # default_factory creates a new lock for each account; init=False: don't include _lock in __init__ method
    _lock: threading.Lock = field(default_factory=threading.Lock, init=False)

    def deposit(self, amount: float) -> None:
        # Add a positive amount into the account in a thread-safe way.only one thread can change balance at a time.
        with self._lock:
            if amount <= 0:
                raise InvalidAmountError(f"Invalid Deposit amount: ${amount} ")
            self._balance += amount

    #withdrawl positive amount, handling errors
    def withdraw(self, amount: float) -> None:
        with self._lock:
            if amount <= 0:
                raise InvalidAmountError(f"Invalid Withdrawal amount: ${amount}")

            if amount > self._balance:
                raise InsufficientFundsError(f"Insufficient funds: Available ${self._balance} in your balance.")
            self._balance -= amount

    # Returns the current balance in a thread-safe way.
    def get_balance(self) -> float:
        with self._lock:
            return self._balance

    # Transfer amount from this account to target_account in a thread-safe way.
    def transfer_to(self, target_account: "BankAccount", amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError(f"Invalid Transfer amount: ${amount}")
        #Lock both accounts in consistent order to prevent deadlocks and ensure thread safety.id = memory address
        first_lock, second_lock = (self._lock, target_account._lock) if id(self) < id(target_account) else (target_account._lock, self._lock)
        with first_lock:
            with second_lock:
                if amount > self._balance:
                    raise InsufficientFundsError(f"Insufficient funds: Available ${self._balance} in your balance.")
                self._balance -= amount
                target_account._balance += amount






