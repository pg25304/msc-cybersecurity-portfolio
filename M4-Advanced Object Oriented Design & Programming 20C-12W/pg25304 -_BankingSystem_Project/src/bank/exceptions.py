# src/bank/exceptions.py -pg25304
#- When you write class InvalidAmountError(Exception):, you’re saying:
#InvalidAmountError is a new kind of error, and it behaves like a standard Python exception.”


class InvalidAmountError(Exception):
    """Exception raised for invalid amount operations in banking transactions."""
    pass
class InsufficientFundsError(Exception):
    """Exception raised when an account has insufficient funds for a withdrawal."""
    pass
