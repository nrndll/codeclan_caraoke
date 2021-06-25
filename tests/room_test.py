import unittest
from classes.room import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Kamurocho")

    def test_room_has_name(self):
        self.assertEqual("Kamurocho", self.room.name)