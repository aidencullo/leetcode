class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance[:]
        self.n = len(balance)

    def validate_account(self, account: int):
        return account > 0 and account < self.n + 1
    

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.validate_account(account1) or not self.validate_account(account2):
            return False
        withdrawal = self.withdraw(account1, money)
        if not withdrawal:
            return False
        self.deposit(account2, money)
        return True
        

    def deposit(self, account: int, money: int) -> bool:
        if not self.validate_account(account):
            return False
        self.balance[account - 1] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if not self.validate_account(account):
            return False
        if money > self.balance[account - 1]:
            return False
        self.balance[account - 1] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
