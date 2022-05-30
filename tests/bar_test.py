import unittest
from src.bar import Bar

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar()
