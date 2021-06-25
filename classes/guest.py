class Guest:

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song
        self.bar_tab = 0

    def can_afford_entry_fee(self, room):
        if self.wallet >= room.entry_fee:
            return True
        else:
            return False

    # def pay_entry_fee(self, room, bar):
    #     if self.can_afford_entry_fee(room):
    #         bar.take_cash_from_guest(room.entry_fee, self)

    def favourite_song_cheer(self, room):
        for song in room.songs:
            if song == self.favourite_song:
                return "SUGOI!"