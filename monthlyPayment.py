import sys
import unittest
import util

class testMonthlyPayment(unittest.TestCase):
    principalLoan=0
    years=0
    rate=0
    def test_monthlyPayment(self):
        payment=util.util.monthlyPayment(self.principalLoan,self.years,self.rate)
        self.assertEqual(payment,377.42,"should be 377.42 for p=20000,r=5%,y=5")
        self.assertNotEqual(payment,377)

if __name__ == "__main__":
    try:
        if len(sys.argv)>0:
            testMonthlyPayment.rate=float(sys.argv.pop())
            testMonthlyPayment.years=float(sys.argv.pop())
            testMonthlyPayment.principalLoan=float(sys.argv.pop())
    
    except IndexError:
        print("kindly enter the Principal loan, Years and Rate from the command line")
    except ValueError:
        print("kindly enter valid inputs")
    else:
        unittest.main()
    