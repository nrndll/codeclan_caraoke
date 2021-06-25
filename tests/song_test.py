import unittest
from classes.song import *

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Bakamitai")

    def test_song_has_name(self):
        self.assertEqual("Bakamitai", self.song.name)