class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []

    def check_in_guest(self, guest):
        self.guests.append(guest)