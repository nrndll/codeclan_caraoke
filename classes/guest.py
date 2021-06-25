class Guest:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def can_afford_entry_fee(self, room):
        if self.wallet >= room.entry_fee:
            return True
        else:
            return False