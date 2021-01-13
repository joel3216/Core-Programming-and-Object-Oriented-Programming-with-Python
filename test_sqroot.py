import unittest
import util

class testSqroot(unittest.TestCase):
    def test_sqroot(self):
        try:
            number=int(input("enter a positive integer"))
            if number<=0:
                raise ValueError
        except ValueError:
            print("kindly enter only positive integers")
        else:
            sqroot=util.util.sqrt(number)
            self.assertEqual(sqroot,2,"should be 2 for 4")

if __name__ == "__main__":
    unittest.main()