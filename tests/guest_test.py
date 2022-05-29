import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Tim", 20, 200, "Bad Romance")
        self.guest_2 = Guest("Jimmy", 35, 100, "I Kissed a Girl")


    def test_guest_has_name(self):
        self.assertEqual("Tim", self.guest.name)
        self.assertEqual("Jimmy", self.guest_2.name)

    def test_guest_has_age(self):
        self.assertEqual(20, self.guest.age)
        self.assertEqual(35, self.guest_2.age)
    
    def test_guest_has_money(self):
        self.assertEqual(200, self.guest.money)