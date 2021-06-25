import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Kiryu")

    def test_guest_has_name(self):
        self.assertEqual("Kiryu", self.guest.name)