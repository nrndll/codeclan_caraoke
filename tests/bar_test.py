import unittest
from classes.bar import *
from classes.guest import *
from classes.room import *

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar("Karaokekan")
        self.guest = Guest("Majima", 55.00, "Rouge of Love")
        self.room = Room("Nagasugai", 15, 10.00)

    def test_bar_has_name(self):
        self.assertEqual("Karaokekan", self.bar.name)

    def test_bar_has_total_cash(self):
        self.assertEqual(0, self.bar.total_cash)

    # def test_take_cash_from_guest(self):
    #     self.bar.take_cash_from_guest(self.room.entry_fee, self.guest)
    #     self.assertEqual(45.00, self.guest.wallet)
    #     self.assertEqual(10.00, self.bar.total_cash)

    # def test_can_add_to_bar_tab(self):
    #     self.bar.add_to_bar_tab(self.guest, self.room.entry_fee)
    #     self.assertEqual(10.00, self.guest.bar_tab)

    def test_can_check_in_guest(self):
        self.bar.check_in_guest(self.room, self.guest)
        self.assertEqual(1, len(self.room.guests))
        self.assertEqual(10.00, self.guest.bar_tab)

    def test_can_check_out_guest(self):
        self.bar.check_in_guest(self.room, self.guest)
        self.bar.check_out_guest(self.room, self.guest)
        self.assertEqual(0, len(self.room.guests))