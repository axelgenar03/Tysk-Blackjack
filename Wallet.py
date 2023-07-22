class Wallet:

    def __init__(self):
        self.balance = 100

    def deduct_balance(self, amount) -> None:
        self.balance -= amount
        print(f"Your balance is: {self.balance}")


