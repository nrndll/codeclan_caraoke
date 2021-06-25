class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []
        self.maximum_occupants = 10

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def space_for_guest(self):
        if len(self.guests) < self.maximum_occupants:
            return True
        else:
            return False