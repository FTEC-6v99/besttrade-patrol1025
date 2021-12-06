class Portfolio():
    def __init__(self, account_number:int, ticker:str, quantity:int, purchase_price:float):
        self.account_number=account_number
        self.ticker=ticker
        self.quantity=quantity
        self.purchase_price=purchase_price

    def __str__(self):
        return f'account number: {self.account_number} |ticker: {self.ticker} |quantity: {self.quantity} |purchase price: {self.purchase_price}'

    def __dict__(self):
        return {
            "account_number": self.account_number,
            "ticker": self.ticker,
            "quantity": self.quantity,
            "purchase_price": str(self.purchase_price)
        }