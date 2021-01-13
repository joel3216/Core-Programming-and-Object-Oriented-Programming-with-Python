import unittest
import util
    
class testTemperatureConversion(unittest.TestCase):    
    def test_temperatureConversion(self):
        try:
            unit=input("enter the unit of temperature(celcius or fahrenheit)")
            if "fahrenheit" not in unit and "celcius" not in unit:
                raise ValueError
            temperature=float(input("enter the temperature"))
        except ValueError:
            print("kindly enter the proper details")
        else:
            convertedTemperature=util.util.temperatureConversion(temperature,unit)
            print(convertedTemperature)
            self.assertEqual(convertedTemperature,194,"should be 194f for 90c")

if __name__ == "__main__":
    unittest.main()
