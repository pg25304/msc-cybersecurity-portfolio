## src/bank/test_account.py -pg25304
from bank.account import BankAccount
from bank.exceptions import InvalidAmountError, InsufficientFundsError
## Import the TransactionSimulator class which encapsulates concurrency logic
from bank.transaction_simulator import TransactionSimulator
import threading

#Functional Test
def main():
    account = BankAccount("987654321")
    #Test deposit - Python tries code in 'try' block if exception occurs (an error), it jumps to except block
    try:
        print(f"Depositing $100.00")
        account.deposit(100.00)
        print(f"New Balance: ${account.get_balance():.2f}")
    except InvalidAmountError as exception:
        print(f"Deposit is failed: {exception}")

    #Test Withdrawal Functionality
    try:
        print(f"Withdrawing $50.00")
        account.withdraw(50.00)
        print(f"New Balance: ${account.get_balance():.2f}")
    except (InvalidAmountError, InsufficientFundsError) as exception:
        print(f"Withdrawal is failed: {exception}")

    #Test Insufficient withdrawal
    try:
        print("trying withdrawing $1000.00")
        account.withdraw(1000.00)
    except (InvalidAmountError, InsufficientFundsError) as exception:
        print(f"Withdrawal failed: {exception}")

    #Test Invalid withdrawal
    try:
        print("trying withdrawing $-20.00")
        account.withdraw(-20.00)
    except (InvalidAmountError, InsufficientFundsError) as exception:
        print(f"Withdrawal failed: {exception}")
    return account

# Concurrency test: multiple users deposit concurrently
def concurrency_test(account):
    sim = TransactionSimulator(account)
    sim.run_concurrent_deposits(deposit_amount=10, num_users=10)
    print(f"\n---Concurrency Test Completed---")
    print(f"Expected balance: $150.00")
    print(f"Final Balance after concurrent deposits: ${account.get_balance():.2f}")
# Mixed concurrency test: simultaneous deposits and withdrawals
def mixed_concurrency_test(account):
    sim = TransactionSimulator(account)
    sim.run_mixed_operations(deposit_amount=10, withdraw_amount=10, num_pairs=5)
    print(f"\n---Mixed Concurrency Test Completed---")
    print(f"Expected balance: $150.00")
    print(f"Final Balance after mixed operations: ${account.get_balance():.2f}")
# Transfer test: bidirectional transfer between two accounts to validate deadlock prevention
def transfer_test():
    account_a = BankAccount("111111111"); account_b = BankAccount("222222222")
    account_a.deposit(100); account_b.deposit(100)
    TransactionSimulator.run_bidirectional_transfers(account_a, account_b, amount=50, num_each_direction=1)
    print("\n---Transfer deadlock Test Completed---")
    print(f"Account A Balance: ${account_a.get_balance():.2f}")
    print(f"Account B Balance: ${account_b.get_balance():.2f}")
    print("Expected balance for both accounts: $100.00, no deadlock occurred")

def extreme_transfer_test():
    acc1 = BankAccount("333333333"); acc2 = BankAccount("444444444")
    acc1.deposit(200); acc2.deposit(200)
    TransactionSimulator.run_bidirectional_transfers(acc1, acc2, amount=10, num_each_direction=10)
    print("\n---Extreme Transfer deadlock Test Completed---")
    print(f"Account 1 Balance: ${acc1.get_balance():.2f}")
    print(f"Account 2 Balance: ${acc2.get_balance():.2f}")
    print("Expected balance for both accounts: $200.00, no deadlock occurred")

# Transfer insufficient funds test: simulate failed transfers due to invalid amounts or insufficient balance
def transfer_insufficient_funds_test():
    acc1 = BankAccount("555555555")
    acc2 = BankAccount("666666666")
    #initial deposits
    acc1.deposit(50)
    acc2.deposit(100)
    def try_large_transfer():
        try:
            acc1.transfer_to(acc2, 200)
        except InsufficientFundsError as exception:
            print(f"Transfer failed in thread: {exception}")
        try:
            print("\nTrying to transfer -$20 invalid amount from account 2 to Account 1")
            acc2.transfer_to(acc1, -20)
        except InvalidAmountError as exception:
            print(f"Transfer failed in thread: {exception}")

    # Run transfer attempts inside a thread to simulate concurrency
    t = threading.Thread(target= try_large_transfer)
    t.start()
    t.join()

    print("\n---Transfer Insufficient Funds Test Completed---")
    print(f"Account 1 Balance: ${acc1.get_balance():.2f}")
    print(f"Account 2 Balance: ${acc2.get_balance():.2f}")
    print("Expected balance for both accounts: $50.00 each, transfer should fail due to insufficient funds")



# Only run main() if this file is executed directly, not when imported as a module
if __name__ == "__main__":
    acc = main()                       #main() creates account and return it
    concurrency_test(acc)              #reusing the same account
    mixed_concurrency_test(acc)        # reuse the same account
    transfer_test()                    #test transfer deadlock scenario
    extreme_transfer_test()            #test extreme transfer deadlock scenario
    transfer_insufficient_funds_test()  #test transfer insufficient funds scenario




