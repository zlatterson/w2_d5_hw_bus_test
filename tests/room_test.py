import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1)
        self.room_2 = Room(2)

        self.guest = Guest("Jamie", 23, 100, "Get Back")
        self.guest_2 = Guest("Aaron", 24, 50, "Wonderwall")
        self.guest_3 = Guest("Paul", 22, 0, "American Pie")

        self.song = Song("Oasis", "Wonderwall")
        self.song_2 = Song("Michael Jackson", "Thriller")
        self.song_3 = Song("Michael Jackson", "Billy Jean")

        self.room.add_song_to_room(self.song.band_name, self.song.song_name)
        self.room.add_song_to_room(self.song_2.band_name, self.song_2.song_name)
        self.room.add_song_to_room(self.song_3.band_name, self.song_3.song_name)

    def test_room_number(self):
        self.assertEqual(1, self.room.room_number)
    
    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)

        self.assertEqual("Jamie", self.room.guests[0])
        self.assertEqual("Aaron", self.room.guests[1])
        self.assertEqual(20, self.room.money)
        # self.assertEqual("Paul", self.room.guests[2])

    def test_check_in_guest__has_paid(self):
        self.temporary_guest = Guest("Melissa", 18, 30, "Friday")
        self.room.check_in_guest(self.temporary_guest)
        self.assertEqual(20, self.temporary_guest.money)
        self.assertEqual("Melissa", self.room.guests[0])

    def test_check_in_guest__cannot_afford(self):
        self.temporary_guest_2 = Guest("Tom", 53, 9, "I Need a Dollar")
        self.room.check_in_guest(self.temporary_guest_2)
        self.assertEqual(9, self.temporary_guest_2.money)
        # self.assertEqual("Tom", self.room.guests[0])


    def test_display_playlist(self):
        self.assertEqual(self.room.display_playlist(self.guest), "I am indifferent to this playlist")
        self.assertEqual(self.room.display_playlist(self.guest_2), "That's my favourite song!")


    # def test_add_money(self):
        

    