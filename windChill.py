import sys
t=float(sys.argv[1])
v=float(sys.argv[2])

try:
    if abs(t)>50 or v<3 or v>120:
        print("the formula is not valid for these values")
    else:
        w= 35.74 + 0.6215*t + (0.4275*t - 35.75)*(v**0.16)
        print("the wind chill factor is "+str(w))
except Exception as e:
    print("An exception occured : "+str(e))
