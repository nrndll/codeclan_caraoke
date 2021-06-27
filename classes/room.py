import pdb

class Room:
    def __init__(self, name, maximum_occupants, entry_fee):
        self.name = name
        self.guests = []
        self.songs = []
        self.maximum_occupants = maximum_occupants
        self.entry_fee = entry_fee
        # self.total_cash = 0

    # def check_in_guest(self, guest):
    #     if self.space_for_guest():
    #         if guest.can_afford_entry_fee(self):
    #             self.guests.append(guest)
    #             self.add_to_bar_tab(guest, self.entry_fee)
    #         else:
    #             return "Not enough money."
    #     else: 
    #         return "No space available, try another room."

    # def check_out_guest(self, guest):
    #     self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def space_for_guest(self):
        if len(self.guests) < self.maximum_occupants:
            return True
        else:
            return False

    # def add_to_bar_tab(self, guest, amount):
    #     guest.bar_tab += amount

    # def charge_guest_bar_tab(self, guest):
    #     guest.wallet -= guest.bar_tab
    #     self.total_cash += guest.bar_tab

