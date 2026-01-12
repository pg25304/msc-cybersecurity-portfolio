# src/bank/transaction_simulator.py - pg25304
#Developed for Uni assignment -Pg25304
import threading
from typing import List, Tuple
from bank.account import BankAccount

#Simulator for transaction concurrently by multiple users.
class TransactionSimulator:

    # Initialize a BankAccount store in self.account
    def __init__(self, account: BankAccount):
        self.account = account

    #multiple users concurrent depositing money
    def run_concurrent_deposits(self, deposit_amount: float, num_users: int) -> None:

        threads: List[threading.Thread] = []
        for _ in range(num_users):
            t = threading.Thread(target=self.account.deposit, args=(deposit_amount,))
            threads.append(t)
            #deposit happens concurrently
            t.start()
        for t in threads:
            #wait for all threads to complete
            t.join()

    # half threads deposit, half withdraw concurrently
    def run_mixed_operations(self, deposit_amount: float, withdraw_amount: float, num_pairs: int) -> None:
        threads: List[threading.Thread] = []
        for _ in range(num_pairs):
            threads.append(threading.Thread(target=self.account.deposit, args=(deposit_amount,)))
            threads.append(threading.Thread(target=self.account.withdraw, args=(withdraw_amount,)))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    # static method to run bidirectional transfers,independent of self
    @staticmethod
    def run_bidirectional_transfers(a: BankAccount, b: BankAccount, amount: float, num_each_direction: int) -> None:
        threads: List[threading.Thread] = []
        for _ in range(num_each_direction):
            threads.append(threading.Thread(target=a.transfer_to, args=(b, amount)))
            threads.append(threading.Thread(target=b.transfer_to, args=(a, amount)))
        for t in threads:
            t.start()
        for t in threads:
            t.join()


