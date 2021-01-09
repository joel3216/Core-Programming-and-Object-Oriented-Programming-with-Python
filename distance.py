import math
def euclideanDistance(x,y):
    distance=math.sqrt(x*x+y*y)
    print("the euclidean distance between (0,0) and ("+str(x)+","+str(y)+") is "+str(distance))

try:
    x=float(input("enter the x coordinate"))
    y=float(input("enter the y coordinate"))
    euclideanDistance(x,y)
except ValueError:
    print("kindly enter only integers")