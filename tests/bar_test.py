import unittest
from classes.bar import *

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar("Karaokekan")

    def test_bar_has_name(self):
        self.assertEqual("Karaokekan", self.bar.name)