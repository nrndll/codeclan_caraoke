import unittest
from classes.room import *
from classes.guest import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Kamurocho")
        self.guest = Guest("Daigo")

    def test_room_has_name(self):
        self.assertEqual("Kamurocho", self.room.name)

    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))