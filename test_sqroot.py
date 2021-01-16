import unittest
import util

class testSqroot(unittest.TestCase):
    def test_sqroot(self):
        sqroot=util.util.sqrt(4)
        self.assertEqual(sqroot,2,"should be 2 for 4")
        self.assertNotEqual(sqroot,4)

if __name__ == "__main__":
    unittest.main()