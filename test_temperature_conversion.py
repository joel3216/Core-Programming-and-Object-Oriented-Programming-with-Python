import unittest
import util
    
class testTemperatureConversion(unittest.TestCase):    
    def test_temperatureConversion(self):
        convertedTemperature=util.util.temperatureConversion(90,"celcius")
        print(convertedTemperature)
        self.assertEqual(convertedTemperature,194,"should be 194f for 90c")

if __name__ == "__main__":
    unittest.main()
