import unittest
from classes.room import *
from classes.guest import *
from classes.song import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Kamurocho", 10, 25.00)
        self.guest = Guest("Daigo", 85.00, "Today is a Diamond")
        self.song = Song("Rouge of Love")

    def test_room_has_name(self):
        self.assertEqual("Kamurocho", self.room.name)

    def test_room_has_guests(self):
        self.assertEqual(0, len(self.room.guests))

    def test_room_has_songs(self):
        self.assertEqual(0, len(self.room.songs))

    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))
        self.assertEqual(25.00, self.guest.bar_tab)

    def test_can_check_out_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))

    def test_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.songs))

    def test_remove_song(self):
        self.room.add_song(self.song)
        self.room.remove_song(self.song)
        self.assertEqual(0, len(self.room.songs))

    def test_room_has_maximum_occupancy(self):
        self.assertEqual(10, self.room.maximum_occupants)

    def test_is_there_space_for_guest__True(self):
        self.room.space_for_guest()
        self.assertEqual(True, self.room.space_for_guest())

    def test_is_there_space_for_guest__False(self):
        self.room.maximum_occupants = 1
        self.room.check_in_guest(self.guest)
        self.room.space_for_guest()
        self.assertEqual(False, self.room.space_for_guest())

    def test_check_in_guest_when_there_is_no_room(self):
        self.room.maximum_occupants = 1
        self.room.check_in_guest(self.guest)
        self.assertEqual("No space available, try another room.", self.room.check_in_guest(self.guest))
        self.assertEqual(1, len(self.room.guests))

    def test_room_has_entry_fee(self):
        self.assertEqual(25.00, self.room.entry_fee)

    def test_check_in_guest_cannot_afford(self):
        self.guest.wallet = 5.00
        self.assertEqual("Not enough money.", self.room.check_in_guest(self.guest))
        self.assertEqual(0, len(self.room.guests))
        self.assertEqual(0, self.guest.bar_tab)

    # def test_can_add_to_bar_tab(self):
    #     self.room.add_to_bar_tab(self.guest, self.room.entry_fee)
    #     self.assertEqual(25.00, self.guest.bar_tab)