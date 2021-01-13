import unittest
import util

class testToBinary(unittest.TestCase):
    def test_toBinary(self):
        binary=util.util.toBinary(142)
        self.assertEqual(binary,10001110,"expected 10001110 for 142")

if __name__ == "__main__":
    unittest.main()