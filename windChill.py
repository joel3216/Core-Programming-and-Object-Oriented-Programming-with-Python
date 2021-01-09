import sys

def getWindChill(temperature,velocity):
    windChill= 35.74 + 0.6215*temperature + (0.4275*temperature - 35.75)*(velocity**0.16)
    return windChill

try:

    temperature=float(sys.argv[1])
    velocity=float(sys.argv[2])

    if abs(temperature)>50 or velocity<3 or velocity>120:
        print("the formula is not valid for these values")
    else:
        windChill=getWindChill(temperature,velocity)
        print("the wind chill factor is "+str(windChill))
except ValueError:
    print("kindly enter numbers only")
except IndexError:
    print("kindly enter the temperature and velocity from the command line")
