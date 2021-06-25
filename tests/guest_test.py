import unittest
from classes.guest import *
from classes.room import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Kiryu", 75.00)
        self.room = Room("Onomichi", 5, 15.00)

    def test_guest_has_name(self):
        self.assertEqual("Kiryu", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(75.00, self.guest.wallet)

    def test_guest_can_afford_entry_fee__True(self):
        self.assertEqual(True, self.guest.can_afford_entry_fee(self.room))

    def test_guest_can_afford_entry_fee__False(self):
        self.room = Room("Ryukyu", 25, 990.00)
        self.assertEqual(False, self.guest.can_afford_entry_fee(self.room))

    def test_guest_pay_entry_fee(self):
        self.guest.pay_entry_fee(self.room)
        self.assertEqual(60.00, self.guest.wallet)