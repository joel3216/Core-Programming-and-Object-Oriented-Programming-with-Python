import math
a=float(input("enter the value of the first constant in the eqn"))
b=float(input("enter the value of the second constant in the eqn"))
c=float(input("enter the value of the third constant in the eqn"))

try:
    delta= b*b - 4*a*c
    root1= (-b+math.sqrt(delta))/(2*a)
    root2= (-b-math.sqrt(delta))/(2*a)
    print("the roots of the equation are "+str(root1)+" and "+str(root2))
except Exception as e:
    print("An exeption occured : "+str(e))
    print("the equation has no real solution")