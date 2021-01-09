import math

def getRoots(constant1,constant2,constant3):
    try:
        delta= constant2*constant2 - 4*constant1*constant3
        root1= (-constant2+math.sqrt(delta))/(2*constant1)
        root2= (-constant2-math.sqrt(delta))/(2*constant1)
        print("the roots of the equation are "+str(root1)+" and "+str(root2))
    except ValueError:
        print("the equation has no real solution")


try:
    constant1=float(input("enter the value of the first constant in the eqn"))
    constant2=float(input("enter the value of the second constant in the eqn"))
    constant3=float(input("enter the value of the third constant in the eqn"))
    getRoots(constant1,constant2,constant3)
except ValueError:
    print("kindly enter numbers only")