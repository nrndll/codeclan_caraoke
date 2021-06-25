class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)