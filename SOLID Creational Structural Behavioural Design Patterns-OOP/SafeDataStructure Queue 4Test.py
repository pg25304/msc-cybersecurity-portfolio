
import threading
from queue import Queue
from dataclasses import dataclass, field
from bank.exceptions import InvalidAmountError, InsufficientFundsError

@dataclass
class BankAccount:
    account_number: str
    _balance: float = 0.0
    _operations: Queue = field(default_factory=Queue, init=False)
    _worker_thread: threading.Thread = field(init=False)

    def __post_init__(self):
        # Start a worker thread to process queued operations
        self._worker_thread = threading.Thread(target=self._process_operations, daemon=True)
        self._worker_thread.start()

    def _process_operations(self):
        while True:
            func, args = self._operations.get()
            try:
                func(*args)
            finally:
                self._operations.task_done()

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError(f"Invalid Deposit amount: ${amount}")
        self._operations.put((self._deposit_internal, (amount,)))

    def _deposit_internal(self, amount: float):
        self._balance += amount

    def withdrew(self, amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError(f"Invalid Withdrawal amount: ${amount}")
        self._operations.put((self._withdraw_internal, (amount,)))

    def _withdraw_internal(self, amount: float):
        if amount > self._balance:
            raise InsufficientFundsError(f"Insufficient funds: Available ${self._balance}")
        self._balance -= amount

    def get_balance(self) -> float:
        # This is safe because only worker thread modifies balance
        return self._balance

    def transfer_to(self, target_account: "BankAccount", amount: float) -> None:
        if amount <= 0:
            raise InvalidAmountError(f"Invalid Transfer amount: ${amount}")
        self._operations.put((self._transfer_internal, (target_account, amount)))

    def _transfer_internal(self, target_account: "BankAccount", amount: float):
        if amount > self._balance:
            raise InsufficientFundsError(f"Insufficient funds: Available ${self._balance}")
        self._balance -= amount
        target_account.deposit(amount)  # Enqueue deposit in target account
