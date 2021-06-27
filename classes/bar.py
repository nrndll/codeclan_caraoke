class Bar:

    def __init__(self, name):
        self.name = name
        self.total_cash = 0

    def check_in_guest(self, room, guest):
        if room.space_for_guest():
            if guest.can_afford_entry_fee(room):
                room.guests.append(guest)
                self.add_to_bar_tab(room, guest)
            else:
                return "Not enough money."
        else: 
            return "No space available, try another room."

    def check_out_guest(self, room, guest):
        room.guests.remove(guest)
        self.charge_guest_bar_tab(guest)

    def add_to_bar_tab(self, room, guest):
        guest.bar_tab += room.entry_fee

    def charge_guest_bar_tab(self, guest):
        guest.wallet -= guest.bar_tab
        self.total_cash += guest.bar_tab
        guest.bar_tab = 0