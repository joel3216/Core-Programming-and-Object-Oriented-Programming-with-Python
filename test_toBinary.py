import unittest
import util

class testToBinary(unittest.TestCase):
    def test_toBinary(self):
        try:
            number=int(input("enter an integer"))
        except ValueError:
            print("kindly enter only integers")
        else:
            binary=util.util.toBinary(number)
            self.assertEqual(binary,10001110,"expected 10001110 for 142")

if __name__ == "__main__":
    unittest.main()