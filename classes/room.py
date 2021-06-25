import pdb

class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []
        self.maximum_occupants = 10

    def check_in_guest(self, guest):
        if self.space_for_guest():
            self.guests.append(guest)
        else: 
            return "No space available, try another room."

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