import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Kiryu", 75.00)

    def test_guest_has_name(self):
        self.assertEqual("Kiryu", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(75.00, self.guest.wallet)