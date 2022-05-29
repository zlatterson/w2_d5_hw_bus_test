import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("The Beatles", "A day in the life")

    def test_song_band(self):
        self.assertEqual("The Beatles", self.song.band_name)

    def test_song_name(self):
        self.assertEqual("A day in the life", self.song.song_name)

