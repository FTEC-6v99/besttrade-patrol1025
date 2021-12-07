class Account():
    def __init__(self, account_number:int, investor_id:int, balance:float):
        self.account_number = account_number
        self.investor_id = investor_id
        self.balance = balance

    def __str__(self):
        return f'account number: {self.account_number} |investor id: {self.investor_id} |balance: {self.balance}'
