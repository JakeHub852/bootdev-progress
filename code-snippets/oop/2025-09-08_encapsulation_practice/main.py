class BankAccount:
    # Initialize private account number and balance
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    # Account number getter
    def get_account_number(self):
        return self.__account_number

    # Balance getter
    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount):
        # Validate positive amount
        if amount <= 0:
            raise ValueError("cannot deposit zero or negative funds")
        # Update balance
        self.__balance += amount

    def withdraw(self, amount):
        # Validate positive amount
        if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")
        # Validate sufficient funds
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        # Update balance
        self.__balance -= amount