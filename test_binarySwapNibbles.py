import unittest
import binarySwapNibbles

class testBinarySwapNibbles(unittest.TestCase):
    def test_binarySwap(self):
        swapbinary=binarySwapNibbles.binarySwapNibbles.swapNibbles(binarySwapNibbles,2)
        decimal=binarySwapNibbles.binarySwapNibbles.binary2Decimal(binarySwapNibbles,int(swapbinary))
        powerOfTwoCheck=binarySwapNibbles.binarySwapNibbles.isPowerOfTwo(binarySwapNibbles,decimal)

        self.assertEqual(swapbinary,"00100000")
        self.assertEqual(decimal,32)
        self.assertEqual(powerOfTwoCheck,True)
if __name__ == "__main__":
    unittest.main()