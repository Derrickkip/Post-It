import unittest
from app import register

class Tests(unittest.TestCase):

    def test_registration(self):
        register()

if __name__ == '__name__':
    unittest.main()