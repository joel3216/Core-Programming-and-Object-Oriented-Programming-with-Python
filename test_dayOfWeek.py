import sys
import unittest
import util

class testDayOfWeek(unittest.TestCase):
    day=0
    month=0
    year=0
    def test_day(self):
        dayName,monthName=util.util.dayOfWeek(self.day,self.month,self.year)
        self.assertEqual(dayName,"Wednesday","should be wednesday for 13/1/2021")
        self.assertEqual(monthName,"January","should be january for 13/1/2021")
    
if __name__ == "__main__":
    try:
        if len(sys.argv)>0:
            testDayOfWeek.year=int(sys.argv.pop())
            testDayOfWeek.month=int(sys.argv.pop())
            testDayOfWeek.day=int(sys.argv.pop())
    
    except IndexError:
        print("kindly enter the day, month and year from the command line")
    except ValueError:
        print("kindly enter valid inputs")
    else:
        unittest.main()