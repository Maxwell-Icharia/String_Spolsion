import unittest
from main.string_spolsion import string_spolsion

class TestStringSplosion(unittest.TestCase):

    def test_string_splosion(self):
        self.assertTrue(string_spolsion('hhere'), str)

if __name__ == '__main__':
    unittest.main()