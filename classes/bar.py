class Bar:

    def __init__(self, name):
        self.name = name
        self.total_cash = 0

    def take_cash_from_guest(self, amount, guest):
        guest.wallet -= amount
        self.total_cash += amount
