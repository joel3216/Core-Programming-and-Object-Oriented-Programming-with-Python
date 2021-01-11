import unittest
class utility:
    @staticmethod
    def temperatureConversion(temperature,unit):
        if unit=="fahrenheit":
            return (temperature-32)*(5/9)
        else:
            return (temperature*9/5)+32
    
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
            convertedTemperature=utility.temperatureConversion(temperature,unit)
            print(convertedTemperature)
            self.assertEqual(convertedTemperature,194,"should be 194f for 90c")

if __name__ == "__main__":
    unittest.main()
