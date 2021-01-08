import math
x=int(input("enter the x coordinate"))
y=int(input("enter the y coordinate"))

try:
    distance=math.sqrt(x*x+y*y)
    print("the euclidean distance between (0,0) and ("+str(x)+","+str(y)+") is "+str(distance))
except Exception as e:
    print("An error occured : "+str(e))